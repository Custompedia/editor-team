"""Find every abrupt picture change in the rendered video and compare with the planned ones.
Any hard change that is NOT explained by the plan is a bug (flash, popped zoom, wrong frame).
Usage: python3 tools/scene_check.py <file.mp4> [threshold=0.08]"""
import sys, re, json, subprocess
video = sys.argv[1]; th = sys.argv[2] if len(sys.argv) > 2 else "0.08"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vf",
                f"scale=270:480,select='gt(scene,{th})',metadata=print:file=/tmp/_scene.txt", "-an", "-f", "null", "-"], check=True)
found = [(round(float(a) * 30), float(b)) for a, b in re.findall(r"pts_time:([\d.]+)\n.*?scene_score=([\d.]+)", open("/tmp/_scene.txt").read())]
d = json.load(open("video/src/data.json"))
fulls = [e for e in d["events"] if e["type"] in d["fullTypes"]]
planned = {}
for e in fulls: planned[e["f"]] = "insert in: " + e["type"]; planned[e["t"]] = "insert out: " + e["type"]
for s in d["segs"][1:]: planned[s["start"]] = "segment join"
for e in d["events"]:
    for it in e.get("items", []): planned[it.get("f", -99)] = "overlay item"
    planned.setdefault(e["f"], "event start: " + e["type"])
    if e["type"] == "split": planned.setdefault(e["t"], "split out")
bad = 0
for f, score in found:
    why = next((planned[p] for p in planned if -8 <= f - p <= 14), None)   # fade-outs start ~7 frames before, slides last up to ~14 frames after
    if why is None: bad += 1
    print(f"frame {f:>5} ({f / 30:6.2f}s) score {score:.2f}  {why or '<<< UNEXPLAINED: look at this frame'}")
print(f"{len(found)} hard changes, {bad} unexplained")
