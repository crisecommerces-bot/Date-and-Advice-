# Final Video — Production Record

**Status:** Produced (pending user visual QC). ~30s, 720×1280 vertical, testimonial.

## Final assembled video
- **Job ID:** `3383e26b-8ef3-476c-8812-6ee2f8fa8353` (explainer_video: 6 blocks + Maya VO + burned speech captions)

## Reusable Higgsfield references
- **Sora** (character): `d5f7fcc0-3d77-4fd5-aadd-9b0c358a1695`
- **HydroSaeng-Serum** (real bottle, prop): `e01f9de4-2524-4908-9027-f895e6e6dd03`
- Voice: preset **Maya** `b0f766b7-8703-4bd1-b973-f857c36837b6`

## Per-clip assets (start frame → animated clip → voice line)
| # | Scene | Start frame (image) | Clip (video) | Voice (audio) | Real bottle |
|---|-------|--------------------|--------------|---------------|-------------|
| 1 | hook — bottle near cheek | `a56411b9…` | `2f1e869c…` | `7112c3b9…` | ✅ |
| 2 | touches jaw, glass skin | `9ea1a718…` | `9d3926bb…` | `607f9853…` | — |
| 3 | dropper macro | `77944a6a…` | `88b8149c…` | `8aacc4db…` | ✅ |
| 4 | pats serum in | `8feb03d7…` | `6e91e64a…` | `1848020e…` | — |
| 5 | dewy glow smile | `6874cdc0…` | `69584a64…` | `9b5449cd…` | — |
| 6 | CTA — bottle beside face | `efbf69aa…` | `aeb8a3e1…` | `54ab0c8a…` | ✅ |

## Notes
- Sora recast to relatable ~40 East-Asian woman with flawless glass skin (no wrinkles) per brand direction.
- Real product registered from user-uploaded packshots (media `97fa6bfc…`, `4916a3cb…`).
- To regenerate any single clip: re-run its start-frame prompt (03 / run-sheet) then Kling 3.0 Turbo
  (720p, 9:16, 5s) with that frame as `start_image`; re-assemble via explainer_video.
- On-screen text overlays (per 03) added natively in TikTok/CapCut on top of the burned captions.
