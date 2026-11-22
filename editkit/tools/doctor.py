"""Preflight: is this machine ready to edit? Run it before the first edit and whenever something fails.
Usage: python3 tools/doctor.py        (run from the project folder, with the venv active if you use one)
Prints OK / WARN / FAIL per requirement with the fix. Exit code 1 if anything is FAIL."""
import sys, os, shutil, subprocess, json, importlib, platform
bad = 0
def say(level, name, msg=""):
    global bad
    bad += level == "FAIL"
    print(f"[{level:<4}] {name}" + (f": {msg}" if msg else ""))
def run(cmd, **kw):
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=180, shell=isinstance(cmd, str), **kw)
    except Exception as ex: return subprocess.CompletedProcess(cmd, 1, "", str(ex))

print(f"system: {platform.system()} {platform.machine()}, python {platform.python_version()}, {os.cpu_count()} cpu threads")
# --- python
say("OK" if sys.version_info >= (3, 9) else "FAIL", "python >= 3.9", platform.python_version())
if os.path.isdir(".venv") and sys.prefix == sys.base_prefix:
    say("WARN", "venv", ".venv exists but is not active: prefix commands with `source .venv/bin/activate &&`")
for mod, pipname, need in [("faster_whisper", "faster-whisper", True), ("numpy", "numpy", True), ("PIL", "pillow", True),
                           ("playwright", "playwright", True), ("gdown", "gdown", False), ("yt_dlp", "yt-dlp", False)]:
    try:
        m = importlib.import_module(mod); say("OK", f"python module {pipname}", getattr(m, "__version__", ""))
    except Exception:
        say("FAIL" if need else "WARN", f"python module {pipname}", f"pip install {pipname}" + ("" if need else "  (optional: Google Drive / reference video download)"))
# --- ffmpeg
for tool in ("ffmpeg", "ffprobe"):
    say("OK" if shutil.which(tool) else "FAIL", tool, "" if shutil.which(tool) else "install ffmpeg (apt install ffmpeg / brew install ffmpeg / winget install Gyan.FFmpeg)")
if shutil.which("ffmpeg"):
    enc, flt = run(["ffmpeg", "-hide_banner", "-encoders"]).stdout, run(["ffmpeg", "-hide_banner", "-filters"]).stdout
    for name, hay in [("libx264", enc), ("aac", enc), ("loudnorm", flt), ("afftdn", flt), ("acompressor", flt), ("anoisesrc", flt), ("aevalsrc", flt)]:
        if name not in hay: say("FAIL", f"ffmpeg feature {name}", "this ffmpeg build is too minimal: install a full build")
    say("OK", "ffmpeg version", run(["ffmpeg", "-version"]).stdout.split("\n")[0][:60])
# --- node / remotion
node = run(["node", "-v"]).stdout.strip()
major = int(node[1:].split(".")[0]) if node.startswith("v") else 0
say("OK" if major >= 18 else "FAIL", "node >= 18 (20 recommended)", node or "not found: install Node 20 LTS")
say("OK" if shutil.which("npx") else "FAIL", "npx", "" if shutil.which("npx") else "comes with Node")
def ver(pkg):
    try: return json.load(open(f"video/node_modules/{pkg}/package.json"))["version"]
    except Exception: return None
if not os.path.exists("video/package.json"): say("FAIL", "video/ project", "kit files are missing: copy or extract the kit first")
elif not ver("remotion"): say("FAIL", "video/node_modules", "run: cd video && npm install")
else:
    say("OK" if ver("remotion") == "4.0.290" else "WARN", "remotion", f"{ver('remotion')} (tested with 4.0.290)")
    say("OK" if ver("typescript") == "5.5.4" else "FAIL", "typescript", f"{ver('typescript')} (must be 5.5.4: newer versions break Remotion's bundler)")
    r = run("npx remotion browser ensure", cwd="video")
    say("OK" if r.returncode == 0 else "FAIL", "remotion browser (Chrome Headless Shell)", "" if r.returncode == 0 else (r.stdout + r.stderr)[-300:] + "  Linux: install the shared libraries listed in the guide")
# --- playwright chromium
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto("about:blank"); b.close()
    say("OK", "playwright chromium launches")
except Exception as ex:
    say("FAIL", "playwright chromium", "run: python3 -m playwright install chromium   (Linux: add --with-deps)  | " + str(ex).split("\n")[0][:120])
# --- kit files, sfx, folders
need = ["tools/normalize.sh", "tools/transcribe.py", "tools/envelope.py", "tools/build_timeline.py", "tools/make_sfx.sh", "tools/shot.py", "tools/stock.py",
        "tools/sheet.py", "tools/scene_check.py", "tools/render.sh", "tools/verify_audio.py", "video/stills.mjs", "video/tsconfig.json",
        "video/src/index.ts", "video/src/Root.tsx", "video/src/theme.ts", "video/src/Main.tsx", "video/src/Visuals.tsx"]
missing = [f for f in need if not os.path.exists(f)]
say("FAIL" if missing else "OK", "kit files", "missing: " + ", ".join(missing) if missing else f"{len(need)} files")
sfx = [f for f in ("whoosh", "swish", "pop", "click") if not os.path.exists(f"video/public/sfx/{f}.wav")]
say("FAIL" if sfx else "OK", "sound effects", "run: bash tools/make_sfx.sh" if sfx else "4 files")
clips = [f for f in os.listdir("raw")] if os.path.isdir("raw") else []
say("OK" if clips else "WARN", "raw/ clips", f"{len(clips)} files" if clips else "put the source clips in raw/ (never edit them)")
# --- resources
free = shutil.disk_usage(".").free / 1e9
say("OK" if free > 10 else "WARN" if free > 5 else "FAIL", "free disk", f"{free:.0f} GB (need ~5 GB once for model + browsers + node_modules, plus ~2 GB per video)")
try:
    ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 1e9
    say("OK" if ram >= 15 else "WARN" if ram >= 7 else "FAIL", "RAM", f"{ram:.0f} GB" + ("" if ram >= 15 else "  (use WHISPER_MODEL=medium and CONCURRENCY=2 tools/render.sh)"))
except Exception: say("WARN", "RAM", "could not read; 16 GB recommended, 8 GB minimum")
hub = os.path.join(os.environ.get("HF_HOME", os.path.expanduser("~/.cache/huggingface")), "hub")
model = os.environ.get("WHISPER_MODEL", "large-v3")
cached = os.path.isdir(hub) and any(f"faster-whisper-{model}" in d for d in os.listdir(hub))
say("OK" if cached else "WARN", f"whisper model {model}", "cached" if cached else "not downloaded yet: the first transcription downloads ~3 GB (needs internet, once)")
# --- network (assets, fonts, model)
import urllib.request
for name, url in [("internet: fonts.googleapis.com", "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans"), ("internet: huggingface.co", "https://huggingface.co"), ("internet: pexels.com", "https://www.pexels.com/robots.txt")]:
    try: urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=15); say("OK", name)
    except Exception as ex: say("WARN", name, f"{str(ex)[:80]}  (agent sandbox without network? enable network access for the agent)")
print("\nRESULT:", "NOT READY: fix every FAIL above, then run this again" if bad else "READY")
sys.exit(1 if bad else 0)
