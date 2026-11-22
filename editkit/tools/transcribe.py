"""Word-level transcription of every clip.
Usage: python3 tools/transcribe.py [language] ["domain vocabulary, brand names, ..."]
Reads video/public/*.mp4 (normalized clips). Writes work/tx/<clip>.json (list of {w,s,e,p})
and work/tx/<clip>.txt (readable: word index, text, start time, gaps, low-confidence marks)."""
import sys, glob, json, os, subprocess
from faster_whisper import WhisperModel
lang = sys.argv[1] if len(sys.argv) > 1 else "id"
prompt = sys.argv[2] if len(sys.argv) > 2 else None
os.makedirs("work/tx", exist_ok=True)
# large-v3 on CPU is the tested default. Weak machine: WHISPER_MODEL=medium. NVIDIA GPU: WHISPER_DEVICE=cuda WHISPER_COMPUTE=float16
model = WhisperModel(os.environ.get("WHISPER_MODEL", "large-v3"), device=os.environ.get("WHISPER_DEVICE", "cpu"),
                     compute_type=os.environ.get("WHISPER_COMPUTE", "int8"), cpu_threads=os.cpu_count() or 4)
for f in sorted(glob.glob("video/public/*.mp4")):
    name = os.path.splitext(os.path.basename(f))[0]
    wav = f"work/tx/{name}.wav"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    # vad_filter off + no conditioning: keeps stumbles and repeated takes visible instead of "cleaning" them away
    segs, _ = model.transcribe(wav, language=lang, word_timestamps=True, vad_filter=False, beam_size=5,
                               condition_on_previous_text=False, initial_prompt=prompt)
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 2)}
             for s in segs for w in s.words]
    json.dump(words, open(f"work/tx/{name}.json", "w"), ensure_ascii=False)
    lines, line = [], []
    for i, w in enumerate(words):
        if i and w["s"] - words[i - 1]["e"] > 0.35:
            lines.append(" ".join(line)); line = []
            lines.append("    -- gap %.2fs --" % (w["s"] - words[i - 1]["e"]))
        line.append("%d:%s%s[%.2f]" % (i, w["w"], "?" if w["p"] < 0.5 else "", w["s"]))
    lines.append(" ".join(line) + "   (end %.2f)" % (words[-1]["e"] if words else 0))
    open(f"work/tx/{name}.txt", "w").write("\n".join(lines) + "\n")
    print(name, len(words), "words")
