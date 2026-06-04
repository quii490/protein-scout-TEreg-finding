---
type: protein-evaluation
gene: "SPANXD"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPANXD -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPANXD / SPANXE |
| Protein Name | Sperm protein associated with the nucleus on the X chromosome D |
| Protein Size | 97 aa, ~11.0 kDa |
| UniProt ID | Q9BXN6 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus |
| Protein Size | 5/10 | x1 | **5** | 97 aa, ~11.0 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=4 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=68.9; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR010007; Pfam: PF07458 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 3 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **128.0/180** | |
| **Normalized Total** | | | **71.1/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | By similarity |
| UniProt | Nucleus | By similarity |
| GO-CC | nucleus | HDA:UniProtKB |
| HPA | Nucleoplasm; Additional: Vesicles | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPANXD is 97 amino acids in length (~11.0 kDa). Small/large (97 aa), presents moderate experimental challenges. Score 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| Alias context | Aliases observed but not used for scoring: SPANXE |
| Novelty category | <=20 -> 10 |

**Key Research Context**: No functional annotation available. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 26625006 | Hypermethylation of genes in testicular embryonal carcinomas. | British journal of cancer |
| 17012309 | Hominoid-specific SPANXA/D genes demonstrate differential expression in individuals and protein localization to a distin | Molecular human reproduction |
| 41129177 | Multiomic Selection of Cancer-Testis Antigens as Precision Immuno-oncologic Targets in Head and Neck Cancer. | JAMA otolaryngology-- head & neck surgery |
| 17373721 | Mutational analysis of SPANX genes in families with X-linked prostate cancer. | The Prostate |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 68.9 |
| High confidence residues (pLDDT > 90) | 6.2% |
| Confident residues (pLDDT 70-90) | 39.2% |
| Medium confidence (pLDDT 50-70) | 44.3% |
| Low confidence (pLDDT < 50) | 10.3% |
| Ordered region (pLDDT > 70) | 45.4% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=68.9), 45.4% ordered. Structure usable. Score 6/10.

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
| IntAct | 3 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SPANXN4 | 0.655 | 0.000 | 0.0 | 0.655 |
| SRY | 0.652 | 0.000 | 0.0 | 0.652 |
| GAGE2A | 0.603 | 0.000 | 0.0 | 0.573 |
| GAGE2E | 0.602 | 0.000 | 0.0 | 0.573 |
| SPANXN3 | 0.583 | 0.000 | 0.0 | 0.583 |
| XAGE2 | 0.570 | 0.000 | 0.0 | 0.570 |
| GAGE1 | 0.555 | 0.000 | 0.0 | 0.540 |
| LGALS4 | 0.551 | 0.046 | 0.0 | 0.549 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| FLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SETBP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPANXB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

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

**Recommendation Level**: Recommended (Score: 71.1/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Workable protein size (97 aa)
3. High novelty (PubMed count ~4)
4. AlphaFold prediction available (pLDDT 68.9)
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

**FINAL DECISION**: NOT REJECTED. The protein scores 71.1/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXN6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXN6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXD
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000196406-SPANXD/subcellular
- Data harvested: 2026-06-04 03:27:28
