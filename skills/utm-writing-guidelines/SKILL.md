---
name: utm-writing-guidelines
description: Use when drafting, editing, reviewing, formatting, or recreating UTM conference abstracts, academic papers/articles, reports, or license thesis/project documents
---

# UTM Writing Guidelines

## First Choice

Choose exactly one target before formatting:

- conference abstract: use `paper/abstract/abstract.tex`;
- conference article/paper: use `paper/article/main.tex`;
- report: use `report-thesis/report-example/main.tex`;
- license thesis/project: use `report-thesis/thesis-example/main.tex`.

Do not mix article limits with thesis/report structure. If a teacher, supervisor, department, or council gives a stricter rule, follow the stricter rule and mention the deviation.

## Local References

Primary repository:

```text
D:\uni\year2\guidelines\paper\utm-academic-paper-template
```

Read these before final formatting:

- Romanian rules: `shared/rules/UTM-writing-rules-and-formats-RO.md`;
- English rules: `shared/rules/UTM-writing-rules-and-formats-EN.md`;
- source comparison: `shared/rules/source-comparison.md`;
- validator: `tools/check_utm_templates.py`.

## Non-Negotiable Rules

- Use A4 portrait with margins: top 2 cm, bottom 2 cm, right 2 cm, left 2.5 cm.
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

## Report Or Thesis

Use `report-thesis/utmreport.cls`.

For reports, start from `report-thesis/report-example/main.tex`. For theses/projects, start from `report-thesis/thesis-example/main.tex`.

The class provides:

- UTM cover page with logo;
- formal title page;
- abstract/adnotare environment;
- table of contents;
- chapter structure;
- figures, tables, equations, listings, bibliography, and appendices;
- 1.5 line spacing and 1.25 cm paragraph indentation.

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
cd report-thesis\report-example
tectonic main.tex
```

```powershell
cd report-thesis\thesis-example
tectonic main.tex
```

Before saying a document is ready, confirm that validation passed, Tectonic compiled successfully, Romanian diacritics survived in the PDF, and no stricter local rule is being ignored.

## Honest Limit

No template can guarantee council acceptance. Acceptance also depends on originality, scientific quality, correct results, supervisor approval, signatures, deadlines, and department-specific checks.
