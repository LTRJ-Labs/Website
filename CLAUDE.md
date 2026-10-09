# LTRJ Labs Website — context

Single-page static site for ltrjlabs.com (GitHub Pages, `CNAME` = www.ltrjlabs.com). No build step, no framework.

## Status (as of 2026-10-09)
- Branch `overhaul` replaces the old Bootstrap multi-page site (still on `dev`/`main` and in git history).
- Direction chosen: **Swiss / International Typographic Style**. The whole site is `index.html` (inline CSS/JS). Press G to toggle the 12-col grid overlay.
- No top bar / nav and no logo at the top by design; the hero is a centred, left-aligned square block. The orange logo fills the footer.
- Light/dark theme: fixed switch bottom-right sets `data-theme="dark"` on `<html>` (remembered in localStorage `ltrj-theme`; `?theme=dark` forces dark for previews). All colours are CSS tokens in `:root` / `:root[data-theme="dark"]` — don't hard-code colours.
- MothNode links go to **https://mothnode.net** (the brief's `mothnode.com` is outdated).
- Events uses a calendar-leaf card (layout borrowed from the old Neumorphism concept, flattened to Swiss blocks); timeline is a vertical track with square markers.
- All other concepts (Ethereal, Monolith, Neumorphism, Bento, Minimalism, etc.) and the concept switcher are deleted but recoverable from git history.

## Source of truth
- `docs/BRIEF.md` — original handoff brief. Copy in its "Core Copy" section must be used verbatim.
- Brand: Swiss page uses paper `#f4f3ef`, ink `#0a0a0a`, signal orange `#ff5a00`. Logos live in `img/SVGLogos/` (orange + `_Black` variants), `img/HiResLogos/`, `img/LowResLogos/` — always use these files, never retype the wordmark.

## Conventions
- Photos in `img/photo/` are pre-resized to 2000px JPEG q72; keep new photos similarly small.
- `img/model/mothnode-enclosure.glb` (~10 MB) is unused — delete it or only load it on user action.
- Analytics: `js/analytics.js` (GA4 `G-508YGMKJ4D`); add `data-track="id"` to links to log CTA clicks.
- Every page must work at 390px wide with no horizontal scroll, and respect `prefers-reduced-motion`.

## Open questions
- Investors & hardware contact is `puritch@ltrjlabs.com` (carried over from the old site) — confirm.
- Old privacy page was removed; site still runs GA, so consider adding one back.
- `img/photo/lab-portrait.jpg` is kept but unused.
- Preview: `python3 -m http.server` → http://localhost:8000
