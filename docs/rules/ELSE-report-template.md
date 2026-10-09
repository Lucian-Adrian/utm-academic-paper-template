# ELSE mandatory report profile

The report defaults follow `MANDATORY_report_memplate (1).docx`, supplied by the owner on 2 October 2026. Its SHA-256 is `95274233D56A71BB9F1DE24E2403EB2D43BC3C0DE01231622FA6B8C156C78BF7`. The Word source is not redistributed here. Measurements were read from its section properties, paragraph styles and native Word rendering; explanatory text in the source is guidance, not completed report content.

The current public FCIM ELSE page [Reguli de redactare](https://else.fcim.utm.md/mod/book/tool/print/index.php?id=66357) was printed 1 September 2026 and checked on 9 October 2026. It confirms the shared formatting rules below. The supplied Word model continues to control report-specific cover fields and finer layout. The title, assignment sheet, signed approvals and research content are not inferred from the general rules.

## Page and body

- A4 portrait; top, bottom and left margins 2 cm; right margin 1 cm.
- Times New Roman 12 pt, black, justified, 1.5 line spacing; first-line indent 1.25 cm; no paragraph spacing before or after.
- Count preliminary pages continuously, but hide their printed numbers. Print centered Arabic numbers starting with Introduction, without resetting the count. With one cover, one contents page and one abstract page, Introduction is page 4.
- The abstract summarizes the actual work and includes 5–7 lowercase keyword terms.
- Cover, contents, abstract, introduction, numbered body, conclusions, references, appendices. The source requires an abbreviations list before Introduction, with a contents entry, for abbreviations or terms outside the language of instruction. The accepted Filetracker report omitted that page as a project-specific exception; define terms at first use and preserve that exception when adapting its report.

## Headings, code and captions

- Chapters start on a new page: `1 CHAPTER TITLE`, centered, uppercase, bold 13 pt, one space after the number. Introduction, Conclusions and References are unnumbered. Do not prefix headings with “Chapter”.
- Subchapters: `1.1 Subchapter title`, left aligned, bold 12 pt, indented 1.25 cm; 12 pt before and 6 pt after. Use at most three numbered levels.
- Contents: titled TABLE OF CONTENTS; regular-weight entries with dot leaders; chapter-level entries (ABSTRACT, INTRODUCTION, numbered chapters, CONCLUSIONS, REFERENCES, APPENDICES) in uppercase; subchapters and `APPENDIX A – Title` entries indented 0.5 cm.
- The source requires impersonal prose and prohibits first-person pronouns. Its internship/thesis guidance gives Introduction about 1–2 pages and each subchapter at least one full page. The public examples demonstrate layout and fields, not completed content satisfying those length rules. Do not pad short lab answers to imply a full internship chapter.
- Keep headings with the following paragraph. Write opening prose before the first subchapter; do not leave a heading alone at a page bottom.
- Code: Courier New 10 pt, single spacing. Place actual program listings longer than half a page in a referenced appendix.
- Figures: `Figure 1.1 – Title`, centered bold 12 pt caption below. Tables: `Table 1.1 – Title`, right-aligned bold 12 pt caption above; table text 11 pt, single spacing. Introduce each item in prose; never start a page with a table or figure.
- Bulleted lists use a hyphen at the paragraph indent. Content enumerations use a), b), c) and end each item with a semicolon.
- References: REFERENCES heading with a contents entry; entries numbered `1.`, `2.` in first-use order, in the model formats (for example `AUTHOR 1, A.B.; AUTHOR 2, C.D. Title. Journal Year, Volume, pages, doi.`, or for websites `Title of Site. Available online: URL (accessed on Day Month Year).`). Cite each entry, italicize source titles, and use the body’s 1.5 spacing.
- The abstract ends with a separate indented `Keywords:` paragraph of 5–7 lowercase terms.

## Cover and context

The source has a logo beside the institutional block, including university, faculty, department and study programme. The report type is 20 pt bold and the project title 18 pt bold, both uppercase. The internship cover continues with the 13 pt team line, the bold “Team members:” label and a single-spaced table whose third column reads “*Signature”. The 10 pt italic attestation starts with an asterisk, the submission date defaults to dotted blanks, and “Chișinău, 2026” closes the page. The extracted English logo is `shared/assets/UTM_Logo_English.jpeg`, copied into each English template as `utm-logo.jpeg`.

The owner explicitly requested right alignment for name and group. `\makeutmreporttitlepage` applies it to the individual student/group/coordinator block. `\makeutminternshiptitlepage` applies it to member name/group cells while retaining the source’s team and signature table. Neither cover adds a ministry line or thesis admission block.

Use `templates/report/` for individual coursework. Use `templates/internship/` for the mandatory team internship report, including mentor, blank signatures, attestation and submission date. The completed internship summary belongs at the end with its own contents entry. The accepted Filetracker package used one team-level summary page; this example follows that placement. Duplicate it only if the course explicitly requires separate member summaries. The final example preserves the blank fields of the supplied `SUMMARY_REPORT_en.docx` (SHA-256 `4394c2bb2850d0bb9edf01b2e9c860e969f7e6cc04b180ccde55198f8d1a2a8f`): host, unit, programme, study mode/year/group, period, activities, results, difficulties, conclusions/recommendations, date and student signature. Replace the blank narrative lines with the actual account; do not fabricate signatures. Do not add these internship-specific fields to laboratory reports. The source’s suggested 1–2 page introduction and the accepted Filetracker introduction length are content guidance, not a mandatory length for every lab.

## LaTeX use

The default `utmreport` class selects this profile. Set `\selectlanguage{english}` for an English report. Call the appropriate title-page macro, `\tableofcontents`, the abstract, `\utmintroduction`, numbered chapters, and `\utmconclusions`. `\utmmainmatter` is available when an assignment uses a differently named opening chapter. Do not insert Roman numbering or a main-page counter reset.

Report appendices have an APPENDICES collection heading, then a centered bold 12 pt `APPENDIX A – Title` line, as in the Word example. (The Word guidance note puts the title beneath the label, but its example puts both on one line; the template follows the example.) Every later appendix begins on a new page. Write `\appendix`, then `\chapter{Title}`.

Placeholder text is wrapped in `\placeholder{...}` and printed in red, like the red text in the Word model. `python tools/check.py <folder>` lists any placeholders that remain.

The explicit `[thesis]` option retains the previous thesis layout. Conference article and abstract classes keep their own source rules. This report profile takes precedence over older generic report margins in the bilingual conference/thesis guidance.
