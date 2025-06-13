import whisper
import os
import glob
import sys

def transcribe_and_write_srt(mp3_path, language="fr"):
    model = whisper.load_model("medium")
    print(f"Transcribing {mp3_path} with Whisper...")
    result = model.transcribe(mp3_path, language=language)
    segments = result["segments"]

    # Write SRT using phrase-level segments
    srt_path = mp3_path + ".srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments):
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()
            f.write(f"{i+1}\n")
            f.write(f"{format_srt_time(start)} --> {format_srt_time(end)}\n")
            f.write(f"{text}\n\n")
    print(f"SRT file saved: {srt_path}")

def format_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

if __name__ == "__main__":
    downloads_folder = os.path.expanduser('~/Downloads')
    file_types = ('.mp3', '.wav', '.m4a')
    files = []
    for file_type in file_types:
        files.extend(glob.glob(os.path.join(downloads_folder, f'*{file_type}')))
    if not files:
        print("No audio files found in Downloads folder.")
        sys.exit(1)
    newest_file = max(files, key=os.path.getmtime)
    print(f"Newest file found: {newest_file}")
    transcribe_and_write_srt(newest_file, language="fr")


