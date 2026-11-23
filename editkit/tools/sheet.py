"""Contact sheets you can LOOK at (the agent must open the resulting jpg files).
  python3 tools/sheet.py stills <out.jpg> [frame ...]     grid of video/out/f*.jpg (all, or the listed frames)
  python3 tools/sheet.py video <file.mp4> <prefix> [every_sec=1]   one frame per N seconds -> <prefix>_0.jpg, _1.jpg ...
  python3 tools/sheet.py strips <file.mp4> <prefix>       12 consecutive frames around EVERY transition in data.json
  python3 tools/sheet.py assets <out.jpg> <img> [img ...]  grid of candidate images with their file names"""
import sys, glob, json, os, subprocess, tempfile
from PIL import Image, ImageDraw

def grid(items, out, cols, W, H):
    """items: list of (PIL image, label)"""
    rows = (len(items) + cols - 1) // cols
    sh = Image.new("RGB", (cols * W, rows * H), "black"); d = ImageDraw.Draw(sh)
    for i, (im, label) in enumerate(items):
        if im.mode in ("RGBA", "LA", "P"):                      # transparent logos: show them on light grey, not black
            im = im.convert("RGBA"); bg = Image.new("RGBA", im.size, (225, 225, 228, 255)); bg.alpha_composite(im); im = bg
        im = im.convert("RGB"); im.thumbnail((W, H))
        x, y = (i % cols) * W, (i // cols) * H
        sh.paste(im, (x, y)); d.rectangle([x, y, x + 8 * len(label) + 8, y + 16], fill="black"); d.text((x + 4, y + 2), label, fill="yellow")
    sh.save(out, quality=85); print(out, sh.size)

def grab(video, frame, fps=30, W=216, H=384):
    with tempfile.TemporaryDirectory(prefix="sheet_") as td:     # per-process temp file: parallel jobs never share it
        tmp = os.path.join(td, "frame.jpg")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "%.4f" % (frame / fps + 0.5 / fps), "-i", video, "-frames:v", "1",
                        "-vf", f"scale={W}:{H}", "-q:v", "4", tmp], check=True)
        with Image.open(tmp) as im: return im.copy()

mode = sys.argv[1]
if mode == "stills":
    fs = sorted(glob.glob("video/out/f*.jpg")) if len(sys.argv) < 4 else ["video/out/f%05d.jpg" % int(x) for x in sys.argv[3:]]
    grid([(Image.open(f), os.path.basename(f)[1:6]) for f in fs], sys.argv[2], min(6, len(fs)), 360, 640)
elif mode == "assets":
    grid([(Image.open(f), os.path.basename(f)[:26]) for f in sys.argv[3:]], sys.argv[2], 6, 300, 460)
elif mode == "video":
    video, prefix = sys.argv[2], sys.argv[3]; every = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video], capture_output=True, text=True).stdout)
    times = [t for t in (i * every for i in range(int(dur / every) + 1)) if t < dur - 2 / 30]   # job02: a sample on/after the last frame crashed ffmpeg
    for part in range(0, len(times), 44):
        grid([(grab(video, round(t * 30), W=270, H=480), "%.0fs" % t) for t in times[part:part + 44]], f"{prefix}_{part // 44}.jpg", 11, 270, 480)
elif mode == "strips":
    video, prefix = sys.argv[2], sys.argv[3]
    d = json.load(open("video/src/data.json"))
    fulls = [e for e in d["events"] if e["type"] in d["fullTypes"]]
    points = [("in  " + e["type"], e["f"]) for e in fulls] + [("out " + e["type"], e["t"]) for e in fulls if e["t"] < d["total"]]
    points += [(n + " split", e[k]) for e in d["events"] if e["type"] == "split" for n, k in (("in ", "f"), ("out", "t")) if e[k] < d["total"]]
    points += [("join", s["start"]) for s in d["segs"][1:]] + [("zoom", s["f"]) for s in d["shots"][1:]]
    points = sorted(set(points), key=lambda p: p[1])
    rows = [[(grab(video, f), f"{name} {f}") for f in range(max(0, c - 5), min(d["total"], c + 7))] for name, c in points]
    for part in range(0, len(rows), 8):
        grid([x for r in rows[part:part + 8] for x in (r + [(Image.new("RGB", (216, 384)), "")] * (12 - len(r)))], f"{prefix}_{part // 8}.jpg", 12, 216, 384)
