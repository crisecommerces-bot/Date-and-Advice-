# Beat map for intro v2 (AI-VOICE edition). t_end = absolute seconds in the
# AI-voice vo-final.wav (58.51s). Anchored to silence-detected phrase spans.
NAVY=(30,42,69,255); RED=(255,71,87,255); GREEN=(46,213,115,255)
BEATS = [
    (1.90,  "V2", "vid",   {"t0":0.0},              "I'M JOHN",                GREEN),
    (5.20,  "V1", "vid",   {"t0":0.0},              "A 2-YEAR EXPERIMENT",     RED),
    (8.40,  "K1", "card",  {},                      None,                      None),
    (13.27, "V2", "vid",   {"t0":2.0},              "HOW WOMEN THINK",         NAVY),
    (15.30, "SMITTEN","still",{},                   "WHAT TRIGGERS ATTRACTION",RED),
    (16.60, "V3", "vid",   {"t0":0.0},              "SPOT RED FLAGS",          RED),
    (19.38, "CB1","card",  {},                      None,                      None),
    (21.43, "S4", "still", {},                      "STAY OR WALK AWAY",       GREEN),
    (25.06, "S2", "still", {},                      "EVERYTHING I LEARNED",    NAVY),
    (26.78, "CB2","card",  {},                      None,                      None),
    (30.70, "V2", "vid",   {"t0":4.5,"zoom":1.25},  "BETTER AT DATING",        GREEN),
    (32.40, "S1", "still", {},                      "FOR THE BROS",            NAVY),
    (33.47, "S1", "still", {"z0":1.3,"z1":1.45,"ytop":0.05}, "I GOT YOU.",     GREEN),
    (37.07, "SHOCKED","still",{},                   "I SEARCHED YOUTUBE",      NAVY),
    (39.00, "SHOCKED","still",{"z0":1.3,"z1":1.45,"ytop":0.05},"NO REAL DATING CHANNEL",RED),
    (40.72, "S3", "still", {},                      "FOR THE BROS",            RED),
    (43.39, "V2", "vid",   {"t0":6.0},              "MY UNFILTERED TRUTH",     NAVY),
    (46.20, "V2", "vid",   {"t0":1.0,"zoom":1.2},   "REAL EXPERIENCE",         GREEN),
    (48.60, "S1", "still", {},                      "KNOWLEDGE. SHARED.",      NAVY),
    (51.66, "S6", "still", {},                      "THE BOOK IS COMING",      RED),
    (55.27, "V1", "vid",   {"t0":5.5,"zoom":1.2},   "LIKE + SUBSCRIBE",        GREEN),
    (58.51, "CB3","card",  {},                      None,                      None),
]
