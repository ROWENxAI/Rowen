"""转录直播视频 H:\小绿点\视频号 -> H:\转录\视频转录\直播"""
import os, sys, json, time, subprocess, traceback
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

SRC = r"H:\小绿点\视频号"
OUTPUT = r"H:\转录\视频转录\直播"
LOG_DIR = r"H:\转录\任务日志"
os.makedirs(OUTPUT, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

DONE_LOG = os.path.join(LOG_DIR, "live_done.json")
PROGRESS_LOG = os.path.join(LOG_DIR, "live_progress.log")
ERROR_LOG = os.path.join(LOG_DIR, "live_errors.log")

MEDIA_EXTS = {'.ts', '.mp4', '.mov', '.avi', '.mkv', '.flv', '.mp3', '.m4a', '.wav'}

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    try: print(line, flush=True)
    except: print(line.encode('utf-8',errors='replace').decode('utf-8'), flush=True)
    with open(PROGRESS_LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def log_error(fp, reason):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {fp}: {reason}\n")

def load_done():
    if os.path.exists(DONE_LOG):
        with open(DONE_LOG, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_done(s):
    with open(DONE_LOG, "w", encoding="utf-8") as f:
        json.dump(list(s), f, ensure_ascii=False, indent=2)

def get_duration(fp):
    try:
        r = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",fp], capture_output=True, text=True, timeout=60)
        return float(r.stdout.strip())
    except:
        return 0

def fmt_ts(sec):
    h = int(sec//3600); m = int((sec%3600)//60); s = int(sec%60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def extract_audio(fp, out):
    try:
        subprocess.run(["ffmpeg","-i",fp,"-vn","-acodec","pcm_s16le","-ar","16000","-ac","1","-y",out], capture_output=True, timeout=1800)
        return os.path.exists(out)
    except:
        return False

def safe_fn(name):
    for ch in ['<','>',':','"','/','\\','|','?','*']:
        name = name.replace(ch, '_')
    return name[:200]

def main():
    log("=" * 60)
    log("=== Live Stream Transcription Started ===")
    log(f"Source: {SRC}")
    log("=" * 60)

    media_files = []
    for dirpath, _, filenames in os.walk(SRC):
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in MEDIA_EXTS:
                media_files.append(os.path.join(dirpath, f))

    media_files.sort(key=lambda x: os.path.getsize(x))
    log(f"Found {len(media_files)} media files")

    done = load_done()
    remaining = [f for f in media_files if f not in done]
    log(f"Already done: {len(done)}, remaining: {len(remaining)}")

    if not remaining:
        log("All done!")
        return

    log("Loading whisper model (small, cuda)...")
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cuda", compute_type="float16")
    log("Model loaded!")

    start_time = time.time()
    for i, fp in enumerate(remaining):
        try:
            fn = os.path.basename(fp)
            name = os.path.splitext(fn)[0]
            ext = os.path.splitext(fn)[1].lower()
            safe_name = safe_fn(name)

            transcript_path = os.path.join(OUTPUT, f"{safe_name}_逐字稿.md")
            notes_path = os.path.join(OUTPUT, f"{safe_name}_学习笔记.md")

            if os.path.exists(transcript_path):
                done.add(fp)
                save_done(done)
                continue

            log(f"[{i+1}/{len(remaining)}] {fn} ({os.path.getsize(fp)/1e6:.1f}MB)")

            duration = get_duration(fp)
            if duration == 0:
                log(f"  Cannot get duration, skipping")
                log_error(fp, "Cannot get duration")
                continue

            log(f"  Duration: {fmt_ts(duration)}")

            is_audio = ext in {'.mp3','.m4a','.wav'}
            temp_audio = None

            t0 = time.time()
            if is_audio:
                audio_path = fp
            else:
                temp_audio = os.path.join(os.environ.get("TEMP", r"C:\temp"), f"live_{os.getpid()}.wav")
                os.makedirs(os.path.dirname(temp_audio), exist_ok=True)
                log(f"  Extracting audio...")
                if not extract_audio(fp, temp_audio):
                    log(f"  Failed to extract audio")
                    log_error(fp, "Failed to extract audio")
                    continue
                audio_path = temp_audio

            log(f"  Transcribing...")
            segments_iter, info = model.transcribe(
                audio_path, language="zh", beam_size=5,
                vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500)
            )
            segments = []
            for seg in segments_iter:
                segments.append({"start": round(seg.start,2), "end": round(seg.end,2), "text": seg.text.strip()})

            t1 = time.time()

            if temp_audio and os.path.exists(temp_audio):
                try: os.remove(temp_audio)
                except: pass

            if not segments:
                log(f"  No speech detected")
                done.add(fp)
                save_done(done)
                continue

            # Write transcript
            full_text = ""
            md = f"---\ntitle: \"{name}\"\ntype: live-transcript\nduration: \"{fmt_ts(duration)}\"\n"
            md += f"date: {datetime.now().strftime('%Y-%m-%d')}\ntags: [直播, 逐字稿]\n"
            md += f"source: \"{fp}\"\n---\n\n"
            md += f"# {name} 直播逐字稿\n\n"
            md += f"> 时长: {fmt_ts(duration)} | 转录时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            for seg in segments:
                ts = fmt_ts(seg["start"])
                md += f"**`[{ts}]`** {seg['text']}\n\n"
                full_text += seg["text"] + " "
            md += f"\n---\n\n> [!note] 全文统计\n> 总字数: {len(full_text)} | 段落数: {len(segments)}\n"

            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(md)

            # Write study notes
            md2 = f"---\ntitle: \"{name} 学习笔记\"\ntype: live-notes\nduration: \"{fmt_ts(duration)}\"\n"
            md2 += f"date: {datetime.now().strftime('%Y-%m-%d')}\ntags: [直播, 学习笔记]\n"
            md2 += f"source: \"{fp}\"\n---\n\n"
            md2 += f"# {name} 直播学习笔记\n\n"
            md2 += f"> 时长: {fmt_ts(duration)} | 来源: `{fn}`\n\n"

            section_dur = max(300, duration / 10)
            sections = []
            cur = []
            cur_start = 0
            for seg in segments:
                if seg["start"] >= cur_start + section_dur and cur:
                    sections.append((cur_start, cur))
                    cur_start = seg["start"]
                    cur = []
                cur.append(seg)
            if cur:
                sections.append((cur_start, cur))

            md2 += "## 内容概要\n\n"
            for idx, (start, segs) in enumerate(sections, 1):
                text = " ".join(s["text"] for s in segs)
                end = segs[-1]["end"]
                md2 += f"### 第{idx}部分 `[{fmt_ts(start)}-{fmt_ts(end)}]`\n\n"
                md2 += text[:800] + "\n\n"

            md2 += "## 完整内容\n\n"
            md2 += f"详见 [[{safe_name}_逐字稿.md|逐字稿]]\n"

            with open(notes_path, "w", encoding="utf-8") as f:
                f.write(md2)

            done.add(fp)
            save_done(done)

            log(f"  Done: {len(segments)} segments, {len(full_text)} chars, {t1-t0:.1f}s")
            elapsed = time.time() - start_time
            rate = (i+1) / elapsed * 3600
            eta = (len(remaining)-i-1) / (rate/3600) if rate > 0 else 0
            if (i+1) % 2 == 0:
                log(f"  Progress: {i+1}/{len(remaining)} | ETA: {eta/3600:.1f}h")

        except Exception as e:
            log(f"  ERROR: {e}")
            log_error(fp, traceback.format_exc())

    log("=" * 60)
    log(f"=== Live Transcription Complete: {len(done)} files ===")
    log("=" * 60)

if __name__ == "__main__":
    main()
