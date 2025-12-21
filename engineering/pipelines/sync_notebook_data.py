"""
Sync data artifacts from /notebooks to /data/processed

Rule:
- Copy everything in /notebooks EXCEPT Jupyter notebooks (*.ipynb)
- This keeps Coursera compatibility while maintaining clean data organization.

Notes:
- By default: copies only files located directly under /notebooks (non-recursive).
"""

from __future__ import annotations

import shutil
from pathlib import Path


EXCLUDED_SUFFIXES = {".ipynb"}  # strict: exclude only notebooks
EXCLUDED_NAMES = {".placeholder"}


def should_copy(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name in EXCLUDED_NAMES:
        return False
    return path.suffix.lower() not in EXCLUDED_SUFFIXES



def sync_notebooks_artifacts_to_data_processed() -> int:
    project_root = Path(__file__).resolve().parents[2]  # .../engineering/pipelines/ -> project root
    notebooks_dir = project_root / "notebooks"
    data_processed_dir = project_root / "data" / "processed"

    if not notebooks_dir.exists():
        raise FileNotFoundError(f"Not found: {notebooks_dir}")

    data_processed_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0

    for p in notebooks_dir.iterdir():
        if should_copy(p):
            dest = data_processed_dir / p.name
            shutil.copy2(p, dest)
            copied += 1
            print(f"Copied: {p.name} -> data/processed/")
        else:
            skipped += 1

    print(f"\nDone. Copied: {copied}. Skipped: {skipped} (includes .ipynb and non-files).")
    return copied


if __name__ == "__main__":
    sync_notebooks_artifacts_to_data_processed()
