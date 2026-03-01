import argparse
from pathlib import Path
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH   # ← Add this import

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path or glob pattern")
    parser.add_argument("--output-dir", default="output_midi", help="Where to save .mid files")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    audio_paths = [str(p) for p in Path(".").glob(args.input) if p.is_file()]

    if not audio_paths:
        print("No audio files found.")
        return

    predict_and_save(
        audio_path_list=audio_paths,               # changed name for clarity (old: audio_paths)
        output_directory=str(output_dir),
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
        model_or_model_path=ICASSP_2022_MODEL_PATH  # ← This fixes the error
    )
    print(f"Done. MIDI files saved to {output_dir}")

if __name__ == "__main__":
    main()
