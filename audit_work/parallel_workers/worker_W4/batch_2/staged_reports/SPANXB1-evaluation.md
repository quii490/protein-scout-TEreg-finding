---
type: protein-evaluation
gene: "SPANXB1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPANXB1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPANXB1 / SPANXB, SPANXB2, SPANXF1 |
| Protein Name | Sperm protein associated with the nucleus on the X chromosome B1 |
| Protein Size | 103 aa, ~11.8 kDa |
| UniProt ID | Q9NS25 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Uncertain); GO-CC: nucleus |
| Protein Size | 8/10 | x1 | **8** | 103 aa, ~11.8 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=9 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=68.0; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR010007; Pfam: PF07458 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 14 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **131.0/180** | |
| **Normalized Total** | | | **72.8/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | Experimental |
| UniProt | Nucleus | Experimental |
| GO-CC | nucleus | HDA:UniProtKB |
| HPA | Nucleoplasm; Additional: Vesicles | Reliability: Uncertain |

**IF Image Status**: HPA did not detect reliable IF image signal. Nuclear evidence based on HPA subcellular annotation, UniProt, and GO-CC terms.

**Manual Review Assessment**: UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Uncertain); GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPANXB1 is 103 amino acids in length (~11.8 kDa). Acceptable size (103 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 9 |
| PubMed broad count | 19 |
| Alias context | Aliases observed but not used for scoring: SPANXB, SPANXB2, SPANXF1 |
| Novelty category | <=20 -> 10 |

**Key Research Context**: No functional annotation available. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 29453317 | Histone H3.3K27M Mobilizes Multiple Cancer/Testis (CT) Antigens in Pediatric Glioma. | Molecular cancer research : MCR |
| 35096583 | Screening and Identification of Novel Potential Biomarkers for Breast Cancer Brain Metastases. | Frontiers in oncology |
| 37057240 | Identification of Cancer/Testis Antigens Related to Gastric Cancer Prognosis Based on Co-Expression Network and Integrat | Advanced biomedical research |
| 33200223 | Evaluating the biological functions of the prognostic genes identified by the Pathology Atlas in bladder cancer. | Oncology reports |
| 31406142 | Cancer Testis Antigen Promotes Triple Negative Breast Cancer Metastasis and is Traceable in the Circulating Extracellula | Scientific reports |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 68.0 |
| High confidence residues (pLDDT > 90) | 15.5% |
| Confident residues (pLDDT 70-90) | 32.0% |
| Medium confidence (pLDDT 50-70) | 31.1% |
| Low confidence (pLDDT < 50) | 21.4% |
| Ordered region (pLDDT > 70) | 47.5% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=68.0), 47.5% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR010007 |  |
| Pfam | PF07458 |  |

**Domain Analysis**:  The protein contains 1 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 14 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SPANXA1 | 0.999 | 0.000 | 0.0 | 0.066 |
| SPANXC | 0.787 | 0.000 | 0.0 | 0.061 |
| LGALS4 | 0.650 | 0.046 | 0.0 | 0.649 |
| SRY | 0.571 | 0.000 | 0.0 | 0.571 |
| GAGE2E | 0.570 | 0.000 | 0.0 | 0.570 |
| ARID4B | 0.468 | 0.462 | 0.0 | 0.052 |
| XAGE2 | 0.455 | 0.000 | 0.0 | 0.447 |
| GAGE2A | 0.446 | 0.000 | 0.0 | 0.446 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| UBL5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNX32 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARID4B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PAPSS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| BPGM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| HMGCS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

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
2. Ideal protein size (103 aa) for experimental characterization
3. High novelty (PubMed count ~9)
4. AlphaFold prediction available (pLDDT 68.0)
5. Some domain annotations present (3 domains)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS25
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXB1
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000227234-SPANXB1/subcellular
- Data harvested: 2026-06-04 03:27:05
