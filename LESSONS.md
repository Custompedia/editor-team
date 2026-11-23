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
- User feedback on v4: "rada kurang". Wanted: more creative treatment (customer questions as left/right chat bubbles at the
  open, dark/dim beat on the "gabisa" punchline), more and clearer visuals with judgement on when NOT to, good real images,
  neat animation, deliberate full-screen vs not, and a full-screen Pinterest ending instead of a small IG chip.
  The user shared reference edits (Drive 1WrAilhmWzUBkdZGg0X-5fp4JYrzF8UlT) → study archived in docs/reference-studies/parcelin-study.md.
- Lesson: "clean" must not mean "sparse". Guide density targets matter; a 15% insert share read as flat to the user.
- Worker requirement: Opus 5.5, effort high.

## Reference study (after job01 v4)
- Reference vs v4 (same footage): ~25 visual beats vs 13; full-screen ~35% vs 15%; longest face-only 6-7 s vs 16 s.
- Biggest gap was not colour/font (reference used kit defaults) but visual thinking: illustrate the CONCEPT spoken
  (3D box for "ukuran", hands folding for "desain", gold foil macro for "finishing"), quotes as stacked chat bubbles with
  thumbnails, B&W/dim beat on "nggak bisa", price tags on the object, strike READY STOCK -> CUSTOM, spec form that fills in,
  third-party article proof with highlight, big full-screen ending.
- Brand naming seen in references: "Parcelinpack" (JPNN article) and IG @parcelinpack (~132k followers); v4 used
  @parcelincompany from the website footer -> confirm with user; prefer the account the brand itself shows in its videos.
- Kit backlog: generic primitives only, see docs/reference-studies/BENCHMARK_NOTES.md §7 and reference/visual-craft.md §9
  (content-specific items from the first gap list such as form, box3d, dmchat were dropped).

## 2026-11-23 — repo becomes source of truth
- Pushed kit to Custompedia/editor-team. Verified a from-scratch install using only the repo (fresh venv + node_modules):
  doctor READY, new_job, transcribe, Remotion render OK. Everything a new chat needs is in the repo.

## 2026-11-23 — repo restructure (token efficiency)
- One skill, progressive disclosure: SKILL.md 150k -> 11.5k chars (map + rules); details in reference/*.md read per stage.
  Embedded kit code (74k chars, and stale: old Google-Fonts theme) removed from the instructions; code lives only in editkit/.
  Checked: 523/524 lines of guide Bagian 1,3-9 carried over verbatim (only a heading renamed).
- CLAUDE.md is lead-only and short (loaded every turn); worker rules moved into the skill.
- Workers read the skill at /home/user/editkit/skill (symlink to the repo). No global ~/.claude/skills copy.
- Not yet proven on a real job: confirm on the next job that the worker reads the reference files at the named stages
  (STATE.md must list them); if a worker skips them, tighten SKILL.md.

## 2026-11-23 — parallel team (5 workers) on benchmark study + guide rewrite
- BUG found by running workers in parallel: tools/sheet.py, scene_check.py, verify_audio.py use fixed /tmp paths
  (/tmp/_frame.jpg, /tmp/_scene.txt, /tmp/_final.wav). Parallel jobs overwrite each other -> a contact sheet contained
  frames of another video. Until the fix is merged: never run these tools in two jobs at once; re-check sheets made in parallel.
- Subagents in a long session keep the instruction files as loaded at session start: a deleted/stale CLAUDE.md still
  reaches them. After changing instructions mid-session, say in the brief which file is authoritative.
- PM pattern that worked: one shared framework file for parallel study workers, one output file per worker, nobody edits
  the repo, lead integrates.

## 2026-11-23 — guide rewrite from the owner's audit + second benchmark
- Owner's audit goal: the guide must teach HOW TO THINK (any model), not fixed looks. My first "quality bar" was a template
  of one editor's solutions and I had made it mandatory: wrong. Replaced by reference/visual-thinking.md (why / per-sentence
  chain / situations / real assets / code policy / look / self-check as questions) and reference/visual-craft.md (news
  cut-outs, when to cut, position, timing, motion, captions, sparse vs crowded, what the kit can do).
- 11 owner requirements recorded (docs/review-tests.md maps tests to them): when to visualise, when to cut, tidy position,
  full screen vs not, the visual fits, never sparse for long, real assets first, smooth fitting motion, timing understood,
  creative use of moments (chat bubbles for speech = fine; fake app/article as evidence = never), not too much either.
- Second benchmark (3 TikToks, different editor): density and layout differ hugely per video (speaker hidden 52% / 67% / 1%),
  so full-screen % is NOT a target. Constant across both editors: visual on the word, real evidence, one focus per frame,
  face never covered, no long quiet stretch, opinion goes back to the face, tonal turns marked briefly.
  "Not quiet" does not always mean graphics: punch-ins, angle changes and big text count.
- Words lose against code: the kit's default theme and the absence of any density check shaped job01 more than the guide did.
  Now enforced in the kit: required `theme` (no default look) and a quiet-stretch gate (job01 v4 would have failed at 0:27-0:44).
- Owner-specific wishes for one brand go to docs/brands/<brand>.md, not into the general guide.
- Not proven yet: the new guide on a real job; weaker models; kit primitives the benchmark uses but the kit lacks
  (hard cut / blur-in entries, speaker B&W, headline strip under the chin, caption modes, highlight anchored to words).
