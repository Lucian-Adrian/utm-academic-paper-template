from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_latex(text: str) -> str:
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r" \1 ", text)
    text = re.sub(r"[$^_{}\\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def between(text: str, begin: str, end: str) -> str:
    match = re.search(re.escape(begin) + r"(.*?)" + re.escape(end), text, flags=re.S)
    return match.group(1) if match else ""


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def check_article(failures: list[str]) -> None:
    tex = read(ROOT / "paper/article/main.tex")
    cls = read(ROOT / "paper/article/utmconf.cls")
    if "top=2cm,bottom=2cm,left=2.5cm,right=2cm" not in cls.replace(" ", ""):
        fail(failures, "article margins must be top/bottom/right 2 cm and left 2.5 cm")
    for section in ["Introducere", "Materiale și metode", "Rezultate și discuții", "Concluzii", "Referințe"]:
        if section not in tex:
            fail(failures, f"article missing section: {section}")
    abstract = between(tex, r"\begin{rezumat}", r"\end{rezumat}")
    words = re.findall(r"\b[\w\-]+\b", strip_latex(abstract), flags=re.UNICODE)
    if not (150 <= len(words) <= 200):
        fail(failures, f"article abstract must have 150-200 words; found {len(words)}")
    if "\\cite" in abstract or re.search(r"\[[0-9,\-\s]+\]", abstract):
        fail(failures, "article abstract must not contain citations")
    check_keywords(tex, r"\\cuvintecheie\{([^}]*)\}", "article", failures)
    check_enumerations(tex, failures, ignore_after="Referințe")


def check_abstract(failures: list[str]) -> None:
    tex = read(ROOT / "paper/abstract/abstract.tex")
    cls = read(ROOT / "paper/abstract/utmabstract.cls")
    for token in ["\\abstracttitle", "\\abstractauthors", "\\abstractaffiliations", "\\begin{rezumat}", "\\cuvintecheie"]:
        if token not in tex:
            fail(failures, f"abstract template missing {token}")
    if "fontsize{14pt}" not in cls or "fontsize{10pt}" not in cls:
        fail(failures, "abstract class must define 14 pt title and 10 pt affiliation metadata")
    check_keywords(tex, r"\\cuvintecheie\{([^}]*)\}", "abstract", failures)


def check_report_thesis(failures: list[str]) -> None:
    cls = read(ROOT / "shared/classes/utmreport.cls")
    for token in ["\\makeutmcover", "\\makeutmreporttitlepage", "\\makeutmthesistitlepage", "\\setstretch{1.5}", "\\setlength{\\parindent}{1.25cm}", "\\newenvironment{utmenumerate}"]:
        if token not in cls:
            fail(failures, f"report/thesis class missing {token}")
    for rel, label, documentclass, titlepage in [
        ("report/main.tex", "report", "\\documentclass{../shared/classes/utmreport}", "\\makeutmreporttitlepage"),
        ("thesis/main.tex", "thesis", "\\documentclass[thesis]{../shared/classes/utmreport}", "\\makeutmthesistitlepage"),
    ]:
        tex = read(ROOT / rel)
        if documentclass not in tex:
            fail(failures, f"{label} example must use shared utmreport class")
        if titlepage not in tex:
            fail(failures, f"{label} example must use its specific title-page macro")
        if "\\tableofcontents" not in tex:
            fail(failures, f"{label} example must include table of contents")
        check_enumerations(tex, failures)
    for token in ["left=2cm,right=1cm", r"\makeutminternshiptitlepage", r"\utmintroduction", r"\utmconclusions", r"\UTMFrontMattertrue", r"\raggedleft", "Courier New", "fontsize{13pt}"]:
        if token not in cls:
            fail(failures, f"ELSE report class missing {token}")
    for rel in ["report/main.tex", "report/internship.tex"]:
        tex = read(ROOT / rel)
        for token in [r"\utmintroduction", r"\utmconclusions", r"\selectlanguage{english}", "UTM_Logo_English.jpeg"]:
            if token not in tex:
                fail(failures, f"{rel} missing {token}")
        if not (tex.index(r"\tableofcontents") < tex.index(r"\begin{utmabstract}") < tex.index(r"\utmintroduction")):
            fail(failures, f"{rel} needs contents, abstract, introduction in source order")
        if r"\pagenumbering{roman}" in tex or r"\setcounter{page}{1}" in tex:
            fail(failures, f"{rel} must preserve continuous page counting")
        check_keywords(tex, r"\\utmkeywords\{([^}]*)\}", rel, failures, minimum=5, maximum=7)
    if r"\makeutminternshiptitlepage" not in read(ROOT / "report/internship.tex"):
        fail(failures, "internship example must use its mandatory team cover")
    for rel in ["shared/rules/ELSE-report-template.md", "shared/assets/UTM_Logo_English.jpeg"]:
        if not (ROOT / rel).is_file():
            fail(failures, f"missing report source support: {rel}")
    report_tex = read(ROOT / "report/main.tex")
    report_before_abstract = report_tex.split("\\begin{utmabstract}", 1)[0]
    for forbidden in ["Admis la susținere", "Proiect / teză de licență", "Raport de proiect"]:
        if forbidden in report_before_abstract:
            fail(failures, f"report title page must not contain thesis/project wording: {forbidden}")


def check_keywords(tex: str, pattern: str, label: str, failures: list[str], minimum: int = 4, maximum: int = 6) -> None:
    match = re.search(pattern, tex)
    if not match:
        fail(failures, f"{label} keywords missing")
        return
    keywords = [k.strip() for k in match.group(1).split(",") if k.strip()]
    if not (minimum <= len(keywords) <= maximum):
        fail(failures, f"{label} keywords must contain {minimum}-{maximum} terms; found {len(keywords)}")
    bad = [k for k in keywords if k != k.lower()]
    if bad:
        fail(failures, f"{label} keywords must be lowercase: {', '.join(bad)}")


def check_enumerations(tex: str, failures: list[str], ignore_after: str | None = None) -> None:
    ignored = False
    for line_no, line in enumerate(tex.splitlines(), start=1):
        stripped = line.strip()
        if ignore_after and ignore_after in stripped:
            ignored = True
        if stripped.startswith(r"\section") or stripped.startswith(r"\chapter"):
            if not (ignore_after and ignore_after in stripped):
                ignored = False
        if stripped.startswith(r"\item") and not ignored and not stripped.endswith(";"):
            fail(failures, f"enumeration item must end with semicolon at line {line_no}")


def main() -> int:
    failures: list[str] = []
    check_article(failures)
    check_abstract(failures)
    check_report_thesis(failures)
    if failures:
        print("UTM template check failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("UTM template check passed for article, abstract, report, and thesis.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
