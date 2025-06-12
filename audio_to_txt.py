import whisper
import os
import glob
import time
import sys

def transcribe_newest_audio(downloads_folder=None):
    # Set your Downloads folder path
    if downloads_folder is None:
        downloads_folder = os.path.expanduser('~/Downloads')

    # Define which file types to consider
    file_types = ('.mp3', '.wav', '.m4a')

    # Gather all matching files
    files = []
    for file_type in file_types:
        files.extend(glob.glob(os.path.join(downloads_folder, f'*{file_type}')))

    # Check if we found any files
    if not files:
        print("No audio files found in Downloads folder.")
        sys.exit(1)

    # Find the newest file by modification time
    newest_file = max(files, key=os.path.getmtime)

    # Print info
    print(f"Newest file found: {newest_file}")

    # Load the Whisper model
    model = whisper.load_model('medium')

    # Transcribe the file
    result = model.transcribe(newest_file, language='fr')

    # Save the transcription
    output_file = newest_file + '.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['text'])

    print(f"Transcription saved to {output_file}")

if __name__ == '__main__':
    transcribe_newest_audio()


