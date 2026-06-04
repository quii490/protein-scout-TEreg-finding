---
type: protein-evaluation
gene: "SKOR1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SKOR1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SKOR1 / CORL1, FUSSEL15, LBXCOR1 |
| Protein Name | SKI family transcriptional corepressor 1 |
| Protein Size | 965 aa, ~99.8 kDa |
| UniProt ID | P84550 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus |
| Protein Size | 8/10 | x1 | **8** | 965 aa, ~99.8 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=18 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=54.1; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR014890, IPR009061, IPR010919, IPR003380, IPR037000; Pfam: PF08782, PF02437 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 10 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **131.0/180** | |
| **Normalized Total** | | | **72.8/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | By similarity |
| GO-CC | nucleus | IBA:GO_Central |
| HPA | Nucleoplasm | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SKOR1 is 965 amino acids in length (~99.8 kDa). Acceptable size (965 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 18 |
| PubMed broad count | 38 |
| Alias context | Aliases observed but not used for scoring: CORL1, FUSSEL15, LBXCOR1 |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Acts as a transcriptional corepressor of LBX1 (By similarity). Inhibits BMP signaling. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 39695147 | Overexpression of PDSS2-Del2 in HCC promotes tumor metastasis by interacting with macrophages. | Cell death discovery |
| 38267254 | Genetic Association Studies in Restless Legs Syndrome: Risk Variants & Ethnic Differences. | The Canadian journal of neurological sciences. Le journal ca |
| 32572201 | SKOR1 has a transcriptional regulatory role on genes involved in pathways related to restless legs syndrome. | European journal of human genetics : EJHG |
| 25817513 | Genetic markers of Restless Legs Syndrome in Parkinson disease. | Parkinsonism & related disorders |
| 36209572 | Functional analysis of litter size and number of teats in pigs: From GWAS to post-GWAS. | Theriogenology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 54.1 |
| High confidence residues (pLDDT > 90) | 18.3% |
| Confident residues (pLDDT 70-90) | 9.3% |
| Medium confidence (pLDDT 50-70) | 7.9% |
| Low confidence (pLDDT < 50) | 64.5% |
| Ordered region (pLDDT > 70) | 27.6% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=54.1), 27.6% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR014890 |  |
| InterPro | IPR009061 |  |
| InterPro | IPR010919 |  |
| InterPro | IPR003380 |  |
| InterPro | IPR037000 |  |
| InterPro | IPR023216 |  |
| Pfam | PF08782 |  |
| Pfam | PF02437 |  |

**Domain Analysis**:    The protein contains 6 InterPro and 2 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 10 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| MAP2K5 | 0.974 | 0.000 | 0.0 | 0.967 |
| LBX1 | 0.887 | 0.000 | 0.0 | 0.883 |
| BTBD9 | 0.884 | 0.000 | 0.0 | 0.884 |
| MEIS1 | 0.844 | 0.000 | 0.0 | 0.844 |
| TLE1 | 0.746 | 0.095 | 0.0 | 0.731 |
| PTPRD | 0.671 | 0.000 | 0.0 | 0.671 |
| TOX3 | 0.655 | 0.000 | 0.0 | 0.655 |
| SMAD3 | 0.613 | 0.071 | 0.0 | 0.600 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| Hdac1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |
| Tle1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |
| Ctbp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |
| ENSMUSP00000055037.8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15528197 |
| Lbx1 | psi-mi:"MI:0031"(protein cross-linking with a bifunctional reagent) | pubmed:15528197 |
| Hipk2 | psi-mi:"MI:0428"(imaging technique) | pubmed:15528197 |
| TRIM27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| PRKAA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 6%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 72.8/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (965 aa) for experimental characterization
3. High novelty (PubMed count ~18)
4. AlphaFold prediction available (pLDDT 54.1)
5. Well-annotated domain architecture (8 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 72.8/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P84550
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P84550
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKOR1
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000188779-SKOR1/subcellular
- Data harvested: 2026-06-04 03:19:40
