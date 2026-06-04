---
type: protein-evaluation
gene: "SPANXA2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPANXA2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPANXA2 / SPANXA |
| Protein Name | Sperm protein associated with the nucleus on the X chromosome A |
| Protein Size | 97 aa, ~11.0 kDa |
| UniProt ID | Q9NS26 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus |
| Protein Size | 5/10 | x1 | **5** | 97 aa, ~11.0 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=3 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=65.6; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR010007; Pfam: PF07458 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 4 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **128.0/180** | |
| **Normalized Total** | | | **71.1/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | Experimental |
| UniProt | Nucleus | Experimental |
| GO-CC | nucleus | HDA:UniProtKB |
| HPA | Nucleoplasm; Additional: Vesicles | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Nucleus; HPA: Nucleoplasm; (Reliability: Approved); GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPANXA2 is 97 amino acids in length (~11.0 kDa). Small/large (97 aa), presents moderate experimental challenges. Score 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 3 |
| PubMed broad count | 8 |
| Alias context | Aliases observed but not used for scoring: SPANXA |
| Novelty category | <=20 -> 10 |

**Key Research Context**: No functional annotation available. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 34646842 | LncRNA SPANXA2-OT1 Participates in the Occurrence and Development of EMT in Calcium Oxalate Crystal-Induced Kidney Injur | Frontiers in medicine |
| 17012309 | Hominoid-specific SPANXA/D genes demonstrate differential expression in individuals and protein localization to a distin | Molecular human reproduction |
| 17373721 | Mutational analysis of SPANX genes in families with X-linked prostate cancer. | The Prostate |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 65.6 |
| High confidence residues (pLDDT > 90) | 2.1% |
| Confident residues (pLDDT 70-90) | 40.2% |
| Medium confidence (pLDDT 50-70) | 49.5% |
| Low confidence (pLDDT < 50) | 8.2% |
| Ordered region (pLDDT > 70) | 42.3% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=65.6), 42.3% ordered. Structure usable. Score 6/10.

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
| IntAct | 4 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SPANXA1 | 0.999 | 0.000 | 0.0 | 0.000 |
| SPANXN4 | 0.917 | 0.000 | 0.0 | 0.917 |
| AKAP4 | 0.745 | 0.000 | 0.0 | 0.745 |
| TSN | 0.711 | 0.000 | 0.0 | 0.711 |
| SRY | 0.681 | 0.000 | 0.0 | 0.681 |
| LGALS4 | 0.670 | 0.046 | 0.0 | 0.669 |
| CSAG3 | 0.634 | 0.292 | 0.0 | 0.505 |
| CT45A1 | 0.617 | 0.000 | 0.0 | 0.608 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| SPANXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EML2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SETBP1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
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
3. High novelty (PubMed count ~3)
4. AlphaFold prediction available (pLDDT 65.6)
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
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS26
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS26
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXA2
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000203926-SPANXA2/subcellular
- Data harvested: 2026-06-04 03:26:42
