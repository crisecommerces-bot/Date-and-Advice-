# Channel Identity — What Goes Where in YouTube Studio

| File | Where it goes | How |
|---|---|---|
| `pfp.png` | Profile picture | YouTube Studio → Customization → Branding → **Picture** → Upload. (Square source; YouTube crops to a circle — the face is centered so nothing important is lost. Must read at 98×98 px — verified by downscale test.) |
| `banner.png` | Channel banner | Customization → Branding → **Banner image**. 2560×1440; everything critical (Ace + "DATE & ADVICE" + tagline) sits inside the 1546×423 TV/desktop/mobile safe zone. |
| `watermark.png` | Video watermark | Customization → Branding → **Video watermark**. Shows bottom-right on desktop players; keep "entire video" display setting. |
| `master-character-sheet.png` | Nowhere (internal) | The single source of truth for Ace. Registered on Higgsfield as element `Ace-DatingMascot-Master` (`1949b5d7-5025-4ff4-bd7b-e456848c1f58`) — embed it in every future avatar generation. |
| `fonts/` | Nowhere (internal) | Anton / Archivo Black / Inter — the caption + cover fonts used by the production scripts. |

Channel fields while you're in Studio:
- **Name:** Date & Advice
- **Handle:** @DateAndAdvice (fallbacks: @DateAndAdviceShow, @DateAdvice)
- **Description (bio):** Dating advice from the friend who's been through it. Red flags, green flags, and the stories behind them — 45 seconds at a time.
- Add `{{AFFILIATE_LINK}}` as a channel link once you've signed up (see `monetization/`).

Provenance: `pfp-raw.png` / `banner-raw.png` are the untouched Higgsfield outputs; `master-character-sheet-v1/v2.png` are earlier design iterations (hoodie concept → user-directed redesign → final green-A version).
