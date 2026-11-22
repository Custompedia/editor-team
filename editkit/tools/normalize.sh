#!/usr/bin/env bash
# Normalize every raw clip: upright 1080x1920, 30 fps, short GOP (fast frame seeking), cleaned + leveled voice.
# Usage: tools/normalize.sh            (reads raw/*.mp4|mov, writes video/public/<name>.mp4)
# Wide (16:9) source: CROP_X=0..1 picks which part of the width to keep (0 = left, 0.5 = centre, 1 = right) and
# SUFFIX names the result, e.g.  CROP_X=0.2 SUFFIX=_L tools/normalize.sh ; CROP_X=0.8 SUFFIX=_R tools/normalize.sh
set -euo pipefail
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; elif [ -f .venv/Scripts/activate ]; then . .venv/Scripts/activate; fi
X=${CROP_X:-0.5}; SUFFIX=${SUFFIX:-}
mkdir -p video/public
for f in raw/*.mp4 raw/*.mov raw/*.MP4 raw/*.MOV; do
  [ -e "$f" ] || continue
  name=$(basename "${f%.*}")$SUFFIX
  # ffmpeg applies rotation metadata automatically; scale+crop fills 9:16 without distortion.
  ffmpeg -loglevel error -y -i "$f" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920:(iw-1080)*$X:0,eq=contrast=1.06:saturation=1.12:brightness=0.01,unsharp=5:5:0.5" \
    -r 30 -c:v libx264 -preset fast -crf 15 -g 10 -pix_fmt yuv420p \
    -af "highpass=f=90,afftdn=nr=10:nf=-28,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=9" \
    -ar 48000 -c:a aac -b:a 192k "video/public/$name.mp4"
  ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of csv=p=0 "video/public/$name.mp4" | tr '\n' ' '; echo " <- $name"
done
