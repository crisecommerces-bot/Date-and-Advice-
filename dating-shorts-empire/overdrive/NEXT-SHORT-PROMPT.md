# NEXT-SHORT-PROMPT — the repeatable machine

Paste everything below the line into a fresh Claude Code session in this repo, then paste your raw script where marked. Output: a finished vertical MP4 + posting package, matching this project's brand exactly.

---

Produce Short #NN for the "Date & Advice" channel in this repo (`dating-shorts-empire/`). Read `CHECKPOINT.md`, `DECISIONS.md`, and `report/model-economics.md` first — they define the environment quirks (blocked egress → use the GitHub Actions asset relay via `.asset-manifest.json`) and the pipeline.

FIXED PROJECT STANDARDS (do not re-derive):
- Character: reference element `Ace-DatingMascot-Master` (id `1949b5d7-5025-4ff4-bd7b-e456848c1f58`) — embed `<<<1949b5d7-5025-4ff4-bd7b-e456848c1f58>>>` in every avatar image prompt. Master sheet: `channel-identity/master-character-sheet.png`.
- Voice: Xavier via ElevenLabs — model `text2speech_v2` with `variant: "elevenlabs"`, `voice_id 43173c95-3ec8-446a-a162-6504332c578b`, `voice_type preset`, beat-sized takes (0.3cr each). Do NOT use plain seed_audio (user rejected its flat delivery).
- Models: stills `seedream_v5_lite` (1cr) + element ref; non-avatar stills `z_image` (0.15cr); video `seedance1_5` 9:16 (4s=4.8cr / 8s=9.6cr) with `start_image` = a generated still's job id; NEVER `gemini_omni` (30cr) or kling (plan-gated). Submit ONE job per model family at a time (429s otherwise). Decline any preset_recommendation notice with `declined_preset_id`.
- Brand: colors #FF4757 / #2ED573 / #1E2A45 on #FFF6EC; fonts in `channel-identity/fonts/`; red/green flag motif.
- Script rules: ~45s (110–150 words), hook in line one (no greeting), open loop early + close it last, 2–4 beats each ending on a turn, one micro-CTA max, save raw to `scripts/NN-raw.md`, final to `scripts/NN-final.md`, beat map table to `scripts/NN-beat-map.md` (≤2s per visual hold, avatar in hook + every ~8s + closer, captions every beat, ~10 unique generated assets serving ~24 beats via punch-ins/re-crops).
- Assembly: copy `shorts/assemble_01.py` to `assemble_NN.py`, adjust the BLOCKS table to the new beat map (block per VO take, beats per block sized so take_duration/beats ≤ 2.0s), assets in `shorts/assetsNN/`, cards via a `make_cards.py` variant. Output `shorts/NN-<slug>.mp4`, 1080×1920, loudnorm -14 LUFS, <60s hard.
- Download route: append {url, path} entries to `dating-shorts-empire/.asset-manifest.json`, commit + push (relay workflow fetches and commits), `git pull` to receive.
- Budget: check `balance` before batches; log every judgment call in `DECISIONS.md`; append the Short's row to `report/COST-REPORT.md`.
- Deliver: MP4 + QC notes appended to `shorts/QC-NOTES.md` + posting package `posting-packages/NN-<slug>.md` marked READY TO POST (copy format from `01-*.md`), cover via `covers/compose_covers.py` pattern.

MY RAW SCRIPT (rewrite for retention per the rules above, show me the rewrite for ONE approval, then run everything else autonomously):

<<<PASTE RAW SCRIPT HERE>>>
