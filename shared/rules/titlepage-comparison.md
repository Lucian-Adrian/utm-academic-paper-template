# UTM Title Page Comparison

Source checked: `D:\uni\year2\guidelines\paper\sustinereTezeLicenta.pdf`, especially Anexa 1 and Anexa 2.

## Cover Page (Anexa 1)

Required source elements:

- UTM logo and institution name;
- project/thesis title;
- student name;
- supervisor name and academic/scientific title;
- place: Chișinău;
- year of defense/submission.

Implemented in `report-thesis/utmreport.cls` through `\makeutmcover`:

- `\includegraphics` uses the UTM logo asset;
- `\UTMInstitution` prints institution name;
- `\UTMReportTitle` and optional `\UTMReportSubtitle` print the title block;
- `\student{...}{...}` prints name and group;
- `\supervisor{...}{...}` prints supervisor title and name;
- `\cityyear{Chișinău}{2026}` prints place and year.

## Title Page (Anexa 2)

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

Implemented in `report-thesis/utmreport.cls` through `\makeutmtitlepage`:

- current ministry label: `Ministerul Educației și Cercetării al Republicii Moldova`;
- `\institution`, `\faculty`, and `\department` macros;
- admission block: `Admis la susținere`, department-head line, date line;
- `\reporttitle` and `\documenttype` macros;
- student, supervisor, and optional consultant metadata;
- `\cityyear` for Chișinău/year.

## Deliberate Modernizations

- The old guide uses 2010-era ministry wording and Arial notes in the annex. The new template uses current UTM-friendly wording and Times New Roman to stay consistent with the extracted paper/report rules.
- The old guide contains engineering-frame annex pages. The modern template keeps the academic cover/title structure while avoiding discipline-specific frames unless a department explicitly requires them.
- The class is shared by report and thesis examples so students do not maintain two diverging preambles.
