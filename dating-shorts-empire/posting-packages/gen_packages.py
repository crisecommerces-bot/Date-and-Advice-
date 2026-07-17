#!/usr/bin/env python3
"""Generate 33 posting packages + _master.csv from research/ideas.csv."""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CSVP = os.path.join(HERE, "..", "research", "ideas.csv")
FTC = "Some links are affiliate links — I may earn a commission at no extra cost to you."
CTA = ("Feeling stuck on the self-work part? Online therapy is the cheat code: "
       "{{AFFILIATE_LINK}}")

QUESTION = {
 1: "What's the red flag that made YOU leave a date early?",
 2: "Which phrase have you heard word-for-word? Drop it below.",
 3: "What's the biggest red flag you ignored — and for how long?",
 4: "Which red flag do you think is overrated? Defend it.",
 5: "Name an ick that people treat like a felony.",
 6: "What do you text first after getting a number?",
 7: "What's the worst dating advice you've ever followed?",
 8: "Would you have stayed or left? Tell me why.",
 9: "What loyalty green flag do you look for on date one?",
10: "Story time: what's YOUR biggest first-date disaster?",
11: "What's the most attractive non-physical trait? Go.",
12: "Ever caught someone testing you? What did they do?",
13: "Looks or character — what fooled you longer?",
14: "What texting habit instantly turns you off?",
15: "Which insecure behavior did you have to unlearn?",
16: "Have you ever been love-bombed? How did it end?",
17: "How many times have you been ghosted? Be honest.",
18: "What's a gaslighting phrase you'll never forget?",
19: "What's a green flag nobody talks about?",
20: "How does your partner argue? Red or green flag?",
21: "What's your #1 dating app lesson from year one?",
22: "What does a healthy after-fight look like to you?",
23: "Which photo slot is ruining profiles? 1st, 2nd, or 3rd?",
24: "Do you know by date 2? Or does it take longer?",
25: "Double text: confident or desperate? Pick a side.",
26: "What's the best first message you've ever received?",
27: "Nice vs good — who fooled you?",
28: "Chemistry or consistency — which betrayed you?",
29: "What's your real character test on a first date?",
30: "What's the worst 2am text you ever sent? (We won't judge.)",
31: "Cheapest date that turned into something real — go.",
32: "Was your best relationship 'boring' at first?",
33: "Have you ever left a date early? How did you do it?",
}

def slugify(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return "-".join(s.split("-")[:6])

def tags_for(kw, fmt):
    base = ["dating advice", "dating tips", kw, "relationship advice", "red flags",
            "green flags", "dating", "relationships", "date and advice", "shorts"]
    extra = {"RUN": ["red flag", "toxic relationships"],
             "LOOK": ["green flag", "healthy relationships"],
             "DONT": ["dating mistakes", "what not to do"],
             "DO": ["how to date", "dating hacks"],
             "EXPERIENCE": ["story time", "dating stories"],
             "DIFFERENT": ["lessons learned", "dating stories"]}.get(fmt, [])
    tags, total = [], 0
    for t in base + extra:
        if t not in tags and total + len(t) + 1 <= 480:
            tags.append(t); total += len(t) + 1
    return tags

rows = list(csv.DictReader(open(CSVP)))
master = []
for r in rows:
    rank = int(r["rank"]); slug = slugify(r["title"])
    produced = rank == 0  # set per-produced mapping below
    title = r["title"]
    if len(title) > 80: title = title[:77] + "..."
    hashtags = "#shorts #datingadvice #redflags #dating #relationships"
    desc = (f"{r['hook']}\n"
            f"{CTA}\n"
            f"{FTC}\n\n"
            f"Real {r['keyword']} lessons from 100+ real dates — no gimmicks, no sugarcoating. "
            f"New dating advice Shorts from Date & Advice every week: the dos, the don'ts, "
            f"and the stories behind them.\n\n{hashtags}")
    tags = tags_for(r["keyword"], r["format"])
    pin = (f"{QUESTION[rank]}\n\n"
           f"And if this hit home, the tool I recommend is here: {{{{AFFILIATE_LINK}}}}\n{FTC}")
    body = f"""# Posting Package #{rank:02d} — {r['title']}

## Title (<=80 chars)
{title}

## Description
```
{desc}
```

## Tags ({sum(len(t) for t in tags) + len(tags) - 1} chars)
```
{', '.join(tags)}
```

## Pinned comment
```
{pin}
```

## Cover
`covers/{rank:02d}-{slug}.png`{' (+ A/B variants 01A/01B)' if rank == 1 else ''}
"""
    with open(os.path.join(HERE, f"{rank:02d}-{slug}.md"), "w") as f:
        f.write(body)
    master.append({"rank": rank, "title": title, "description": desc.replace("\n", " | "),
                   "tags": ", ".join(tags)})

with open(os.path.join(HERE, "_master.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["rank", "title", "description", "tags"])
    w.writeheader(); w.writerows(master)
print(f"wrote {len(rows)} packages + _master.csv")
