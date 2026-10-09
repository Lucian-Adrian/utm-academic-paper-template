# Source Comparison and Decisions

## Current UTM and FCIM source check, 9 October 2026

The report and thesis profiles were checked against current institutional sources. The supplied `MANDATORY_report_memplate (1).docx` remains the authority for the report cover and its measured layout. The public FCIM ELSE page [Reguli de redactare](https://else.fcim.utm.md/mod/book/tool/print/index.php?id=66357), printed 1 September 2026, confirms the shared report/thesis requirements for margins, type, headings, abbreviations, code, figures, tables, formulas, references and page numbering.

For the thesis, the course resource `PAPER FORMATTING GUIDELINES.pdf` is retained beside these rules. It came from the DAS807 course resource at [ELSE](https://else.fcim.utm.md/pluginfile.php/219333/mod_resource/content/1/PAPER%20FORMATTING%20GUIDELINES.pdf); its PDF metadata gives a creation date of 7 April 2026 and its SHA-256 is `83FBEEBEBBDEC1A625C4383D7054B5D5D6CFA398F221231E8C859816D4D01586`. It repeats the current FCIM formatting profile. The structure is taken from the UTM-linked [Ghidul privind elaborarea și susținerea proiectelor/tezelor de licență](https://utm.md/wp-content/uploads/2019/12/Ghid-Elaborarea-si-sustinerea-proiectelor-tezelor-de-licenta.pdf), which recommends 50-80 pages and says the department sets exact limits.

The class and thesis starter now follow the current thesis rules for 2 cm top/bottom/left margins and 1 cm right margin, 13 pt uppercase chapter headings, 1.25 cm subchapter indentation, hidden preliminary page numbers, unnumbered Introduction and Conclusions, chapter-level captions, IEEE-style numeric citations, and appendices. The starter provides visible placeholders for the approved task sheet, handwritten student declaration and supervisor opinion, and separate Romanian and English abstract pages. These fields remain for the student, department or supervisor to complete.

UTM's owner-provided 2026 policy sources were also checked: [Regulamentul privind organizarea evaluării activității de învățare a studenților](https://utm.md/wp-content/uploads/2026/10/regulament-utm-evaluare-studenti_modificat-2026.pdf) (REG-89-OEAÎS, Edition 2, Revision 1), [Politica UTM de Integritate Academică](https://utm.md/wp-content/uploads/2026/10/politica-utm-de-integritate-academica-29.09.2026.pdf) (P 5.2.1, Edition 1, Revision 0), and [Procedura PO-UTM-03 privind etica și integritatea academică](https://utm.md/wp-content/uploads/2026/10/po-utm-03_etica_integritate_academica_utm.pdf) (Edition 1, Revision 0). Students need clear instructor permission before using generative AI for coursework. Where use is permitted, the procedure requires explicit disclosure and the policy says AI must not replace the student's intellectual contribution. These sources do not give one universal disclosure sentence or placement, so the project points students to the course's instructions instead of adding a fabricated declaration.

The course `PAPER FORMATTING GUIDELINES.pdf` is a thesis-formatting source, not a conference-paper template. The 2026 conference abstract and paper models remain separate and unchanged.

## Current PP3702 internship-summary requirement, 9 October 2026

The live ELSE [PP3702 course](https://else.fcim.utm.md/course/view.php?id=3702) section [Internship report instructions](https://else.fcim.utm.md/course/section.php?id=13631), beside resource 71193, requires each team member's own summary at the end of the report. Each summary must appear as a separate table-of-contents chapter titled `Internship Summary Report_Student's Full Name`; the report is incomplete if any member's summary is missing. `templates/internship/main.tex` now calls the reusable summary body once per listed member and creates one case-preserving TOC entry for each.

The live section's current Word resource at `https://else.fcim.utm.md/pluginfile.php/216017/mod_resource/content/3/MANDATORY_report_memplate.docx` was blocked by the browser with `ERR_BLOCKED_BY_CLIENT`; a fresh copy was not obtained or verified. The local Word model supplied on 2 October 2026 remains a prior reference for layout, not proof of the current resource's bytes. The internship changes in this repository address the observed per-member structure and do not claim a fresh review of the live Word file.

## Report update, 2 October 2026

The supplied `MANDATORY_report_memplate (1).docx` now controls the default report profile. Its measured rules override previous generic report defaults; see [ELSE report rules](ELSE-report-template.md). The thesis profile is explicit via `[thesis]`, and conference classes are unchanged.

## Sources inspected

- `Abstract_template-Conf-UTM-2026-rom.docx`
- `Paper_template-Conf-SMD-UTM-2026-rom.docx`
- `sustinereTezeLicenta.pdf`
- `UTM Latex Template`
- `Thesis_Report_Template_EN`

## Old `UTM Latex Template`

Useful ideas:

- has a custom LaTeX class;
- uses 1.25 cm paragraph indentation;
- includes table/figure/list structure.

Problems for the requested academic article:

- it is a report template, not an article template;
- margins do not match the conference paper template;
- it uses chapters, table of contents, list of figures, appendices, and minted code listings, which are inappropriate for a short 12,000-character paper;
- sample content is not redaction-safe;
- bibliography and caption behavior are report-oriented.

## Old `Thesis_Report_Template_EN`

Useful ideas:

- contains UTM logo assets;
- contains cover and title-page examples;
- includes declaration and supervisor PDF examples.

Problems for the requested academic article:

- it is a thesis template, not an article template;
- margins differ from the article template;
- it uses thesis structure: cover, title page, acknowledgements, declaration, supervisor opinion, abstract, chapters, annexes;
- the thesis guide's recommended 50-80 page memorandum length does not apply to conference papers.

## New template decisions

- Keep the conference article in its own `templates/article/` folder.
- Keep UTM logo assets available but off by default.
- Implement the official conference paper margins.
- Implement title/authors/affiliations/abstract/keywords as in the DOCX template.
- Implement paper sections without report chapters.
- Include a checker script for core rules.
- Include an optional title-page demo only for cases where a teacher asks for UTM title-page branding.

## Mechanical verification performed

- the article checker (now part of `tools/check.py`) passes.
- `tectonic main.tex` compiles to `main.pdf`.
- `tectonic titlepage-demo.tex` compiles to `titlepage-demo.pdf`.
- Generated PDFs are A4-sized.
- Extracted PDF text preserves Romanian diacritics.
- TeX logs contain no missing-character, overfull, or underfull warnings after switching to Times New Roman via XeTeX/fontspec.

## Known limitations

- The template cannot guarantee acceptance by the UTM council because acceptance also depends on scientific quality, originality, supervisor approval, department rules, signatures, and deadlines.
- Tectonic on Windows prints fontconfig/reproducibility warnings because it uses local Windows Times New Roman font files. This is acceptable for local compilation and required for faithful Times New Roman output with Romanian diacritics.
