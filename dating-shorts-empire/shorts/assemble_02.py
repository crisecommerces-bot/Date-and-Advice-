#!/usr/bin/env python3
"""Assemble Short 02 'Leave Before Dessert' — reuses the block/beat engine of
assemble_01.py with Short-02 blocks, assets02/ + reused assets01/ + cards02/."""
import os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("a1", os.path.join(HERE, "assemble_01.py"))
a1 = importlib.util.module_from_spec(spec)
# prevent auto-run: assemble_01 guards main() under __main__, safe to exec
spec.loader.exec_module(a1)

A2 = os.path.join(HERE, "assets02")
A1 = os.path.join(HERE, "assets01")
CARDS2 = os.path.join(HERE, "cards02")
CARDS1 = os.path.join(HERE, "cards")
TMP = os.path.join(HERE, "tmp02"); os.makedirs(TMP, exist_ok=True)
NAVY = a1.NAVY; RED = a1.RED; GREEN = a1.GREEN

# resolve an asset across assets02, assets01, cards02, cards
def src_for(asset, kind):
    if kind == "vid":
        for d in (A2, A1):
            p = os.path.join(d, asset + ".mp4")
            if os.path.exists(p): return p
    elif kind == "still":
        for d in (A2, A1):
            p = os.path.join(d, asset + ".png")
            if os.path.exists(p): return p
    else:
        for d in (CARDS2, CARDS1):
            p = os.path.join(d, asset + ".png")
            if os.path.exists(p): return p
    raise FileNotFoundError(asset)

BLOCKS = [
    ("T1", [("D1V", "vid", dict(t0=0.0), "LEAVE", RED),
            ("D1V", "vid", dict(t0=1.8, zoom=1.4, ytop=0.1), "BEFORE DESSERT", NAVY)]),
    ("T2", [("S3", "still", dict(z0=1.0, z1=1.12), "NOT THE WAITER THING", NAVY),
            ("V3", "vid", dict(t0=0.0), "EVERYONE KNOWS THAT", NAVY),
            ("D1", "still", dict(z0=1.15, z1=1.3, ytop=0.08), "THIS ONE HIDES", RED),
            ("D1", "still", dict(z0=1.35, z1=1.5, ytop=0.05), "IN PLAIN SIGHT", RED)]),
    ("T3", [("C2", "card", {}, None, None),
            ("D2", "still", dict(z0=1.0, z1=1.15), "THEY CORRECT...", RED),
            ("D2", "still", dict(z0=1.3, z1=1.45, ytop=0.05), "EVERY. STORY.", RED),
            ("V2", "vid", dict(t0=2.0, zoom=1.3, ytop=0.08), "NOT TO HELP. TO WIN.", NAVY)]),
    ("T4", [("C3", "card", {}, None, None),
            ("D2", "still", dict(z0=1.15, z1=1.0), "10x IN ONE DINNER?", NAVY),
            ("S3", "still", dict(z0=1.3, z1=1.45, ytop=0.05), "THAT'S A PREVIEW", RED)]),
    ("T5", [("C4", "card", {}, None, None),
            ("D1", "still", dict(z0=1.15, z1=1.0), "IT STARTS SMALL", NAVY),
            ("V3", "vid", dict(t0=1.8, zoom=1.45, ytop=0.1), "IT NEVER SHRINKS", RED)]),
    ("T6", [("S4", "still", dict(z0=1.0, z1=1.12), "BE KIND. SPLIT IT.", GREEN),
            ("S4", "still", dict(z0=1.25, z1=1.4, ytop=0.1), "GO HOME EARLY", GREEN),
            ("C5", "card", {}, None, None),
            ("S1", "still", dict(z0=1.25, z1=1.4, ytop=0.05), "WORTH IT.", GREEN)]),
    ("T7", [("V2", "vid", dict(t0=6.0), "FOLLOW FOR THE NEXT ONE", GREEN),
            ("K5", "card", {}, None, None)]),
]

def main():
    import subprocess, json
    seg_files, audio_files = [], []
    for bi, (take, beats) in enumerate(BLOCKS, 1):
        wav = os.path.join(A2, f"{take}.wav")
        d_take = a1.dur(wav)
        audio_files.append(wav)
        d_beat = d_take / len(beats)
        assert d_beat <= 2.05, f"beat too long block {bi}: {d_beat:.2f}"
        for j, (asset, kind, prm, cap, col) in enumerate(beats):
            out = os.path.join(TMP, f"b{bi}_{j}.mp4")
            src = src_for(asset, kind)
            if kind == "vid":
                t0 = min(prm.get("t0", 0.0), max(0.0, a1.dur(src) - d_beat - 0.05))
                cmd = a1.beat_from_video(src, t0, d_beat, out, prm.get("zoom", 1.0), prm.get("ytop", 0.0))
            elif kind == "still":
                cmd = a1.beat_from_still(src, d_beat, out, prm.get("z0", 1.0), prm.get("z1", 1.12), prm.get("ytop", 0.12))
            else:
                cmd = a1.beat_from_still(src, d_beat, out, 1.0, 1.07, 0.5)
            subprocess.run(cmd, check=True, capture_output=True)
            if cap:
                capped = os.path.join(TMP, f"b{bi}_{j}_cap.mp4")
                a1.TMP = TMP  # caption pngs into tmp02
                cp = a1.caption_png(cap, f"02_{bi}_{j}", col)
                subprocess.run(["ffmpeg", "-y", "-i", out, "-i", cp, "-filter_complex",
                                "[0][1]overlay=0:0", "-c:v", "libx264", "-preset", "fast",
                                "-crf", "18", "-pix_fmt", "yuv420p", capped],
                               check=True, capture_output=True)
                out = capped
            seg_files.append(out)
            print(f"block{bi} beat{j+1} {asset} {d_beat:.2f}s cap={cap!r}")
    lst = os.path.join(TMP, "segs.txt")
    with open(lst, "w") as f:
        for s in seg_files: f.write(f"file '{s}'\n")
    vcat = os.path.join(TMP, "video.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264",
                    "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p", vcat],
                   check=True, capture_output=True)
    alst = os.path.join(TMP, "auds.txt")
    with open(alst, "w") as f:
        for s in audio_files: f.write(f"file '{s}'\n")
    acat = os.path.join(TMP, "audio.wav")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", alst, "-ar", "48000",
                    "-ac", "2", acat], check=True, capture_output=True)
    final = os.path.join(HERE, "02-leave-before-dessert.mp4")
    subprocess.run(["ffmpeg", "-y", "-i", vcat, "-i", acat, "-af",
                    "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "192k", "-movflags", "+faststart", "-shortest", final],
                   check=True, capture_output=True)
    print("FINAL:", final, f"{a1.dur(final):.2f}s")

if __name__ == "__main__":
    main()
