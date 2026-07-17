#!/usr/bin/env python3
"""Compose final channel identity assets from raw Higgsfield outputs.
pfp.png (800x800), banner.png (2560x1440, text in 1546x423 safe zone),
watermark.png (300x300), plus small downscaled *-verify.png previews."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
NAVY = (30, 42, 69, 255)      # 1E2A45
CREAM = (255, 246, 236, 255)  # FFF6EC
RED = (255, 71, 87, 255)      # FF4757
GREEN = (46, 213, 115, 255)   # 2ED573

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

# ---------- pfp ----------
pfp_raw = Image.open(os.path.join(HERE, "pfp-raw.png")).convert("RGB")
pfp = pfp_raw.resize((800, 800), Image.LANCZOS)
pfp.save(os.path.join(HERE, "pfp.png"))
pfp.resize((98, 98), Image.LANCZOS).save(os.path.join(HERE, "pfp-98-verify.png"))

# ---------- banner ----------
W, H = 2560, 1440
SAFE_W, SAFE_H = 1546, 423
sx, sy = (W - SAFE_W) // 2, (H - SAFE_H) // 2  # 507, 508
raw = Image.open(os.path.join(HERE, "banner-raw.png")).convert("RGB")
bg = raw.getpixel((60, 800))
banner = Image.new("RGB", (W, H), bg)
# decorative borders from the art, placed outside the safe zone
top = raw.crop((0, 0, 2848, 170)).resize((W, 150), Image.LANCZOS)
bot = raw.crop((0, 1400, 2848, 1600)).resize((W, 170), Image.LANCZOS)
banner.paste(top, (0, 30))
banner.paste(bot, (0, H - 200))
# figure: crop character, fit head-to-chest into the safe zone height
fig = raw.crop((580, 140, 2230, 1600))
s = 0.532
fw, fh = int(fig.width * s), int(fig.height * s)
fig = fig.resize((fw, fh), Image.LANCZOS)
mask = Image.new("L", (fw, fh), 0)
md = ImageDraw.Draw(mask)
F = 40
md.rectangle([F, F, fw - F, fh - F], fill=255)
mask = mask.filter(__import__("PIL.ImageFilter", fromlist=["GaussianBlur"]).GaussianBlur(F // 2))
banner.paste(fig, (W // 2 - fw // 2, 473), mask)
d = ImageDraw.Draw(banner)

def center_text(draw, cx, cy, text, fnt, fill, stroke=0, stroke_fill=None):
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((cx - w / 2 - bbox[0], cy - h / 2 - bbox[1]), text, font=fnt,
              fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)

anton = font("Anton-Regular.ttf", 84)
cx_l = (sx + (W // 2 - fw // 2)) // 2
center_text(d, cx_l, sy + SAFE_H * 0.30, "DATE &", anton, NAVY, 5, (255, 255, 255, 255))
center_text(d, cx_l, sy + SAFE_H * 0.62, "ADVICE", anton, NAVY, 5, (255, 255, 255, 255))
bar_y = int(sy + SAFE_H * 0.84)
d.rectangle([cx_l - 130, bar_y, cx_l - 8, bar_y + 12], fill=RED)
d.rectangle([cx_l + 8, bar_y, cx_l + 130, bar_y + 12], fill=GREEN)
archivo = font("ArchivoBlack-Regular.ttf", 30)
cx_r = (W // 2 + fw // 2 + sx + SAFE_W) // 2
for i, line in enumerate(["YOUR WINGMAN", "FOR THE HARD", "CONVERSATIONS."]):
    center_text(d, cx_r, sy + SAFE_H * (0.32 + 0.18 * i), line, archivo, NAVY, 3, (255, 255, 255, 255))

banner.save(os.path.join(HERE, "banner.png"))
banner.crop((sx, sy, sx + SAFE_W, sy + SAFE_H)).resize((773, 211), Image.LANCZOS)\
      .save(os.path.join(HERE, "banner-safezone-verify.png"))

# ---------- watermark ----------
wm = pfp_raw.resize((300, 300), Image.LANCZOS)
wm.save(os.path.join(HERE, "watermark.png"))
wm.resize((40, 40), Image.LANCZOS).save(os.path.join(HERE, "watermark-40-verify.png"))

print("composed: pfp.png banner.png watermark.png + verify previews")
