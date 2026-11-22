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
- (to be completed when job01 is delivered: QA results, user feedback on v1)
