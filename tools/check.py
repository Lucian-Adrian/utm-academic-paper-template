"""Check the UTM templates, or a report you are writing.

    python tools/check.py                 check every template in templates/
    python tools/check.py --sync          first copy shared/ files into the templates
    python tools/check.py path/to/report  check your own copy (placeholders, keywords, citations)
"""
from __future__ import annotations

import filecmp
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"

# Each template folder carries copies of these shared files so it compiles on its own.
SYNC = {
    "shared/utmreport.cls": ["templates/report/utmreport.cls", "templates/internship/utmreport.cls", "templates/thesis/utmreport.cls"],
    "shared/assets/UTM_Logo_English.jpeg": ["templates/report/utm-logo.jpeg", "templates/internship/utm-logo.jpeg"],
    "shared/assets/UTM_Logo.png": ["templates/thesis/utm-logo.png", "templates/article/utm-logo.png", "templates/abstract/utm-logo.png"],
    "shared/assets/example-diagram.pdf": ["templates/report/figures/example-diagram.pdf", "templates/internship/figures/example-diagram.pdf"],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def strip_latex(text: str) -> str:
    text = strip_comments(text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r" \1 ", text)
    text = re.sub(r"[$^_{}\\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def between(text: str, begin: str, end: str) -> str:
    match = re.search(re.escape(begin) + r"(.*?)" + re.escape(end), text, flags=re.S)
    return match.group(1) if match else ""


def expand_inputs(main: Path) -> str:
    """Return main.tex with every \\input{...} file inlined (comments removed)."""
    def inline(path: Path, depth: int = 0) -> str:
        text = strip_comments(read(path))
        if depth > 5:
            return text

        def repl(match: re.Match[str]) -> str:
            target = (main.parent / match.group(1)).with_suffix(".tex")
            return inline(target, depth + 1) if target.is_file() else ""

        return re.sub(r"\\input\{([^}]+)\}", repl, text)

    return inline(main)


def sync(failures: list[str], write: bool) -> None:
    for source, targets in SYNC.items():
        for target in targets:
            src, dst = ROOT / source, ROOT / target
            if write:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
            elif not dst.is_file() or not filecmp.cmp(src, dst, shallow=False):
                failures.append(f"{target} differs from {source}; run: python tools/check.py --sync")


def check_keywords(tex: str, pattern: str, label: str, failures: list[str], minimum: int = 4, maximum: int = 6) -> None:
    match = re.search(pattern, tex)
    if not match:
        failures.append(f"{label}: keywords missing")
        return
    value = re.sub(r"\\placeholder\{(.*)\}", r"\1", match.group(1))
    keywords = [k.strip() for k in value.split(",") if k.strip()]
    if not (minimum <= len(keywords) <= maximum):
        failures.append(f"{label}: keywords must contain {minimum}-{maximum} terms; found {len(keywords)}")
    bad = [k for k in keywords if k != k.lower()]
    if bad:
        failures.append(f"{label}: keywords must be lowercase: {', '.join(bad)}")


def check_enumerations(tex: str, label: str, failures: list[str], ignore_after: str | None = None) -> None:
    """Enumeration items end with a semicolon (description items such as \\item[API] are exempt)."""
    ignored = False
    for line_no, line in enumerate(tex.splitlines(), start=1):
        stripped = line.strip()
        if ignore_after and ignore_after in stripped:
            ignored = True
        elif stripped.startswith((r"\section", r"\chapter")):
            ignored = False
        if stripped.startswith(r"\item") and not stripped.startswith(r"\item[") and not ignored:
            if not stripped.rstrip("}").endswith(";"):
                failures.append(f"{label}: enumeration item must end with a semicolon (line {line_no})")


def check_report_body(tex: str, label: str, failures: list[str], thesis: bool = False) -> None:
    """Check report or thesis page order, references and enumerations."""
    if thesis:
        order = [r"\begin{utmabstract}", r"\tableofcontents", r"\utmintroduction"]
    else:
        order = [r"\tableofcontents", r"\begin{utmabstract}", r"\utmintroduction"]
    positions = [tex.find(token) for token in order]
    if -1 in positions or positions != sorted(positions):
        failures.append(f"{label}: has an incorrect contents/abstract/Introduction order")
    if r"\utmconclusions" not in tex:
        failures.append(f"{label}: missing \\utmconclusions")
    if r"\pagenumbering{roman}" in tex or r"\setcounter{page}{1}" in tex:
        failures.append(f"{label}: must keep continuous page counting")
    if thesis:
        check_keywords(tex, r"\\utmkeywords\{(.*)\}", label, failures, minimum=1, maximum=5)
    else:
        check_keywords(tex, r"\\utmkeywords\{(.*)\}", label, failures, minimum=5, maximum=7)
    check_enumerations(tex, label, failures)
    cited = set()
    for group in re.findall(r"\\cite\{([^}]*)\}", tex):
        cited.update(key.strip() for key in group.split(","))
    defined = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", tex))
    for key in sorted(cited - defined):
        failures.append(f"{label}: \\cite{{{key}}} has no \\bibitem")
    for key in sorted(defined - cited):
        failures.append(f"{label}: reference '{key}' is never cited")


def check_templates(failures: list[str]) -> None:
    # Conference article.
    tex = strip_comments(read(TEMPLATES / "article/main.tex"))
    cls = read(TEMPLATES / "article/utmconf.cls")
    if "top=2cm,bottom=2cm,left=2.5cm,right=2cm" not in cls.replace(" ", ""):
        failures.append("article: margins must be top/bottom/right 2 cm and left 2.5 cm")
    for section in ["Introducere", "Materiale și metode", "Rezultate și discuții", "Concluzii", "Referințe"]:
        if section not in tex:
            failures.append(f"article: missing section {section}")
    abstract = between(tex, r"\begin{rezumat}", r"\end{rezumat}")
    words = re.findall(r"\b[\w\-]+\b", strip_latex(abstract), flags=re.UNICODE)
    if not (150 <= len(words) <= 200):
        failures.append(f"article: abstract must have 150-200 words; found {len(words)}")
    if "\\cite" in abstract or re.search(r"\[[0-9,\-\s]+\]", abstract):
        failures.append("article: abstract must not contain citations")
    if "Tabelul \\theutmtable" not in cls or "Figura \\theutmfigure" not in cls:
        failures.append("article: UTM table/figure numbering macros are missing")
    check_keywords(tex, r"\\cuvintecheie\{([^}]*)\}", "article", failures)
    check_enumerations(tex, "article", failures, ignore_after="Referințe")

    # Conference abstract.
    tex = read(TEMPLATES / "abstract/main.tex")
    cls = read(TEMPLATES / "abstract/utmabstract.cls")
    for token in [r"\abstracttitle", r"\abstractauthors", r"\abstractaffiliations", r"\begin{rezumat}", r"\cuvintecheie"]:
        if token not in tex:
            failures.append(f"abstract: missing {token}")
    if "fontsize{14pt}" not in cls or "fontsize{10pt}" not in cls:
        failures.append("abstract: class must define 14 pt title and 10 pt affiliations")
    check_keywords(tex, r"\\cuvintecheie\{([^}]*)\}", "abstract", failures)

    # Shared report/thesis class.
    cls = read(ROOT / "shared/utmreport.cls")
    for token in [r"\makeutmcover", r"\makeutmreporttitlepage", r"\makeutminternshiptitlepage", r"\makeutmthesistitlepage",
                  r"\setstretch{1.5}", r"\setlength{\parindent}{1.25cm}", r"\newenvironment{utmenumerate}",
                  "left=2cm,right=1cm", r"\utmintroduction", r"\utmconclusions", r"\UTMFrontMattertrue",
                  "Courier New", "fontsize{13pt}", r"\placeholder", r"\newenvironment{utmabbreviations}"]:
        if token not in cls:
            failures.append(f"utmreport.cls: missing {token}")

    # Report templates.
    for name, titlepage in [("report", r"\makeutmreporttitlepage"), ("internship", r"\makeutminternshiptitlepage")]:
        main = TEMPLATES / name / "main.tex"
        tex = expand_inputs(main)
        label = f"templates/{name}"
        if r"\documentclass{utmreport}" not in tex:
            failures.append(f"{label}: must use \\documentclass{{utmreport}} from its own folder")
        if titlepage not in tex:
            failures.append(f"{label}: must use {titlepage}")
        if r"\selectlanguage{english}" not in tex:
            failures.append(f"{label}: must select English")
        check_report_body(tex, label, failures)
    internship = strip_comments(read(TEMPLATES / "internship/main.tex"))
    team_members = len(re.findall(r"\\teammember\{", internship))
    summaries = len(re.findall(r"\\internshipsummary\{", internship))
    if team_members != summaries:
        failures.append("templates/internship: include one summary call for every team member")
    if r"Internship Summary Report\_#1" not in internship or r"\addcontentsline{toc}{chapter}{#1}" not in internship:
        failures.append("templates/internship: each summary needs a named TOC chapter")
    report_front = read(TEMPLATES / "report/main.tex").split(r"\begin{utmabstract}", 1)[0]
    for forbidden in ["Admis la susținere", "Proiect / teză de licență", "Raport de proiect"]:
        if forbidden in report_front:
            failures.append(f"templates/report: title page must not contain thesis wording: {forbidden}")

    # Thesis.
    tex = read(TEMPLATES / "thesis/main.tex")
    if r"\documentclass[thesis]{utmreport}" not in tex:
        failures.append("templates/thesis: must use \\documentclass[thesis]{utmreport}")
    for token in [r"\makeutmthesistitlepage", r"\tableofcontents"]:
        if token not in tex:
            failures.append(f"templates/thesis: missing {token}")
    check_enumerations(tex, "templates/thesis", failures)

    # Every template compiles from its own folder: no paths outside it.
    for tex_file in TEMPLATES.rglob("*.tex"):
        if "../" in strip_comments(read(tex_file)):
            failures.append(f"{tex_file.relative_to(ROOT)}: refers to a file outside its template folder")


def check_user_report(folder: Path, failures: list[str]) -> list[str]:
    main = folder / "main.tex" if folder.is_dir() else folder
    if not main.is_file():
        failures.append(f"{main} not found")
        return []
    tex = expand_inputs(main)
    notes: list[str] = []
    left = len(re.findall(r"\\placeholder\{", tex))
    if left:
        failures.append(f"{left} \\placeholder{{...}} text(s) still to replace (red in the PDF)")
    if "utmreport" in tex and r"\utmintroduction" in tex:
        is_thesis = r"\documentclass[thesis]{utmreport}" in tex
        check_report_body(tex, main.name, failures, thesis=is_thesis)
    for image in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex):
        candidates = [main.parent / image, main.parent / "figures" / image]
        if not any(c.exists() or list(c.parent.glob(c.name + ".*")) for c in candidates):
            failures.append(f"image not found: {image} (put it in figures/)")
    if not (main.parent / "utmreport.cls").is_file() and "utmreport" in tex:
        notes.append("utmreport.cls is not next to main.tex; copy it from the template folder")
    return notes


def main(argv: list[str]) -> int:
    failures: list[str] = []
    args = [a for a in argv if not a.startswith("--")]
    if args:
        notes = check_user_report(Path(args[0]).resolve(), failures)
        for note in notes:
            print(f"note: {note}")
        target = args[0]
    else:
        sync(failures, write="--sync" in argv)
        check_templates(failures)
        target = "all templates"
    if failures:
        print(f"Check failed for {target}:")
        for item in failures:
            print(f"- {item}")
        return 1
    print(f"Check passed for {target}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
