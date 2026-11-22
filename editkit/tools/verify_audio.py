"""Re-transcribe the RENDERED video and show the words around every cut, to prove no word was clipped or doubled.
Usage: python3 tools/verify_audio.py <file.mp4> [language=id]"""
import sys, json, subprocess, os
from faster_whisper import WhisperModel
video = sys.argv[1]; lang = sys.argv[2] if len(sys.argv) > 2 else "id"
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", "/tmp/_final.wav"], check=True)
m = WhisperModel(os.environ.get("WHISPER_MODEL", "large-v3"), device=os.environ.get("WHISPER_DEVICE", "cpu"),
                 compute_type=os.environ.get("WHISPER_COMPUTE", "int8"), cpu_threads=os.cpu_count() or 4)
segs, _ = m.transcribe("/tmp/_final.wav", language=lang, word_timestamps=True, beam_size=5, condition_on_previous_text=False)
ws = [(w.word.strip(), w.start) for s in segs for w in s.words]
d = json.load(open("video/src/data.json"))
print("FULL TEXT:\n" + " ".join(w for w, _ in ws) + "\n")
for s in d["segs"][1:]:
    j = s["start"] / d["fps"]
    print("cut at %.2fs: " % j + " ".join(w for w, t in ws if j - 2.2 < t < j) + "  ||  " + " ".join(w for w, t in ws if j <= t < j + 2.2))
