# LTRJ Labs Website — context

Single-page static site for ltrjlabs.com (GitHub Pages, `CNAME` = www.ltrjlabs.com). No build step, no framework.

## Status (as of 2026-10-07)
- Branch `overhaul` replaces the old Bootstrap multi-page site (still on `dev`/`main` and in git history).
- Six design directions are live for comparison (shortlisted 2026-10-08); the final pick has **not** been made yet:
  - A · Ethereal — `index.html` + `css/main.css` + `js/main.js` (follows the brief most closely)
  - B · Monolith — `concepts/monolith.html` (full-screen chapters, huge type)
  - C · Neumorphism — `concepts/neumorphism.html` (soft extruded UI, light/dark switch)
  - D · Bento Grid — `concepts/bento.html` (every section as tiles in one 12-col grid)
  - E · Swiss — `concepts/swiss.html` (International Typographic Style; press G for grid overlay)
  - F · Minimalism — `concepts/minimal.html` (single column, follows system dark mode)
- Removed concepts (Notebook, Console, and the other style studies) are in git history before this shortlist.
- `js/concepts.js` injects a temporary switcher on every page (prev/next arrows, jump menu, `[` / `]` keys). Remove it (and its `<script>` tags) once a direction is chosen, then delete unused concepts.

## Source of truth
- `docs/BRIEF.md` — original handoff brief. Copy in its "Core Copy" section must be used verbatim.
- Brand: safety orange `#FF6600` / `#FF7A1A` on near-black `#08080a`. Logo SVGs in `img/logo/` (single-colour orange).

## Conventions
- Concepts B–F are self-contained (inline CSS/JS) so they can be deleted cleanly.
- Photos in `img/photo/` are pre-resized to 2000px JPEG q72; keep new photos similarly small.
- `img/model/mothnode-enclosure.glb` (~10 MB) is unused since Console was removed — delete it or only load it on user action.
- Analytics: `js/analytics.js` (GA4 `G-508YGMKJ4D`); add `data-track="id"` to links to log CTA clicks.
- Every page must work at 390px wide with no horizontal scroll, and respect `prefers-reduced-motion`.

## Open questions
- Investors & hardware contact is `puritch@ltrjlabs.com` (carried over from the old site) — confirm.
- Old privacy page was removed; site still runs GA, so consider adding one back.
- `img/photo/lab-portrait.jpg` is kept but unused.
- Preview: `python3 -m http.server` → http://localhost:8000
