# Replace {{AFFILIATE_LINK}} project-wide

After your affiliate application is approved, copy your real tracked link and run ONE of these from the repo root (`dating-shorts-empire/`'s parent). Replace `https://your.real/link` first.

**Linux (GNU sed):**
```bash
grep -rl '{{AFFILIATE_LINK}}' dating-shorts-empire | xargs sed -i 's|{{AFFILIATE_LINK}}|https://your.real/link|g'
```

**macOS (BSD sed):**
```bash
grep -rl '{{AFFILIATE_LINK}}' dating-shorts-empire | xargs sed -i '' 's|{{AFFILIATE_LINK}}|https://your.real/link|g'
```

**Verify nothing was missed:**
```bash
grep -rn '{{AFFILIATE_LINK}}' dating-shorts-empire || echo "✅ all replaced"
```

Notes:
- The `|` delimiter means URLs with `/` need no escaping.
- If your link contains `&` (query params), escape it as `\&` in the replacement string.
- Re-run the verify command after; it should print "✅ all replaced".
