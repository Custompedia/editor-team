"""Screenshot a REAL web page (article, profile, search result, product page) as a phone-width PNG for a "screenshot" insert.
Usage: python3 tools/shot.py <url> <out.png> [--height 2000] [--find "text to locate" ...] [--desktop]
Output is 1080 px wide (540 css px at 2x; --desktop = 1280 css px at 1x). Prints the PNG size (-> img_w, img_h)
and, for every --find text, its box in IMAGE pixels (-> "highlights" or "click" in work/edit.json).
Public pages only: never log in, never bypass a private page. Login/cookie pop-ups are removed before the shot."""
import sys, argparse
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--height", type=int, default=2000); ap.add_argument("--find", action="append", default=[]); ap.add_argument("--desktop", action="store_true")
a = ap.parse_args()
cssw, scale = (1280, 1) if a.desktop else (540, 2)
UA = None if a.desktop else "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_context(viewport={"width": cssw, "height": a.height // scale}, device_scale_factor=scale, user_agent=UA, locale="id-ID").new_page()
    page.goto(a.url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(3500)
    # remove overlays that cover the content: dialogs, cookie bars, sticky ad/login banners
    page.evaluate("""() => { for (const el of document.querySelectorAll('[role=dialog],[aria-modal=true],[id*=cookie i],[class*=cookie i],[class*=consent i],[class*=popup i],[class*=modal i],[class*=overlay i]')) el.remove();
        document.documentElement.style.overflow = 'auto'; document.body.style.overflow = 'auto'; }""")
    page.wait_for_timeout(400)
    page.screenshot(path=a.out)
    print(f"{a.out}: img_w={cssw * scale} img_h={a.height // scale * scale}")
    for t in a.find:
        loc, box = page.get_by_text(t), None
        for i in range(min(loc.count(), 20)):          # first match that is actually visible inside the shot
            bb = loc.nth(i).bounding_box()
            if bb and bb["width"] > 0 and 0 <= bb["y"] < a.height // scale: box = bb; break
        print(f'  "{t}":', {"x": round(box["x"] * scale), "y": round(box["y"] * scale), "w": round(box["width"] * scale), "h": round(box["height"] * scale)}
              if box else "NOT FOUND in the shot (check the spelling; it may be inside an image or below --height)")
    b.close()
