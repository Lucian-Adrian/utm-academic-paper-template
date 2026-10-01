# UTM Academic LaTeX Templates

LaTeX templates for students at the Technical University of Moldova (UTM): conference article, conference abstract, report, and license thesis/project.

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
cd report
tectonic main.tex
```

```powershell
cd thesis
tectonic main.tex
```

The generated PDF appears in the same folder as the `.tex` file.

## Which Template Should I Use?

| Need | Start here | Main file |
|---|---|---|
| UTM conference article / academic paper | `paper/article/` | `main.tex` |
| Short UTM conference abstract | `paper/abstract/` | `abstract.tex` |
| Course report, PBL report, laboratory report, semester report | `report/` | `main.tex` |
| Team internship report using the supplied ELSE model | `report/` | `internship.tex` |
| License thesis / graduation project | `thesis/` | `main.tex` |
| Rules in Romanian | `shared/rules/` | `UTM-writing-rules-and-formats-RO.md` |
| Rules in English | `shared/rules/` | `UTM-writing-rules-and-formats-EN.md` |
| Historical old templates | `legacy/` | reference only |

## Repository Layout

```text
paper/
  article/          UTM conference article class and example
  abstract/         UTM conference abstract class and example
report/             individual and team internship report examples
thesis/             license thesis/project example, with cover and defense title page
shared/
  assets/           UTM logo variants
  classes/          shared report/thesis LaTeX class
  rules/            bilingual extracted rules, source comparison, and title-page comparison
  tools/            validation scripts
tools/              root-level validation scripts for easy use
legacy/             old previous-year templates preserved for comparison
```

## Core Formatting Rules

Choose the source profile for the document type:

- A4 portrait page;
- ELSE reports: top, bottom and left margins 2 cm, right margin 1 cm;
- conference formats and the explicit thesis profile retain top/bottom/right 2 cm and left 2.5 cm;
- Times New Roman when available, with a serif fallback for systems without it;
- English or Romanian text, preserving Romanian diacritics where used;
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

## Report Rules

The default shared class now follows the supplied ELSE mandatory Word report model. See [the measured report rules](shared/rules/ELSE-report-template.md) for its provenance and details.

- `report/main.tex`: individual coursework, with right-aligned student, group and coordinator;
- `report/internship.tex`: the mandatory team cover, mentor, blank signature fields and final member summaries;
- Times New Roman 12 pt, justified, 1.5 spacing, 1.25 cm first-line indent;
- uppercase centered 13 pt chapter headings; unnumbered Introduction and Conclusions;
- Courier New 10 pt code; longer programs in referenced appendices;
- bold centered figure captions below; bold right-aligned table captions above;
- cover, contents and abstract count as pages but show no numbers; numbering appears at Introduction without restarting.

Use `\makeutmreporttitlepage` or `\makeutminternshiptitlepage`, then contents and abstract, `\utmintroduction`, numbered chapters and `\utmconclusions`. Select English with `\selectlanguage{english}`. For the internship example, run `tectonic internship.tex` from `report/`.

Coursework reports do not need internship team, mentor, signature or summary fields. The supplied report model does not add a ministry line or thesis admission block. Replace all example content before submission; illustrative values are not measurements.

## Thesis Rules

The thesis template in `thesis/` uses `\documentclass[thesis]{../shared/classes/utmreport}` to retain the thesis profile and calls thesis-specific front matter:

- `\makeutmcover` for the UTM cover;
- `\makeutmthesistitlepage` for the formal defense title page;
- declaration page;
- abstract/adnotare;
- table of contents;
- chapter-based body, bibliography, and annexes.

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

The checker verifies the most important automated rules: article sections, abstract length, keyword count/case, margin tokens, report/thesis macros, table of contents presence, report-vs-thesis title-page wording, and enumeration punctuation. It cannot verify scientific originality, supervisor approval, signatures, or department-specific council decisions.

## Editing Without Technical Experience

1. Open the folder for the document type you need.
2. Edit only the `.tex` example file first.
3. Replace placeholder names, faculty, department, group, supervisor, title, abstract, keywords, and section text.
4. Keep the commands that start with backslash, such as `\documentclass`, `\chapter`, `\section`, `\begin`, and `\end`.
5. Run the checker.
6. Compile with `tectonic`.
7. Open the PDF and visually inspect title page, margins, Romanian diacritics, figures, tables, and references.

## Agent Skill

The repository includes [an agent skill](skills/utm-writing-guidelines/SKILL.md) for choosing a document type, applying its source rules and checking the compiled PDF. Installing it is optional.

## Important Limit

This repository gives students a clean, modern starting point and automates many redaction checks. It cannot guarantee acceptance by a UTM council. Acceptance still depends on scientific quality, originality, correct data, supervisor approval, signatures, deadlines, and any stricter department-specific requirements.
