"""Start a new document from a template.

    python tools/new.py report     D:/edu/faf/sem3/oop/lab-1
    python tools/new.py internship D:/edu/faf/internship/report

Templates: report, internship, thesis, article, abstract.
The folder is created with everything it needs; compile it there with `tectonic main.tex`.
Copying the template folder by hand works just as well.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parents[1] / "templates"
BUILD_OUTPUT = ("*.pdf", "*.aux", "*.log", "*.out", "*.toc", "*.synctex.gz")


def main(argv: list[str]) -> int:
    names = sorted(p.name for p in TEMPLATES.iterdir() if p.is_dir())
    if len(argv) != 2 or argv[0] not in names:
        print(__doc__.strip())
        print(f"\nAvailable: {', '.join(names)}")
        return 2
    source, target = TEMPLATES / argv[0], Path(argv[1]).resolve()
    if target.exists() and any(target.iterdir()):
        print(f"{target} already exists and is not empty; choose a new folder.")
        return 1

    def ignore(folder: str, entries: list[str]) -> set[str]:
        # Keep figures (example images are PDFs); drop compiled output elsewhere.
        if Path(folder).name == "figures":
            return set()
        return {e for e in entries for pattern in BUILD_OUTPUT if Path(e).match(pattern)}

    shutil.copytree(source, target, ignore=ignore, dirs_exist_ok=True)
    print(f"Created {target} from templates/{argv[0]}.")
    print("Next:")
    print(f"  1. open {target / 'main.tex'} and fill in the cover fields")
    print("  2. replace the red \\placeholder{...} text")
    print(f"  3. cd \"{target}\" and run: tectonic main.tex")
    print(f"  4. before submitting: python \"{Path(__file__).with_name('check.py')}\" \"{target}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
