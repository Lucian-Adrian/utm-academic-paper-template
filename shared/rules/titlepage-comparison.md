# UTM Title Page Comparison

Source checked: `sustinereTezeLicenta.pdf`, especially Anexa 1 and Anexa 2.

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

## Report title page

The supplied ELSE report model controls report covers. Its logo sits beside the university, faculty, department and study programme. There is no ministry line or admission-to-defense block. Document type is 20 pt bold and title 18 pt bold.

The individual report uses `\makeutmreporttitlepage` with right-aligned student, group and coordinator, as requested by the owner. The internship report uses `\makeutminternshiptitlepage` with a team table, mentor, blank signatures, attestation and submission date; member name/group cells are right aligned. See [ELSE report rules](ELSE-report-template.md) for source measurements and context.
