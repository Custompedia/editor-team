"""Turn the edit decisions (work/edit.json) + word timestamps (work/tx/*.json) into video/src/data.json.
Everything in the video is anchored to WORDS, never to hand-typed frame numbers, so moving a cut
re-times every subtitle, visual and sound effect automatically.
Usage: python3 tools/build_timeline.py"""
import json, re, sys
E = json.load(open("work/edit.json"))
FPS = E.get("fps", 30)
FULL_TYPES = set(E.get("full_types", ["photo", "clip", "screenshot", "custom", "outro"]))  # cover the whole frame
W = {k: json.load(open(f"work/tx/{v}.json")) for k, v in E["clips"].items()}

# 1) manual word-timing fixes: {"A": {"39": [15.08, 15.60]}}
for k, fixes in E.get("timing", {}).items():
    for i, (s, e) in fixes.items():
        W[k][int(i)]["s"], W[k][int(i)]["e"] = s, e

# 2) segments -> output frames
segs, f = [], 0
for s in E["segments"]:
    d = round((s["out"] - s["in"]) * FPS)
    segs.append({"k": s["clip"], "src": E["clips"][s["clip"]] + ".mp4", "in": s["in"], "out": s["out"], "start": f, "dur": d})
    f += d
total = f + E.get("outro_frames", 0)

def T(k, t):
    """source time in clip k -> output frame (time inside a removed part snaps to the next kept segment)"""
    for s in segs:
        if s["k"] == k and s["in"] - 0.05 <= t <= s["out"] + 0.05:
            return s["start"] + round((t - s["in"]) * FPS)
    for s in segs:
        if s["k"] == k and t < s["in"]:
            return s["start"]
    raise SystemExit(f"time {t} of clip {k} is after the last kept segment")

def anchor(a):
    """int = absolute frame | "end" = last frame | [clip, wordIndex, frameOffset=0, side="s"|"e"]"""
    if isinstance(a, int): return a
    if a == "end": return total
    k, i = a[0], a[1]
    off = a[2] if len(a) > 2 else 0
    side = a[3] if len(a) > 3 else "s"
    return max(0, min(total, T(k, W[k][i][side]) + off))

# 3) words that survive the cut, with text overrides: {"A": {"39": "*NamaBrand", "40": ""}}
#    "*word" = emphasised keyword (big style), "" = hide the word (stumble that stays in the audio)
#    "script": {"A": [{"from": 0, "text": "Nah, aku tuh ... *harganya *berapa?"}]} rewrites a run of words in one go:
#    one token per Whisper word starting at index "from"; "_" hides a word; "~" is a space inside one token.
words = []
for k in E["clips"]:
    ov = dict(E.get("text", {}).get(k, {}))
    for block in E.get("script", {}).get(k, []):
        toks = block["text"].split()
        if block["from"] + len(toks) > len(W[k]): raise SystemExit(f"script block for clip {k} from {block['from']} has {len(toks)} tokens but only {len(W[k]) - block['from']} words remain")
        for n, tok in enumerate(toks):
            ov.setdefault(str(block["from"] + n), "" if tok == "_" else tok.replace("~", " "))
    for i, w in enumerate(W[k]):
        mid = (w["s"] + w["e"]) / 2      # a word belongs to the segment that contains its middle
        seg = next((s for s in segs if s["k"] == k and s["in"] <= mid < s["out"]), None)
        t = ov.get(str(i), w["w"])
        if seg is None:
            if t and any(s["k"] == k and w["s"] < s["out"] and w["e"] > s["in"] for s in segs):
                print(f"WARNING: word {k}{i} '{w['w']}' ({w['s']}-{w['e']}) only partly inside a segment -> no subtitle. If it is audible, fix its time in \"timing\"; if not, ignore.")
            continue
        if not t: continue
        words.append({"k": k, "t": t, "f": T(k, max(w["s"], seg["in"])), "e": T(k, min(w["e"], seg["out"]))})
words.sort(key=lambda w: w["f"])

# 4) subtitle chunks: short phrases; a trailing run of *emphasised* words becomes the big line
MAXC, MAXW = E.get("sub_max_chars", 24), E.get("sub_max_words", 4)
subs, cur = [], []
def flush():
    global cur
    if not cur: return
    j = len(cur)
    while j > 0 and cur[j - 1]["t"].startswith("*"): j -= 1
    strip = lambda ws: [{"t": w["t"].replace("*", ""), "f": w["f"]} for w in ws]
    subs.append({"f": cur[0]["f"], "t": cur[-1]["e"], "small": strip(cur[:j]), "big": strip(cur[j:])})
    cur = []
for w in words:
    if cur:
        prev = cur[-1]; ln = sum(len(x["t"]) for x in cur) + len(cur)
        if (w["f"] - prev["e"] > 9                                   # pause
                or (prev["t"].startswith("*") and not w["t"].startswith("*"))  # keyword ends the chunk
                or re.search(r'[.?!"”]$', prev["t"])                # sentence end
                or ln + len(w["t"]) > MAXC or len(cur) >= MAXW
                or (prev["t"].endswith(",") and ln > 12)
                or w["k"] != prev["k"] or w["f"] < prev["f"]):
            flush()
    cur.append(w)
flush()
for a, b in zip(subs, subs[1:]):
    a["t"] = min(max(a["t"] + 4, a["f"] + 8), b["f"])     # hold a little, never overlap the next chunk
if subs: subs[-1]["t"] = min(total, subs[-1]["t"] + 10)

# 5) events (visuals) -> frames
events = []
for ev in E.get("events", []):
    e = dict(ev); e["f"], e["t"] = anchor(ev["start"]), anchor(ev["end"])
    del e["start"], e["end"]
    for key, val in list(e.items()):                 # any other "*_at" field is an anchor too (e.g. "tap_at")
        if key.endswith("_at"): e[key] = anchor(val)
    for it in e.get("items", []):
        for key in list(it):
            if key == "at": it["f"] = anchor(it.pop("at"))
            elif key.endswith("_at"): it[key] = anchor(it[key])
    if e["type"] == "custom": e.setdefault("light", True)   # diagrams are bright by default -> dark subtitles over them
    if e["t"] - e["f"] < 20: print("WARNING: event shorter than 20 frames:", e["type"], e["f"], e["t"])
    events.append(e)
events.sort(key=lambda e: e["f"])
fulls = [e for e in events if e["type"] in FULL_TYPES]
for a, b in zip(fulls, fulls[1:]):
    if b["f"] < a["t"]: raise SystemExit(f"full-screen events overlap: {a['type']}@{a['f']}-{a['t']} and {b['type']}@{b['f']}")
    if 0 < b["f"] - a["t"] < 24: print(f"WARNING: speaker visible only {b['f'] - a['t']} frames between two inserts at {a['t']}: chain them (same frame) or widen the gap")
# split panels (visual on top, speaker below): may touch a full-screen insert or another split, never overlap one
splits = [e for e in events if e["type"] == "split"]
for e in splits:
    if e.get("shift", 300) > e.get("h", 760): raise SystemExit(f"split@{e['f']}: shift must be <= h, or black shows above the speaker")
    for x in fulls + splits:
        if x is not e and x["f"] < e["t"] and e["f"] < x["t"]: raise SystemExit(f"split@{e['f']}-{e['t']} overlaps {x['type']}@{x['f']}-{x['t']}: make them touch (same frame) or separate them")
    e["pre"] = any(x["t"] == e["f"] for x in fulls); e["post"] = any(x["f"] == e["t"] for x in fulls)
    e["chainPrev"] = any(x["t"] == e["f"] for x in splits); e["chainNext"] = any(x["f"] == e["t"] for x in splits)
    for x in events:
        if x["type"] not in FULL_TYPES and x["type"] != "split" and x["f"] < e["t"] and e["f"] < x["t"]:
            print(f"WARNING: overlay {x['type']}@{x['f']} is on screen during split@{e['f']}: both use the top of the frame, move one")

# 6) speaker zoom levels ("shots"): change ONLY where it cannot look like a glitch:
#    - while a full-screen insert hides the speaker, or
#    - exactly on an exposed jump cut (a segment join with no insert over it) = classic punch-in
groups = []
for e in fulls:
    if groups and groups[-1][-1]["t"] == e["f"]: groups[-1].append(e)
    else: groups.append([e])
hidden = [g[0]["f"] + 12 for g in groups if g[-1]["t"] < total]
joins = [s["start"] for s in segs[1:] if not any(e["f"] + 7 <= s["start"] < e["t"] - 6 for e in fulls)]
shots, z = [], 1.0
for c in sorted(set([0] + hidden + joins)):
    if c: z = 1.0 if z > 1.03 else (1.09 if c in joins else 1.07)
    shots.append({"f": c, "z": z})

# 7) sound effects
sfx = []
for e in fulls:
    chained = any(x["t"] == e["f"] for x in fulls)
    sfx.append({"f": e["f"] + (2 if chained else 0), "k": "swish" if chained else "whoosh"})
    if "click_at" in e: sfx.append({"f": e["click_at"], "k": "click"})
for e in events:
    if e["type"] == "split":
        sfx.append({"f": e["f"], "k": "swish"})
        if "click_at" in e: sfx.append({"f": e["click_at"], "k": "click"})
    elif e["type"] not in FULL_TYPES:
        sfx += [{"f": it["f"], "k": "pop"} for it in e.get("items", []) if "f" in it] or [{"f": e["f"], "k": "pop"}]

json.dump({"fps": FPS, "total": total, "segs": segs, "framing": E.get("framing", {}), "subs": subs, "events": events,
           "fullTypes": sorted(FULL_TYPES), "shots": shots, "sfx": sfx, "keepCase": E.get("keep_case", []), "music": E.get("music")},
          open("video/src/data.json", "w"), ensure_ascii=False, indent=1)

# report: read it every time
covered = sum(e["t"] - e["f"] for e in fulls)
print(f"total {total} frames = {total / FPS:.1f}s | {len(segs)} segments | {len(subs)} subtitle chunks | full-screen inserts cover {100 * covered / total:.0f}%"
      f" | split panels {100 * sum(e['t'] - e['f'] for e in splits) / total:.0f}%")
print("exposed jump cuts (speaker visible across a cut) at frames:", joins or "none")
for e in events: print(f"  {e['type']:<11}{e['f']:>5} -> {e['t']:<5} {(e['t'] - e['f']) / FPS:.1f}s")
for s in subs: print(f"  {s['f']:>5} {' '.join(w['t'] for w in s['small'])} | {' '.join(w['t'] for w in s['big'])}")
