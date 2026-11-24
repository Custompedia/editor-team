import React from 'react';
import {AbsoluteFill, Audio, Easing, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import raw from './data.json';
import {Insert, Overlay, SplitPanel} from './Visuals';
import {SANS, SERIF, EMPH_STYLE, ACCENT, INK, LIGHT, FPS, cl, sp} from './theme';
const data = raw as any;
const isFull = (e: any) => data.fullTypes.includes(e.type);
const fulls = data.events.filter(isFull);
const splits = data.events.filter((e: any) => e.type === 'split');
const overs = data.events.filter((e: any) => !isFull(e) && e.type !== 'split' && e.type !== 'mood');
/* mood (generic): {type:"mood", gray?: 0..1, dim?: 0..1} turns the SPEAKER layer grey/darker over a range (a tonal turn),
   4-frame ramp in/out. Only the speaker changes; inserts, overlays and subtitles keep their colour. */
const moods = data.events.filter((e: any) => e.type === 'mood');
const moodK = (frame: number) => moods.map((e: any) => ({e, k: Math.min(interpolate(frame, [e.f - 1, e.f + 3], [0, 1], cl), interpolate(frame, [e.t - 4, e.t], [1, 0], cl))})).reduce((a: any, b: any) => (b.k > a.k ? b : a), {e: null, k: 0});
/* music volume points (generic): each point ramps the bed to v (x base volume) over `ramp` frames from its frame */
const musicK = (f: number) => {
  let v = 1;
  for (const p of (data.music?.points || [])) { if (f >= p.f) v = interpolate(f, [p.f, p.f + p.ramp], [v, p.v], cl); }
  return v;
};
const chainedAfter = (e: any) => fulls.some((x: any) => x.f === e.t); // another insert starts exactly when this one ends
const chainedBefore = (e: any) => fulls.some((x: any) => x.t === e.f);

/* Split layout: a visual panel on top, the speaker pushed down below it. 0 = normal layout, 1 = fully split.
   The move is animated unless a full-screen insert (pre/post) or another split (chainPrev/chainNext) hides or continues it. */
export const splitP = (e: any, frame: number) => {
  const inn = e.pre || e.chainPrev ? (frame >= e.f - (e.pre ? 10 : 0) ? 1 : 0) : sp(frame, e.f, {damping: 20, stiffness: 150, mass: 0.8});
  const out = e.post || e.chainNext ? (frame < e.t + 10 ? 1 : 0) : interpolate(frame, [e.t - 12, e.t], [1, 0], {...cl, easing: Easing.inOut(Easing.cubic)});   // stays under whatever takes over
  return Math.max(0, Math.min(inn, out));
};
const speakerShift = (frame: number) => Math.max(0, ...splits.map((e: any) => splitP(e, frame) * (e.shift ?? 300)));
/* 0..1: how much of the frame is a BRIGHT full-screen insert ("light": true) right now -> dark subtitles, no bottom darkening */
const lightK = (frame: number) => Math.max(0, ...fulls.filter((e: any) => e.light).map((e: any) => Math.min(
  chainedBefore(e) ? interpolate(frame, [e.f, e.f + 12], [0, 1], cl) : interpolate(frame, [e.f, e.f + 7], [0, 1], cl),
  e.hold_end ? 1 : chainedAfter(e) ? interpolate(frame, [e.t, e.t + 12], [1, 0], cl) : interpolate(frame, [e.t - 6, e.t], [1, 0], cl))));

/* Layer 1: the speaker (A-roll), cut into segments, with zoom levels and a slow drift */
const Speaker: React.FC = () => {
  const frame = useCurrentFrame();
  // skip decoding video while an insert fully hides it (keep it during the insert's fade in/out)
  const covered = fulls.some((e: any) => frame >= e.f + (chainedBefore(e) ? 0 : 9) && frame < e.t - (chainedAfter(e) ? 0 : 7));
  let si = 0;
  data.shots.forEach((s: any, i: number) => { if (frame >= s.f) si = i; });
  const shot = data.shots[si];
  const next = data.shots[si + 1]?.f ?? data.total;
  const drift = interpolate(frame, [shot.f, next], [0, 0.035], cl);
  const down = speakerShift(frame);
  const md = moodK(frame);
  const mf = md.k > 0 ? `grayscale(${md.k * (md.e.gray ?? 1)}) brightness(${1 - md.k * (md.e.dim ?? 0.3)}) contrast(${1 + 0.08 * md.k})` : undefined;
  return (
    <AbsoluteFill style={{backgroundColor: '#000', filter: mf}}>
      {data.segs.map((s: any, i: number) => {
        const fr = data.framing[s.k] || {}; // per-clip reframing so the face sits in the same place in every clip
        const z = (fr.scale || 1) * (shot.z + drift);
        return (
          <Sequence key={i} from={s.start} durationInFrames={s.dur} layout="none">
            <Audio src={staticFile(s.src)} startFrom={Math.round(s.in * FPS)} endAt={Math.round(s.in * FPS) + s.dur}
              volume={(f) => interpolate(f, [0, s.fi ?? 2, s.dur - (s.fo ?? 2), s.dur], [0, 1, 1, 0], cl)} />
            {!covered && (
              <AbsoluteFill style={{transform: `translate(${fr.x || 0}px, ${(fr.y || 0) + down}px) scale(${z})`, transformOrigin: '50% 45%'}}>
                <OffthreadVideo muted src={staticFile(s.src)} startFrom={Math.round(s.in * FPS)} style={{width: 1080, height: 1920}} />
              </AbsoluteFill>
            )}
          </Sequence>
        );
      })}
      <AbsoluteFill style={{background: 'radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.38) 100%)'}} />
    </AbsoluteFill>
  );
};

/* Top layer: subtitles. Small line = spoken phrase (word-by-word highlight), big line = keyword */
const keep = new RegExp('^(' + ['Rp', ...data.keepCase].join('|') + ')');
const clean = (t: string) => {
  const s = t.replace(/["“”]/g, '').replace(/[.,]+$/g, '');
  return keep.test(s) ? s : s.toLowerCase();
};
const shadow = '0 0 14px rgba(0,0,0,0.85), 0 3px 6px rgba(0,0,0,0.9), 0 0 2px rgba(0,0,0,1)';
const Subs: React.FC = () => {
  const frame = useCurrentFrame();
  const c = data.subs.find((s: any) => frame >= s.f && frame < s.t);
  if (!c) return null;
  const inn = interpolate(frame - c.f, [0, 4], [0, 1], cl);
  const ink = lightK(frame) > 0.5;                                  // on a bright insert: dark text, soft white glow
  const sh = ink ? '0 0 16px rgba(255,255,255,0.95)' : shadow;
  const top = (data.subTop ?? 1270) + (c.dy ?? 0) + Math.min(120, speakerShift(frame) * 0.4);   // sub_top in edit.json: caption band top (per video, from where the mouth sits)      // in split layout the speaker sits lower: keep the text under the chin
  return (
    <AbsoluteFill style={{top, height: 260, justifyContent: 'center', alignItems: 'center', flexDirection: 'column', opacity: 0.25 + 0.75 * inn, transform: `translateY(${(1 - inn) * 10}px)`}}>
      {/* on a bright full-screen insert the dark caption gets a calm backing in the panel colour, so it stays readable over busy pages */}
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', padding: ink ? '10px 34px 14px' : 0, borderRadius: 30,
        background: ink ? `${LIGHT}E8` : 'transparent', boxShadow: ink ? '0 8px 26px rgba(0,0,0,0.12)' : 'none', maxWidth: 1000}}>
      {c.small.length > 0 && (
        <div style={{fontFamily: SANS, fontWeight: 700, fontSize: c.big.length ? 50 : 56, color: ink ? INK : '#fff', textShadow: sh, letterSpacing: -0.5, textAlign: 'center', padding: ink ? 0 : '0 70px', lineHeight: 1.15}}>
          {c.small.map((w: any, i: number) => (
            <span key={i} style={{opacity: frame >= w.f - 1 ? 1 : 0.5, marginRight: 13, display: 'inline-block'}}>{clean(w.t)}</span>
          ))}
        </div>
      )}
      {c.big.length > 0 && (
        <div style={{fontFamily: SERIF, fontStyle: EMPH_STYLE, fontWeight: 800, fontSize: 112, color: ink ? INK : ACCENT, textShadow: sh, lineHeight: 1.0, marginTop: c.small.length ? 2 : 0, textAlign: 'center', letterSpacing: -1.5, whiteSpace: 'nowrap', fontVariantNumeric: 'lining-nums'}}>
          {c.big.map((w: any, i: number) => {
            const p = sp(frame, w.f - 2, {damping: 14, stiffness: 220, mass: 0.6});
            return <span key={i} style={{display: 'inline-block', marginRight: 22, opacity: Math.min(1, p * 1.5), transform: `scale(${0.7 + 0.3 * p})`}}>{clean(w.t)}</span>;
          })}
        </div>
      )}
      </div>
    </AbsoluteFill>
  );
};

export const Main: React.FC = () => {
  const frame = useCurrentFrame();
  return (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <Speaker />
    {overs.map((e: any, i: number) => (
      <Sequence key={'o' + i} from={e.f} durationInFrames={e.t - e.f} layout="none"><Overlay e={e} /></Sequence>
    ))}
    {splits.map((e: any, i: number) => (
      // mounted a little longer when a full-screen insert or the next split panel takes over, so nothing pops
      <Sequence key={'p' + i} from={e.f - (e.pre ? 10 : 0)} durationInFrames={e.t - e.f + (e.pre ? 10 : 0) + (e.post || e.chainNext ? 10 : 0)} layout="none">
        <SplitPanel e={e} p={splitP} />
      </Sequence>
    ))}
    {fulls.map((e: any, i: number) => (
      // a chained insert stays mounted 14 extra frames, underneath the next one sliding in
      <Sequence key={'f' + i} from={e.f} durationInFrames={e.t - e.f + (chainedAfter(e) ? 14 : 0)} layout="none">
        <Insert e={e} chained={chainedAfter(e)} prevChained={chainedBefore(e)} />
      </Sequence>
    ))}
    {/* darken top and bottom so white text stays readable on any footage or insert */}
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.28) 0%, rgba(0,0,0,0) 14%, rgba(0,0,0,0) 56%, rgba(0,0,0,0.62) 74%, rgba(0,0,0,0.72) 100%)', opacity: 1 - lightK(frame)}} />
    {data.sfx.map((x: any, i: number) => (
      <Sequence key={'s' + i} from={Math.max(0, x.f - (x.k === 'pop' || x.k === 'click' ? 0 : 4))} durationInFrames={20} layout="none">
        <Audio src={staticFile('sfx/' + x.k + '.wav')} volume={0.85} />
      </Sequence>
    ))}
    {/* optional background music, far below the voice, faded in and out */}
    {data.music ? (
      <Audio src={staticFile(data.music.src)} loop volume={(f) => (data.music.volume ?? 0.06) * interpolate(f, [0, 20, data.total - 45, data.total], [0, 1, 1, 0], cl) * musicK(f)} />
    ) : null}
    <Subs />
  </AbsoluteFill>
  );
};
