#!/usr/bin/env python3
"""Assemble intro v6 (NEW script, ElevenLabs Jerry B VO). Same timestamp-based
engine as assemble_01b: BEATS holds (t_end, asset, kind, params, caption, color);
each beat runs from the previous t_end, long spans auto-split into <=1.9s
wide/punch sub-beats. VO track and output name differ from 01b."""
import os, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("a1", os.path.join(HERE, "assemble_01.py"))
a1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(a1)
A = os.path.join(HERE, "assets01")
CARDS = {"K1": "cards", "K1g": "cards", "K5": "cards",
         "CB1": "cards01b", "CB2": "cards01b", "CB3": "cards01b"}
VO = os.path.join(HERE, "..", "voice-vo", "01-jerry-final.wav")
TMP = os.path.join(HERE, "tmp01c"); os.makedirs(TMP, exist_ok=True)
NAVY, RED, GREEN = a1.NAVY, a1.RED, a1.GREEN

def src_for(asset, kind):
    if kind == "card":
        return os.path.join(HERE, CARDS[asset], asset + ".png")
    ext = ".mp4" if kind == "vid" else ".png"
    return os.path.join(A, asset + ext)

def render(beats):
    seg_files = []
    t_prev = 0.0
    a1.TMP = TMP
    for i, (t_end, asset, kind, prm, cap, col) in enumerate(beats):
        d = t_end - t_prev
        n = max(1, int(-(-d // 1.9)))
        sub = d / n
        for j in range(n):
            out = os.path.join(TMP, f"b{i}_{j}.mp4")
            punch = (j % 2 == 1)
            if kind == "vid":
                src = src_for(asset, kind)
                t0 = min(prm.get("t0", 0.0) + j * sub, max(0.0, a1.dur(src) - sub - 0.05))
                cmd = a1.beat_from_video(src, t0, sub, out,
                                         1.35 if punch else prm.get("zoom", 1.0),
                                         prm.get("ytop", 0.08))
            elif kind == "still":
                src = src_for(asset, kind)
                if punch:
                    cmd = a1.beat_from_still(src, sub, out, 1.3, 1.45, 0.06)
                else:
                    cmd = a1.beat_from_still(src, sub, out, prm.get("z0", 1.0), prm.get("z1", 1.14), prm.get("ytop", 0.1))
            else:
                src = src_for(asset, kind)
                cmd = a1.beat_from_still(src, sub, out, 1.0 + 0.04 * j, 1.05 + 0.04 * j, 0.5)
            subprocess.run(cmd, check=True, capture_output=True)
            if cap:
                capped = os.path.join(TMP, f"b{i}_{j}c.mp4")
                cp = a1.caption_png(cap, f"01c_{i}_{j}", col)
                subprocess.run(["ffmpeg", "-y", "-i", out, "-i", cp, "-filter_complex",
                                "[0][1]overlay=0:0", "-c:v", "libx264", "-preset", "fast",
                                "-crf", "18", "-pix_fmt", "yuv420p", capped],
                               check=True, capture_output=True)
                out = capped
            seg_files.append(out)
            print(f"beat {i}.{j} {asset} {sub:.2f}s cap={cap!r}")
        t_prev = t_end
    lst = os.path.join(TMP, "segs.txt")
    with open(lst, "w") as f:
        for s in seg_files: f.write(f"file '{s}'\n")
    vcat = os.path.join(TMP, "video.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264",
                    "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p", vcat],
                   check=True, capture_output=True)
    final = os.path.join(HERE, "01-intro.mp4")
    subprocess.run(["ffmpeg", "-y", "-i", vcat, "-i", VO, "-af",
                    "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "192k", "-movflags", "+faststart", "-shortest", final],
                   check=True, capture_output=True)
    print("FINAL:", final, f"{a1.dur(final):.2f}s")

if __name__ == "__main__":
    from beats_01c import BEATS as B
    render(B)
