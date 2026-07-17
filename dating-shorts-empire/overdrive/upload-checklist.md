# First-Upload Checklist — step by step

## 1. Create the channel (~10 min)
1. youtube.com → sign in → avatar → "Create a channel".
2. Name: **Date & Advice** · Handle: **@DateAndAdvice** (fallbacks: @DateAndAdviceShow, @DateAdvice).
3. YouTube Studio → Customization → Basic info → paste the bio from `channel-identity/README.md`.

## 2. Upload identity assets (~5 min)
- Picture: `channel-identity/pfp.png`
- Banner: `channel-identity/banner.png`
- Video watermark: `channel-identity/watermark.png`
(Placement details: `channel-identity/README.md`.)

## 3. Affiliate before first upload (~15 min)
1. Apply: https://www.online-therapy.com/affiliate.php (steps in `monetization/affiliate-dossier.md`).
2. Once you have your link, run the one-liner in `monetization/replace-link.md`.
3. Verify: `grep -rn '{{AFFILIATE_LINK}}' dating-shorts-empire || echo done`.

## 4. QC the Short (non-negotiable human pass)
Watch `shorts/01-100-dates-intro.mp4` **muted first, then with sound** — checklist in `shorts/QC-NOTES.md`.

## 5. Upload
1. Upload from the **mobile app** if you want to set the cover image (YouTube only allows Shorts cover selection on mobile; on desktop you'd be stuck with an auto frame). 
2. Copy title/description/tags/pinned comment from `posting-packages/00-channel-intro-READY-TO-POST.md`.
3. **Disclosure:** in upload details, open "Altered content" and answer YES — this video is AI-generated animation with an AI voice. Required by YouTube's synthetic-media policy; the label is minor for animation-style content and protects the channel.
4. Visibility: Public. Post at 6–8 PM local (see calendar).
5. Immediately post the pinned comment, then pin it.

## 6. Shorts covers — how they work
- The cover shows on your channel's Shorts grid and in some search surfaces (not in the swipe feed itself).
- Set it during mobile upload: tap the pencil on the preview → choose frame OR upload from gallery → pick `covers/01A-*.png`.
- A/B plan: 01A for the first 48h; if the grid click-through feels weak and swipe-away is high, switch to 01B (Edit → cover) and compare the next 48h.

## 7. After posting (first hour matters most)
- Reply to every comment in hour one (see `growth-playbook.md`).
- Don't delete and re-upload unless something is factually broken — re-uploads reset velocity.
