# COST REPORT — Date & Advice build session (2026-07-17)

## Higgsfield credits — measured, not estimated
Balance cross-check: **start 261.85** (00:59 UTC) → **end 218.15** = **43.70 credits spent**, which matches the itemized transaction log below to the cent. Budget cap was 157 (AUTO = 60% of start); **27.8% of cap used**.

> Plan note: the account showed `plus` at boot and `free` by session end. That downgrade is why `kling3_0_turbo` (1080p video) and `virality_predictor` (automated QC) returned "requires basic plan or higher" mid-session — both were routed around (seedance 720p + manual QC).

### Per-asset ledger (from `transactions`, session window 03:32–04:53 UTC)
| Phase | Asset | Model | Credits |
|---|---|---|---|
| P2 | Master character sheet v1 | nano_banana_pro | 2.0 |
| P2 | Redesign edit (user direction) | nano_banana_2 | 1.5 |
| P2 | Green-A emblem edit (user direction) | nano_banana_2 | 1.5 |
| P2 | pfp art | seedream_v5_lite | 1.0 |
| P2 | banner art | seedream_v5_lite | 1.0 |
| P5 | Stills S1–S6 | seedream_v5_lite ×6 | 6.0 |
| P5 | VO takes T1–T7 (Xavier) | seed_audio ×7 | 4.7 |
| P5 | Hook clip V1 (8s) | seedance1_5 | 9.6 |
| P5 | Talking clip V2 (8s) | seedance1_5 | 9.6 |
| P5 | Red-flag clip V3 (4s) | seedance1_5 | 4.8 |
| P6 | Cover poses (smitten, shocked) | seedream_v5_lite ×2 | 2.0 |
| | **Total** | | **43.70** |

### Phase totals
| Phase | Credits |
|---|---|
| P2 Brand + avatar (one-time) | 7.0 |
| P5 Short 01 production | 34.7 |
| P6 Covers (35 covers from 2 new + 6 reused poses, composed locally) | 2.0 |
| P1/P3/P4/P7/P8 (research, scripts, packages, report) | 0 |

### Cost per finished Short & projections
- **Short 01 direct cost: 34.7 credits** (~40s, 25 beats, 16 generated assets).
- Repeatable per-Short cost going forward: **~30–35 credits** (brand assets amortized; reaction stills reusable).
- **All 33 ideas produced at this efficiency: ~1,000–1,150 credits** (i.e., a 1,000-credit pack ≈ a month of daily Shorts, or ~4.4× the current remaining 218.15 balance).
- Covers scale essentially free: 35 covers cost 2.0 credits total (local composition), ~0.06/cover.

## Claude side (labeled honestly)
`npx ccusage session` for this session: **308 input + 138,146 output + 631,091 cache-write + ~28.25M cache-read ≈ 29.0M total tokens → $47.78 at API list rates.**
⚠️ ccusage prices tokens at API rates — on a Pro/Max subscription this session drew from the plan's included usage rather than billing that amount. Run `/cost` (API billing view) or `/usage` (subscription limits view) inside Claude Code for the official numbers.

## Summary block
| Metric | Value |
|---|---|
| Wall-clock elapsed | ~4h 10m (00:57–05:07 UTC, incl. ~35 min paused waiting for the user's script + ~90 min of research blocked until the WebSearch window reset at 02:30) |
| Shorts produced | 1 of 1 provided script (40s, 1080×1920) — plus 1 bonus draft in overdrive if budget allows |
| Generated assets | 21 Higgsfield jobs (10 identity/pose images, 6 stills, 3 video clips... see ledger) |
| Files delivered | see FINAL manifest (research 3, identity 10+, scripts 3, shorts 1 MP4 + tooling, covers 35 + sheet, packages 34, monetization 2, overdrive 5+, reports 3) |
| Credits: spent / cap / balance | 43.70 / 157 / 218.15 remaining |
| Cost per Short | 34.7 cr direct; ~30–35 cr repeatable |
| 30-day calendar fill estimate | 29 more Shorts × ~33 cr ≈ **~960 credits** (assumes current models/prices, ~10 gen-assets per Short, covers/packages already done — estimate, not a quote) |
