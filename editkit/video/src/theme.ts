import {Easing, spring} from 'remotion';
import raw from './data.json';
// THE LOOK IS DATA, NOT A DEFAULT. Colours and fonts come from the "theme" block of work/edit.json, which
// tools/build_timeline.py validates (hex colours, installed fonts, a written reason) and copies into data.json.
// To change the look, edit work/edit.json -> "theme" and run build_timeline.py again. Do not hard-code colours/fonts here.
// FONTS IN THIS CLOUD ENVIRONMENT: fonts are installed as SYSTEM fonts (fontconfig), not loaded as web fonts.
// Tested: any web font (@remotion/google-fonts, @remotion/fonts, FontFace) makes Chrome's renderer hang after ~90 frames here.
// Brand font: put the static .ttf/.otf files in /home/user/editkit/fonts, run bash /home/user/editkit/tools/install_fonts.sh,
// check `fc-list : family | grep -i <name>`, then put that family name in theme.font_text / theme.font_emph.
const T = (raw as any).theme;
if (!T || !T.accent || !T.font_text) {
  throw new Error('data.json has no "theme": add a "theme" block to work/edit.json and run tools/build_timeline.py (see edit-json.md)');
}
export const SANS = `'${T.font_text}', sans-serif`;       // subtitles, labels, UI text
export const SERIF = `'${T.font_emph}', sans-serif`;      // big emphasis words, title line 2, numbers (name kept for old code: need not be a serif)
export const EMPH_STYLE: 'italic' | 'normal' = T.emph_style;   // font-style of everything drawn with SERIF
export const ACCENT: string = T.accent;                   // emphasis colour: big words, highlights, the bar/point that matters
export const ON_ACCENT: string = T.on_accent;             // text drawn on an ACCENT fill (computed by build_timeline for contrast)
export const MARKER: string = T.marker;                   // screenshot marker-pen highlight (multiply): a light tint
export const LIGHT: string = T.light, INK: string = T.ink; // bright panel/diagram background, dark text
export const FPS = 30;
export const cl = {extrapolateLeft: 'clamp' as const, extrapolateRight: 'clamp' as const};
export const ease = Easing.bezier(0.2, 0.8, 0.2, 1);
export const sp = (frame: number, at: number, cfg: any = {damping: 15, stiffness: 180, mass: 0.7}) =>
  spring({frame: frame - at, fps: FPS, config: cfg});
