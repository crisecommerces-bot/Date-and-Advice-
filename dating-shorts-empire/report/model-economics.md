# Model Economics — measured via get_cost preflights (2026-07-17)

Starting balance: **261.85 credits** (plan: plus). Budget cap (AUTO 60%): **157 credits**.

## Image models (9:16 supported unless noted)
| Model | Credits/image | Notes |
|---|---|---|
| `z_image` | **0.15** | Cheapest. Text-to-image only (no reference input) — use for backgrounds/props where avatar isn't needed |
| `nano_banana_2_lite` | 1.00 | Cheap general model |
| `seedream_v5_lite` | 1.00 | **Supports reference elements/character** → pick for all avatar-consistent images |
| `recraft_v4_1` | 1.25 | Vector-style specialist (flat 2D) |
| `nano_banana_2` | 1.50 | Reference support, 1k default |
| `nano_banana_pro` | 2.00 | Premium; use only for master character sheet quality anchor if needed |

## Video models (9:16 native)
| Model | Credits | Per-second | Notes |
|---|---|---|---|
| `seedance1_5` | 4.8 (4s) / 9.6 (8s) | **1.20/s** | Durations [4, 8, 12]. Cheapest per second |
| `kling3_0_turbo` | 9.0 (6s) | 1.50/s | 3–15s flexible, 720p/**1080p**, `start_image` image-to-video confirmed → animate our own stills = character consistency |
| `wan2_6` | 13 (5s) | 2.60/s | Durations [5, 10, 15] |
| `seedance_2_0_mini` | 15 (6s) | 2.50/s | |
| `gemini_omni` | 30 (10s) | 3.00/s | video-explainer workflow default — too expensive for our budget |

## Audio
| Model | Credits | Notes |
|---|---|---|
| `seed_audio` (TTS) | **0.5 / take** | Per beat-sized narration take. Voice: **Xavier** (user-selected), voice_id `43173c95-3ec8-446a-a162-6504332c578b`, voice_type `preset` — same voice across every Short |

## Pipeline decision (vertical Shorts assembly)
- Higgsfield's catalog exposes ONE workflow: `video-explainer` (N × fixed 10s blocks, server-side `explainer_video` assembly, 720×1280 vertical, gemini_omni clips at 30cr/block). At ~150cr per 50s Short it does not fit the 157cr cap, and fixed 10s single-clip blocks can't honor the ≤2s visual-change rule or true 1080×1920.
- **Chosen pipeline (hybrid):** generate stills (`seedream_v5_lite` w/ character reference + `z_image` for non-avatar shots) and 2–4 hero video clips per Short (`kling3_0_turbo` @1080p, `start_image` = our own avatar stills), narration via `seed_audio` (Xavier) in beat-sized takes — then assemble locally with ffmpeg: punch-ins/re-crops turn one asset into 2–4 beats, brand-font captions (Anton/Archivo Black, downloaded) burned in the safe zone, exact 1080×1920 output.

## Per-Short cost model (45s, ~22–28 beats, ~10 unique assets)
| Item | Qty | Credits |
|---|---|---|
| Avatar stills (seedream_v5_lite w/ ref) | 5–6 | 5–6 |
| Non-avatar stills (z_image) | 3–4 | ~0.6 |
| Video clips (kling3_0_turbo 5–6s @1080p) | 2–3 | 15–27 |
| Narration takes (seed_audio) | 5–7 | 2.5–3.5 |
| **Total per Short** | | **~23–37** |

## QC tools
- `virality_predictor` / `video_analysis_*` — cost checked at time of use; run once per finished Short if affordable.
