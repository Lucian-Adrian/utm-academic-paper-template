# ELSE mandatory report profile

The report defaults follow `MANDATORY_report_memplate (1).docx`, supplied by the owner on 2 October 2026. Its SHA-256 is `95274233D56A71BB9F1DE24E2403EB2D43BC3C0DE01231622FA6B8C156C78BF7`. The Word source is not redistributed here. Measurements were read from its section properties, paragraph styles and native Word rendering; explanatory text in the source is guidance, not completed report content.

## Page and body

- A4 portrait; top, bottom and left margins 2 cm; right margin 1 cm.
- Times New Roman 12 pt, black, justified, 1.5 line spacing; first-line indent 1.25 cm; no paragraph spacing before or after.
- Count preliminary pages continuously, but hide their printed numbers. Print centered Arabic numbers starting with Introduction, without resetting the count. With one cover, one contents page and one abstract page, Introduction is page 4.
- The abstract summarizes the actual work and includes 5–7 lowercase keyword terms.
- Cover, contents, abstract, introduction, numbered body, conclusions, references, appendices. The source requires an abbreviations list before Introduction, with a contents entry, for abbreviations or terms outside the language of instruction. The accepted Filetracker report omitted that page as a project-specific exception; define terms at first use and preserve that exception when adapting its report.

## Headings, code and captions

- Chapters start on a new page: centered, uppercase, bold 13 pt. Introduction and Conclusions are unnumbered. Do not prefix headings with “Chapter”.
- Subchapters: left aligned, bold 12 pt, indented 1.25 cm; 12 pt before and 6 pt after. Use at most three numbered levels.
- The source requires impersonal prose and prohibits first-person pronouns. Its internship/thesis guidance gives Introduction about 1–2 pages and each subchapter at least one full page. The public examples demonstrate layout and fields, not completed content satisfying those length rules. Do not pad short lab answers to imply a full internship chapter.
- Keep headings with the following paragraph. Write opening prose before the first subchapter; do not leave a heading alone at a page bottom.
- Code: Courier New 10 pt, single spacing. Place actual program listings longer than half a page in a referenced appendix.
- Figures: centered bold 12 pt caption below. Tables: right-aligned bold 12 pt caption above. Use an en dash between number and caption. Introduce each item in prose.
- Number references in first-use order, cite each entry, italicize source titles, and give actual access dates for online sources. References use the body’s 1.5 spacing.

## Cover and context

The source has a logo beside the institutional block, including university, faculty, department and study programme. The report type is 20 pt bold; project title is 18 pt bold. The extracted English logo is `shared/assets/UTM_Logo_English.jpeg`.

The owner explicitly requested right alignment for name and group. `\makeutmreporttitlepage` applies it to the individual student/group/coordinator block. `\makeutminternshiptitlepage` applies it to member name/group cells while retaining the source’s team and signature table. Neither cover adds a ministry line or thesis admission block.

Use `report/main.tex` for individual coursework. Use `report/internship.tex` for the mandatory team internship report, including mentor, blank signatures, attestation and submission date. The completed internship summary belongs at the end with its own contents entry. The accepted Filetracker package used one team-level summary page; this example follows that placement. Duplicate it only if the course explicitly requires separate member summaries. The final example preserves the blank fields of the supplied `SUMMARY_REPORT_en.docx` (SHA-256 `4394c2bb2850d0bb9edf01b2e9c860e969f7e6cc04b180ccde55198f8d1a2a8f`): host, unit, programme, study mode/year/group, period, activities, results, difficulties, conclusions/recommendations, date and student signature. Replace the blank narrative lines with the actual account; do not fabricate signatures. Do not add these internship-specific fields to laboratory reports. The source’s suggested 1–2 page introduction and the accepted Filetracker introduction length are content guidance, not a mandatory length for every lab.

## LaTeX use

The default `utmreport` class selects this profile. Set `\selectlanguage{english}` for an English report. Call the appropriate title-page macro, `\tableofcontents`, the abstract, `\utmintroduction`, numbered chapters, and `\utmconclusions`. `\utmmainmatter` is available when an assignment uses a differently named opening chapter. Do not insert Roman numbering or a main-page counter reset.

Report appendices have an APPENDICES collection heading and an APPENDIX A label with the centered title below; each appendix begins on a new page.

The explicit `[thesis]` option retains the previous thesis layout. Conference article and abstract classes keep their own source rules. This report profile takes precedence over older generic report margins in the bilingual conference/thesis guidance.
