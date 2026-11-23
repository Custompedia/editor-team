# Acceptance criteria from the owner (2026-11-23) — the guide and the kit must make EVERY worker able to do this

The owner's words (translated): "Make sure each agent really knows when to give a visualisation and when to cut, positions
must be tidy, knows when one full screen and when not, the visualisation must fit, and never let a video stay quiet too long —
I mean visuals that are too sparse."

1. WHEN to visualise and when not: a decision per sentence with a written reason (not a default, not a quota).
2. WHEN to cut: when to change the picture (cut to a visual, cut back to the speaker, punch-in/zoom on the speaker, chain
   visuals) and when to hold; and that speech cuts never land mid-sentence. The guide must teach the reasons for a cut.
3. POSITION is tidy: where each kind of element sits and why (face never covered, subtitle zone, platform UI safe areas,
   consistent alignment and margins, one focus per frame), checked on stills.
4. FULL SCREEN vs not: explicit reasoning for full screen / split / small overlay / speaker only.
5. The visual FITS: it shows the concept being spoken (cover-the-subtitle test), real asset first.
6. NEVER sparse for long: no long stretch without a visual change. This one is enforced mechanically by the kit
   (build_timeline reports every quiet stretch; a long one needs either a visual or a written reason) AND checked by the lead.
   Evidence so far: two independent editors keep the longest speaker-only stretch between ~2.5 s and ~7 s; our rejected
   job01 v4 had 16 s.
These six are confirmed by the owner directly, so they are requirements, not one editor's style.

## Added by the owner (2026-11-23, later message)
"Try to use real assets for the visuals, whatever it is. Make sure the animation is smooth, good and fitting. When the
visualisation appears, and for how many seconds — the agent must truly understand that."

7. REAL ASSETS FIRST, always: for any visual, look for the real thing before anything drawn. A drawn visual needs a written
   reason why no real asset can show it.
8. ANIMATION is smooth, good and FITS: entry/exit motion chosen for what it means, consistent within a video, no jerky or
   random motion; checked on consecutive-frame strips, not assumed.
9. TIMING is understood, not guessed: WHEN a visual appears (on which word, how many frames before/after it), HOW LONG it
   stays (long enough to read/recognise, gone when the topic ends), and how that differs by kind of visual. The guide must give
   the reasoning plus observed ranges from the benchmarks; the kit reports each visual's duration so it can be checked.

## Added by the owner (2026-11-23, third message)
"Every moment can be put to use. E.g. something another party says can be animated as a WhatsApp chat, left and right, above
the speaker — as creative as possible. Make sure the visuals are not too sparse, but also not too many. The AI must really
know when to have one and when not."

10. CREATIVE USE OF MOMENTS: look for what each moment offers (a quote → chat bubbles left/right above the speaker, a turn →
    a change of the whole picture, a named thing → the thing itself…). The guide must teach how to FIND such opportunities,
    with varied examples, not prescribe one device.
    Boundary to state clearly: showing what someone SAID as chat bubbles is an illustration of speech (fine, encouraged);
    faking a real app screen/profile/article as if it were evidence is not (use the real one or ask the user).
11. NOT TOO SPARSE AND NOT TOO MUCH — both directions matter. Lower bound is enforced by the kit (quiet gate). Upper bound is
    judgement the guide must teach and the worker must show: one focus per frame, no visual that adds nothing ("if removed,
    is anything lost?"), room for the speaker to land important lines, no stacking of competing elements. The build report
    gives the numbers (changes per second, % speaker hidden) so the lead can question an edit that is far denser or far
    sparser than the benchmarks for its kind of content.

## Added by the owner (2026-11-23, feedback on job02 "Box Lebaran" final_v4)
The owner's words (Indonesian, as written):
"'lebih cepat lebih baik' di akhir itu harusnya animasi closing logo Parcelin dkk; kalau ada 'hubungi aku' di akhir, nah baru bisa
pakai approach yang sekarang. Sama kamu dari awal kebanyakan cut, harus memenuhi requirement di bawah:
1. tidak kebanyakan cut, diusahakan banget video jangan sampai tiba-tiba kepotong / ke-skip; jadi jangan cuma fokus di voice /
   subtitle tapi ya bener-bener biarin si video flow biar enak dilihat dan tidak patah-patah atau ke-skip-skip
2. pastikan backsound sesuai dengan momen; visual juga pastikan pas, tidak terlalu panjang dan tidak terlalu pendek
3. desain visual jujur udah better, keep it improve
4. 'habis Natal, Lebaran' ini mending momen bener-bener foto asli, bukan packaging, dan 1 layar full. Pada bagian 'konsultasi ke
   Parcelin' ini juga 1 halaman aja, jangan cuma card di tengah, aneh.
Pastikan aset-aset yang dibutuhkan / konfirmasi yang dibutuhkan kamu tanyakan di awal. Langsung aja diperbaiki di skills-ku biar
masukan ini permanen disimpannya."

12. THE PICTURE FLOWS — FEW CUTS: the video must never look as if it suddenly cuts or skips. Do not optimise only for the voice and
    the subtitles: a join that sounds clean can still look like a jump. Prefer one continuous take; cut only where it is needed;
    no cut where the speaker is visible on both sides unless there is a written reason. Enforced by the kit (CUT CHECK in
    build_timeline; `cut_ok` needs a reason) AND checked by the lead on the strips. Evidence: job02 v4 had 5 cuts in 52.7 s
    (one per ~10 s), mixing two takes sentence by sentence; three of them showed the speaker jumping.
13. BACKGROUND MUSIC FITS THE MOMENT: a video has a music bed chosen for its mood, and the music follows the turns of the script
    (opening, turn, call to action). Licence must allow the platform use; the track and its licence are reported.
14. EVERY VISUAL LASTS THE RIGHT TIME: not too long, not too short (sharpens 9). Evidence: job02 v4 showed a photo for 0.9 s because
    the next visual needed lead-in; that is a planning error, not an acceptable squeeze.
15. A MOMENT IS SHOWN AS THE MOMENT: when the speaker names an occasion or event (Christmas, Lebaran), show a real photo of that
    moment, full screen. Not the brand's product for that occasion (job02: packaging photos for "abis Natal, terus Lebaran").
16. A PAGE IS SHOWN AS A PAGE: a website the viewer is sent to fills the screen as one whole page. A small card floating in the
    middle of the frame "looks odd" (job02: parcelin.id as a rounded card on a dark blurred background).
17. THE ENDING FOLLOWS THE LAST LINE: a closing line such as a slogan ("lebih cepat lebih baik") ends on a brand closing animation
    (logo and the brand's other marks). A profile/contact card (job02's Instagram-profile ending) is right only when the speaker
    ends with "contact me / hubungi aku".
18. ASK FIRST: the assets and confirmations a job needs are asked for at the START, in one list, not discovered after delivery
    (job02: closing content, logo file, music and the moment photos were all decided by assumption).
Also from this message: the visual design of job02 was judged "already better, keep improving" (3): the look decisions of job02
(theme from the footage, chat bubbles, grey beat, timeline) are a baseline to build on, not a template.
