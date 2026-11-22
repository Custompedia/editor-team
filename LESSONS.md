# Editor Team — Lessons log (makin ke kanan makin improve)

Read this at the start of every session. After EVERY job, the lead appends: what went well, what broke, the user's feedback,
and the rule that prevents it next time. A rule that applies to all jobs is also copied into CLAUDE.md.

## 2026-11-22 — setup in cloud
- Web fonts hang Remotion's Chrome after ~90 frames here → fonts installed as system fonts (fixed in kit).
- PyAV 19 breaks faster-whisper 1.2.1 → pinned av<17 (fixed in installer).
- Pexels (bot check) and Wikimedia (HTTP 429) unusable from this container → use brand's own public pages, Openverse, user assets.

## job01 — PARCELIN "Cara Hitung Hardbox" (5 clips, Google Drive)
- Whisper heard the brand as Parcelon/Parcellen even with a vocab prompt; worker wrote "not found on web" without trying
  other spellings → rule: search spelling variants before giving up; always confirm brand name in brief.
- User preference: colours/fonts per video (no default yellow), clean, real assets (brand's own Pinterest/IG) over code visuals.
- User expects the finished video in one go: ask open questions early, but continue on marked assumptions instead of
  stopping when the user is waiting for the result.
- Delivered final_v4 (112 s). Total ~2h20m on 4 vCPU; one 112 s render ≈ 25 min → each failed QA round costs ~30 min.
- QA caught real problems: v1 speaker sipping a drink at a cut, v2 a single black frame (Remotion glitch, re-render fixed it),
  v3 nine subtitle words >0.2 s off → fixed with timing corrections. Rule: run blackdetect in QA1; run QA5 (subtitle vs
  speech) BEFORE the full render using stills + transcript, to save a render round.
- Real brand assets found via the brand website + public Pinterest pins; Instagram blocked by login (no IG screenshot/click).
  Brand colour (#DE6B17) and site font (Poppins, static files) taken from the brand site → good match to "no fixed look".
- Insert share only 15% (target 30-45% for Jualan) because real assets ran out; chose not to pad. Ask the user for more
  portfolio photos up front when they want denser visuals.
- (pending) user feedback on v4.
