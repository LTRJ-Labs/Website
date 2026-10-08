# LTRJ Labs Website — context

Single-page static site for ltrjlabs.com (GitHub Pages, `CNAME` = www.ltrjlabs.com). No build step, no framework.

## Status (as of 2026-10-07)
- Branch `overhaul` replaces the old Bootstrap multi-page site (still on `dev`/`main` and in git history).
- Four design directions are live for comparison; the final pick has **not** been made yet:
  - A · Ethereal — `index.html` + `css/main.css` + `js/main.js` (follows the brief most closely)
  - B · Notebook — `concepts/notebook.html` (light graph-paper, editorial serif)
  - C · Console — `concepts/console.html` (bento instrument panel, simulated telemetry, click-to-load 3D model)
  - D · Monolith — `concepts/monolith.html` (full-screen chapters, huge type)
- `js/concepts.js` injects a temporary switcher on every page. Remove it (and its `<script>` tags) once a direction is chosen, then delete unused concepts.

## Source of truth
- `docs/BRIEF.md` — original handoff brief. Copy in its "Core Copy" section must be used verbatim.
- Brand: safety orange `#FF6600` / `#FF7A1A` on near-black `#08080a`. Logo SVGs in `img/logo/` (single-colour orange).

## Conventions
- Concepts B–D are self-contained (inline CSS/JS) so they can be deleted cleanly.
- Photos in `img/photo/` are pre-resized to 2000px JPEG q72; keep new photos similarly small.
- `img/model/mothnode-enclosure.glb` is ~10 MB — only load on user action.
- Analytics: `js/analytics.js` (GA4 `G-508YGMKJ4D`); add `data-track="id"` to links to log CTA clicks.
- Every page must work at 390px wide with no horizontal scroll, and respect `prefers-reduced-motion`.

## Open questions
- Investors & hardware contact is `puritch@ltrjlabs.com` (carried over from the old site) — confirm.
- Old privacy page was removed; site still runs GA, so consider adding one back.
- `img/photo/lab-portrait.jpg` is kept but unused.
- Preview: `python3 -m http.server` → http://localhost:8000
