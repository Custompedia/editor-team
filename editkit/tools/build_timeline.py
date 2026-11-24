"""Turn the edit decisions (work/edit.json) + word timestamps (work/tx/*.json) into video/src/data.json.
Everything in the video is anchored to WORDS, never to hand-typed frame numbers, so moving a cut
re-times every subtitle, visual and sound effect automatically.
Usage: python3 tools/build_timeline.py"""
import json, re, subprocess, sys
E = json.load(open("work/edit.json"))

# 0) the LOOK of this video is a decision, not a default: "theme" is required and has no fallback.
#    "theme": {"accent": "#RRGGBB", "light": "#RRGGBB", "ink": "#RRGGBB", "font_text": "<family>", "font_emph": "<family>",
#              "emph_style": "italic"|"normal", "why": "<reason>", optional "on_accent", "marker"}
THEME_HELP = """Decide the look of THIS video (accent colour, panel/text colours, fonts) from the brand, the footage and the brief,
write the choice + the reason in work/brief.md, then add to work/edit.json:
  "theme": {"accent": "#RRGGBB", "light": "#RRGGBB", "ink": "#RRGGBB",
            "font_text": "<installed font family>", "font_emph": "<installed font family>",
            "emph_style": "italic" | "normal", "why": "<the reason, same as in work/brief.md>"}
There is no default look (see edit-json.md, field "theme")."""
HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

def lum(hx):
    """relative luminance (WCAG) of #RGB / #RRGGBB"""
    hx = hx[1:]
    if len(hx) == 3: hx = "".join(c * 2 for c in hx)
    ch = [int(hx[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
contrast = lambda a, b: (max(lum(a), lum(b)) + 0.05) / (min(lum(a), lum(b)) + 0.05)

def check_theme(t):
    if not isinstance(t, dict): raise SystemExit("ERROR: work/edit.json has no \"theme\" block.\n" + THEME_HELP)
    errs = []
    for k in ("accent", "light", "ink"):
        if not isinstance(t.get(k), str) or not HEX.match(t[k].strip()): errs.append(f'theme.{k} must be a hex colour like "#DE6B17" (got {t.get(k)!r})')
    for k in ("on_accent", "marker"):     # optional
        if k in t and (not isinstance(t[k], str) or not HEX.match(t[k].strip())): errs.append(f'theme.{k} must be a hex colour like "#111111" (got {t[k]!r})')
    for k in ("font_text", "font_emph"):
        v = t.get(k)
        if not isinstance(v, str) or not v.strip() or re.search(r"[,'\"]", v): errs.append(f'theme.{k} must be ONE font family name without quotes or commas, e.g. "Poppins" (got {v!r})')
    if t.get("emph_style") not in ("italic", "normal"): errs.append(f'theme.emph_style must be "italic" or "normal" (got {t.get("emph_style")!r})')
    why = t.get("why")
    if not isinstance(why, str) or len(why.strip()) < 8: errs.append("theme.why is required: the reason for this look (brand colour/font, footage, brief), same as in work/brief.md")
    elif why.strip().upper().startswith("CONTOH"): errs.append("theme.why is still the text from edit.example.json: decide the look for THIS video and write your own reason")
    if errs: raise SystemExit("ERROR: invalid \"theme\" in work/edit.json:\n  - " + "\n  - ".join(errs) + "\n" + THEME_HELP)
    # fonts must be installed as SYSTEM fonts (web fonts hang the renderer here); fc-list lists every family name of every face
    try: out = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError) as x: raise SystemExit(f"ERROR: cannot run fc-list to check the theme fonts ({x})")
    fams = {n.strip().lower() for line in out.splitlines() for n in line.split(",") if n.strip()}
    missing = sorted({t[k].strip() for k in ("font_text", "font_emph") if t[k].strip().lower() not in fams})
    if missing: raise SystemExit(f"ERROR: theme font(s) not installed as system fonts: {', '.join(missing)}\n"
        "  Put the static .ttf/.otf files in /home/user/editkit/fonts, run: bash /home/user/editkit/tools/install_fonts.sh\n"
        "  then check: fc-list : family | grep -i '<name>'   and use the family name exactly as fc-list prints it.\n"
        "  Never load web fonts (@remotion/google-fonts, @remotion/fonts, FontFace): they hang the renderer here.")
    def slanted(fam):                # one bool per installed face of the family: True = italic/oblique face
        r = subprocess.run(["fc-list", f":family={fam}", "style"], capture_output=True, text=True).stdout
        return [any(w in line.lower() for w in ("italic", "oblique")) for line in r.splitlines() if line.strip()]
    for k, want in (("font_text", "normal"), ("font_emph", t["emph_style"])):
        fam, f = t[k].strip(), slanted(t[k].strip())
        if want == "italic" and not any(f):
            print(f"WARNING: theme.{k} '{fam}' has no italic face installed: Chrome will slant it artificially. Install the italic files or use emph_style \"normal\".")
        if want == "normal" and all(f):
            print(f"WARNING: theme.{k} '{fam}' has ONLY italic faces installed: it will render italic although \"normal\" is asked. Install the upright files or choose another font.")
    th = {k: t[k].strip() for k in ("accent", "light", "ink", "font_text", "font_emph", "emph_style")}
    # text drawn ON the accent (title highlight, chip numbers, SUMBER tag, CTA): the darker or lighter of ink/white, whichever reads better
    th["on_accent"] = t.get("on_accent", "").strip() or max([th["ink"], "#FFFFFF"], key=lambda c: contrast(c, th["accent"]))
    # screenshot marker-pen highlight (multiply): must be a LIGHT tint or it hides the text under it
    th["marker"] = t.get("marker", "").strip() or th["accent"]
    if lum(th["marker"]) < 0.35 and any(ev.get("type") == "screenshot" and ev.get("highlights") for ev in E.get("events", [])): print(f"WARNING: screenshot highlights use {th['marker']} with multiply: too dark, it will hide the text. Set theme.marker to a light tint of the accent (e.g. a pale version).")
    if contrast(th["ink"], th["light"]) < 4.5: print(f"WARNING: theme.ink {th['ink']} on theme.light {th['light']} has low contrast ({contrast(th['ink'], th['light']):.1f}:1, want >= 4.5)")
    print(f"theme: accent {th['accent']} (text on it {th['on_accent']}) | light {th['light']} ink {th['ink']} | text font '{th['font_text']}' | emphasis '{th['font_emph']}' {th['emph_style']}")
    return th
THEME = check_theme(E.get("theme"))
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
    sg = {"k": s["clip"], "src": E["clips"][s["clip"]] + ".mp4", "in": s["in"], "out": s["out"], "start": f, "dur": d}
    # optional designed move at a join (job05, generic): "enter"/"exit": {"scale": k, "x": px, "y": px, "frames": n}
    #   enter = the segment starts at k x its framing (+x,y screen px) and eases back to normal over n frames (match + pull back);
    #   exit  = over its last n frames it eases from normal to k x (+x,y) (push in to match the next shot). Zoom does not punch there.
    for key in ("enter", "exit"):
        if s.get(key): sg[key] = {"scale": float(s[key].get("scale", 1)), "x": float(s[key].get("x", 0)), "y": float(s[key].get("y", 0)), "frames": int(s[key].get("frames", 14))}
    segs.append(sg)
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
        words.append({"k": k, "i": i, "t": t, "f": T(k, max(w["s"], seg["in"])), "e": T(k, min(w["e"], seg["out"]))})
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
# "punch" (generic, job05): {"type": "punch", "start": anchor, "end": anchor, "z": 1.12} = speaker punch-in on a chosen word, no cut
#   (emphasis without a graphic, visual-craft.md 3). It only changes the speaker zoom (shots); it is not drawn as an overlay.
punches = [e for e in events if e["type"] == "punch"]
events = [e for e in events if e["type"] != "punch"]
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
designed = {sg["start"] for i, sg in enumerate(segs) if i and (sg.get("enter") or segs[i - 1].get("exit"))}   # move transition: base zoom, no punch-in
shots, z = [], 1.0
for c in sorted(set([0] + hidden + joins)):
    if c: z = 1.0 if (c in designed or z > 1.03) else (1.09 if c in joins else 1.07)
    shots.append({"f": c, "z": z})
if punches:
    def zat(f):
        z = shots[0]["z"]
        for sh in shots:
            if sh["f"] <= f: z = sh["z"]
        return z
    marks = sorted({sh["f"] for sh in shots} | {p["f"] for p in punches} | {p["t"] for p in punches})
    new_shots = []
    for b in marks:
        pp = next((p for p in punches if p["f"] <= b < p["t"]), None)
        if pp:   # zoom about a point ~400 px below the kit origin (mouth/chin line) so the mouth never slides into the subtitle band
            zb = zat(b); zp = round(zb * float(pp.get("z", 1.12)), 4)
            new_shots.append({"f": b, "z": zp, "y": round(-(zp - zb) * float(pp.get("pivot", 400)) + float(pp.get("dy", 0)))})
        else: new_shots.append({"f": b, "z": zat(b)})
    shots = new_shots
    print("punch-ins: " + ", ".join(f"{p['f']}->{p['t']} x{p.get('z', 1.12)}" for p in punches))

# 7) sound effects
sfx = []
#   "sfx": false on an event silences its entry sound (restraint: only sounds that mark something);
#   "tap_at" (custom page/igpage) gets a soft click like "click_at".
for e in fulls:
    chained = any(x["t"] == e["f"] for x in fulls)
    if e.get("sfx", True) is not False: sfx.append({"f": e["f"] + (2 if chained else 0), "k": "swish" if chained else "whoosh"})
    for key in ("click_at", "tap_at"):
        if key in e: sfx.append({"f": e[key], "k": "click"})
for e in events:
    if e.get("sfx", True) is False and e["type"] not in FULL_TYPES: continue
    if e["type"] == "split":
        sfx.append({"f": e["f"], "k": "swish"})
        if "click_at" in e: sfx.append({"f": e["click_at"], "k": "click"})
    elif e["type"] == "mood": pass          # speaker grey/dim beat is silent
    elif e["type"] not in FULL_TYPES:
        sfx += [{"f": it["f"], "k": "pop"} for it in e.get("items", []) if "f" in it] or [{"f": e["f"], "k": "pop"}]

# 8) QUIET STRETCHES: the picture must not stay unchanged for long. A visual change = an event entering or leaving (any type),
#    an item/click/highlight appearing inside an event, or a speaker zoom change (shots). Subtitle words do NOT count.
#    Every stretch longer than "max_quiet_s" (default 6.0) needs a decision: a visual that shows what is said, or a
#    "quiet_ok" entry {"from": anchor, "to": anchor, "why": "..."} saying why the bare speaker is right there.
MAXQ = float(E.get("max_quiet_s", 6.0))
talk_end = min([e["f"] for e in events if e["type"] == "outro"] + [total])      # the outro card is not part of the talk
changes = {s["f"] for s in shots}
for e in events:
    changes |= {e["f"], e["t"]} | {v for key, v in e.items() if key.endswith("_at") and isinstance(v, int)}
    for it in e.get("items", []):
        changes |= {v for key, v in it.items() if (key == "f" or key.endswith("_at")) and isinstance(v, int)}
    if e["type"] == "screenshot":   # marker highlights draw on at their own time (same default as Visuals.tsx)
        changes |= {e["f"] + h.get("at", 20 + i * 26) for i, h in enumerate(e.get("highlights", [])) if e["f"] + h.get("at", 20 + i * 26) < e["t"]}
pts = sorted({0, talk_end} | {c for c in changes if 0 < c < talk_end})
# moving footage (a "clip" insert, or a "split" playing a video "src") is never quiet: those stretches are skipped and the clock
# restarts when it ends. Its start/end are already change points, so every stretch is either fully on moving footage or not at all.
moving = [e for e in events if e["type"] == "clip" or (e["type"] == "split" and e.get("src"))]
on_moving = lambda f: any(e["f"] <= f < e["t"] for e in moving)
stretches = [(a, b) for a, b in zip(pts, pts[1:]) if not on_moving(a)]
said = lambda a, b: " ".join(w["t"].replace("*", "") for w in words if a <= w["f"] < b)
fmt = lambda f: f"{f // FPS // 60}:{f / FPS % 60:05.2f}"
quiet_ok = []
for q in E.get("quiet_ok", []):
    if not str(q.get("why", "")).strip(): raise SystemExit(f"ERROR: quiet_ok entry {q} has no \"why\": write the reason the bare speaker is right there")
    quiet_ok.append({"f": anchor(q["from"]), "t": anchor(q["to"]), "why": q["why"], "used": False})
TOL = FPS     # an entry may start/end up to 1 s inside the stretch (word anchors rarely sit exactly on the change)
long_, bare = [], []
for a, b in stretches:
    if (b - a) / FPS <= MAXQ: continue
    q = next((q for q in quiet_ok if q["f"] <= a + TOL and q["t"] >= b - TOL), None)
    if q: q["used"] = True
    long_.append((a, b, q)); bare += [] if q else [(a, b)]
# calibration totals over the talk (outro excluded)
kind = {"full": 0, "split": 0, "overlay": 0, "speaker": 0}
for f in range(talk_end):
    on = [e for e in events if e["f"] <= f < e["t"]]
    kind["full" if any(e["type"] in FULL_TYPES for e in on) else "split" if any(e["type"] == "split" for e in on) else "overlay" if on else "speaker"] += 1
nchg = len(pts) - 2
longest = max(stretches, key=lambda s: s[1] - s[0]) if stretches else (0, 0)
print(f"QUIET CHECK (talk {talk_end / FPS:.1f}s, outro excluded, max_quiet_s {MAXQ:g}): {nchg} visual changes, avg unchanged stretch {talk_end / FPS / max(1, nchg + 1):.1f}s"
      f" | longest unchanged stretch {(longest[1] - longest[0]) / FPS:.1f}s at {fmt(longest[0])}-{fmt(longest[1])}")
print("  (visual change = an event in/out, an item/click/highlight appearing, a speaker zoom change; subtitle words do not count;"
      " time on moving footage - clip, split with a video src - is never quiet; a static insert held long still is)")
print(f"  screen time (moving footage {100 * sum(on_moving(f) for f in range(talk_end)) / max(1, talk_end):.0f}% of the talk): " + " | ".join(f"{n} {100 * kind[k] / max(1, talk_end):.0f}%" for k, n in
      (("full", "full-screen"), ("split", "split"), ("overlay", "speaker+overlay"), ("speaker", "speaker only"))))
for a, b, q in long_:
    print(f"  {'quiet_ok' if q else 'TOO QUIET'} {fmt(a)}-{fmt(b)} ({(b - a) / FPS:.1f}s, frames {a}-{b}): \"{said(a, b)}\"" + (f"  <- why: {q['why']}" if q else ""))
for q in quiet_ok:
    if not q["used"]: print(f"WARNING: quiet_ok {fmt(q['f'])}-{fmt(q['t'])} covers no long quiet stretch (stale? remove it or fix its anchors)")
if bare:
    hint = []
    for a, b in bare:
        ws = [w for w in words if a <= w["f"] < b]
        hint.append(f"  {fmt(a)}-{fmt(b)} ({(b - a) / FPS:.1f}s, frames {a}-{b}): \"{said(a, b)}\"")
        if ws: hint.append(f'      quiet_ok entry would be: {{"from": ["{ws[0]["k"]}", {ws[0]["i"]}], "to": ["{ws[-1]["k"]}", {ws[-1]["i"]}, 0, "e"], "why": "..."}}')
    sys.stdout.flush()
    raise SystemExit(f"ERROR: {len(bare)} stretch(es) longer than {MAXQ:g}s with no visual change. data.json NOT written.\n" + "\n".join(hint) + "\n"
        "  This is a DECISION, not a quota. For each stretch, either:\n"
        "  - add a visual that SHOWS what is being said there (event, split, chips item, click, ...), or\n"
        "  - if the bare speaker is right (e.g. a personal story where the face IS the content), add to work/edit.json\n"
        "    \"quiet_ok\": [{\"from\": <anchor>, \"to\": <anchor>, \"why\": \"<the reason>\"}] covering the stretch (edit-json.md, quiet_ok).")

# 9) CUT CHECK (owner requirement 12: the picture must flow, never look cut or skipped). A join where the speaker is visible on
#    both sides is a jump cut. Each one needs a decision: remove the cut, cover it with a full-screen insert that is fully on
#    screen >= 7 frames before the join and stays >= 6 frames after it, or a "cut_ok" entry {"join": n, "why": "..."}
#    (join n = between segment n and n+1, counted from 1) giving a PICTURE reason.
cut_ok = {}
for c in E.get("cut_ok", []):
    if not str(c.get("why", "")).strip(): raise SystemExit(f"ERROR: cut_ok entry {c} has no \"why\": write the picture reason this visible cut is right")
    cut_ok[int(c["join"])] = c["why"]
njoin = len(segs) - 1
exposed = [(i, sg["start"]) for i, sg in enumerate(segs) if i and sg["start"] in joins]
print(f"CUT CHECK: {njoin} cut(s) in {total / FPS:.1f}s" + (f" (one per {total / FPS / njoin:.1f}s)" if njoin else "")
      + f" | speaker visible across {len(exposed)} of them | clips used: {', '.join(sorted({sg['k'] for sg in segs}))}")
jump = []
for i, f0 in exposed:
    line = (f"join {i} at {fmt(f0)} (frame {f0}), {segs[i - 1]['k']} {segs[i - 1]['out']:.2f} -> {segs[i]['k']} {segs[i]['in']:.2f}: "
            f"\"...{said(max(0, f0 - 45), f0)}\" || \"{said(f0, f0 + 45)}...\"")
    if i in cut_ok: print("  cut_ok   " + line + "  <- why: " + cut_ok[i])
    else: print("  JUMP CUT " + line); jump.append(line)
for i in cut_ok:
    if i not in [x for x, _ in exposed]: print(f"WARNING: cut_ok join {i} is not a visible cut (stale? remove it or fix the number)")
if jump:
    sys.stdout.flush()
    raise SystemExit(f"ERROR: {len(jump)} cut(s) where the speaker is visible on both sides. data.json NOT written.\n"
        "  The viewer sees these as the video skipping. This is a DECISION, not a quota. For each one, either:\n"
        "  - do not cut there (keep the pause or the filler word; prefer one continuous take), or\n"
        "  - cover the join with a full-screen visual that SHOWS what is said there (fully in >= 7 frames before, still on >= 6 after), or\n"
        "  - if a visible cut is right (change of place, a new section that looks like one), add to work/edit.json\n"
        "    \"cut_ok\": [{\"join\": <n>, \"why\": \"<the picture reason>\"}] (edit-json.md, cut_ok). \"The audio is clean\" is not a reason.")

# music volume points (generic): "music": {"src", "volume", "points": [{"at": anchor, "v": 0..1 (x volume), "ramp": frames}]}
#   lets the bed follow the script (dip under a turn, return after) without a second track.
MUSIC = dict(E["music"]) if E.get("music") else None
if MUSIC and MUSIC.get("points"):
    MUSIC["points"] = sorted([{"f": anchor(p["at"]), "v": float(p["v"]), "ramp": int(p.get("ramp", 12))} for p in MUSIC["points"]], key=lambda p: p["f"])
    print("music points: " + ", ".join(f"{fmt(p['f'])} x{p['v']:g}" for p in MUSIC["points"]))
json.dump({"fps": FPS, "total": total, "theme": THEME, "segs": segs, "framing": E.get("framing", {}), "subs": subs, "events": events,
           "fullTypes": sorted(FULL_TYPES), "shots": shots, "sfx": sfx, "keepCase": E.get("keep_case", []), "music": MUSIC},
          open("video/src/data.json", "w"), ensure_ascii=False, indent=1)

# report: read it every time
covered = sum(e["t"] - e["f"] for e in fulls)
print(f"total {total} frames = {total / FPS:.1f}s | {len(segs)} segments | {len(subs)} subtitle chunks | full-screen inserts cover {100 * covered / total:.0f}%"
      f" | split panels {100 * sum(e['t'] - e['f'] for e in splits) / total:.0f}%")
for e in events: print(f"  {e['type']:<11}{e['f']:>5} -> {e['t']:<5} {(e['t'] - e['f']) / FPS:.1f}s")
for s in subs: print(f"  {s['f']:>5} {' '.join(w['t'] for w in s['small'])} | {' '.join(w['t'] for w in s['big'])}")
