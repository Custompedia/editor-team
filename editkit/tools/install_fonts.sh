#!/usr/bin/env bash
# Install kit + brand fonts as system fonts (fontconfig) so Remotion's Chrome uses them without web-font loading.
# The family names printed at the end are the exact names to use in work/edit.json -> theme.font_text / theme.font_emph.
set -euo pipefail
mkdir -p ~/.local/share/fonts/editkit
cp /home/user/editkit/fonts/*.[ot]tf ~/.local/share/fonts/editkit/ 2>/dev/null || true
fc-cache -f >/dev/null
fc-scan --format "%{family[0]}\n" ~/.local/share/fonts/editkit/ 2>/dev/null | sort -u
