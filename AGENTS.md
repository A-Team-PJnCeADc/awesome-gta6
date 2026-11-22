# AGENTS.md

Curated awesome list. `README.md` is the product; keep entries factual and clean-room (see `CONTRIBUTING.md`).

## Graphics

- `assets/banner.png`, `assets/ecosystem-map.png` and `assets/social-preview.png` are **rendered**, not hand-edited.
  Sources live in `assets/src/*.html` (+ `shared.css`, `sunset.jpg`). Re-render with:

  ```bash
  uv run assets/src/render.py
  ```

- Ship PNGs, not SVGs with text: GitHub renders `<img>` SVGs without web fonts, so text reflows per OS.
- When a project is added to or removed from the README, update the `COLS` / `SPECS` lists in `assets/src/ecosystem-map.html` and re-render (the big numbers are counted from those lists).
- Keep the graphics plain: the photo, flat colours, one typeface per job. No gradient text, glass chips, grain, or glow; that look reads as AI-generated. The map is drawn at 960 CSS px so its smallest type stays readable at README width.

## README layout

- Top of the page stays short: banner, tagline, one badge row, nav row, one-line warning. The long callouts live in "Safety & Scope" near the end. No Contents list (the nav row and GitHub's outline cover it).
- Project tables have two columns: `**[Name](url)**&nbsp;<star badge><br><sub>stack (license) · platform</sub>` and a description of one to three sentences. Copy a neighbouring row for the badge markup. Trim, don't pile on: per-release detail belongs in the project's README.
- `social-preview.png` must stay exactly 1280x640 and under 1 MB; upload it in repo Settings > Social preview after changes.

---

Ahmet Dedeler · [github.com/Ahmet-Dedeler](https://github.com/Ahmet-Dedeler) · [ahmetdedeler.com](https://ahmetdedeler.com)
