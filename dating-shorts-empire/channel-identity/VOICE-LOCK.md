# 🔒 CHANNEL VOICE — LOCKED (user-approved)

**This is the official Date & Advice narrator voice for ALL videos.**

| Setting | Value |
|---|---|
| Voice | **Xavier** |
| voice_id | `43173c95-3ec8-446a-a162-6504332c578b` |
| voice_type | `preset` |
| Engine (model) | `text2speech_v2` |
| **variant** | **`elevenlabs`** ← this is what makes it sound natural |
| Cost | ~0.3 credits per take |

## ❌ Do NOT use
- Plain `seed_audio` (reads monotone — user rejected it).
- `voice_change` conversion of a personal recording (still reads robotic — user rejected it, session V5).

## How the intro was produced (repeatable recipe)
1. Split the script into 2–4 natural **sentence-group takes** (whole sentences = best prosody; avoid tiny fragments — they sound choppy).
2. Generate each take: `generate_audio` → `text2speech_v2`, `variant:"elevenlabs"`, the voice_id above.
3. Trim leading/trailing silence off each take, concat with ~0.14s gaps.
4. Fit under 60s: mild pitch-safe tempo (`atempo`, cap ~1.06×) + `loudnorm=I=-14`.
5. Time captions to the concatenated track via silence-detected phrase spans (see `shorts/prep_vo.py` / `assemble_01b.py` pattern).

ElevenLabs reads ~190 wpm, so ~175 script words ≈ 57–58s — a full ~175-word script fits one Short with a light tempo trim.

Reference build: intro `shorts/01-intro.mp4` (57.0s), takes were tts-A/B/C via this exact recipe (session 2026-07-20).
