import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
from audio_to_txt import transcribe_newest_audio

# test_audio_to_txt.py


# Absolute import from namespace package

class TestAudioToTxt(unittest.TestCase):
    @patch('audio_to_txt.os.path.expanduser')
    @patch('audio_to_txt.glob.glob')
    @patch('audio_to_txt.os.path.getmtime')
    @patch('audio_to_txt.whisper.load_model')
    @patch('audio_to_txt.open', new_callable=mock_open)
    def test_no_audio_files(self, mock_open_fn, mock_load_model, mock_getmtime, mock_glob, mock_expanduser):
        mock_expanduser.return_value = '/fake/Downloads'
        mock_glob.return_value = []
        with patch('audio_to_txt.print') as mock_print, self.assertRaises(SystemExit):
            transcribe_newest_audio('/fake/Downloads')
        mock_print.assert_any_call("No audio files found in Downloads folder.")
        mock_load_model.assert_not_called()

    @patch('audio_to_txt.os.path.expanduser')
    @patch('audio_to_txt.glob.glob')
    @patch('audio_to_txt.os.path.getmtime')
    @patch('audio_to_txt.whisper.load_model')
    @patch('audio_to_txt.open', new_callable=mock_open)
    def test_transcribe_newest_audio(self, mock_open_fn, mock_load_model, mock_getmtime, mock_glob, mock_expanduser):
        mock_expanduser.return_value = '/fake/Downloads'
        mock_glob.side_effect = [
            ['/fake/Downloads/a.mp3'],
            ['/fake/Downloads/b.wav'],
            []
        ]
        files = ['/fake/Downloads/a.mp3', '/fake/Downloads/b.wav']
        mock_getmtime.side_effect = lambda f: {'/fake/Downloads/a.mp3': 1, '/fake/Downloads/b.wav': 2}[f]
        mock_model = MagicMock()
        mock_model.transcribe.return_value = {'text': 'Bonjour!'}
        mock_load_model.return_value = mock_model

        with patch('audio_to_txt.print') as mock_print:
            transcribe_newest_audio('/fake/Downloads')

        mock_load_model.assert_called_once_with('base')
        mock_model.transcribe.assert_called_once_with('/fake/Downloads/b.wav', language='fr')
        mock_open_fn.assert_called_once_with('/fake/Downloads/b.wav.txt', 'w', encoding='utf-8')
        handle = mock_open_fn()
        handle.write.assert_called_once_with('Bonjour!')
        mock_print.assert_any_call("Newest file found: /fake/Downloads/b.wav")
        mock_print.assert_any_call("Transcription saved to /fake/Downloads/b.wav.txt")

if __name__ == '__main__':
    unittest.main()