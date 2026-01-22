import zipfile
from pathlib import Path

DATA_DIR = Path("data")
UNZIPPED_DIR = DATA_DIR / "erp_core"

def unzip_all():
    UNZIPPED_DIR.mkdir(exist_ok=True)
    
    for zip_path in DATA_DIR.glob("sub-*.zip"):
        subject_id = zip_path.stem
        subject_dir = UNZIPPED_DIR / subject_id
        
        if subject_dir.exists():
            print(f"[SKIP] {subject_id} already extracted")
            continue
        
        print(f"[EXTRACT] {subject_id}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(subject_dir)

if __name__ == "__main__":
    unzip_all()