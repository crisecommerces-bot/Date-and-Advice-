#!/usr/bin/env python3
"""Prepare final VO track: trim lead/tail, compress pauses, fit under ceiling.
Usage: prep_vo.py <input_audio> <output_wav> ; prints JSON incl. time mapping."""
import json, os, re, subprocess, sys

SRC, OUT = sys.argv[1], sys.argv[2]
TMP = OUT + ".tmp.wav"
TARGET = 58.5
KEEP = 0.22

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())

subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", SRC, "-ar", "48000", "-ac", "1", TMP], check=True)
total = dur(TMP)
r = subprocess.run(["ffmpeg", "-i", TMP, "-af", "silencedetect=noise=-30dB:d=0.28",
                    "-f", "null", "-"], capture_output=True, text=True)
log = r.stderr
starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", log)]
pauses = list(zip(starts, ends + [total] * (len(starts) - len(ends))))

segs = []          # (orig_start, orig_end) intervals we keep, in order
cursor = 0.0
for a, b in pauses:
    if a <= 0.01:                       # leading silence: keep last 0.3s of it
        cursor = max(b - 0.3, 0.0)
        continue
    if a > cursor:
        segs.append((cursor, a))        # speech
    if b >= total - 0.02:               # trailing silence: keep 0.5s then stop
        segs.append((a, min(a + 0.5, total)))
        cursor = total
        break
    segs.append((a, a + KEEP))          # compressed pause
    cursor = b
if cursor < total - 0.02:
    segs.append((cursor, total))

parts, joins = [], ""
for i, (a, b) in enumerate(segs):
    parts.append(f"[0]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[p{i}]")
    joins += f"[p{i}]"
fc = ";".join(parts) + f";{joins}concat=n={len(segs)}:v=0:a=1[out]"
subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", TMP, "-filter_complex", fc,
                "-map", "[out]", OUT + ".tight.wav"], check=True)
d1 = dur(OUT + ".tight.wav")
tempo = min(max(d1 / TARGET, 1.0), 1.06)
if tempo > 1.005:
    subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", OUT + ".tight.wav",
                    "-af", f"atempo={tempo:.4f}", OUT], check=True)
    os.remove(OUT + ".tight.wav")
else:
    os.replace(OUT + ".tight.wav", OUT)

# orig->final mapping table: cumulative kept time / tempo
mapping = []
acc = 0.0
for a, b in segs:
    mapping.append({"orig_start": round(a, 3), "orig_end": round(b, 3),
                    "final_start": round(acc / tempo, 3),
                    "final_end": round((acc + b - a) / tempo, 3)})
    acc += b - a
os.remove(TMP)
print(json.dumps({"orig": total, "tight": d1, "tempo": round(tempo, 4),
                  "final": dur(OUT), "map": mapping}))
