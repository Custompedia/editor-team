"""Loudness envelope around a candidate cut point, to place cuts in real silence.
Usage: python3 tools/envelope.py <clip name> <t0> <t1> [window_sec=0.01]
Prints time:dB pairs. Speech is roughly > -25 dB, pauses < -35 dB (after normalize.sh)."""
import sys, subprocess, numpy as np
name, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
win = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f"video/public/{name}.mp4", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
t, out = t0, []
while t < t1:
    s = x[int(t * 16000):int((t + win) * 16000)]
    out.append("%.2f:%d" % (t, 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-6)))
    t += win
print(" ".join(out))
