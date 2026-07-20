#!/usr/bin/env python3
"""Prepare the final VO track from the voice-converted video.
Extract audio -> trim lead/tail -> compress internal pauses (>0.5s -> 0.3s)
-> tempo-fit under 58.5s if needed (max 1.06x, pitch-safe) -> vo-final.wav."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VO_DIR = os.path.join(HERE, "..", "voice-vo")
SRC = os.path.join(VO_DIR, "john-converted.mp4")
RAW = os.path.join(VO_DIR, "vo-raw.wav")
OUT = os.path.join(VO_DIR, "vo-final.wav")
TARGET = 58.5

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())

subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", SRC, "-ar", "48000", "-ac", "1", RAW], check=True)
total = dur(RAW)

# find silences
r = subprocess.run(["ffmpeg", "-i", RAW, "-af", "silencedetect=noise=-32dB:d=0.5",
                    "-f", "null", "-"], capture_output=True, text=True)
log = r.stderr
sil = []
for m in re.finditer(r"silence_start: ([\d.]+)", log):
    sil.append([float(m.group(1)), None])
for i, m in enumerate(re.finditer(r"silence_end: ([\d.]+)", log)):
    if i < len(sil):
        sil[i][1] = float(m.group(1))
sil = [(a, b if b else total) for a, b in sil]

# build keep-intervals: compress each internal silence to 0.3s, lead to 0.3s, tail to 0.5s
KEEP = 0.3
segs = []
cursor = 0.0
for a, b in sil:
    if a > cursor:
        segs.append((cursor, a))
    if a <= 0.01:                      # leading silence
        cursor = max(b - 0.3, 0.0)
        segs = []
        segs.append((cursor, cursor))  # placeholder start
        segs = [] ; cursor = b - 0.3 if b - 0.3 > 0 else 0.0
        continue
    if b >= total - 0.01:              # trailing silence
        segs.append((a, min(a + 0.5, total)))
        cursor = total
        break
    segs.append((a, a + KEEP))         # compressed pause
    cursor = b
if cursor < total - 0.01:
    segs.append((cursor, total))
# merge/normalize
segs = [(max(0, a), min(total, b)) for a, b in segs if b - a > 0.01]

parts = []
for i, (a, b) in enumerate(segs):
    parts.append(f"[0]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[p{i}]")
joins = "".join(f"[p{i}]" for i in range(len(segs)))
fc = ";".join(parts) + f";{joins}concat=n={len(segs)}:v=0:a=1[out]"
subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", RAW, "-filter_complex", fc,
                "-map", "[out]", os.path.join(VO_DIR, "vo-tight.wav")], check=True)
d1 = dur(os.path.join(VO_DIR, "vo-tight.wav"))
tempo = min(max(d1 / TARGET, 1.0), 1.06)
if tempo > 1.005:
    subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", os.path.join(VO_DIR, "vo-tight.wav"),
                    "-af", f"atempo={tempo:.4f}", OUT], check=True)
else:
    os.replace(os.path.join(VO_DIR, "vo-tight.wav"), OUT)
print(json.dumps({"orig": total, "tight": d1, "tempo": round(tempo, 4), "final": dur(OUT)}))
