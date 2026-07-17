#!/usr/bin/env python3
"""Generate brand-style kinetic text cards (1080x1920 PNGs) for Short 01."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "channel-identity", "fonts")
OUT = os.path.join(HERE, "cards")
os.makedirs(OUT, exist_ok=True)
NAVY = (30, 42, 69)
CREAM = (255, 246, 236)
RED = (255, 71, 87)
GREEN = (46, 213, 115)
W, H = 1080, 1920

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

def center(d, cy, text, fnt, fill, stroke=0, sfill=None):
    b = d.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    d.text(((W - b[2] + b[0]) / 2 - b[0], cy - (b[3] - b[1]) / 2 - b[1]),
           text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=sfill)

def tally(d, x, y, scale=1.0, color=NAVY):
    """5-bar tally mark."""
    wgap, hgt, wd = int(22 * scale), int(90 * scale), int(9 * scale)
    for i in range(4):
        d.rounded_rectangle([x + i * wgap, y, x + i * wgap + wd, y + hgt], 5, fill=color)
    d.line([x - 8, y + hgt - 6, x + 3 * wgap + wd + 8, y + 6], fill=RED, width=wd)

# K1 — tally wall "100 DATES"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
import random
random.seed(7)
for row in range(6):
    for col in range(5):
        tally(d, 120 + col * 180 + random.randint(-8, 8),
              360 + row * 150 + random.randint(-6, 6), 0.85)
center(d, 1420, "100", font("Anton-Regular.ttf", 330), RED, 10, CREAM)
center(d, 1650, "DATES", font("Anton-Regular.ttf", 150), NAVY)
img.save(os.path.join(OUT, "K1.png"))

# K1g — green reprise "100 REAL DATES"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
for row in range(6):
    for col in range(5):
        tally(d, 120 + col * 180 + random.randint(-8, 8),
              360 + row * 150 + random.randint(-6, 6), 0.85)
center(d, 1380, "100", font("Anton-Regular.ttf", 300), GREEN, 10, CREAM)
center(d, 1600, "REAL DATES", font("Anton-Regular.ttf", 130), NAVY)
img.save(os.path.join(OUT, "K1g.png"))

# K2 — "NOT ABOUT THE NUMBER"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
center(d, 700, "NOT ABOUT", font("Anton-Regular.ttf", 170), NAVY)
big = font("Anton-Regular.ttf", 380)
center(d, 1000, "#", big, RED)
d.line([300, 1180, 780, 830], fill=NAVY, width=26)
center(d, 1350, "THE NUMBER", font("Anton-Regular.ttf", 150), NAVY)
img.save(os.path.join(OUT, "K2.png"))

# K3 — repelling arrows "WHAT PUSHES AWAY"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
center(d, 640, "WHAT PUSHES", font("Anton-Regular.ttf", 150), NAVY)
center(d, 830, "PEOPLE AWAY", font("Anton-Regular.ttf", 150), RED)
# two hearts pushed apart by arrows
def heart(dr, cx, cy, s, color):
    dr.polygon([(cx, cy + s), (cx - s, cy - s * 0.2), (cx - s * 0.5, cy - s * 0.9),
                (cx, cy - s * 0.35), (cx + s * 0.5, cy - s * 0.9), (cx + s, cy - s * 0.2)],
               fill=color)
heart(d, 340, 1250, 130, RED)
heart(d, 740, 1250, 130, NAVY)
for x0, x1 in [(480, 400), (600, 680)]:
    d.line([540, 1250, x1, 1250], fill=NAVY, width=18)
    ar = 30 if x1 < 540 else -30
    d.polygon([(x1, 1250 - 25), (x1, 1250 + 25), (x1 - ar, 1250)], fill=NAVY)
img.save(os.path.join(OUT, "K3.png"))

# K4 — price tag cut "FEWER $$$ MISTAKES"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
center(d, 640, "FEWER", font("Anton-Regular.ttf", 190), NAVY)
center(d, 980, "$ $ $", font("Anton-Regular.ttf", 260), RED)
d.line([230, 1120, 850, 850], fill=NAVY, width=24)
center(d, 1330, "MISTAKES", font("Anton-Regular.ttf", 170), NAVY)
img.save(os.path.join(OUT, "K4.png"))

# K5 — end card "FOLLOW FOR MORE"
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
center(d, 760, "FOLLOW", font("Anton-Regular.ttf", 260), NAVY, 8, CREAM)
center(d, 1000, "FOR MORE", font("Anton-Regular.ttf", 130), NAVY)
d.rectangle([340, 1130, 530, 1160], fill=RED)
d.rectangle([550, 1130, 740, 1160], fill=GREEN)
center(d, 1290, "DATE & ADVICE", font("ArchivoBlack-Regular.ttf", 72), NAVY)
img.save(os.path.join(OUT, "K5.png"))

print("cards written:", sorted(os.listdir(OUT)))
