## LTRJ Labs Website

Single-page site for [ltrjlabs.com](https://www.ltrjlabs.com). Static HTML/CSS/JS, no build step.

```
index.html          Concept A — Ethereal (main page)
css/main.css        Styles for index.html
js/main.js          Scroll reveal, nav highlight, card glow
js/analytics.js     GA4 + CTA click tracking (data-track="...")
concepts/           Alternate design directions (B Notebook, C Console, D Monolith)
js/concepts.js      TEMPORARY concept switcher — remove once a direction is picked
img/logo, img/photo, img/model
```

Preview locally: `python3 -m http.server` then open http://localhost:8000.
