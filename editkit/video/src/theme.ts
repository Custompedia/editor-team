import {Easing, spring} from 'remotion';
// One place for the look. Swap fonts/colours here when the user has a brand kit.
// FONTS IN THIS CLOUD ENVIRONMENT: fonts are installed as SYSTEM fonts (fontconfig), not loaded as web fonts.
// Tested: any web font (@remotion/google-fonts, @remotion/fonts, FontFace) makes Chrome's renderer hang after ~90 frames here.
// Kit fonts live in /home/user/editkit/fonts and are installed by: bash /home/user/editkit/tools/install_fonts.sh
// Brand font: put the .ttf/.otf files in /home/user/editkit/fonts (or ~/.local/share/fonts), run install_fonts.sh,
// check `fc-list | grep -i <name>`, then use its family name below.
export const SANS = "'Plus Jakarta Sans', sans-serif";
export const SERIF = "'Playfair Display', serif";
export const ACCENT = '#FFD60A';                 // keyword colour on dark footage; use the brand colour when there is one
export const LIGHT = '#F5F5F7', INK = '#1D1D1F';  // bright, clean default for diagrams and panels
export const FPS = 30;
export const cl = {extrapolateLeft: 'clamp' as const, extrapolateRight: 'clamp' as const};
export const ease = Easing.bezier(0.2, 0.8, 0.2, 1);
export const sp = (frame: number, at: number, cfg: any = {damping: 15, stiffness: 180, mass: 0.7}) =>
  spring({frame: frame - at, fps: FPS, config: cfg});
