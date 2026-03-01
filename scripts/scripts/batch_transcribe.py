import argparse
from pathlib import Path
from basic_pitch.inference import predict_and_save

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default="audio")
    parser.add_argument("--output-dir", default="output_midi")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    audio_files = []
    for ext in ["*.mp3", "*.wav", "*.m4a", "*.ogg"]:
        audio_files.extend(input_dir.glob(ext))

    if not audio_files:
        print("No audio files found in input directory.")
        return

    print(f"Transcribing {len(audio_files)} files...")
    predict_and_save(
        [str(f) for f in audio_files],
        str(output_dir),
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
    )
    print("Batch transcription complete.")

if __name__ == "__main__":
    main()
