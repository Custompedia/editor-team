#!/usr/bin/env bash
# One-time setup of a project folder (safe to run again). Needs: python3 (3.9+), node (18+, 20 recommended), ffmpeg.
# Usage: bash tools/setup.sh
set -euo pipefail
for t in python3 node npm ffmpeg ffprobe; do command -v $t >/dev/null || { echo "MISSING: $t  -> install it first (see the guide, 'Yang harus terpasang')"; exit 1; }; done
mkdir -p raw work/tx video/public/sfx video/out out
[ -d .venv ] || python3 -m venv .venv
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; else . .venv/Scripts/activate; fi
python3 -m pip install --quiet --upgrade pip
python3 -m pip install --quiet faster-whisper numpy pillow playwright gdown yt-dlp
if [ "$(uname -s)" = "Linux" ] && command -v sudo >/dev/null && sudo -n true 2>/dev/null; then python3 -m playwright install --with-deps chromium; else python3 -m playwright install chromium; fi
(cd video && npm install --no-audit --no-fund && npx remotion browser ensure)
bash tools/make_sfx.sh
python3 tools/doctor.py
