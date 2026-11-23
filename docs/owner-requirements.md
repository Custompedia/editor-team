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
