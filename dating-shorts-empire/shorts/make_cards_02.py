#!/usr/bin/env python3
"""Kinetic text cards for Short 02 (brand style, 1080x1920)."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "channel-identity", "fonts")
OUT = os.path.join(HERE, "cards02"); os.makedirs(OUT, exist_ok=True)
NAVY = (30, 42, 69); CREAM = (255, 246, 236); RED = (255, 71, 87); GREEN = (46, 213, 115)
W, H = 1080, 1920

def font(n, s): return ImageFont.truetype(os.path.join(FONTS, n), s)

def center(d, cy, text, f, fill, stroke=0, sfill=None):
    b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
    d.text(((W - b[2] + b[0]) / 2 - b[0], cy - (b[3] - b[1]) / 2 - b[1]), text,
           font=f, fill=fill, stroke_width=stroke, stroke_fill=sfill)

# C2 — THE CORRECTION GAME
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
center(d, 700, "THE", font("Anton-Regular.ttf", 120), NAVY)
center(d, 900, "CORRECTION", font("Anton-Regular.ttf", 165), RED)
center(d, 1100, "GAME", font("Anton-Regular.ttf", 165), NAVY)
d.line([220, 960, 860, 930], fill=NAVY, width=10)  # red-pen strike vibe
img.save(os.path.join(OUT, "C2.png"))

# C3 — 1 vs 10
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
center(d, 620, "1x = QUIRK", font("Anton-Regular.ttf", 140), NAVY)
center(d, 960, "10x =", font("Anton-Regular.ttf", 140), NAVY)
center(d, 1180, "A PREVIEW", font("Anton-Regular.ttf", 170), RED)
img.save(os.path.join(OUT, "C3.png"))

# C4 — CONTEMPT STARTS SMALL
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
center(d, 640, "CONTEMPT", font("Anton-Regular.ttf", 170), RED)
center(d, 850, "STARTS", font("Anton-Regular.ttf", 120), NAVY)
center(d, 1030, "small", font("Anton-Regular.ttf", 70), NAVY)
# growing bars
for i, (w_, c) in enumerate([(60, GREEN), (140, NAVY), (260, NAVY), (420, RED)]):
    d.rectangle([540 - w_ // 2, 1180 + i * 70, 540 + w_ // 2, 1180 + i * 70 + 44], fill=c)
img.save(os.path.join(OUT, "C4.png"))

# C5 — 1 EVENING vs 2 YEARS
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img)
center(d, 620, "LOSE", font("Anton-Regular.ttf", 110), NAVY)
center(d, 800, "1 EVENING", font("Anton-Regular.ttf", 160), GREEN)
center(d, 1010, "NOT", font("Anton-Regular.ttf", 110), NAVY)
center(d, 1190, "2 YEARS", font("Anton-Regular.ttf", 160), RED)
img.save(os.path.join(OUT, "C5.png"))
print("cards02:", sorted(os.listdir(OUT)))
