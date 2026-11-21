# AGENTS.md

Curated awesome list. `README.md` is the product; keep entries factual and clean-room (see `CONTRIBUTING.md`).

## Graphics

- `assets/banner.png`, `assets/ecosystem-map.png` and `assets/social-preview.png` are **rendered**, not hand-edited.
  Sources live in `assets/src/*.html` (+ `shared.css`, `sunset.jpg`). Re-render with:

  ```bash
  uv run assets/src/render.py
  ```

- Ship PNGs, not SVGs with text: GitHub renders `<img>` SVGs without web fonts, so text reflows per OS.
- When a project is added to or removed from the README, update the lanes in `assets/src/ecosystem-map.html` and re-render.
- `social-preview.png` must stay exactly 1280x640 and under 1 MB; upload it in repo Settings > Social preview after changes.
