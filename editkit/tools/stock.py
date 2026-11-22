"""Find and download REAL stock photos / footage / logos without any API key.
Usage:
  python3 tools/stock.py photo "hands counting cash" [-n 6] [--landscape]   Pexels photos   -> work/cand/<slug>/*.jpg
  python3 tools/stock.py video "barista pouring coffee" [-n 4]               Pexels videos   -> work/cand/<slug>/*.mp4
  python3 tools/stock.py commons "TikTok logo" [-n 6]                        Wikimedia Commons (logos, people, places, objects)
  python3 tools/stock.py open "night market jakarta" [-n 6]                  Openverse (CC-licensed photos, fallback)
Prints one line per file with its source URL and licence (copy the ones you use into work/visual_plan.md), then
writes a contact sheet work/cand/<slug>.jpg: OPEN IT and pick. Search in English, name the concrete object.
Pexels is searched through a headless browser (public search page). If it shows a bot check, use `open`/`commons`,
or let the user download the files by hand into video/public/."""
import sys, os, re, json, time, argparse, subprocess, urllib.request, urllib.parse, urllib.error
ap = argparse.ArgumentParser()
ap.add_argument("kind", choices=["photo", "video", "commons", "open"]); ap.add_argument("query")
ap.add_argument("-n", type=int, default=6); ap.add_argument("--landscape", action="store_true")
a = ap.parse_args()
slug = re.sub(r"[^a-z0-9]+", "-", a.query.lower()).strip("-")
out = f"work/cand/{slug}"; os.makedirs(out, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
BOT_UA = "aroll-edit-kit/1.0 (local video editing; python-urllib)"   # Wikimedia/Openverse want an honest, descriptive agent
def get(url, path=None):
    ua = UA if "pexels.com" in url else BOT_UA
    for attempt in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": ua}), timeout=60).read(); break
        except urllib.error.HTTPError as ex:
            if ex.code != 429 or attempt == 2: raise
            time.sleep(4 * (attempt + 1))       # rate limited: wait and retry
    time.sleep(0.6)
    if path: open(path, "wb").write(data)
    return data
def pexels_page(url):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
        pg = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 2400}).new_page()
        pg.goto(url, wait_until="domcontentloaded", timeout=60000); pg.wait_for_timeout(5000)
        html = pg.content(); b.close()
    return html
files = []
q = urllib.parse.quote(a.query)
if a.kind == "photo":
    html = pexels_page(f"https://www.pexels.com/search/{q}/?orientation={'landscape' if a.landscape else 'portrait'}")
    for pid in list(dict.fromkeys(re.findall(r"images\.pexels\.com/photos/(\d+)/", html)))[:a.n]:
        path = f"{out}/pexels_{pid}.jpg"
        try: get(f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=1600", path)
        except Exception as ex: print("  skip", pid, ex); continue
        files.append(path); print(f"{path}  <- https://www.pexels.com/photo/{pid}/  (Pexels licence: free to use)")
elif a.kind == "video":
    html = pexels_page(f"https://www.pexels.com/search/videos/{q}/?orientation={'landscape' if a.landscape else 'portrait'}")
    urls = {}
    for u in re.findall(r"https://videos\.pexels\.com/video-files/\d+/[^\"'\\ ]+?\.mp4", html):
        urls.setdefault(re.search(r"video-files/(\d+)/", u).group(1), u)
    for vid, u in list(urls.items())[:a.n]:
        path = f"{out}/pexels_{vid}.mp4"
        try: get(u, path)
        except Exception as ex: print("  skip", vid, ex); continue
        files.append(path); print(f"{path}  <- https://www.pexels.com/video/{vid}/  (Pexels licence: free to use)")
elif a.kind == "commons":
    # Wikimedia throttles originals and odd thumbnail sizes (HTTP 429): ask for the standard sizes 1280 / 960 / 500 only.
    cand = {}
    for w in (1280, 960, 500):
        api = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6"
               f"&gsrlimit={a.n}&gsrsearch={q}&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth={w}")
        for p in json.loads(get(api)).get("query", {}).get("pages", {}).values():
            ii = p["imageinfo"][0]
            c = cand.setdefault(p["title"], {"ii": ii, "tries": []})
            if ii.get("thumburl") and ii["thumburl"] not in c["tries"]: c["tries"].append(ii["thumburl"])
    for title, c in cand.items():
        ii = c["ii"]; name = re.sub(r"[^A-Za-z0-9.]+", "_", title[5:]); svg = name.lower().endswith(".svg")
        path = f"{out}/{name}.png" if svg else f"{out}/{name}"; ok = False   # an SVG is fetched as its PNG render (transparent)
        for src in c["tries"]:
            try: get(src, path); ok = True; break
            except Exception as ex: err = ex
        if not ok: print("  skip", name, err); continue
        if svg:                                                               # plus the vector itself when the server allows it
            try: get(ii["url"], f"{out}/{name}")
            except Exception: pass
        files.append(path); print(f"{path}  <- {ii['descriptionurl']}  ({ii['extmetadata'].get('LicenseShortName', {}).get('value', '?')})")
else:
    api = f"https://api.openverse.org/v1/images/?q={q}&page_size={a.n * 2}"
    for r in json.loads(get(api))["results"]:
        if len(files) >= a.n: break
        if max(r.get("width") or 0, r.get("height") or 0) < 900: continue
        path = f"{out}/openverse_{r['id'][:8]}.jpg"
        try: get(r["url"], path)
        except Exception as ex: print("  skip", r["id"][:8], ex); continue
        files.append(path); print(f"{path}  <- {r['foreign_landing_url']}  (CC {r['license']} {r.get('license_version', '')}, by {r.get('creator')})")
if not files: sys.exit("nothing found: try other English keywords, another source (open / commons), or ask the user for the asset")
if a.kind == "video":     # one mid frame per video so the candidates can be looked at
    thumbs = []
    for f in files:
        t = f[:-4] + ".jpg"; subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "1", "-i", f, "-frames:v", "1", t]); thumbs.append(t)
    files = [t for t in thumbs if os.path.exists(t)]
imgs = [f for f in files if not f.lower().endswith(".svg")]
if imgs: subprocess.run([sys.executable, "tools/sheet.py", "assets", f"work/cand/{slug}.jpg"] + imgs)
