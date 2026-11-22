# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.48"]
# ///
"""
Render the README graphics from the HTML sources in this folder.

    uv run assets/src/render.py            # everything
    uv run assets/src/render.py banner     # just one

Uses the locally installed Google Chrome (channel="chrome"), so no Playwright
browser download is needed. Fonts come from Google Fonts at render time; the
output PNGs are self-contained, which is why we ship PNGs instead of SVGs
(GitHub renders <img> SVGs without web fonts, so text reflowed per OS).
"""

import shutil
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SRC = Path(__file__).resolve().parent
OUT = SRC.parent

# name -> (css width, viewport height, device scale factor, transparent corners)
TARGETS = {
    "banner": (1280, 400, 2, True),
    "ecosystem-map": (960, 600, 2, True),  # 960 wide so small type survives README width
    "social-preview": (1280, 640, 1, False),  # GitHub wants exactly 1280x640
}


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        only = set(sys.argv[1:])  # optional: render just these names
        for name, (w, h, scale, transparent) in TARGETS.items():
            if only and name not in only:
                continue
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
            page.goto((SRC / f"{name}.html").as_uri())
            page.wait_for_load_state("networkidle")
            page.evaluate("document.fonts.ready")
            out = OUT / f"{name}.png"
            # Screenshot the card itself so its height follows the content.
            page.locator(".card").screenshot(path=str(out), omit_background=transparent)
            # Photo and grain PNGs are large; pngquant gets them back under ~400 KB.
            if shutil.which("pngquant"):
                subprocess.run(["pngquant", "--quality", "80-95", "--speed", "1", "--force",
                                "--output", str(out), str(out)], check=True)
            print(f"wrote {out.relative_to(OUT.parent)}")
            page.close()
        browser.close()


if __name__ == "__main__":
    main()
