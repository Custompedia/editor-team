# Benchmark study — shared framework (all benchmark workers follow this)

Benchmarks (public TikTok, @raymondchins): v1 = 7628165590825422098 (58 s), v2 = 7708964677828578568 (90 s), v3 = 7473068001151978758 (90 s).
Files: /home/user/jobs/bench01/work/ref/v{1,2,3}.mp4, transcripts v{N}_transcript.txt + v{N}_words.json (word times).
The user's focus: how NEWS/ARTICLE cut-outs are done ("just the cut-out, no device frame, only a screenshot crop that fits"),
the ANIMATION BEHIND them, and the SUBTITLE TEXT ANIMATION — and the whole thing as the minimum benchmark for our edits.
The goal is to learn HOW THE EDITOR DECIDES (principles any AI model can apply), not to copy colours/fonts/looks.

You cannot hear or watch: build images and OPEN them with the Read tool. 1-fps contact sheets for overview; DENSE strips
(every frame or every 2nd frame over 1–2 s, tiled at readable size) around every visual event to see motion; full-resolution
single frames of each distinct visual type to see crop edges, shadows, highlights, labels, textures. At least ~8 dense strips
per video. A finished command is not evidence. Reference the image path for every claim.

Analyse:
A. NEWS / ARTICLE CUT-OUTS: what is shown (headline only? + image? paragraph?), crop tightness, any device/browser frame or card
   chrome, edges/corners/shadow/rotation/paper-cut look, size and position, how many at once, text highlight/underline and how it
   animates, source/logo/date visible?, duration, entry/exit (direction, feel, frames), which spoken words it is anchored to.
B. BEHIND THE CUT-OUTS: speaker still visible (dimmed, blurred, scaled, moved, B&W)? or a designed background (colour, gradient,
   texture, grid, blurred footage, moving shapes)? how it animates; when the edit leaves the speaker entirely and when not.
C. SUBTITLES / TEXT ANIMATION: position, size relative to frame, font character (weight/width/case; exact name not needed),
   colours and when they change, words per chunk, per-word vs per-phrase reveal, the appearance motion (pop/scale/slide/fade,
   frames), emphasis treatment, stroke/shadow/box, behaviour over inserts. Compare with our kit's subtitles
   (/home/user/jobs/bench01/video/src/Main.tsx `Subs`: small white line, word-by-word opacity, occasional big accent word).
D. OTHER VISUAL TYPES and when used: logos, product/people photos, screen recordings, app UI, charts/numbers, maps, memes,
   b-roll, text cards, speaker zooms/punch-ins. Real asset or drawn? How presented?
E. RHYTHM: table sentence by sentence (time | what is said | what is shown | layout | duration). Count visual beats; share of
   time speaker-only / speaker+overlay / speaker hidden; longest stretch without change; hook in first 3 s; ending/CTA.
F. THE THINKING: for each visual, WHY this visual for this sentence, why this size/layout/duration.

Rules: heavy commands via `flock /home/user/jobs/.heavy.lock ...`; Python via `source /home/user/jobs/bench01/.venv/bin/activate`.
Write only inside your own output paths. Do not edit /home/user/editor-team or /home/user/editkit. No cookies/VPN/workarounds.
Do not claim what you did not see in an image or read in a transcript; list what you could not determine.
