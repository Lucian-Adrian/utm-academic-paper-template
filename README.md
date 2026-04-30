# UTM Academic LaTeX Templates

Modern, compile-ready LaTeX templates for students at the Technical University of Moldova (UTM): conference article, conference abstract, and a shared report/thesis template.

The repository was rebuilt from the 2026 UTM conference abstract/paper templates, the thesis/report guidance PDF, and older LaTeX folders. The old templates are preserved under `legacy/` for comparison, but new work should start from the modern folders below.

## Quick Start

Install [Tectonic](https://tectonic-typesetting.github.io/) first. It is the easiest LaTeX compiler because it downloads missing packages automatically.

```powershell
git clone https://github.com/Lucian-Adrian/utm-academic-paper-template.git
cd utm-academic-paper-template
python tools\check_utm_templates.py
```

Compile the document you need:

```powershell
cd paper\article
tectonic main.tex
```

```powershell
cd paper\abstract
tectonic abstract.tex
```

```powershell
cd report-thesis\report-example
tectonic main.tex
```

```powershell
cd report-thesis\thesis-example
tectonic main.tex
```

The generated PDF appears in the same folder as the `.tex` file.

## Which Template Should I Use?

| Need | Start here | Main file |
|---|---|---|
| UTM conference article / academic paper | `paper/article/` | `main.tex` |
| Short UTM conference abstract | `paper/abstract/` | `abstract.tex` |
| Course report, PBL report, laboratory/project report | `report-thesis/report-example/` | `main.tex` |
| License thesis / graduation project | `report-thesis/thesis-example/` | `main.tex` |
| Rules in Romanian | `shared/rules/` | `UTM-writing-rules-and-formats-RO.md` |
| Rules in English | `shared/rules/` | `UTM-writing-rules-and-formats-EN.md` |
| Historical old templates | `legacy/` | reference only |

## Repository Layout

```text
paper/
  article/          UTM conference article class and example
  abstract/         UTM conference abstract class and example
report-thesis/
  utmreport.cls     shared class for reports and theses
  report-example/   universal report example
  thesis-example/   license thesis/project example
  shared/           logo assets used by report/thesis examples
shared/
  assets/           UTM logo variants
  rules/            bilingual extracted rules, source comparison, and title-page comparison
  tools/            validation scripts
tools/              root-level validation scripts for easy use
legacy/             old previous-year templates preserved for comparison
```

## Core Formatting Rules

These are the non-negotiable defaults encoded in the templates:

- A4 portrait page;
- margins: top 2 cm, bottom 2 cm, right 2 cm, left 2.5 cm;
- Times New Roman when available, with a serif fallback for systems without it;
- Romanian text with diacritics;
- impersonal academic style;
- all reused ideas, figures, tables, formulas, schemes, scans, and adapted materials must be cited;
- enumerations introduced by a colon, with each item starting lowercase and ending with a semicolon;
- stricter teacher, department, supervisor, or council instructions override the template.

## Article Rules

The article template in `paper/article/` follows the UTM conference paper structure:

- title: uppercase, centered, 14 pt, bold;
- authors: centered, 12 pt, bold;
- affiliations: centered, 10 pt, italic;
- abstract: 150-200 words, italic, justified, no citations;
- keywords: 4-6 lowercase terms, comma-separated;
- required sections: Introduction, Materials and Methods, Results and Discussion, Conclusions, References;
- tables: title above the table;
- figures: caption below the figure;
- equations: centered and numbered;
- references cited in square brackets before punctuation.

The official article model does not require a UTM logo. A logo command is included but disabled by default. Enable it only if a teacher or department asks for branded pages.

## Abstract Rules

The abstract template in `paper/abstract/` is for short conference submissions. Keep it focused, compact, and formatted like the source abstract model:

- title and author block first;
- corresponding author and scientific supervisor included;
- abstract body in `rezumat`;
- keywords in `\cuvintecheie{...}`;
- no oversized report/thesis title page.

## Report And Thesis Rules

The `report-thesis/utmreport.cls` class is shared by both reports and theses because the layout requirements are similar. It includes:

- UTM cover page with logo;
- formal title page;
- abstract/adnotare environment;
- table of contents;
- chapter-based structure;
- figure, table, equation, listing, and bibliography support;
- 1.5 line spacing and 1.25 cm paragraph indentation;
- optional consultant metadata.

For a thesis/project, also keep the academic content ratios from the extracted guide in mind:

- explanatory memorandum: usually 60-80 pages, excluding annexes;
- theoretical part: about 30-40%, not more than 40%;
- practical/applied part: about 60-70%;
- figures and graphs: not more than 30% of total volume;
- bibliography: normally 15-30 sources;
- defense presentation: 10-15 minutes.

## Validation

Run the checker before compiling or submitting:

```powershell
python tools\check_utm_templates.py
```

For article-only checks:

```powershell
python tools\check_utm_article.py
```

The checker verifies the most important automated rules: article sections, abstract length, keyword count/case, margin tokens, report/thesis macros, table of contents presence, and enumeration punctuation. It cannot verify scientific originality, supervisor approval, signatures, or department-specific council decisions.

## Editing Without Technical Experience

1. Open the folder for the document type you need.
2. Edit only the `.tex` example file first.
3. Replace placeholder names, faculty, department, group, supervisor, title, abstract, keywords, and section text.
4. Keep the commands that start with backslash, such as `\documentclass`, `\chapter`, `\section`, `\begin`, and `\end`.
5. Run the checker.
6. Compile with `tectonic`.
7. Open the PDF and visually inspect title page, margins, Romanian diacritics, figures, tables, and references.

## Agent Skill

A Codex/agent skill is included in `skills/utm-writing-guidelines/SKILL.md`. Install it by copying that folder into your local skills directory, or use the installed version if it already exists at:

```text
C:\Users\dev\.agents\skills\utm-writing-guidelines\SKILL.md
```

The skill tells an agent how to choose the correct UTM document type, apply the rules, use the templates, and verify the result before claiming it is ready.

## Important Limit

This repository gives students a clean, modern starting point and automates many redaction checks. It cannot guarantee acceptance by a UTM council. Acceptance still depends on scientific quality, originality, correct data, supervisor approval, signatures, deadlines, and any stricter department-specific requirements.


