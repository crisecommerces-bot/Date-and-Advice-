#!/usr/bin/env python3
"""Assemble Short 01 (1080x1920) from generated assets + local cards.

Design: 7 audio blocks (one per VO take). Each block's beats split the take's
real duration evenly, so audio and video stay locked. Every beat <= 2.0s
(beat counts per block were chosen so duration/beats <= 2).
Captions are Pillow-rendered PNG overlays (brand fonts/colors, safe zone).
"""
import json, os, subprocess, math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets01")         # S1..S6.png, V1..V3.mp4, T1..T7.wav
CARDS = os.path.join(HERE, "cards")
TMP = os.path.join(HERE, "tmp01"); os.makedirs(TMP, exist_ok=True)
FONTS = os.path.join(HERE, "..", "channel-identity", "fonts")
FPS = 30
NAVY = (30, 42, 69, 255); CREAM = (255, 246, 236, 255)
RED = (255, 71, 87, 255); GREEN = (46, 213, 115, 255)

def dur(path):
    out = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                          "-of", "json", path], capture_output=True, text=True)
    return float(json.loads(out.stdout)["format"]["duration"])

def caption_png(text, name, color=NAVY, sub=None):
    """Big Anton caption on a rounded cream box, centered ~y1300 (safe zone)."""
    img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    size = 95
    f = ImageFont.truetype(os.path.join(FONTS, "Anton-Regular.ttf"), size)
    while d.textbbox((0, 0), text, font=f)[2] > 950:
        size -= 5; f = ImageFont.truetype(os.path.join(FONTS, "Anton-Regular.ttf"), size)
    b = d.textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0], b[3] - b[1]
    cx, cy = 540, 1300
    pad = 34
    d.rounded_rectangle([cx - w/2 - pad, cy - h/2 - pad, cx + w/2 + pad, cy + h/2 + pad],
                        26, fill=CREAM, outline=NAVY, width=6)
    d.text((cx - w/2 - b[0], cy - h/2 - b[1]), text, font=f, fill=color)
    if sub:
        f2 = ImageFont.truetype(os.path.join(FONTS, "ArchivoBlack-Regular.ttf"), 44)
        b2 = d.textbbox((0, 0), sub, font=f2)
        d.text((cx - (b2[2]-b2[0])/2, cy + h/2 + pad + 18), sub, font=f2,
               fill=CREAM, stroke_width=5, stroke_fill=NAVY)
    p = os.path.join(TMP, f"cap_{name}.png"); img.save(p); return p

def beat_from_video(src, t0, dcur, out, zoom=1.0, ytop=0.0):
    """Cut dcur seconds from src at t0; optional punch-in (zoom>1)."""
    vf = f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"
    if zoom > 1.001:
        cw, ch = int(1080/zoom), int(1920/zoom)
        vf += f",crop={cw}:{ch}:{(1080-cw)//2}:{int((1920-ch)*ytop)},scale=1080:1920"
    return ["ffmpeg", "-y", "-ss", f"{t0:.3f}", "-i", src, "-t", f"{dcur:.3f}",
            "-vf", vf + f",fps={FPS}", "-an", "-c:v", "libx264", "-preset", "fast",
            "-crf", "18", "-pix_fmt", "yuv420p", out]

def beat_from_still(src, dcur, out, z0=1.0, z1=1.12, ytop=0.12):
    """Ken Burns zoom on a still. ytop: vertical focus (0=top)."""
    frames = max(2, int(dcur * FPS))
    vf = (f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
          f"zoompan=z='{z0}+({z1}-{z0})*on/{frames}':d={frames}"
          f":x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*{ytop}':s=1080x1920:fps={FPS}")
    return ["ffmpeg", "-y", "-loop", "1", "-i", src, "-t", f"{dcur:.3f}", "-vf", vf,
            "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-pix_fmt", "yuv420p", out]

# ---- blocks: (take, [(asset, kind, params, caption, capcolor), ...]) ----
BLOCKS = [
    ("T1", [("V1", "vid", dict(t0=0.0), "100 DATES", RED),
            ("V1", "vid", dict(t0=2.0, zoom=1.45, ytop=0.08), "IN 2 YEARS", NAVY),
            ("K1", "card", {}, None, None)]),
    ("T2", [("V1", "vid", dict(t0=4.2, zoom=1.2, ytop=0.2), "A SOCIAL EXPERIMENT", NAVY),
            ("S1", "still", dict(z0=1.05, z1=1.22), "WHAT I LEARNED...", NAVY),
            ("V2", "vid", dict(t0=0.0), "I'M JOHN", GREEN)]),
    ("T3", [("K2", "card", {}, None, None),
            ("S2", "still", dict(z0=1.2, z1=1.02), "HOW DATING ACTUALLY WORKS", NAVY)]),
    ("T4", [("V2", "vid", dict(t0=2.0, zoom=1.4, ytop=0.05), "WHAT ATTRACTS", GREEN),
            ("K3", "card", {}, None, None),
            ("V3", "vid", dict(t0=0.0), "RED FLAG? RUN", RED),
            ("V3", "vid", dict(t0=2.0, zoom=1.5, ytop=0.1), "RUN.", RED),
            ("S4", "still", dict(z0=1.0, z1=1.15), "WALKING AWAY = WINNING", GREEN)]),
    ("T5", [("S5", "still", dict(z0=1.0, z1=1.12), "NO \"ALPHA\" GIMMICKS", NAVY),
            ("S5", "still", dict(z0=1.3, z1=1.45, ytop=0.05), "NO SUGARCOATING", RED),
            ("K1g", "card", {}, None, None)]),
    ("T6", [("V2", "vid", dict(t0=4.5, zoom=1.25, ytop=0.1), "CONFIDENCE", GREEN),
            ("K4", "card", {}, None, None),
            ("S3", "still", dict(z0=1.25, z1=1.05), "STRAIGHT ANSWERS", NAVY),
            ("V1", "vid", dict(t0=5.5, zoom=1.35, ytop=0.08), "FOR THE BROS", NAVY),
            ("S1", "still", dict(z0=1.25, z1=1.4, ytop=0.05), "I'VE GOT YOUR BACK", GREEN)]),
    ("T7", [("S6", "still", dict(z0=1.0, z1=1.15), "THE BOOK", NAVY),
            ("S6", "still", dict(z0=1.3, z1=1.5, ytop=0.15), "IT'S COMING", RED),
            ("V2", "vid", dict(t0=6.0), "FOLLOW FOR MORE", GREEN),
            ("K5", "card", {}, None, None)]),
]

def main():
    seg_files, audio_files, t_cursor = [], [], 0.0
    report = []
    for bi, (take, beats) in enumerate(BLOCKS, 1):
        wav = os.path.join(A, f"{take}.wav")
        d_take = dur(wav)
        audio_files.append(wav)
        n = len(beats)
        d_beat = d_take / n
        assert d_beat <= 2.05, f"beat too long in block {bi}: {d_beat:.2f}s"
        for j, (asset, kind, prm, cap, col) in enumerate(beats):
            out = os.path.join(TMP, f"b{bi}_{j}.mp4")
            # last video beat of a video asset must not run past its length
            if kind == "vid":
                src = os.path.join(A, f"{asset}.mp4")
                t0 = min(prm.get("t0", 0.0), max(0.0, dur(src) - d_beat - 0.05))
                cmd = beat_from_video(src, t0, d_beat, out,
                                      prm.get("zoom", 1.0), prm.get("ytop", 0.0))
            elif kind == "still":
                src = os.path.join(A, f"{asset}.png")
                cmd = beat_from_still(src, d_beat, out, prm.get("z0", 1.0),
                                      prm.get("z1", 1.12), prm.get("ytop", 0.12))
            else:
                src = os.path.join(CARDS, f"{asset}.png")
                cmd = beat_from_still(src, d_beat, out, 1.0, 1.07, 0.5)
            subprocess.run(cmd, check=True, capture_output=True)
            if cap:
                capped = os.path.join(TMP, f"b{bi}_{j}_cap.mp4")
                cp = caption_png(cap, f"{bi}_{j}", col)
                subprocess.run(["ffmpeg", "-y", "-i", out, "-i", cp,
                                "-filter_complex", "[0][1]overlay=0:0",
                                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                                "-pix_fmt", "yuv420p", capped],
                               check=True, capture_output=True)
                out = capped
            seg_files.append(out)
            report.append(f"block{bi} beat{j+1} {asset} {d_beat:.2f}s cap={cap!r}")
            t_cursor += d_beat
    # concat video
    lst = os.path.join(TMP, "segs.txt")
    with open(lst, "w") as f:
        for s in seg_files:
            f.write(f"file '{s}'\n")
    vcat = os.path.join(TMP, "video.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                    "-pix_fmt", "yuv420p", vcat], check=True, capture_output=True)
    # concat audio
    alst = os.path.join(TMP, "auds.txt")
    with open(alst, "w") as f:
        for s in audio_files:
            f.write(f"file '{s}'\n")
    acat = os.path.join(TMP, "audio.wav")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", alst,
                    "-ar", "48000", "-ac", "2", acat], check=True, capture_output=True)
    # mux (loudness-normalized)
    final = os.path.join(HERE, "01-100-dates-intro.mp4")
    subprocess.run(["ffmpeg", "-y", "-i", vcat, "-i", acat,
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", "-shortest", final],
                   check=True, capture_output=True)
    print("\n".join(report))
    print("FINAL:", final, f"{dur(final):.2f}s")

if __name__ == "__main__":
    main()
