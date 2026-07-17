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
bg = raw.getpixel((910, 725))  # sample beside the figure so the paste blends
banner = Image.new("RGB", (W, H), bg)
# figure (Ace + flags), cropped free of the heart decorations
fig = raw.crop((900, 60, 1950, 1390))
s = 0.5416  # maps hair-top..waist into the 423px safe zone height
fw, fh = int(fig.width * s), int(fig.height * s)
fig = fig.resize((fw, fh), Image.LANCZOS)
# feathered mask so the crop edge never shows against the fill
mask = Image.new("L", (fw, fh), 0)
md = ImageDraw.Draw(mask)
F = 48
md.rectangle([F, F, fw - F, fh - F], fill=255)
mask = mask.filter(__import__("PIL.ImageFilter", fromlist=["GaussianBlur"]).GaussianBlur(F // 2))
banner.paste(fig, (W // 2 - fw // 2, 464), mask)
# reuse the art's heart clusters as corner decoration (outside the safe zone)
for box, pos in [((150, 90, 960, 260), (80, 140)),
                 ((1860, 90, 2740, 260), None),
                 ((150, 1413, 960, 1533), (80, 1210)),
                 ((1860, 1413, 2740, 1533), None)]:
    cl = raw.crop(box)
    cl = cl.resize((int(cl.width * 0.7), int(cl.height * 0.7)), Image.LANCZOS)
    if pos is None:
        pos = (W - cl.width - 80, 140 if box[1] < 500 else 1210)
    banner.paste(cl, pos)
d = ImageDraw.Draw(banner)

def center_text(draw, cx, cy, text, fnt, fill, stroke=0, stroke_fill=None):
    bbox = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((cx - w / 2 - bbox[0], cy - h / 2 - bbox[1]), text, font=fnt,
              fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)

# left block: channel name stacked, centered between safe-zone left edge and the figure
anton = font("Anton-Regular.ttf", 120)
cx_l = (sx + (W // 2 - fw // 2)) // 2        # ~750
center_text(d, cx_l, sy + SAFE_H * 0.30, "DATE &", anton, NAVY, 6, CREAM)
center_text(d, cx_l, sy + SAFE_H * 0.66, "ADVICE", anton, NAVY, 6, CREAM)
# small red/green underline flags under the name
bar_y = int(sy + SAFE_H * 0.90)
d.rectangle([cx_l - 190, bar_y, cx_l - 10, bar_y + 14], fill=RED)
d.rectangle([cx_l + 10, bar_y, cx_l + 190, bar_y + 14], fill=GREEN)

# right block: tagline, centered between the figure and safe-zone right edge
archivo = font("ArchivoBlack-Regular.ttf", 42)
cx_r = (W // 2 + fw // 2 + sx + SAFE_W) // 2  # ~1810
for i, line in enumerate(["YOUR WINGMAN", "FOR THE HARD", "CONVERSATIONS."]):
    center_text(d, cx_r, sy + SAFE_H * (0.30 + 0.20 * i), line, archivo, NAVY, 4, CREAM)

banner.save(os.path.join(HERE, "banner.png"))
# safe-zone-only preview (what mobile sees), downscaled
banner.crop((sx, sy, sx + SAFE_W, sy + SAFE_H)).resize((773, 211), Image.LANCZOS)\
      .save(os.path.join(HERE, "banner-safezone-verify.png"))

# ---------- watermark ----------
wm = pfp_raw.resize((300, 300), Image.LANCZOS)
wm.save(os.path.join(HERE, "watermark.png"))
wm.resize((40, 40), Image.LANCZOS).save(os.path.join(HERE, "watermark-40-verify.png"))

print("composed: pfp.png banner.png watermark.png + verify previews")
