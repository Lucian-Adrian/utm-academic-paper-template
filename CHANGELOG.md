# Changes

## 2026-10-09 (current thesis and integrity rules)

- Checked the supplied report model against the current FCIM ELSE formatting page; the report profile remains governed by the supplied Word model.
- Updated the thesis class to the current FCIM margins, chapter/subchapter styles, hidden preliminary numbering, bold figure/table captions, table text, IEEE citation labels and appendix headings.
- Replaced generic thesis sample claims with red placeholders and added the required task-sheet, handwritten-declaration, supervisor-opinion and Romanian/English abstract pages.
- Added the current UTM generative-AI permission and explicit-disclosure rules to the writing guidance. No universal disclosure wording is invented.
- Preserved the course's `PAPER FORMATTING GUIDELINES.pdf` in `docs/rules/`; its SHA-256 was verified after the move.
- Updated the internship starter for PP3702's per-member requirement: one final summary chapter and TOC entry per team member, using the supplied summary form body.

## 2026-10-02 (layout and fidelity)

- Reorganized the repository around `templates/`: `report`, `internship`, `thesis`, `article` and `abstract`. Every template folder is self-contained (class, logo, example figure) and compiles after being copied anywhere.
- Added `tools/new.py` to copy a template to a destination, `tools/build.py` to compile previews into `docs/previews/`, and merged both checkers into `tools/check.py`, which syncs `shared/` into the templates (`--sync`), detects drift, and checks a student's own folder for placeholders, keywords, citations, images and enumerations.
- Moved the rules to `docs/rules/` and the canonical class to `shared/utmreport.cls`.
- Split the internship template into numbered `chapters/` files that follow the Word template's order.
- Matched the ELSE Word template more closely: TABLE OF CONTENTS title and plain uppercase entries; `1 TITLE` heading spacing; REFERENCES heading with contents entry and `1.` numbering; one-line `APPENDIX A – Title` headings indented in the contents; uppercase cover title, 13 pt team line, compact member table with `*Signature` cells, asterisked attestation and dotted submission date; separate keywords paragraph; 11 pt single-spaced tables; hyphen bullets; optional list of abbreviations; red `\placeholder` text.

## 2026-10-02

- Adapted the report class to the supplied ELSE mandatory Word template: source margins, chapter styles, code font, captions and continuous page counting with hidden preliminary numbers.
- Right-aligned the individual student/group/coordinator block and internship member name/group cells at the owner's request.
- Added an English individual report and a team internship example, the exact source logo, measured formatting notes and validation for the report profile.
- Kept the previous thesis layout behind the explicit `thesis` option; conference formats retain their own rules.
