# Source Comparison and Decisions

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
- the thesis guide's 60-80 page requirement does not apply to conference papers.

## New template decisions

- Create a new article-first folder: `utm-academic-paper-template`.
- Keep UTM logo assets available but off by default.
- Implement the official conference paper margins.
- Implement title/authors/affiliations/abstract/keywords as in the DOCX template.
- Implement paper sections without report chapters.
- Include a checker script for core rules.
- Include an optional title-page demo only for cases where a teacher asks for UTM title-page branding.

## Mechanical verification performed

- `tools/check_utm_article.py` passes.
- `tectonic main.tex` compiles to `main.pdf`.
- `tectonic titlepage-demo.tex` compiles to `titlepage-demo.pdf`.
- Generated PDFs are A4-sized.
- Extracted PDF text preserves Romanian diacritics.
- TeX logs contain no missing-character, overfull, or underfull warnings after switching to Times New Roman via XeTeX/fontspec.

## Known limitations

- The template cannot guarantee acceptance by the UTM council because acceptance also depends on scientific quality, originality, supervisor approval, department rules, signatures, and deadlines.
- Tectonic on Windows prints fontconfig/reproducibility warnings because it uses local Windows Times New Roman font files. This is acceptable for local compilation and required for faithful Times New Roman output with Romanian diacritics.
