import os
from pathlib import Path

from polylith.files import create_file

keep_file_name = ".keep"


def create_dir(path: Path, dir_name: str, keep=True) -> Path:
    d = path / dir_name
    try:
        if not os.path.isdir(d):
            d.mkdir(parents=True)

        if keep:
            create_file(d, keep_file_name)
    except Exception:
        pass
    return d
