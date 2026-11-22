#!/usr/bin/env bash
# Install kit + brand fonts as system fonts (fontconfig) so Remotion's Chrome uses them without web-font loading.
set -euo pipefail
mkdir -p ~/.local/share/fonts/editkit
cp /home/user/editkit/fonts/*.[ot]tf ~/.local/share/fonts/editkit/ 2>/dev/null || true
fc-cache -f >/dev/null
fc-list : family | grep -iE "jakarta|playfair" | sort -u
