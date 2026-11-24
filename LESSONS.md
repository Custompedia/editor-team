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

## job02 — "Box Lebaran" (2 klip = 2 take naskah yang sama, akun @prahenditaputri / Parcelin)
- Delivered final_v4 (52.7 s) in one working session: v1 internal (leftover word at a join), v2 rejected by the lead, v3 superseded by
  the worker itself, v4 delivered. Kit install from an empty container ~10 min; one 53 s render ~12 min.
- What worked: density. 31 visual changes, longest unchanged stretch 4.5 s, 0 quiet_ok, speaker-only 28% (job01 v4: 16 s without a
  change). The quiet gate + per-sentence plan did their job; the lead found no sparse or crowded stretch on the contact sheet.
- Lead rejected v2 on accuracy, not looks. The worker had "corrected" Whisper's "Juli pasir" to "dulu di Parcelin" (a brand name on a
  guess) and showed a subtitle "dulu." for a word that the cut had removed. Found by diffing `text` overrides against work/tx/*.json and
  the re-transcription of the final. -> worker rule in reference/workflow.md (Tahap 5) and lead test T24.
- The lead guessed too: from the syllable count I told the user it was probably "dulu, pasti". Prompt-free re-transcription then heard
  "Parselen / Parsel / parser", so the brand probably IS said. Rule for the lead: an envelope tells you where a word is and whether a text
  fits, not what the word is. Do not offer the user a replacement word; say "unverified", blank it, and ask the one person who can listen.
- The lead also judged a join "clean" from the envelope and a Whisper "Kamu," as a timing artefact: wrong, the word was fully audible
  (slices starting at the cut heard it 4/4). When a re-transcription of the FINAL has an extra word at a join, believe it until a slice
  test says otherwise. Asking for that slice test (R6) is what caught it.
- Prompt-free slices at 0.7x speed hallucinate ("Tunggu", "Jangan lupa", "Sampai jumpa di video selanjutnya"): use x1 as the main
  evidence, 0.7x only as a second opinion, and never a run with the vocab prompt as proof of a name.
- User input mid-job: an Instagram profile screenshot ("output akhir untuk Instagram seperti ini, dirapikan, dianimasikan bebas") and
  "aset cari aja di internet". Lead stated its reading (ending = that profile, account = that handle) and went on; the user did not
  object. Ending built as `igprofile`: real crops for avatar/tiles, text re-typeset exactly, not an imitation of the app.
- A 1069x830 desktop screenshot is too small for a 1080x1920 end card (tiles upscaled ~1.9x, soft). Ask for a phone screenshot up front.
- Usage limit killed the worker right after the v4 render, before its QA and before STATE.md was updated (it still ended at v2).
  Nothing on disk was lost; SendMessage after the reset resumed it. Rule: worker updates STATE.md BEFORE each render starts; the lead,
  on resume, checks out/ and the newest logs before assuming where the worker stopped.
- Brand site trap: the "Hampers Idul Fitri" product page on parcelin.id uses a "Gemini_Generated_Image" photo and lorem ipsum. The
  worker caught it by file name. Portfolio photos show client products (JNE, L'Oreal): reported to the user, not silently used.
- Kit: ported from the job into editkit after the render proved them: event `mood` (speaker grey/dim beat), custom `timeline` and
  `igprofile`, `hold_end`, chips `top/step/scale`, no dark top gradient on `light` photos. Fixed `sheet.py video` crashing on a sample
  at the last frame. Known: a `custom` event's own data must not use a field called `name` (documented in edit-json.md).
- Not verified by anyone: the audio. Flagged to the user: 0:35.4 (tight join "…Lebaran" -> "Kalian", possible <0.1 s residue), the
  two unsubtitled words at 0:36, 0:31.1, and the sung opener.
- Open for next time: the new subtitle-evidence rule and T24 are untested on a fresh worker; the eid photo got only 0.9 s because the
  screenshot needed lead-in for the cursor (acceptable here, check T12 when a visual is squeezed by its neighbour).

## job02 — owner feedback on final_v4 (2026-11-23) -> requirements 12–18
- Verdict: design "udah better, keep it improve"; but too many cuts ("patah-patah / ke-skip"), no backsound, wrong ending, two
  visuals wrong in kind (product instead of the moment; a card instead of a full page), and questions not asked up front.
  Full wording: docs/owner-requirements.md (12–18).
- Too many cuts was a method error, not a slip: the workflow picked the best sentence from each of two takes (voice/subtitle first),
  which gave 5 cuts in 52.7 s (one per ~10 s) against the skill's own "3–8 segments per 2 minutes". The build even printed
  "exposed jump cuts at frames [...]" and the kit turned them into punch-ins. Neither the worker nor the lead treated that line as
  a problem. -> skill: one base take, every cut needs a reason and a picture plan; kit: CUT CHECK gate with `cut_ok`; lead: T25.
- The lead misread the Instagram screenshot as "the ending of this video". The owner meant: that style of ending is for videos
  that end on "hubungi aku"; a slogan ending gets a brand logo closing. I stated my reading and the owner answered "aman kan", which
  I took as agreement. Rule: when an asset arrives mid-job, ask the one concrete question ("ini untuk penutup video INI?") instead
  of presenting an interpretation and reading a short reply as a yes.
- "Real assets first" was applied too literally: "abis Natal, terus Lebaran" got the brand's Christmas and Eid boxes. The words name
  a moment in time, so the real asset is a photo of the moment. Product photos belong to sentences about the product.
- Music was never raised (the skill said "only if asked"). Now a default with licence rules; per-moment volume is a kit gap.
- "Ask at the start": the first message did ask, but only generic items. Closing content, logo file, music and script-specific
  assets were missing. Now two lists: generic before the worker, script questions after Tahap 3.
- Status: final_v4 is NOT re-edited yet under these rules; the owner announced a next challenge. Re-edit only on request.

## 2026-11-23 — skill must work for any company and for no company (owner)
- Owner: "pastikan skills tidak cuma Parcelin, bisa ke berbagai perusahaan lain, dan yang tidak terikat perusahaan juga; semuanya
  end to end harus dipahami oleh AI". Audit: the method (stages, gates, content types) was already generic and brand facts already
  lived in docs/brands/. What was coupled: (a) the three owner rulings I had just written were phrased around Parcelin and the ending
  rule had no branch for a video without a brand; (b) the lead's intake list and my own proposed defaults assumed a brand (I offered
  Parcelin defaults for the NEXT job before knowing whose video it is); (c) nothing told a worker to decide whose video it is first,
  or forbade borrowing identity from another brand's profile; (d) both real jobs so far were Parcelin, so nothing else is proven.
- Fix: SKILL.md "Berlaku untuk siapa saja" (three cases, decided first in Tahap 0); rulings rewritten principle-first with examples
  from other fields and an ending table with a no-company column; design.md 6.2b (content type and owner are separate decisions);
  lead scope rule in CLAUDE.md; T31; docs/brands/_template.md.
- Fresh-reader test (a smaller model, skill files only, two invented jobs: a new coffee-shop company; a personal resignation story
  with a wrong "Parcelin (ASUMSI)" line in the brief). It got right: owner of the video decided first, the wrong brand line dropped,
  no borrowed identity, one base take + cut rules + CUT CHECK, moment/page/ending rulings applied to other fields, bubbles for the
  boss's quote, cut-out (not full page) for the BPS sentence. It found and I fixed: "follow the brand profile" stated unconditionally,
  "CTA at the end" required even when nothing is asked, dead pause vs meaningful pause, no fallback look for a new brand without
  material, density numbers from one brand reading like a norm, 3-minute roll vs the default length, unrelated clip.
- Still open (cannot be fixed by wording): no proven reachable source for licensed music or stock video from this container; the kit
  cannot change music volume per moment or punch in on a chosen word; everything above is tested by reading, not by a real job for
  another company. The next non-Parcelin job is the real test: watch music, moment footage and the quiet gate on pauses.

## job03 — "Cara Hitung Hardbox" (Parcelin, same footage as job01; first job under requirements 12–21)
- Delivered final_v4 (125.3 s). Owner on the v3 preview: "bagus sih editannya". job01 v4 on the same footage was "rada kurang".
- What made the difference, in order: (1) ONE line through the footage in recording order, 2 cuts in 125 s (job02: 5 in 53 s), both
  joins covered by a photo on the word being spoken, CUT CHECK 0 exposed; (2) questions asked before and after Tahap 3, so the ending,
  music, size and brand were the owner's decisions, not assumptions; (3) density without padding: 65 visual changes, longest unchanged
  stretch 4.9 s, 0 quiet_ok, speaker-only 23%.
- The worker understood all five clips before cutting: two consecutive parts plus three failed bridge takes. Nothing from the three
  short clips was needed. "Understand the whole roll first" is what kept the cut count at two.
- The CUT CHECK gate worked on its first real job. The worker planned the covering visuals at Tahap 3 instead of fixing jumps after
  a failed build; the lead's reply to the Tahap 3 report took minutes and changed nothing structural.
- v1 failed the worker's own QA4: the spoken self-cue "Ulangi" leaked at a join because Whisper's word time was ~0.6 s off. Rule kept
  in the skill: after a self-cue or restart, test the `in` point with a prompt-free slice before rendering.
- Lead review of v3 passed every hard test but sent it back for finish: full-screen photos shown as a band between blurred bars, a
  CC BY photo (credit obligation for the owner in every post) where a CC0 one existed, captions unreadable over a busy light page,
  5.7 s of near-still end card. All four are now rules or kit behaviour (full-bleed rule, CC0 first, caption backing on light
  inserts, staged end card). Showing the v3 PREVIEW to the owner while v4 rendered cost nothing and got the audio heard earlier.
- Owner rulings at the start: the Instagram profile for a "hubungi aku" ending is rebuilt in code, 100% the same as the screenshot;
  music free but "jangan spam musik"; Reels. The code-built page matched the screenshot on every text and number (lead compared
  them side by side); only photos are crops.
- Licensed sources are reachable after all: Openverse API for photos and audio (Freesound CC0, Jamendo CC BY). Stock VIDEO is still
  unproven.
- parcelin.id returned 404 DEPLOYMENT_NOT_FOUND during the job (it worked in the morning). Reported to the owner. A brand's site
  can vanish mid-day: keep a second source (here the public Pinterest) in the brand profile.
- The repo is PUBLIC (found when checking whether another session can work from it). Told the owner. Nothing private is stored, and
  the owner's profile images are deliberately not committed.
- Kit: ported after the v4 render: `page` (real page full screen with scroll/mark/tap), `gallery`, `measure`, `igpage`, `Tap`,
  `music.points`, `sfx: false`, caption backing on light inserts, `stills_full.mjs`.
- Not verified by anyone but the owner's ears: the two joins (0:52, 1:28), the kept false start "Kita bisa—" (~1:33), the music.
- Cost: one worker session ~2 h 20 min including three renders (~25 min each for 125 s). A render round is still the expensive unit;
  catching "Ulangi" before render 1 would have saved one.

## job04-rev — revisi video jadi "Box Lebaran" (…230555, ekspor CapCut): situs baru + baris penutup (2026-11-24)
- Delivered final_revB (52,65 s). Owner's request: at 0:42 show the new site parcelincreative.com and click the bottom-right CTA; end
  line parcelin.id → parcelincreative.com. Brand fact recorded in docs/brands/parcelin.md.
- The project that made the video was gone (job folders are not in the repo; the file was the owner's CapCut re-export). So the revision
  was a PATCH on the delivered frames, not a rebuild: measure the laptop screen per frame (pure scale + shift), capture the real site with
  Playwright on virtual time (50 consecutive frames, real 3D motion and real hover state), composite only inside the screen, re-typeset
  the end line from per-frame measurements of the old one (font found by glyph positions + pixel RMSE). Proof that nothing else moved:
  0 changed pixels outside the declared region before encoding, audio stream copy with identical md5, same frame count. One full
  re-encode (crf 13) instead of splicing GOPs from two encoders. Preview ~55 min, final + QA ~25 min.
- Owner's gate, stated twice: "kasih aku view frame-nya dulu, kalau ku acc baru render akhir". And the owner asked "udah?" six times in
  90 minutes while the folder was still empty. Rule for the lead: brief the worker to write TWO early full-size stills as soon as the
  first composite exists and to message the lead; forward them at once, labelled "not final". A site screenshot is not a video frame:
  the owner said so ("i mean preview frame video").
- The real CTA was weak on screen: an orange button on an orange hero, ~40 px in the mockup, under the cursor. Not faked. What kept it
  honest and readable: a narrower real viewport (1024 px, same layout) so the real button is as large as the old green one, the cursor
  pausing BESIDE the button for ~8 frames, the site's real hover state, a white click ripple. Two variants shown; lead recommended B.
- The owner answered the A/B question with "kalau menurut kamu sudah sesuai, langsung aja dibuat" in a message about the other jobs. The
  lead read it as leave to use its own recommendation, said so in the reply, and rendered B. Open: the owner has not confirmed B.
- First two minutes of a fresh container: the proxy refused drive.google.com, the brand site and huggingface.co (403), then allowed all
  of them. I almost told the owner to change the environment's network settings. Rule: on a refusal at session start, finish the kit
  install, retry after 2–3 minutes with curl AND python, and only then report a blocked host.
- `doctor.py` said READY while Whisper was not cached and the model download had just failed: READY means "installed", not "can
  transcribe". Check the "whisper model" line, and re-run install.sh once the network answers.
- Three opus/high workers in parallel reached the 5-hour usage limit together at ~3 h, right after two final renders had finished and
  before their QA. Nothing was lost (STATE.md before each heavy step; files on disk); SendMessage after the reset resumed each one.
  Rule: on resume, look at out/ and the newest log first, then tell the worker exactly what exists and what is missing.
- Not verified by anyone: the audio was not listened to (it is bit-identical to the source), the motion was judged on frames only.
- Open question for the owner: revisions of older videos would be faster if each job's small text files (edit.json, script, sources)
  were archived. They are not, because the repo is public and job folders are excluded by rule.
