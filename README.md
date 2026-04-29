# UTM Academic Paper LaTeX Template

Modern LaTeX template for UTM-style academic conference papers/articles based on the 2026 Romanian conference paper template.

## What This Is

- Article/paper template, not a thesis/report template.
- Uses A4, portrait, margins required by the conference paper template: top/bottom/right 2 cm and left 2.5 cm.
- Uses Times New Roman through Tectonic/XeTeX so Romanian diacritics render correctly.
- Includes optional UTM logo assets, but the logo is off by default because the official paper template does not require it.
- Includes a checker for core redaction rules.

## Files

- `main.tex`: compile-ready sample article.
- `utmconf.cls`: UTM conference paper class.
- `assets/`: UTM logo files copied from the older thesis template.
- `titlepage-demo.tex`: optional UTM title-page demo inspired by the thesis guide annex. Do not include it in a conference paper unless requested.
- `tools/check_utm_article.py`: automated checks for abstract length, keywords, required sections, and enumeration punctuation.
- `docs/`: bilingual rules and comparison notes.

## Compile

```powershell
python tools\check_utm_article.py
tectonic main.tex
tectonic titlepage-demo.tex
```

## Important Notes

- The official conference paper template does not show a UTM logo. If a teacher asks for branding, uncomment `\UTMShowLogotrue` in `main.tex`.
- Tectonic on Windows uses local Times New Roman fonts and may print reproducibility warnings. The generated PDF is still valid and preserves Romanian diacritics.
- A committee can still reject a paper for scientific content, plagiarism, missing signatures, or department-specific instructions. This template only enforces the extracted formatting and structure rules.
