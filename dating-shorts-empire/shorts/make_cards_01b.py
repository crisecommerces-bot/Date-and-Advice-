#!/usr/bin/env python3
"""Three extra cards for intro v2 (user-voice edition)."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "channel-identity", "fonts")
OUT = os.path.join(HERE, "cards01b"); os.makedirs(OUT, exist_ok=True)
NAVY=(30,42,69); CREAM=(255,246,236); RED=(255,71,87); GREEN=(46,213,115)
W,H = 1080,1920
def font(n,s): return ImageFont.truetype(os.path.join(FONTS,n),s)
def center(d,cy,t,f,fill,stroke=0,sf=None):
    b=d.textbbox((0,0),t,font=f,stroke_width=stroke)
    d.text(((W-b[2]+b[0])/2-b[0],cy-(b[3]-b[1])/2-b[1]),t,font=f,fill=fill,stroke_width=stroke,stroke_fill=sf)

# CB1 — DO'S & DON'TS (check vs cross)
img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
center(d,600,"THE DO'S",font("Anton-Regular.ttf",160),GREEN)
center(d,830,"& DON'TS",font("Anton-Regular.ttf",160),RED)
d.line([340,1080,470,1210],fill=GREEN,width=34); d.line([470,1210,700,960],fill=GREEN,width=34)
d.line([660,1300,860,1500],fill=RED,width=34); d.line([860,1300,660,1500],fill=RED,width=34)
img.save(os.path.join(OUT,"CB1.png"))

# CB2 — REAL. UNFILTERED.
img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
center(d,660,"REAL.",font("Anton-Regular.ttf",220),NAVY)
center(d,940,"UNFILTERED.",font("Anton-Regular.ttf",140),RED)
center(d,1180,"ADVICE.",font("Anton-Regular.ttf",180),NAVY)
img.save(os.path.join(OUT,"CB2.png"))

# CB3 — LIKE + SUBSCRIBE end card
img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
center(d,700,"LIKE",font("Anton-Regular.ttf",230),RED)
center(d,950,"+ SUBSCRIBE",font("Anton-Regular.ttf",130),NAVY)
d.rectangle([340,1120,530,1150],fill=RED); d.rectangle([550,1120,740,1150],fill=GREEN)
center(d,1280,"DATE & ADVICE",font("ArchivoBlack-Regular.ttf",72),NAVY)
img.save(os.path.join(OUT,"CB3.png"))
print("cards01b:", sorted(os.listdir(OUT)))
