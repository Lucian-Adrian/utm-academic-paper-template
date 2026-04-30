from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "paper" / "article" / "main.tex"
CLS = ROOT / "paper" / "article" / "utmconf.cls"


def strip_latex(text: str) -> str:
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r" \1 ", text)
    text = re.sub(r"[$^_{}\\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def find_between(text: str, begin: str, end: str) -> str:
    pattern = re.compile(re.escape(begin) + r"(.*?)" + re.escape(end), re.S)
    match = pattern.search(text)
    return match.group(1) if match else ""


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    if not MAIN.exists():
        fail("main.tex is missing", failures)
    if not CLS.exists():
        fail("utmconf.cls is missing", failures)
    if failures:
        print("\n".join(failures))
        return 1

    main_tex = MAIN.read_text(encoding="utf-8")
    cls_tex = CLS.read_text(encoding="utf-8")

    required_geometry = "top=2cm,bottom=2cm,left=2.5cm,right=2cm"
    if required_geometry not in cls_tex.replace(" ", ""):
        fail("conference page geometry must be A4 with top/bottom/right 2 cm and left 2.5 cm", failures)

    for section in ["Introducere", "Materiale și metode", "Rezultate și discuții", "Concluzii", "Referințe"]:
        if section not in main_tex:
            fail(f"required article section missing: {section}", failures)

    abstract = find_between(main_tex, r"\begin{rezumat}", r"\end{rezumat}")
    words = re.findall(r"\b[\w\-]+\b", strip_latex(abstract), flags=re.UNICODE)
    if not (150 <= len(words) <= 200):
        fail(f"conference paper abstract must have 150-200 words; found {len(words)}", failures)
    if "\\cite" in abstract or re.search(r"\[[0-9,\-\s]+\]", abstract):
        fail("conference paper abstract must not contain citations", failures)

    kw_match = re.search(r"\\cuvintecheie\{([^}]*)\}", main_tex)
    if not kw_match:
        fail("keywords command missing", failures)
    else:
        keywords = [k.strip() for k in kw_match.group(1).split(",") if k.strip()]
        if not (4 <= len(keywords) <= 6):
            fail(f"keywords must contain 4-6 terms; found {len(keywords)}", failures)
        bad_case = [k for k in keywords if k != k.lower()]
        if bad_case:
            fail("keywords must be lowercase: " + ", ".join(bad_case), failures)

    in_references = False
    for line_no, line in enumerate(main_tex.splitlines(), start=1):
        stripped = line.strip()
        if r"\section*{Referințe}" in stripped or r"\section*{Referinte}" in stripped:
            in_references = True
        if stripped.startswith(r"\section*{") and r"\section*{Referințe}" not in stripped and r"\section*{Referinte}" not in stripped:
            in_references = False
        if stripped.startswith(r"\item") and not in_references and not stripped.endswith(";"):
            fail(f"enumeration item must end with semicolon at line {line_no}", failures)

    if "Tabelul \\theutmtable" not in cls_tex or "Figura \\theutmfigure" not in cls_tex:
        fail("custom UTM table/figure numbering macros are missing", failures)

    if failures:
        print("UTM article check failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("UTM article check passed.")
    print(f"Abstract words: {len(words)}")
    print(f"Keywords: {len(keywords)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
