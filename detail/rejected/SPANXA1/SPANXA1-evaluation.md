---
type: protein-evaluation
gene: "SPANXA1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPANXA1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPANXA1 / SPANXA |
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
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=12 (<=20 -> 10) |
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

SPANXA1 is 97 amino acids in length (~11.0 kDa). Small/large (97 aa), presents moderate experimental challenges. Score 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 12 |
| PubMed broad count | 35 |
| Alias context | Aliases observed but not used for scoring: SPANXA |
| Novelty category | <=20 -> 10 |

**Key Research Context**: No functional annotation available. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 33175201 | Hypomethylated SPANXA1/A2 promotes the metastasis of head and neck squamous cell carcinoma. | Medical oncology (Northwood, London, England) |
| 29453317 | Histone H3.3K27M Mobilizes Multiple Cancer/Testis (CT) Antigens in Pediatric Glioma. | Molecular cancer research : MCR |
| 31289536 | Iodine promotes thyroid cancer development via SPANXA1 through the PI3K/AKT signalling pathway. | Oncology letters |
| 22737227 | Genome-wide profiling of pluripotent cells reveals a unique molecular signature of human embryonic germ cells. | PloS one |
| 33290900 | Biological features of tissue and bone sarcomas investigated using an in vitro model of clonal selection. | Pathology, research and practice |


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
| SPANXB1 | 0.999 | 0.000 | 0.0 | 0.066 |
| SPANXA2 | 0.999 | 0.000 | 0.0 | 0.000 |
| SPANXC | 0.999 | 0.000 | 0.0 | 0.055 |
| SPANXN4 | 0.846 | 0.000 | 0.0 | 0.846 |
| AKAP4 | 0.754 | 0.000 | 0.0 | 0.753 |
| TSN | 0.718 | 0.000 | 0.0 | 0.718 |
| SRY | 0.669 | 0.000 | 0.0 | 0.668 |
| LGALS4 | 0.640 | 0.046 | 0.0 | 0.639 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| SPANXA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
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
3. High novelty (PubMed count ~12)
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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXA1
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000198021-SPANXA1/subcellular
- Data harvested: 2026-06-04 03:26:18
