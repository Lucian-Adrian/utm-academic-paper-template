---
name: utm-writing-guidelines
description: Use when drafting, editing, reviewing, formatting, or recreating UTM conference abstracts, academic papers/articles, reports, or license thesis/project documents
---

# UTM Writing Guidelines

## First Choice

Choose exactly one target before formatting:

- conference abstract: use `paper/abstract/abstract.tex`;
- conference article/paper: use `paper/article/main.tex`;
- individual report: use `report/main.tex`;
- mandatory team internship report: use `report/internship.tex`;
- license thesis/project: use `thesis/main.tex`.

Do not mix report and thesis front matter. Reports must not contain `Admis la susținere`, `Proiect / teză de licență`, or thesis-defense signature blocks. If a teacher, supervisor, department, or council gives a stricter rule, follow the stricter rule and mention the deviation.

## Local References

Use this repository checkout as the primary template source.

Read these before final formatting:

- Measured ELSE report rules: `shared/rules/ELSE-report-template.md`;
- Romanian rules: `shared/rules/UTM-writing-rules-and-formats-RO.md`;
- English rules: `shared/rules/UTM-writing-rules-and-formats-EN.md`;
- source comparison: `shared/rules/source-comparison.md`;
- title-page comparison: `shared/rules/titlepage-comparison.md`;
- validator: `tools/check_utm_templates.py`.

## Non-Negotiable Rules

- Use the document’s own source profile: ELSE reports have top/bottom/left 2 cm and right 1 cm; conference formats and the explicit thesis profile retain top/bottom/right 2 cm and left 2.5 cm.
- Use Times New Roman or the template serif fallback.
- Use Romanian diacritics in Romanian documents.
- Use impersonal academic style; avoid first person.
- Explain abbreviations, symbols, and notations at first use.
- Cite every reused idea, text, figure, table, scheme, formula, scan, or adapted item.
- Never cite sources inside a conference article abstract.
- For content enumerations, the introductory sentence ends with a colon, every item starts lowercase, and every item ends with a semicolon.
- The enumeration semicolon rule does not apply to bibliography entries.

## Conference Article

Use `paper/article/utmconf.cls` and `paper/article/main.tex`.

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

Use `paper/abstract/utmabstract.cls` and `paper/abstract/abstract.tex`.

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

Use the default shared class and the measured ELSE report rules. `report/main.tex` is individual coursework; `report/internship.tex` preserves the mandatory team internship fields. Keep preliminary page numbers hidden but count them continuously. Use contents before abstract, `\utmintroduction`, numbered chapters and `\utmconclusions`. Do not reset body numbering.

Match Times New Roman 12 pt, 1.5 spacing, 1.25 cm first-line indent, centered uppercase bold 13 pt chapters, and Courier New 10 pt single-spaced code. Program listings longer than half a page belong in a referenced appendix. Keep figures centered with bold captions below and tables with bold right-aligned captions above. Introduce visuals in prose and write opening prose before subchapters.

Right-align student/group/coordinator in individual reports and member name/group cells in internship covers. Use the supplied English logo for English reports. Keep titles and contents black. Cite every bibliography entry in first-use order, italicize titles, and include actual web access dates. Define abbreviations at first use. The source conditionally requires an abbreviations list before Introduction; preserve the accepted Filetracker omission as a project-specific exception. The source also gives minimum subchapter length and introduction guidance; distinguish a short layout example from a complete internship report.

Do not impose internship mentor, signature or final-summary requirements on labs. For internships, leave signatures blank and append the completed official summary last with its own contents entry. The accepted Filetracker package uses one team-level page; separate member summaries require an explicit course instruction. Preserve verified work and distinguish measured results from examples. The accepted Filetracker introduction length is specific to that report.

## Thesis Or License Project

Use `thesis/main.tex`, which loads `shared/classes/utmreport.cls` with `[thesis]` and calls:

- `\makeutmcover`;
- `\makeutmthesistitlepage`;
- declaration page;
- abstract/adnotare;
- table of contents.

Thesis/project content reminders:

- explanatory memorandum: usually 60-80 pages excluding annexes;
- theory: about 30-40%, not above 40%;
- practical/applied part: about 60-70%;
- figures/graphs: not above 30% of volume;
- bibliography: normally 15-30 sources;
- defense: 10-15 minutes.

## Correct Workflow

From the repository root:

```powershell
python tools\check_utm_templates.py
```

Compile the relevant document:

```powershell
cd paper\article
tectonic main.tex
```

```powershell
cd paper\abstract
tectonic abstract.tex
```

```powershell
cd report
tectonic main.tex
```

```powershell
cd thesis
tectonic main.tex
```

Before saying a document is ready, confirm that validation passed, Tectonic compiled successfully, Romanian diacritics survived in the PDF, and no stricter local rule is being ignored.

## Honest Limit

No template can guarantee council acceptance. Acceptance also depends on originality, scientific quality, correct results, supervisor approval, signatures, deadlines, and department-specific checks.
