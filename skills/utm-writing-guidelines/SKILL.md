---
name: utm-writing-guidelines
description: Use when drafting, editing, reviewing, formatting, or recreating UTM conference abstracts, academic papers/articles, reports, or license thesis/project documents
---

# UTM Writing Guidelines

## First Choice

Choose exactly one target before formatting:

- conference abstract: `templates/abstract/`;
- conference article/paper: `templates/article/`;
- individual report (lab, course, PBL, semester): `templates/report/`;
- mandatory team internship report: `templates/internship/` (cover in `main.tex`, parts in `chapters/`);
- license thesis/project: `templates/thesis/`.

Start a document by copying the whole template folder (`python tools/new.py <template> <destination>`); each folder compiles on its own with `tectonic main.tex`. Replace every red `\placeholder{...}` and run `python tools/check.py <destination>` before calling the document ready.

Do not mix report and thesis front matter. Reports must not contain `Admis la susținere`, `Proiect / teză de licență`, or thesis-defense signature blocks. If a teacher, supervisor, department, or council gives a stricter rule, follow the stricter rule and mention the deviation.

## Local References

Use this repository checkout as the primary template source.

Read these before final formatting:

- Measured ELSE report rules: `docs/rules/ELSE-report-template.md`;
- Romanian rules: `docs/rules/UTM-writing-rules-and-formats-RO.md`;
- English rules: `docs/rules/UTM-writing-rules-and-formats-EN.md`;
- source comparison: `docs/rules/source-comparison.md`;
- title-page comparison: `docs/rules/titlepage-comparison.md`;
- validator: `tools/check.py`.

## Non-Negotiable Rules

- Use the document’s own source profile: ELSE reports and license theses have top/bottom/left 2 cm and right 1 cm; the conference article and abstract keep their separate margins.
- Use Times New Roman or the template serif fallback.
- Use Romanian diacritics in Romanian documents.
- Use impersonal academic style; avoid first person.
- Explain abbreviations, symbols, and notations at first use.
- Cite every reused idea, text, figure, table, scheme, formula, scan, or adapted item.
- Never cite sources inside a conference article abstract.
- For content enumerations, the introductory sentence ends with a colon, every item starts lowercase, and every item ends with a semicolon.
- The enumeration semicolon rule does not apply to bibliography entries.
- Generative AI may be used for coursework only when the instructor clearly permits it. When permitted, disclose the use explicitly in the form the course specifies; AI must not replace the student's intellectual contribution.

## Conference Article

Use `templates/article/` (`utmconf.cls`, `main.tex`).

Required checks:

- title uppercase, centered, 14 pt, bold;
- authors centered, 12 pt, bold;
- affiliations centered, 10 pt, italic;
- abstract 150-200 words, italic, justified, without citations;
- keywords 4-6 lowercase terms;
- sections: Introducere, Materiale și metode, Rezultate și discuții, Concluzii, Referințe;
- tables have title above;
- figures have caption below;
- equations are centered and numbered;
- citations use square brackets before punctuation.

The official article template does not require the UTM logo. Keep `\UTMShowLogotrue` commented unless branding is explicitly requested.

## Conference Abstract

Use `templates/abstract/` (`utmabstract.cls`, `main.tex`).

Required order:

1. title;
2. authors;
3. affiliations;
4. corresponding author;
5. scientific supervisor/coordinator;
6. abstract text;
7. keywords.

Keep the abstract compact and do not add report/thesis title pages.

## Report

Use the default shared class and the measured ELSE report rules. `templates/report/` is individual coursework; `templates/internship/` reproduces the mandatory team internship model. Keep preliminary page numbers hidden but count them continuously. Use contents before abstract, `\utmintroduction`, numbered chapters and `\utmconclusions`. Do not reset body numbering.

Match Times New Roman 12 pt, 1.5 spacing, 1.25 cm first-line indent, centered uppercase bold 13 pt chapters, and Courier New 10 pt single-spaced code. Program listings longer than half a page belong in a referenced appendix. Keep figures centered with bold captions below and tables with bold right-aligned captions above. Introduce visuals in prose and write opening prose before subchapters.

Right-align student/group/coordinator in individual reports and member name/group cells in internship covers. Use the supplied English logo for English reports. Keep titles and contents black: no `\placeholder` (red) text may remain. Cite every bibliography entry in first-use order, italicize titles, and include actual web access dates. Define abbreviations at first use. The source conditionally requires an abbreviations list before Introduction; preserve the accepted Filetracker omission as a project-specific exception. The source also gives minimum subchapter length and introduction guidance; distinguish a short layout example from a complete internship report.

Do not impose internship mentor, signature or final-summary requirements on labs. For the current PP3702 internship report, append one completed official summary per team member after all appendices. Give each a separate contents entry named `Internship Summary Report_Full Name`. The `\internshipsummary{Full Name}` command repeats the supplied form. Each student signs their own summary. Preserve verified work and distinguish measured results from examples.

## Thesis Or License Project

Use `templates/thesis/`, whose `main.tex` loads `utmreport.cls` with `[thesis]` and provides:

- `\makeutmcover`;
- `\makeutmthesistitlepage`;
- task-sheet placeholder;
- handwritten student-declaration placeholder;
- supervisor-opinion placeholder;
- Romanian and English abstracts;
- table of contents.

For a thesis written in a language other than Romanian, prepare title pages in the thesis language and Romanian. The title-page command can be called for each language after setting the corresponding institutional fields. Preliminary pages count but are not numbered; pagination starts at Introduction. Introduction and Conclusions are unnumbered.

Use Zotero with IEEE style for thesis references. Cite sources in square brackets in order of first appearance. Never invent the title, research, results, approvals, signatures or AI disclosure. Check the course curriculum for clear permission before using generative AI; if permitted, disclose use explicitly as instructed and keep the author's intellectual contribution.

Thesis/project content reminders:

- explanatory memorandum: 50-80 pages excluding annexes is recommended; the department sets the exact limit;
- theory: about 30-40%, not above 40%;
- practical/applied part: about 60-70%;
- figures/graphs: not above 30% of volume;
- use up to three numbered levels;
- code exceeding half a page belongs in a referenced appendix;
- defense: 10-15 minutes.

## Correct Workflow

From the document folder (a copy of a template):

```powershell
tectonic main.tex
python <template-repo>\tools\check.py .
```

When changing the templates themselves, run `python tools\check.py --sync` and `python tools\build.py` from the repository root.

Before saying a document is ready, confirm that validation passed, Tectonic compiled successfully, Romanian diacritics survived in the PDF, and no stricter local rule is being ignored.

## Honest Limit

No template can guarantee council acceptance. Acceptance also depends on originality, scientific quality, correct results, supervisor approval, signatures, deadlines, and department-specific checks.
