# Additional Metadata

## Clarified Semantics

- `satscores.rtype` distinguishes row granularity: `"S"` (1749 rows) are school-level records where `sname` is populated, while `"D"` (520 rows) are district-level aggregates where `dname`/`cname` are populated and `sname` is null.
- `satscores` numeric scores (`AvgScrRead/Math/Write`, `NumGE1500`, `NumTstTakr`) are null in most `"D"` rows for many test-taking reasons (e.g. 0 takers); missing averages indicate a school with no/reported test takers, not a zero score.
- `satscores.cds` for `"D"` rows is a district-level CDS identifier; only 35 of these match a `frpm.CDSCode`, most district aggregate rows have no school-level meal data.
- `frpm` is entirely school-level: all 9986 `frpm.CDSCode` values map 1:1 to a `schools` record (0 orphans). `schools` is broader (17686 rows); ~7700 `schools` rows have no `frpm` meal record.
- `schools.StatusType` holds lifecycle state; `satscores` school rows (`S`) all map to `StatusType='Closed'` schools, while `"D"` district rows map to `StatusType='Active'` entities — so school-vs-district rows differ systematically in status.
- `frpm`/`schools` encode the same school descriptors under different names: `frpm."School Type"` ≈ `schools.SOCType` (and code `SOC`); `frpm."District Type"` ≈ `schools.DOCType`; `frpm."Educational Option Type"` ≈ `schools.EdOpsName`; grade bands ≈ `schools.EILCode/EILName`.
- CDS code (`frpm.CDSCode`, `schools.CDSCode`, `satscores.cds`) is the 14-digit composite of county/district/school codes and is the reliable key; district CDS values equal the school CDS of the district-office record.

## Potential Join Strategies

- **`frpm` ↔ `schools`** on `frpm.CDSCode = schools.CDSCode`: 1:1, no orphans. Join counts vary by `schools.StatusType`; prefer filtering `StatusType='Active'` to isolate currently-operating schools and reduce the ~7700 non-`frpm` `schools` rows.
- **`satscores` ↔ `schools`** on `satscores.cds = schools.CDSCode`: valid for all 2269 rows, but scope school-level comparisons to `rtype='S'` and note those correspond to `StatusType='Closed'` entities (historic SAT records).
- **`frpm` ↔ `satscores`**: no declared FK; bridge through `schools` (decode count reaches `frpm`/`schools` matches plus `satscores`). Only `rtype='S'` rows are meaningful at school level; prepend the `schools` join or filter `rtype='S'` to avoid the ~35 spurious district matches.
- **County-level join** on `frpm."County Name" = satscores.cname = schools.County`: all three are 58 distinct named counties; many-to-many across tables, useful for county rollups.
- **District-level join** on `frpm."District Name" = satscores.dname = schools.District`: cardinality differs (schools 1411 distinct vs frpm 1000), so this is a loose semantic join; disambiguate by combining with county name or by using `frpm."District Code"` against the `schools` district-representative CDS.
- **School-name join** on `frpm."School Name" = satscores.sname = schools.School`: names are not unique across districts (e.g. repeated school names); always anchor to `CDSCode`/`cds` when names are ambiguous.