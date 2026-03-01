# Audio → MIDI Transcription (GitHub Actions + Basic Pitch)

AI-powered automatic music transcription: drop audio files → get MIDI files via GitHub Actions.

## Features
- Uses Spotify's [Basic Pitch](https://github.com/spotify/basic-pitch)
- Runs on push to `audio/` or manually via workflow dispatch
- Supports MP3, WAV, etc.
- Outputs MIDI with note + pitch bend estimation

## How to Use
1. Add audio file(s) to `/audio/` folder → commit & push
2. Or: Actions tab → "AI Audio → MIDI Transcription" → Run workflow
3. Download artifacts from the run summary

## Local Testing
```bash
pip install -r requirements.txt
python scripts/transcribe.py --input "audio/my-song.mp3"
# or batch
python scripts/batch_transcribe.py
