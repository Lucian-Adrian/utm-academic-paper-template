"""Compile every template with Tectonic and store the PDFs in docs/previews/.

    python tools/build.py              all templates
    python tools/build.py internship   one template
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = {  # preview name: (template folder, main file)
    "report": ("report", "main.tex"),
    "internship": ("internship", "main.tex"),
    "thesis": ("thesis", "main.tex"),
    "article": ("article", "main.tex"),
    "article-titlepage-demo": ("article", "titlepage-demo.tex"),
    "abstract": ("abstract", "main.tex"),
}


def find_tectonic() -> str | None:
    found = shutil.which("tectonic")
    live = Path("D:/apps/tectonic/tectonic.exe")
    local = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Tectonic" / "tectonic.exe"
    return found or (str(live) if live.is_file() else (str(local) if local.is_file() else None))


def main(argv: list[str]) -> int:
    tectonic = find_tectonic()
    if not tectonic:
        print("Tectonic not found. Install it from https://tectonic-typesetting.github.io/")
        return 1
    wanted = {k: v for k, v in DOCUMENTS.items() if not argv or v[0] in argv or k in argv}
    out_dir = ROOT / "docs" / "previews"
    out_dir.mkdir(parents=True, exist_ok=True)
    failed = []
    for name, (folder, main_file) in wanted.items():
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([tectonic, "--outdir", tmp, main_file], cwd=ROOT / "templates" / folder,
                                    capture_output=True, text=True, encoding="utf-8", errors="replace")
            pdf = Path(tmp) / Path(main_file).with_suffix(".pdf").name
            if result.returncode or not pdf.is_file():
                failed.append(name)
                print(f"FAILED {name}\n{result.stderr[-2000:]}")
                continue
            shutil.copyfile(pdf, out_dir / f"{name}.pdf")
            print(f"ok     {name} -> docs/previews/{name}.pdf")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
