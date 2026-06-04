# TEreg Protein Audit Report

Generated: 2026-05-31T03:47:23

## Scope

- Existing reports validated: 1969
- Final summary after rebuild: see `protein-finding.md` (1019 scored + 976 rejected)
- Sheet3 `研究很多`: 800 genes, 800 not yet evaluated, chunked in `audit_work/sheet3_research_many_missing_chunks/`
- Sheet4 `重新pa一下`: 1281 genes, 1274 not yet evaluated, chunked in `audit_work/sheet4_repa_missing_chunks/`

## Audit Results

- Before safe repair: 348 reports with errors; 636 reports with warnings
- After safe repair: 35 reports with errors; 402 reports with warnings
- Remaining total errors: 35
- Remaining total warnings: 402

## Safe Repairs Applied

- Safe repair files touched in last pass: 402
- Historical unlabeled score rows fixed: 39
- 402: recomputed raw/normalized score from score table
- 110: added explicit PAE absence note
- 12: fixed novelty score 10->8 for PubMed=28
- 11: fixed novelty score 10->8 for PubMed=30
- 11: fixed novelty score 10->8 for PubMed=21
- 11: fixed novelty score 10->8 for PubMed=25
- 10: fixed novelty score 10->6 for PubMed=42
- 10: fixed novelty score 10->8 for PubMed=22
- 10: fixed novelty score 10->6 for PubMed=51
- 9: fixed novelty score 10->8 for PubMed=23
- 9: fixed novelty score 10->8 for PubMed=26
- 9: fixed novelty score 10->4 for PubMed=70
- 8: fixed novelty score 10->8 for PubMed=39
- 8: fixed novelty score 10->4 for PubMed=62
- 8: fixed novelty score 10->8 for PubMed=34
- 8: fixed novelty score 10->4 for PubMed=74
- 8: fixed novelty score 10->8 for PubMed=37
- 7: fixed novelty score 10->4 for PubMed=68
- 7: fixed novelty score 10->6 for PubMed=45
- 7: fixed novelty score 10->6 for PubMed=47

## Remaining Error Categories

- 20: PPI section does not explicitly cover: STRING
- 6: PPI section does not explicitly cover: IntAct/BioGrid, STRING
- 3: PPI section does not explicitly cover: STRING, GO-CC
- 3: PPI section does not explicitly cover: GO-CC
- 2: PPI section does not explicitly cover: IntAct/BioGrid, STRING, GO-CC
- 1: PPI section does not explicitly cover: IntAct/BioGrid

## Remaining Warning Categories

- 320: No PAE image found
- 82: Rejected report lacks a clearly parseable PubMed>100 or nuclear<=3 reason

## Remaining Error Reports

- `ALKBH3` (detail/chromatin/ALKBH3/ALKBH3-evaluation.md): PPI section does not explicitly cover: STRING
- `ALKBH4` (detail/nucleolus/ALKBH4/ALKBH4-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `ALKBH8` (detail/nucleoplasm/ALKBH8/ALKBH8-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING, GO-CC
- `ANHX` (detail/nucleoplasm/ANHX/ANHX-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `ANKRD17` (detail/nuclear-envelope/ANKRD17/ANKRD17-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid
- `ANKRD2` (detail/nuclear-body/ANKRD2/ANKRD2-evaluation.md): PPI section does not explicitly cover: STRING
- `ARID5A` (detail/nucleolus/ARID5A/ARID5A-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING, GO-CC
- `ARVCF` (detail/nucleus-cytoplasm/ARVCF/ARVCF-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `ASXL3` (detail/chromatin/ASXL3/ASXL3-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `ATF6B` (detail/nucleus-cytoplasm/ATF6B/ATF6B-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `ATOH8` (detail/nuclear-speckle/ATOH8/ATOH8-evaluation.md): PPI section does not explicitly cover: STRING, GO-CC
- `CBFA2T2` (detail/nucleoplasm/CBFA2T2/CBFA2T2-evaluation.md): PPI section does not explicitly cover: STRING, GO-CC
- `CFDP1` (detail/chromatin/CFDP1/CFDP1-evaluation.md): PPI section does not explicitly cover: GO-CC
- `CHMP7` (detail/nuclear-envelope/CHMP7/CHMP7-evaluation.md): PPI section does not explicitly cover: GO-CC
- `CREB3L4` (detail/chromatin/CREB3L4/CREB3L4-evaluation.md): PPI section does not explicitly cover: STRING, GO-CC
- `CSTF2T` (detail/nucleus-cytoplasm/CSTF2T/CSTF2T-evaluation.md): PPI section does not explicitly cover: GO-CC
- `CWC27` (detail/nucleoplasm/CWC27/CWC27-evaluation.md): PPI section does not explicitly cover: STRING
- `FYTTD1` (detail/nuclear-speckle/FYTTD1/FYTTD1-evaluation.md): PPI section does not explicitly cover: STRING
- `KANSL2` (detail/nucleoplasm/KANSL2/KANSL2-evaluation.md): PPI section does not explicitly cover: STRING
- `KANSL3` (detail/nucleoplasm/KANSL3/KANSL3-evaluation.md): PPI section does not explicitly cover: STRING
- `KCTD1` (detail/nucleoplasm/KCTD1/KCTD1-evaluation.md): PPI section does not explicitly cover: STRING
- `KCTD13` (detail/nucleoplasm/KCTD13/KCTD13-evaluation.md): PPI section does not explicitly cover: STRING
- `KLHDC4` (detail/nucleoplasm/KLHDC4/KLHDC4-evaluation.md): PPI section does not explicitly cover: STRING
- `KPNA4` (detail/nucleus-cytoplasm/KPNA4/KPNA4-evaluation.md): PPI section does not explicitly cover: STRING
- `KTI12` (detail/nucleus-cytoplasm/KTI12/KTI12-evaluation.md): PPI section does not explicitly cover: STRING
- `LCOR` (detail/nucleoplasm/LCOR/LCOR-evaluation.md): PPI section does not explicitly cover: STRING
- `LDOC1` (detail/nucleoplasm/LDOC1/LDOC1-evaluation.md): PPI section does not explicitly cover: STRING
- `LEMD2` (detail/nuclear-envelope/LEMD2/LEMD2-evaluation.md): PPI section does not explicitly cover: STRING
- `LEMD3` (detail/nuclear-envelope/LEMD3/LEMD3-evaluation.md): PPI section does not explicitly cover: STRING
- `LETMD1` (detail/nucleus-cytoplasm/LETMD1/LETMD1-evaluation.md): PPI section does not explicitly cover: STRING
- `LHX5` (detail/nucleoplasm/LHX5/LHX5-evaluation.md): PPI section does not explicitly cover: STRING
- `LLPH` (detail/nucleolus/LLPH/LLPH-evaluation.md): PPI section does not explicitly cover: STRING
- `LRWD1` (detail/chromatin/LRWD1/LRWD1-evaluation.md): PPI section does not explicitly cover: STRING
- `MYEOV` (detail/nucleolus/MYEOV/MYEOV-evaluation.md): PPI section does not explicitly cover: IntAct/BioGrid, STRING
- `MYSM1` (detail/nucleoplasm/MYSM1/MYSM1-evaluation.md): PPI section does not explicitly cover: STRING

## Duplicate Gene Reports Still Present

Total duplicate genes: 26
- `CASC3`: detail/nucleus-cytoplasm/CASC3/CASC3-evaluation.md; detail/nuclear-speckle/CASC3/CASC3-evaluation.md
- `CCAR1`: detail/nucleus-cytoplasm/CCAR1/CCAR1-evaluation.md; detail/nucleoplasm/CCAR1/CCAR1-evaluation.md
- `CCDC137`: detail/nucleoplasm/CCDC137/CCDC137-evaluation.md; detail/chromatin/CCDC137/CCDC137-evaluation.md
- `CDAN1`: detail/nucleus-cytoplasm/CDAN1/CDAN1-evaluation.md; detail/nucleoplasm/CDAN1/CDAN1-evaluation.md
- `CDC14A`: detail/nucleus-cytoplasm/CDC14A/CDC14A-evaluation.md; detail/nucleoplasm/CDC14A/CDC14A-evaluation.md
- `CDX4`: detail/nucleus-cytoplasm/CDX4/CDX4-evaluation.md; detail/nucleoplasm/CDX4/CDX4-evaluation.md
- `CEBPG`: detail/nucleus-cytoplasm/CEBPG/CEBPG-evaluation.md; detail/nucleoplasm/CEBPG/CEBPG-evaluation.md
- `CENPH`: detail/nucleoplasm/CENPH/CENPH-evaluation.md; detail/chromatin/CENPH/CENPH-evaluation.md
- `CENPI`: detail/nucleoplasm/CENPI/CENPI-evaluation.md; detail/chromatin/CENPI/CENPI-evaluation.md
- `CENPK`: detail/nucleoplasm/CENPK/CENPK-evaluation.md; detail/chromatin/CENPK/CENPK-evaluation.md
- `CENPM`: detail/nucleoplasm/CENPM/CENPM-evaluation.md; detail/chromatin/CENPM/CENPM-evaluation.md
- `CENPT`: detail/nucleoplasm/CENPT/CENPT-evaluation.md; detail/chromatin/CENPT/CENPT-evaluation.md
- `CENPU`: detail/nucleoplasm/CENPU/CENPU-evaluation.md; detail/chromatin/CENPU/CENPU-evaluation.md
- `CENPX`: detail/nucleoplasm/CENPX/CENPX-evaluation.md; detail/chromatin/CENPX/CENPX-evaluation.md
- `CHMP1A`: detail/nucleus-cytoplasm/CHMP1A/CHMP1A-evaluation.md; detail/nucleoplasm/CHMP1A/CHMP1A-evaluation.md
- `CHP2`: detail/nucleus-cytoplasm/CHP2/CHP2-evaluation.md; detail/nucleoplasm/CHP2/CHP2-evaluation.md
- `CIPC`: detail/nucleus-cytoplasm/CIPC/CIPC-evaluation.md; detail/nucleoplasm/CIPC/CIPC-evaluation.md
- `CLASP1`: detail/rejected/CLASP1/CLASP1-evaluation.md; detail/nucleoplasm/CLASP1/CLASP1-evaluation.md
- `CLNS1A`: detail/nucleus-cytoplasm/CLNS1A/CLNS1A-evaluation.md; detail/nucleoplasm/CLNS1A/CLNS1A-evaluation.md
- `CRTC3`: detail/nucleus-cytoplasm/CRTC3/CRTC3-evaluation.md; detail/nucleoplasm/CRTC3/CRTC3-evaluation.md
- `CSRP1`: detail/nucleus-cytoplasm/CSRP1/CSRP1-evaluation.md; detail/nucleoplasm/CSRP1/CSRP1-evaluation.md
- `CSRP2`: detail/nucleus-cytoplasm/CSRP2/CSRP2-evaluation.md; detail/nucleoplasm/CSRP2/CSRP2-evaluation.md
- `CSRP3`: detail/nucleus-cytoplasm/CSRP3/CSRP3-evaluation.md; detail/nucleoplasm/CSRP3/CSRP3-evaluation.md
- `CSTF2T`: detail/nucleus-cytoplasm/CSTF2T/CSTF2T-evaluation.md; detail/nucleoplasm/CSTF2T/CSTF2T-evaluation.md
- `CTNNBL1`: detail/nucleus-cytoplasm/CTNNBL1/CTNNBL1-evaluation.md; detail/nucleoplasm/CTNNBL1/CTNNBL1-evaluation.md
- `CUTC`: detail/nucleus-cytoplasm/CUTC/CUTC-evaluation.md; detail/nucleoplasm/CUTC/CUTC-evaluation.md

## Next-Step Policy

- Remaining PPI errors should not be auto-filled without querying IntAct/STRING/GO-CC; these require database-backed repair.
- PAE warnings are acceptable only when AlphaFold/PAE is unavailable or intentionally not downloaded; otherwise fetch and embed PAE.
- Rejected-report warnings mean the rejection reason is not parseable by the validator; they should be normalized before publication-quality release.
- For sheet3/sheet4, process chunk manifests in order and run `python3 protein_gate.py --batch <chunk>` after each batch.
