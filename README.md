# Whisper Audio Transcription Script

This project provides a simple Python script to automatically transcribe the newest audio file in your Downloads folder using OpenAI's Whisper model.

## Features
- Automatically finds the newest `.mp3`, `.wav`, or `.m4a` file in your Downloads folder
- Transcribes the audio to text using Whisper
- Saves the transcription as a `.txt` file next to the audio file
- Supports French language transcription (configurable)

## Requirements
- Python 3.8+
- [openai-whisper](https://github.com/openai/whisper)
- [ffmpeg](https://ffmpeg.org/) (must be installed and in your PATH)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/whisper-audio-transcriber.git
   cd whisper-audio-transcriber
   ```
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install ffmpeg (if not already installed):
   - [Download ffmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.

## Usage
Run the script from the command line:

```sh
python audio_to_txt.py
```

By default, it looks in your `~/Downloads` folder. You can specify a different folder:

```sh
python audio_to_txt.py /path/to/your/folder
```

## Testing
Unit tests are provided using Python's `unittest` framework. To run tests:

```sh
python -m unittest discover
```

## License
MIT License

## Author
Valentin Maissen
