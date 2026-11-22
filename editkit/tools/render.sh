#!/usr/bin/env bash
# Full render + delivery encode + technical checks.
# Usage: tools/render.sh v1            1080x1920
#        tools/render.sh v1 1.3334     1440x2560 (sharper upload; ~1.8x slower). Any Remotion --scale value works.
# CONCURRENCY=2 tools/render.sh v1     fewer parallel browser tabs on a machine with little RAM
set -euo pipefail
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; elif [ -f .venv/Scripts/activate ]; then . .venv/Scripts/activate; fi
V=${1:-v1}; SCALE=${2:-1}
mkdir -p out work
python3 tools/build_timeline.py > work/timeline_$V.log
(cd video && npx tsc --noEmit -p . && npx remotion render src/index.ts Edit out/master_$V.mp4 --codec=h264 --crf=16 --audio-bitrate=256k --color-space=bt709 --scale=$SCALE ${CONCURRENCY:+--concurrency=$CONCURRENCY} --log=error)
# Delivery file. --color-space=bt709 above makes Remotion write limited-range yuv420p tagged BT.709 (its default is
# full-range yuvj420p, which some phones and upload pipelines show washed out or too dark). Keep those tags here.
MAXRATE=$(awk "BEGIN{printf \"%d\", 6000 * $SCALE * $SCALE}")
ffmpeg -loglevel error -y -i video/out/master_$V.mp4 -c:v libx264 -preset medium -crf 22 -maxrate ${MAXRATE}k -bufsize $((MAXRATE * 2))k \
  -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart out/final_$V.mp4
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate,pix_fmt,color_range,color_space -of default=nw=1 out/final_$V.mp4
ffmpeg -hide_banner -i out/final_$V.mp4 -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input Integrated|Input True Peak"
# expected: h264 + aac, 1080x1920 (or scaled), 30/1, yuv420p, tv, bt709, loudness about -14..-16 LUFS, true peak below -1 dBTP
