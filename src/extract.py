from pathlib import Path
import zipfile


RAW_DATA_DIR = Path("data/raw")


def extract_zip(zip_path: Path) -> Path:
    output_dir = RAW_DATA_DIR / zip_path.stem

    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        zip_file.extractall(output_dir)

    return output_dir


if __name__ == "__main__":
    zip_files = list(RAW_DATA_DIR.glob("*.zip"))

    if not zip_files:
        raise FileNotFoundError(
            "No ZIP files found inside data/raw/"
        )

    for zip_path in zip_files:
        output_directory = extract_zip(zip_path)

        print(
            f"Extracted {zip_path.name} "
            f"to {output_directory}"
        )