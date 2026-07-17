# QC Notes — what YOU should review before uploading

## Automated QC status (honest)
- Higgsfield `virality_predictor` and `video_analysis` are **gated above this account's plan** (`Requires basic plan or higher`) — automated hook-scoring was not available. Logged in DECISIONS.md.
- Manual QC performed instead: ffprobe spec check (1080×1920, 30fps, h264+aac, loudnorm −14 LUFS), frame-by-frame spot check of 8 beats (captions inside safe zone, brand palette, character consistency), beat-length audit (all 25 beats ≤ 2.0s), duration 39.77s (inside the 40–50s target window, under the 60s hard ceiling).

## Short 01 — `01-100-dates-intro.mp4` (39.77s, 25 beats)
Watch it TWICE before uploading — once muted, once with sound:
1. **Muted pass:** do the caption boxes alone tell the story? (They should — every beat carries one.) Check no caption clips the YouTube UI zones on your phone.
2. **Sound pass:** VO is 7 concatenated takes — listen for tonal jumps at block boundaries (~3.7s, ~8.8s, ~13.3s, ~21.2s, ~25.9s, ~33.4s). Take-to-take voice consistency was good in generation, but your ear is the final check.
3. **Factual check (your story, your claims):** "more than a hundred dates in two years", "social experiment", the book tease — confirm you're comfortable with each on camera-of-record.
4. **Beat 3 & 16 (tally cards):** tally clusters render 4-bar groups struck through — reads as "many", not literally 100. OK?
5. **720p sources:** video beats were generated at 720p (1080p video models are plan-gated) and upscaled to 1080×1920 in assembly. On a phone screen this is effectively invisible; on a monitor you may notice softness in the 3 video-clip beats vs. the razor-sharp still/card beats. If it bothers you, `upscale_video` on V1–V3 before a re-assembly is a ~1-line change.
6. **Loop test:** let it replay — last beat (FOLLOW card) hard-cuts back into the "100 DATES" hook. Feels seamless?
7. **AI disclosure:** this is fully AI-animated + AI-voiced. Tick YouTube's altered/synthetic content disclosure on upload (see `overdrive/upload-checklist.md`).


## Short 02 — `02-leave-before-dessert.mp4` (39.60s, 22 beats) — ⚠️ script NOT yet approved
1. **Approve (or edit) the script first**: `scripts/02-draft-CLAUDE-NOT-APPROVED.md`. It's my draft, advice-framed on purpose — no invented personal stories. Strongly consider swapping T3–T4 for a real moment from your 100 dates, then re-voice those two takes (~1.2cr) and reassemble (`python3 shorts/assemble_02.py`).
2. Same muted + sound double-watch as Short 01.
3. T7 sets up a "flag that looks green but isn't" follow-up — only keep it if you plan to make that video (it maps to idea #16, Love-Bombing).
4. Same 720p-source caveat on the 2 video-clip beats as Short 01.

## Voice v2 (2026-07-17, second session)
Both MP4s re-voiced with ElevenLabs-engine Xavier (user pick after audition). Old seed_audio takes removed; block boundaries shifted slightly (01: 39.77→42.10s, 02: 39.60→38.70s) — re-do the muted/sound double-watch on the NEW files.

## Avatar v3 (webtoon restyle — user approved Sample A)
Both MP4s rebuilt with the Ace-Final webtoon avatar (user's hero portrait + turnaround as identity). Same VO (ElevenLabs Xavier), same durations (42.10s / 38.70s). Re-do the muted/sound double-watch. Note: kinetic text cards kept the cream brand background against the new white scene background — intentional contrast, flag it if you want them white.
