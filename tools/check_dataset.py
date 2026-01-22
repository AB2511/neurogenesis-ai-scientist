from pathlib import Path

DATA_ROOT = Path("data/erp_core")

def check():
    subjects = sorted(DATA_ROOT.glob("sub-*"))
    print(f"Found {len(subjects)} subjects")
    
    for sub in subjects:
        eeg_dir = sub / "eeg"
        if not eeg_dir.exists():
            print(f"[ERROR] Missing eeg folder in {sub.name}")
            continue
        
        eeg_files = list(eeg_dir.glob("*"))
        if not eeg_files:
            print(f"[ERROR] No EEG files in {sub.name}")
        else:
            print(f"[OK] {sub.name} → {len(eeg_files)} files")

if __name__ == "__main__":
    check()