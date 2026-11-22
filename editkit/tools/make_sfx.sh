#!/usr/bin/env bash
# Synthesize four quiet sound effects with ffmpeg (no downloads, no licences): video/public/sfx/*.wav
set -euo pipefail
mkdir -p video/public/sfx && cd video/public/sfx
ffmpeg -loglevel error -y -f lavfi -i "anoisesrc=d=0.55:c=pink:a=0.5:s=7" -af "bandpass=f=900:w=700,lowpass=f=3500,volume=30dB,afade=t=in:d=0.26:curve=qsin,afade=t=out:st=0.26:d=0.29:curve=qsin" -ar 48000 -ac 2 whoosh.wav
ffmpeg -loglevel error -y -f lavfi -i "anoisesrc=d=0.3:c=pink:a=0.5:s=3" -af "bandpass=f=1800:w=1200,volume=32dB,afade=t=in:d=0.1:curve=qsin,afade=t=out:st=0.1:d=0.2:curve=qsin" -ar 48000 -ac 2 swish.wav
ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='0.5*sin(2*PI*(520+1400*t)*t)*exp(-28*t)':d=0.16:s=48000" -af "afade=t=in:d=0.004,volume=-14dB" -ac 2 pop.wav
ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='(0.6*sin(2*PI*2200*t)+0.4*sin(2*PI*900*t))*exp(-140*t)':d=0.06:s=48000" -af "afade=t=in:d=0.001,volume=-13dB" -ac 2 click.wav
# every effect must peak around -18..-24 dB: far below the voice (-1.5 dB peak), audible but never distracting
for f in *.wav; do printf "%s " "$f"; ffmpeg -hide_banner -i "$f" -af volumedetect -f null - 2>&1 | grep -o "max_volume.*"; done
