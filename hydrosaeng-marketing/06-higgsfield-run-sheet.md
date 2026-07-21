# Higgsfield Run-Sheet — finish the video (5 min once on Basic plan)

**Status:** Everything up to animation is DONE and saved in your Higgsfield workspace.
The only blocked step is video generation, which requires at least the **Basic plan**
(free plan returns `job_minimum_basic_plan_required` for every video model). Once you
upgrade, run the steps below — or start a new session and I'll run them for you.

## Already created (reusable, in your Higgsfield account)
- **Sora Reference Element** (locked identity): `d5f7fcc0-3d77-4fd5-aadd-9b0c358a1695`
- **6 start-frame images** (Sora consistent, blush/caramel UGC, 9:16, IP-check clean):

| Clip | Start-frame job ID | Scene |
|------|--------------------|-------|
| 1 (hook) | `5049535c-263c-40f3-bcc3-e25c9ad099ed` | holds pink serum near cheek, knowing smile |
| 2 | `60fdcd99-c0fd-45bd-9519-73ae7c46f3e5` | touches jaw/cheek, rueful |
| 3 | `02abd5a8-8398-437d-86c4-78eedf5b9d5f` | dropper macro, drop forming |
| 4 | `a87f394c-8434-44f6-8b83-15e433b3d179` | pats serum into cheeks, serene |
| 5 | `5e11b6d1-3dd4-4b94-a177-1535a09ea838` | dewy glow, soft genuine smile |
| 6 (CTA) | `6a7939bc-5c0d-4532-a233-10ba4b4bbeec` | holds bottle beside face, warm smile |

## Step 1 — Animate each frame (image-to-video)
- **Model:** `kling3_0_turbo` (7.5 cr/clip, cheapest) — or `seedance_2_0` (22.5, higher quality).
- **Per clip params:** `duration: 5`, `resolution: 720p`, `aspect_ratio: 9:16`,
  `medias: [{ value: <start-frame job ID>, role: start_image }]`
- **Motion prompts:**
  1. "Subtle motion: warm knowing smile, gently lifts the pink serum bottle closer to her cheek, one soft blink, gentle handheld selfie sway."
  2. "Subtle motion: fingertips slowly graze her jawline and cheek, thoughtful rueful expression, one natural blink, gentle handheld sway."
  3. "Subtle motion: gently squeezes the dropper, a single glistening drop forms and falls toward her fingertip, soft light glint, macro, minimal camera move."
  4. "Subtle motion: softly pats and presses serum into her cheeks, eyes relaxed, calm serene expression, gentle handheld sway."
  5. "Subtle motion: turns her face slightly to catch soft morning light and breaks into a gentle genuine smile, skin glowing, gentle handheld sway."
  6. "Subtle motion: holds the pink serum bottle beside her face, warm genuine nod and smile to camera, gentle handheld sway."

## Step 2 — Voiceover (generate_audio)
- **Model:** `seed_audio`, **voice:** preset `Maya` (`voice_id: b0f766b7-8703-4bd1-b973-f857c36837b6`, `voice_type: preset`)
- One line per clip (matches the script in 03):
  1. "I quit retinol — and this pink serum is what I replaced it with."
  2. "My skin was always tight, flaky, never quite happy. So I switched to this PDRN serum."
  3. "Three drops before bed."
  4. "No sting, no peeling, no purge phase."
  5. "A few weeks in, my skin just looks smoother. More hydrated. That glassy look I thought I'd aged out of."
  6. "Nothing else changed. If your skin's done with harsh actives — it's the gentle one, linked in my bio."

## Step 3 — Assemble (explainer_video)
- 6 blocks, in order, each `{ video: <clip job ID>, audio: <voice job ID> }`
- `width: 720, height: 1280`, `subtitles: { font: "patrick" }` (burns spoken captions)

## Step 4 — On-screen text overlays (add natively in TikTok/CapCut)
Clip1 "I quit retinol 👀" · Clip2 "tight, flaky, never happy" · Clip3 "3 drops before bed" ·
Clip4 "no sting · no peel · no purge" · Clip5 "a few weeks in… 🫧" · Clip6 "the gentle one — in my bio 🩷"

## Estimated cost to finish
6× Kling Turbo (45) + 6 short voice lines (~small) + assembly (free) + subtitles (~0.3) ≈ **~50 credits.**
