#!/usr/bin/env python3
"""Compose 33 branded vertical covers (1080x1920) + 01A/01B variants.

Template: punch words (Anton, <=3 words/line, 2 lines max) at top; Ace pose
(reused Short stills + smitten/shocked) upper-middle; wordmark + flag bars low.
Critical content stays in the center grid-crop zone. Also emits a contact
sheet and a 202x360 grid-size readability check of cover #1."""
import csv, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
POSES = os.path.join(HERE, "poses")     # S1..S6.png, SMITTEN.png, SHOCKED.png
FONTS = os.path.join(HERE, "..", "channel-identity", "fonts")
CSVP = os.path.join(HERE, "..", "research", "ideas.csv")
NAVY = (30, 42, 69); CREAM = (255, 246, 236)
RED = (255, 71, 87); GREEN = (46, 213, 115)
W, H = 1080, 1920

# rank -> (line1, line2, accent_color_for_line1, pose)
# punch words <=3 per line; pose keys: S1 confident, S2 talking, S3 sideeye-redflag,
# S4 walkaway-greenflag, S5 facepalm, S6 book, SMITTEN, SHOCKED
P = {
 1: ("LEAVE", "BEFORE DESSERT", RED, "SHOCKED"),
 2: ("3 PHRASES", "= MANIPULATION", RED, "S3"),
 3: ("I IGNORED IT", "6 MONTHS", RED, "S5"),
 4: ("RED FLAGS", "RANKED", RED, "S1"),
 5: ("ICK OR", "RED FLAG?", NAVY, "S3"),
 6: ("GOT THE NUMBER?", "NOW THIS", GREEN, "S1"),
 7: ("DATING ADVICE", "IS LYING", RED, "SHOCKED"),
 8: ("SHE DID", "THIS.", RED, "SHOCKED"),
 9: ("LOYALTY", "SIGNAL", GREEN, "SMITTEN"),
10: ("3 DATES", "3 DISASTERS", RED, "S5"),
11: ("ATTRACTIVE?", "NOT YOUR FACE", GREEN, "S1"),
12: ("THEY TEST", "YOU", RED, "S3"),
13: ("I CHASED", "PRETTY", RED, "S5"),
14: ("DESPERATE", "TEXTS", RED, "SHOCKED"),
15: ("INSECURITY", "LEAKS", RED, "S3"),
16: ("IT FELT", "AMAZING. TRAP.", RED, "SMITTEN"),
17: ("GHOSTED", "7 TIMES", RED, "S5"),
18: ("“TOO", "SENSITIVE”", RED, "S3"),
19: ("GREEN FLAGS", "NOBODY CLAPS FOR", GREEN, "S4"),
20: ("WATCH HOW", "THEY FIGHT", GREEN, "S2"),
21: ("1 YEAR", "OF APPS", NAVY, "S5"),
22: ("AFTER THE", "FIGHT", GREEN, "SMITTEN"),
23: ("YOUR PHOTOS", "ARE LYING", RED, "SHOCKED"),
24: ("THE 2-DATE", "RULE", GREEN, "S1"),
25: ("DOUBLE TEXT", "MATH", NAVY, "S2"),
26: ("“HEY”", "GETS IGNORED", RED, "S2"),
27: ("NICE ≠", "GOOD", RED, "SHOCKED"),
28: ("CHEMISTRY", "LIES", RED, "S3"),
29: ("THE WAITER", "TEST FAILS", NAVY, "S3"),
30: ("2AM TEXTS", "I REGRET", RED, "S5"),
31: ("$200 DATE?", "BIG MISTAKE", RED, "SHOCKED"),
32: ("BORING =", "GREEN FLAG", GREEN, "S4"),
33: ("LEAVE", "EARLY. NICELY.", GREEN, "S4"),
}
VARIANTS = {  # A/B for produced Short #1 (rank 1 pairs with the intro upload)
 "01A": ("100 DATES", "2 YEARS", RED, "S1"),
 "01B": ("I DATED 100", "SO YOU DON'T", GREEN, "S2"),
}

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

def fit(d, text, name, size, maxw):
    f = font(name, size)
    while d.textbbox((0, 0), text, font=f)[2] > maxw and size > 40:
        size -= 6; f = font(name, size)
    return f

def center(d, cy, text, f, fill, stroke=8, sfill=CREAM):
    b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
    w, h = b[2]-b[0], b[3]-b[1]
    d.text(((W-w)/2 - b[0], cy - h/2 - b[1]), text, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=sfill)
    return h

def make(fname, l1, l2, accent, pose):
    img = Image.new("RGB", (W, H), CREAM)
    # pose art: cover-fit full frame, biased to upper-middle
    p = Image.open(os.path.join(POSES, pose + ".png")).convert("RGB")
    s = W / p.width
    p = p.resize((W, int(p.height * s)), Image.LANCZOS)
    img.paste(p, (0, 320 - int(p.height * 0.06)))
    d = ImageDraw.Draw(img)
    # top punch block
    f1 = fit(d, l1, "Anton-Regular.ttf", 165, 980)
    f2 = fit(d, l2, "Anton-Regular.ttf", 165, 980)
    center(d, 250, l1, f1, accent)
    center(d, 460, l2, f2, NAVY)
    # bottom wordmark (inside frame, below grid-crop critical zone)
    d.rectangle([W//2 - 200, 1700, W//2 - 10, 1726], fill=RED)
    d.rectangle([W//2 + 10, 1700, W//2 + 200, 1726], fill=GREEN)
    fw = font("ArchivoBlack-Regular.ttf", 54)
    center(d, 1790, "DATE & ADVICE", fw, NAVY, 4, CREAM)
    img.save(os.path.join(HERE, fname))
    return img

def slugify(t):
    import re
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return "-".join(s.split("-")[:6])

rows = {int(r["rank"]): r for r in csv.DictReader(open(CSVP))}
made = []
for rank in sorted(P):
    l1, l2, acc, pose = P[rank]
    slug = slugify(rows[rank]["title"])
    fname = f"{rank:02d}-{slug}.png"
    make(fname, l1, l2, acc, pose)
    made.append(fname)
for key, (l1, l2, acc, pose) in VARIANTS.items():
    fname = f"{key}-{slugify(rows[1]['title'])}.png"
    make(fname, l1, l2, acc, pose)
    made.append(fname)

# contact sheet 6x6 grid (35 covers) at 180x320 each
cols, rows_n = 6, 6
sheet = Image.new("RGB", (cols*180, rows_n*320), "white")
for i, f in enumerate(made):
    im = Image.open(os.path.join(HERE, f)).resize((180, 320), Image.LANCZOS)
    sheet.paste(im, ((i % cols)*180, (i // cols)*320))
sheet.save(os.path.join(HERE, "_contact-sheet.png"))
# grid-size readability check of #1
Image.open(os.path.join(HERE, made[0])).resize((202, 360), Image.LANCZOS)\
     .save(os.path.join(HERE, "_grid-size-verify.png"))
print(f"made {len(made)} covers + contact sheet")
