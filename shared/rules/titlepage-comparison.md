# UTM Title Page Comparison

Source checked: `D:\uni\year2\guidelines\paper\sustinereTezeLicenta.pdf`, especially Anexa 1 and Anexa 2.

## Thesis Cover Page (Anexa 1)

Required source elements:

- UTM logo and institution name;
- project/thesis title;
- student name;
- supervisor name and academic/scientific title;
- place: Chișinău;
- year of defense/submission.

Implemented in `shared/classes/utmreport.cls` through `\makeutmcover`, used by `thesis/main.tex` only.

## Thesis Title Page (Anexa 2)

Required source elements:

- ministry name;
- UTM institution name;
- faculty name;
- department/cathedra name;
- admission-to-defense block for department head signature/date;
- title of project/thesis;
- document type, e.g. project/thesis of license;
- student signature/name/group;
- supervisor signature/title/name;
- consultants if applicable;
- place and year.

Implemented in `shared/classes/utmreport.cls` through `\makeutmthesistitlepage`, used by `thesis/main.tex`.

## Report Title Page

Reports are not theses and do not require the thesis defense/admission block unless a teacher explicitly asks for it. The report example therefore uses `\makeutmreporttitlepage`, not the thesis macro.

The report title page keeps the same institutional visual language:

- ministry name;
- UTM institution name;
- faculty name;
- department name;
- UTM logo;
- report title and optional subtitle;
- document type `Raport`;
- student, group, and supervisor;
- Chișinău and year.

The report title page intentionally excludes:

- `Admis la susținere`;
- department-head admission signature/date;
- `Proiect / teză de licență`;
- thesis declaration/front-matter pages.

## Deliberate Modernizations

- The old guide uses 2010-era ministry wording and Arial notes in the annex. The new template uses current UTM-friendly wording and Times New Roman to stay consistent with the extracted paper/report rules.
- The old guide contains engineering-frame annex pages. The modern template keeps the academic cover/title structure while avoiding discipline-specific frames unless a department explicitly requires them.
- Report and thesis now live in separate folders so students do not accidentally submit a report with thesis-defense wording.
- The shared class remains centralized in `shared/classes/` so fixes apply consistently without duplicating the preamble.
