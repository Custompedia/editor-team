import React from 'react';
import {AbsoluteFill, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame, Easing} from 'remotion';
import {SANS, SERIF, EMPH_STYLE, ACCENT, ON_ACCENT, MARKER, LIGHT, INK, FPS, cl, ease, sp} from './theme';

/* ---------- shared pieces ---------- */
const Label: React.FC<{num?: string; label?: string; sub?: string; ink?: boolean}> = ({num, label, sub, ink}) => {   // ink = dark text, for light backgrounds
  const f = useCurrentFrame();
  const p = sp(f, 3);
  if (!label) return null;
  return (
    <div style={{position: 'absolute', left: 64, top: 170, opacity: p, transform: `translateY(${(1 - p) * 30}px)`}}>
      <div style={{display: 'flex', alignItems: 'baseline', gap: 18}}>
        {num ? <span style={{fontFamily: SERIF, fontStyle: EMPH_STYLE, fontWeight: 800, fontSize: 84, color: ink ? INK : ACCENT, textShadow: ink ? 'none' : '0 4px 20px rgba(0,0,0,.6)'}}>{num}</span> : null}
        <span style={{fontFamily: SANS, fontWeight: 800, fontSize: 68, color: ink ? INK : '#fff', letterSpacing: ink ? -1 : 1, textShadow: ink ? 'none' : '0 4px 24px rgba(0,0,0,.75)'}}>{label}</span>
      </div>
      {sub ? <div style={{marginTop: 10, display: 'inline-block', fontFamily: SANS, fontWeight: 600, fontSize: 32, color: ink ? '#fff' : '#111', background: ink ? INK : 'rgba(255,255,255,0.92)', padding: '8px 18px', borderRadius: 12}}>{sub}</div> : null}
    </div>
  );
};
const Grain: React.FC = () => (
  <AbsoluteFill style={{opacity: 0.07, mixBlendMode: 'overlay', backgroundImage: 'repeating-radial-gradient(circle at 17% 32%, #fff 0, #000 1px, transparent 2px, transparent 5px)'}} />
);
const BlurBg: React.FC<{img: string}> = ({img}) => (
  <AbsoluteFill style={{backgroundColor: '#0c0c0e'}}>
    <Img src={staticFile(img)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(40px) brightness(0.32) saturate(1.2)', transform: 'scale(1.3)'}} />
  </AbsoluteFill>
);

/* ---------- photo: full-screen image or generated image, slow push-in, optional label ----------
   {type:"photo", img, label?, num?, sub?, pos?: "50% 40%" (focus point), dim?: 0..1} */
const Photo: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, e.t - e.f], [1.1, 1.22]);
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Img src={staticFile(e.img)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: e.pos || '50% 50%', transform: `scale(${z})`, transformOrigin: e.pos || '50% 50%', filter: `contrast(1.05) saturate(1.05) brightness(${1 - (e.dim || 0)})`}} />
      {e.light ? null : <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 30%)'}} />}
      <Label num={e.num} label={e.label} sub={e.sub} />
    </AbsoluteFill>
  );
};

/* ---------- clip: full-screen B-roll VIDEO (stock footage, product shot, screen recording), always muted ----------
   {type:"clip", src: "broll/x.mp4", from?: seconds into the file, label?, num?, sub?, pos?, dim?}
   The file must be at least 1 s longer than the time it is on screen. */
const Clip: React.FC<{e: any}> = ({e}) => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <OffthreadVideo muted src={staticFile(e.src)} startFrom={Math.round((e.from || 0) * FPS)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: e.pos || '50% 50%', filter: `brightness(${1 - (e.dim || 0)})`}} />
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 30%)'}} />
    <Label num={e.num} label={e.label} sub={e.sub} />
  </AbsoluteFill>
);

/* ---------- screenshot: a REAL page (article, profile, search result, app) as a card ----------
   {type:"screenshot", img, img_w, img_h (pixel size of the png), source?: "SITE · date",
    highlights?: [{x,y,w,h, at?: frames after start}]  marker-pen boxes in image pixels,
    scroll?: px of the image to scroll through while visible,
    click?: {x,y} in image pixels + click_at: anchor  -> a cursor moves there and clicks} */
const Screenshot: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const CARD_W = 960, CARD_TOP = 230, CARD_H = Math.min(1000, (e.img_h * CARD_W) / e.img_w);
  const S = CARD_W / e.img_w;
  const p = sp(f, 0, {damping: 18, stiffness: 120, mass: 0.8});
  const zoom = interpolate(f, [0, d], [1.0, 1.06]);
  const scroll = interpolate(f, [8, d - 4], [0, e.scroll || 0], {...cl, easing: Easing.inOut(Easing.quad)}) * S;
  const clickF = e.click_at !== undefined ? e.click_at - e.f : null;
  const mv = clickF !== null ? interpolate(f, [clickF - 28, clickF - 4], [0, 1], {...cl, easing: Easing.bezier(0.45, 0, 0.2, 1)}) : 0;
  const press = clickF !== null ? interpolate(f, [clickF, clickF + 3, clickF + 9], [0, 1, 0], cl) : 0;
  const tx = e.click ? e.click.x * S : 0, ty = e.click ? e.click.y * S - scroll : 0;
  return (
    <AbsoluteFill>
      <BlurBg img={e.img} />
      {e.source ? (
        <div style={{position: 'absolute', left: 60, top: 150, opacity: p, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: '#fff', letterSpacing: 3}}>
          <span style={{background: ACCENT, color: ON_ACCENT, padding: '6px 14px', borderRadius: 8, marginRight: 14}}>SUMBER</span>{e.source}
        </div>
      ) : null}
      <div style={{position: 'absolute', left: 60, top: CARD_TOP, width: CARD_W, height: CARD_H, borderRadius: 28, overflow: 'hidden', background: '#fff', boxShadow: '0 40px 90px rgba(0,0,0,0.6)', transform: `translateY(${(1 - p) * 420}px) rotate(${(1 - p) * -3}deg) scale(${zoom})`, transformOrigin: '50% 20%', opacity: Math.min(1, p * 2)}}>
        <div style={{position: 'absolute', left: 0, top: -scroll, width: CARD_W}}>
          <Img src={staticFile(e.img)} style={{width: CARD_W, display: 'block'}} />
          {(e.highlights || []).map((h: any, i: number) => {
            const at = h.at ?? 20 + i * 26;
            const w = interpolate(f, [at, at + 14], [0, 1], {...cl, easing: ease});
            return <div key={i} style={{position: 'absolute', left: h.x * S, top: h.y * S, height: h.h * S, width: h.w * S * w, background: MARKER, mixBlendMode: 'multiply'}} />;
          })}
          {e.click ? <div style={{position: 'absolute', left: tx - 150, top: e.click.y * S - 46, width: 300, height: 92, borderRadius: 46, background: '#000', opacity: 0.18 * press}} /> : null}
        </div>
        {clickF !== null && e.click ? (
          <svg width={96} height={96} viewBox="0 0 24 24" style={{position: 'absolute', left: interpolate(mv, [0, 1], [CARD_W + 40, tx]), top: interpolate(mv, [0, 1], [ty + 220, ty]) - Math.sin(mv * Math.PI) * 46, opacity: interpolate(f, [clickF - 30, clickF - 25], [0, 1], cl), transform: `scale(${1 - 0.14 * press})`, transformOrigin: '0% 0%', filter: 'drop-shadow(0 8px 10px rgba(0,0,0,0.45))'}}>
            <path d="M3 2 L3 19.5 L7.6 15.4 L10.7 22.3 L13.6 21 L10.6 14.2 L16.8 14.2 Z" fill="#111" stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
          </svg>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- custom: your own SVG/diagram component for numbers, steps, comparisons ----------
   {type:"custom", name:"chart", ...props}. Register components in CUSTOM. Draw with real SVG
   (paths drawn on with strokeDashoffset, labels that spring in), not boxes of HTML text. */
const Bars: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const max = Math.max(...e.values.map((v: any) => v.n));
  const hi = e.color || ACCENT;   // the one bar that matters (the last one); e.color overrides when ACCENT reads badly on LIGHT
  return (
    <AbsoluteFill style={{background: LIGHT}}>
      <Label ink label={e.label} sub={e.sub} />
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path d="M130 1120 H950" stroke="#D2D2D7" strokeWidth={4} strokeLinecap="round" />
        {e.values.map((v: any, i: number) => {
          const g = sp(f, 10 + i * 8, {damping: 18, stiffness: 120});
          const last = i === e.values.length - 1;
          const h = (v.n / max) * 560 * g, x = 170 + i * (760 / e.values.length), w = 560 / e.values.length;
          return (
            <g key={i}>
              <rect x={x} y={1118 - h} width={w} height={h} rx={16} fill={last ? hi : '#C7C7CC'} />
              <text x={x + w / 2} y={1118 - h - 24} textAnchor="middle" fontFamily={SANS} fontWeight={800} fontSize={42} fill={last ? hi : INK} opacity={g}>{v.text ?? v.n}</text>
              <text x={x + w / 2} y={1184} textAnchor="middle" fontFamily={SANS} fontWeight={700} fontSize={32} fill="#6E6E73">{v.name}</text>
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};

/* ---------- timeline (job02): months BEFORE an event on one line; a bar grows back from the event as each span is said ----------
   {type:"custom", name:"timeline", label?, sub?, event: "Lebaran", months: 4, items: [{at: anchor, from: 3, text: "2-3 bulan"}, ...]}
   Diagram because "how many months before Lebaran" is a time relation with no physical picture. */
const Timeline: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const N = e.months || 4, X0 = 120, X1 = 900, Y = 900;
  const xOf = (m: number) => X1 - ((X1 - X0) * m) / N;            // m months before the event
  const draw = interpolate(f, [2, 16], [1, 0], {...cl, easing: ease});
  const pe = sp(f, 8, {damping: 13, stiffness: 170, mass: 0.7});
  // current span = the last one whose time has come
  const spans = (e.items || []).map((x: any) => ({...x, lf: x.f - e.f}));
  let reach = 0, label = '';
  spans.forEach((x: any) => { const g = interpolate(f, [x.lf, x.lf + 14], [0, 1], {...cl, easing: ease}); if (f >= x.lf) { reach = reach + (x.from - reach) * g; label = x.text; } });
  const cur = spans.filter((x: any) => f >= x.lf).pop();
  const lp = cur ? sp(f, cur.lf, {damping: 14, stiffness: 200, mass: 0.6}) : 0;
  return (
    <AbsoluteFill style={{background: LIGHT}}>
      <Label ink label={e.label} sub={e.sub} />
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path d={`M${X0 - 30} ${Y} H${X1}`} stroke={INK} strokeOpacity={0.18} strokeWidth={10} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={draw} />
        {Array.from({length: N}, (_, i) => N - i).map((m) => (
          <g key={m} opacity={interpolate(f, [6 + (N - m) * 3, 14 + (N - m) * 3], [0, 1], cl)}>
            <circle cx={xOf(m)} cy={Y} r={13} fill={reach >= m - 0.02 ? INK : LIGHT} stroke={INK} strokeWidth={5} />
            <text x={xOf(m)} y={Y + 78} textAnchor="middle" fontFamily={SANS} fontWeight={700} fontSize={40} fill={INK} opacity={0.7}>{m} bln</text>
          </g>
        ))}
        {reach > 0 ? <path d={`M${xOf(reach)} ${Y} H${X1}`} stroke={ACCENT} strokeWidth={34} strokeLinecap="round" /> : null}
        <g transform={`translate(${X1} ${Y}) scale(${pe})`}>
          <circle r={46} fill={ACCENT} stroke={INK} strokeWidth={6} />
          <path d="M-14 -2 L-3 10 L16 -12" stroke={INK} strokeWidth={8} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        </g>
        <text x={X1} y={Y + 112} textAnchor="middle" fontFamily={SERIF} fontStyle={EMPH_STYLE} fontWeight={800} fontSize={52} fill={INK} opacity={pe}>{e.event}</text>
        {cur ? (
          <g opacity={Math.min(1, lp * 1.4)} transform={`translate(${(xOf(reach) + X1) / 2} ${Y - 170}) scale(${0.8 + 0.2 * lp})`}>
            <text textAnchor="middle" fontFamily={SERIF} fontStyle={EMPH_STYLE} fontWeight={800} fontSize={120} fill={INK}>{label}</text>
            <text y={72} textAnchor="middle" fontFamily={SANS} fontWeight={600} fontSize={44} fill={INK} opacity={0.65}>{e.after || ''}</text>
          </g>
        ) : null}
      </svg>
    </AbsoluteFill>
  );
};

/* ---------- igprofile (job02): end card presenting a REAL Instagram account from the user's screenshot ----------
   Text re-typeset 1:1 from the screenshot in this video's look (the screenshot is too small to show sharp); avatar and post tiles are
   real crops of the screenshot. Not drawn to look like the Instagram app. Facts only from the screenshot.
   {type:"custom", name:"igprofile", avatar, handle, verified, full_name, stats:[[n,label]...], role, bio:[lines; "@x" words bold], link, button,
    tiles:[img...] (rows of 3), row2_at?: anchor} */
const IgProfile: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const z = interpolate(f, [0, d], [1.0, 1.035]);
  const up = (at: number) => { const p = sp(f, at, {damping: 16, stiffness: 150, mass: 0.7}); return {opacity: Math.min(1, p * 1.3), transform: `translateY(${(1 - p) * 34}px)`}; };
  const row2 = e.row2_at !== undefined ? e.row2_at - e.f : 40;
  const TW = 300, TH = 400, GAP = 14, GX = (1080 - 3 * TW - 2 * GAP) / 2, GY = 820;
  const bio = (line: string, i: number) => (
    <div key={i} style={{...up(12 + i * 3), fontFamily: SANS, fontWeight: 500, fontSize: 36, color: INK, lineHeight: 1.35}}>
      {line.split(/(@[\w.]+)/).map((w: string, j: number) => w.startsWith('@') ? <span key={j} style={{fontWeight: 700, borderBottom: `5px solid ${ACCENT}`}}>{w}</span> : <span key={j}>{w}</span>)}
    </div>
  );
  return (
    <AbsoluteFill style={{background: LIGHT, transform: `scale(${z})`, transformOrigin: '50% 30%'}}>
      <div style={{position: 'absolute', left: 64, top: 170, display: 'flex', alignItems: 'center', gap: 40}}>
        <div style={{...up(0), width: 220, height: 220, borderRadius: 110, padding: 7, background: '#fff', boxShadow: '0 14px 40px rgba(0,0,0,0.18)'}}>
          <Img src={staticFile(e.avatar)} style={{width: 206, height: 206, borderRadius: 103, display: 'block'}} />
        </div>
        <div>
          <div style={{...up(4), display: 'flex', alignItems: 'center', gap: 14}}>
            <span style={{fontFamily: SANS, fontWeight: 800, fontSize: 56, color: INK, letterSpacing: -1}}>{e.handle}</span>
            {e.verified ? (
              <svg width={46} height={46} viewBox="0 0 40 40"><circle cx={20} cy={20} r={18} fill="#0095F6" /><path d="M12 20.5 L17.5 26 L28.5 14.5" stroke="#fff" strokeWidth={4.5} fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
            ) : null}
          </div>
          <div style={{...up(6), fontFamily: SANS, fontWeight: 500, fontSize: 34, color: INK, opacity: 0.8, marginTop: 4}}>{e.full_name}</div>
          <div style={{...up(8), display: 'flex', gap: 34, marginTop: 18}}>
            {(e.stats || []).map((x: any, i: number) => (
              <div key={i} style={{fontFamily: SANS, fontSize: 32, color: INK}}><span style={{fontWeight: 800}}>{x[0]}</span> <span style={{fontWeight: 500, opacity: 0.75}}>{x[1]}</span></div>
            ))}
          </div>
        </div>
      </div>
      <div style={{position: 'absolute', left: 64, right: 64, top: 430}}>
        {e.role ? <div style={{...up(10), fontFamily: SANS, fontWeight: 500, fontSize: 32, color: INK, opacity: 0.6, marginBottom: 6}}>{e.role}</div> : null}
        {(e.bio || []).map(bio)}
        {e.link ? <div style={{...up(22), fontFamily: SANS, fontWeight: 700, fontSize: 34, color: INK, marginTop: 6}}>🔗 {e.link}</div> : null}
      </div>
      {(e.tiles || []).map((src: string, i: number) => {
        const r = Math.floor(i / 3), c = i % 3;
        const at = (r === 0 ? 18 : row2) + c * 4;
        const p = sp(f, at, {damping: 15, stiffness: 160, mass: 0.7});
        return (
          <div key={i} style={{position: 'absolute', left: GX + c * (TW + GAP), top: GY + r * (TH + GAP), width: TW, height: TH, borderRadius: 18, overflow: 'hidden',
            opacity: Math.min(1, p * 1.4), transform: `translateY(${(1 - p) * 60}px) scale(${0.92 + 0.08 * p})`, boxShadow: '0 12px 30px rgba(0,0,0,0.2)'}}>
            <Img src={staticFile(src)} style={{width: TW, height: TH, objectFit: 'cover', display: 'block'}} />
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
const CUSTOM: Record<string, React.FC<{e: any}>> = {bars: Bars, timeline: Timeline, igprofile: IgProfile};

/* ---------- outro: brand/creator end card over an image ----------
   {type:"outro", img, logo?, handle?, cta?} */
const Outro: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const z = interpolate(f, [0, d], [1.06, 1.2]);
  const p = sp(f, Math.max(8, d - 64), {damping: 16, stiffness: 140});
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <Img src={staticFile(e.img)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${z})`, transformOrigin: '50% 45%'}} />
      <AbsoluteFill style={{backgroundColor: `rgba(10,8,6,${0.45 * p})`}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 520, textAlign: 'center', opacity: p, transform: `translateY(${(1 - p) * 40}px)`}}>
        {e.logo ? (
          <div style={{display: 'inline-flex', width: 280, height: 280, borderRadius: 140, background: '#fff', alignItems: 'center', justifyContent: 'center', boxShadow: '0 20px 60px rgba(0,0,0,0.5)'}}>
            <Img src={staticFile(e.logo)} style={{width: 200, height: 200, objectFit: 'contain'}} />
          </div>
        ) : null}
        {e.handle ? <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 66, color: '#fff', marginTop: 34, textShadow: '0 4px 24px rgba(0,0,0,.7)'}}>{e.handle}</div> : null}
        {e.cta ? <div style={{marginTop: 18}}><span style={{fontFamily: SANS, fontWeight: 800, fontSize: 40, color: ON_ACCENT, background: ACCENT, padding: '12px 30px', borderRadius: 16}}>{e.cta}</span></div> : null}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- wrapper for every full-screen insert: owns ALL in/out transitions ---------- */
export const Insert: React.FC<{e: any; chained: boolean; prevChained: boolean}> = ({e, chained, prevChained}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const inn = prevChained ? 1 : interpolate(f, [0, 7], [0, 1], {...cl, easing: ease});          // fade in over the speaker
  const out = chained || e.type === 'outro' || e.hold_end ? 1 : interpolate(f, [d - 6, d], [1, 0], cl);          // fade back to the speaker
  const slide = prevChained ? interpolate(f, [0, 12], [1, 0], {...cl, easing: Easing.bezier(0.45, 0, 0.15, 1)}) : 0; // push over the previous insert
  const body = e.type === 'photo' ? <Photo e={e} /> : e.type === 'clip' ? <Clip e={e} /> : e.type === 'screenshot' ? <Screenshot e={e} /> : e.type === 'outro' ? <Outro e={e} /> : React.createElement(CUSTOM[e.name], {e});
  return (
    <AbsoluteFill style={{opacity: Math.min(inn, out), transform: prevChained ? `translateX(${slide * 1080}px)` : `scale(${1 + (1 - inn) * 0.06})`, overflow: 'hidden', boxShadow: prevChained ? '-30px 0 60px rgba(0,0,0,0.5)' : undefined}}>
      {body}
      <Grain />
    </AbsoluteFill>
  );
};

/* ---------- split: the visual sits in a panel on TOP, the speaker stays visible BELOW it ----------
   {type:"split", img | src (video), h?: 760 panel height px, shift?: 300 px the speaker moves down,
    fit?: "cover" | "contain" (contain = logos, app screens, charts: nothing cropped, padded; pad?: CSS padding), bg?: panel colour, pos?, from?,
    caption?: "short label", click?: {x,y} in PANEL pixels + click_at: anchor -> cursor moves there and clicks}
   Use it when the viewer should keep seeing the speaker (reaction, demo, eye contact) while looking at the thing.
   Main.tsx moves the speaker; `p` is its 0..1 progress so panel and speaker move as one. */
export const SplitPanel: React.FC<{e: any; p: (e: any, frame: number) => number}> = ({e, p}) => {
  const f = useCurrentFrame();                       // local frame of this panel's <Sequence>
  const lead = e.pre ? 10 : 0;
  const abs = e.f - lead + f;                        // absolute frame
  const H = e.h ?? 760;
  const k = p(e, abs);
  const fade = e.chainPrev ? interpolate(abs, [e.f, e.f + 10], [0, 1], cl) : 1;   // a chained panel dissolves over the previous one
  const z = interpolate(abs, [e.f, e.t], [1.0, e.fit === 'contain' ? 1.0 : 1.06], cl);
  const media: React.CSSProperties = {width: '100%', height: '100%', objectFit: e.fit || 'cover', objectPosition: e.pos || '50% 50%', transform: `scale(${z})`,
    boxSizing: 'border-box', padding: e.fit === 'contain' ? (e.pad ?? '130px 110px 90px') : 0};   // contain: breathing room, clear of the app's top bar
  const clickF = e.click_at !== undefined ? e.click_at - e.f + lead : null;
  const mv = clickF !== null ? interpolate(f, [clickF - 26, clickF - 4], [0, 1], {...cl, easing: Easing.bezier(0.45, 0, 0.2, 1)}) : 0;
  const press = clickF !== null ? interpolate(f, [clickF, clickF + 3, clickF + 9], [0, 1, 0], cl) : 0;
  return (
    <div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: H, overflow: 'hidden', background: e.bg || (e.fit === 'contain' ? LIGHT : '#000'), transform: `translateY(${-(1 - k) * H}px)`, opacity: fade, boxShadow: '0 14px 40px rgba(0,0,0,0.35)'}}>
      {e.src ? <OffthreadVideo muted src={staticFile(e.src)} startFrom={Math.round((e.from || 0) * FPS)} style={media} /> : <Img src={staticFile(e.img)} style={media} />}
      {e.caption ? (
        <div style={{position: 'absolute', left: 44, bottom: 36, fontFamily: SANS, fontWeight: 700, fontSize: 34, color: INK, background: 'rgba(255,255,255,0.94)', padding: '10px 22px', borderRadius: 16, opacity: interpolate(f, [lead + 6, lead + 14], [0, 1], cl)}}>{e.caption}</div>
      ) : null}
      {clickF !== null && e.click ? (
        <svg width={88} height={88} viewBox="0 0 24 24" style={{position: 'absolute', left: interpolate(mv, [0, 1], [1080 + 20, e.click.x]), top: interpolate(mv, [0, 1], [e.click.y + 200, e.click.y]) - Math.sin(mv * Math.PI) * 40, transform: `scale(${1 - 0.14 * press})`, transformOrigin: '0% 0%', filter: 'drop-shadow(0 8px 10px rgba(0,0,0,0.45))'}}>
          <path d="M3 2 L3 19.5 L7.6 15.4 L10.7 22.3 L13.6 21 L10.6 14.2 L16.8 14.2 Z" fill="#111" stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
        </svg>
      ) : null}
    </div>
  );
};

/* ---------- overlays: sit on top of the speaker, in the top third (never over the face or subtitles) ----------
   {type:"title", line1, line2}
   {type:"bubbles", items:[{at: anchor, text, img?, side?: "l"|"r", x_at?: anchor}]}  chat/quote bubbles
   {type:"chips",   items:[{at: anchor, n?: "1", text}]}                               numbered key points */
export const Overlay: React.FC<{e: any}> = ({e}) => {
  const f = useCurrentFrame();
  const d = e.t - e.f;
  const out = interpolate(f, [d - 7, d], [1, 0], cl);
  if (e.type === 'title') {
    const p = sp(f, 0, {damping: 14, stiffness: 160, mass: 0.7});
    const hl = interpolate(f, [8, 20], [0, 1], {...cl, easing: ease});
    return (
      <AbsoluteFill style={{opacity: out}}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 120, textAlign: 'center', transform: `translateY(${(1 - p) * -60}px) scale(${0.9 + 0.1 * p})`, opacity: p}}>
          <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 50, color: '#fff', letterSpacing: 5, textShadow: '0 4px 20px rgba(0,0,0,.8)'}}>{e.line1}</div>
          <div style={{display: 'inline-block', position: 'relative', marginTop: 6, padding: '0 34px'}}>
            <div style={{position: 'absolute', left: 0, top: 22, bottom: 10, width: `${hl * 100}%`, background: ACCENT, borderRadius: 14, transform: 'skewX(-8deg)'}} />
            <span style={{position: 'relative', fontFamily: SERIF, fontStyle: EMPH_STYLE, fontWeight: 800, fontSize: 132, color: hl > 0.5 ? ON_ACCENT : '#fff', lineHeight: 1.15}}>{e.line2}</span>
          </div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{opacity: out}}>
      {e.items.map((it: any, i: number) => {
        const at = it.f - e.f;
        if (f < at) return null;
        const p = sp(f, at, {damping: 13, stiffness: 190, mass: 0.6});
        if (e.type === 'chips') {
          return (
            <div key={i} style={{position: 'absolute', left: 50, top: (e.top ?? 140) + i * (e.step ?? 138), display: 'flex', alignItems: 'center', gap: 22, background: 'rgba(14,14,18,0.86)', borderRadius: 60, padding: it.n ? '16px 44px 16px 16px' : '22px 44px', transform: `translateX(${(1 - p) * -80}px) scale(${(0.85 + 0.15 * p) * (e.scale ?? 1)})`, opacity: Math.min(1, p * 1.4), transformOrigin: '0% 50%', boxShadow: '0 16px 40px rgba(0,0,0,0.4)', border: '3px solid rgba(255,255,255,0.14)'}}>
              {it.n ? <div style={{width: 84, height: 84, borderRadius: 42, background: ACCENT, color: ON_ACCENT, fontFamily: SANS, fontWeight: 800, fontSize: 50, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{it.n}</div> : null}
              <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 48, color: '#fff'}}>{it.text}</div>
            </div>
          );
        }
        const right = it.side === 'r';
        const xp = it.x_at !== undefined && f >= it.x_at - e.f ? sp(f, it.x_at - e.f, {damping: 9, stiffness: 220, mass: 0.6}) : 0;
        return (
          <div key={i} style={{position: 'absolute', top: 130 + i * 210, left: right ? undefined : 44, right: right ? 44 : undefined, maxWidth: 800, transformOrigin: right ? '100% 100%' : '0% 100%', transform: `scale(${p}) rotate(${(1 - p) * (right ? 6 : -6)}deg)`}}>
            <div style={{display: 'flex', alignItems: 'center', gap: 22, background: '#fff', borderRadius: 40, borderBottomLeftRadius: right ? 40 : 10, borderBottomRightRadius: right ? 10 : 40, padding: it.img ? '18px 34px 18px 18px' : it.x_at !== undefined ? '24px 100px 24px 36px' : '24px 36px', boxShadow: '0 18px 44px rgba(0,0,0,0.42)'}}>
              {it.img ? <Img src={staticFile(it.img)} style={{width: 132, height: 132, objectFit: 'cover', borderRadius: 26, flexShrink: 0}} /> : null}
              <div style={{fontFamily: SANS, fontWeight: 700, fontSize: 40, lineHeight: 1.22, color: '#15151a', letterSpacing: -0.4}}>{it.text}</div>
            </div>
            {xp ? (
              <div style={{position: 'absolute', right: -26, top: -30, width: 118, height: 118, borderRadius: 59, background: '#FF3B30', display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${xp}) rotate(${(1 - xp) * -40}deg)`, boxShadow: '0 12px 28px rgba(0,0,0,0.45)', border: '6px solid #fff'}}>
                <svg width={60} height={60} viewBox="0 0 60 60"><path d="M12 12 L48 48 M48 12 L12 48" stroke="#fff" strokeWidth={10} strokeLinecap="round" /></svg>
              </div>
            ) : null}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
