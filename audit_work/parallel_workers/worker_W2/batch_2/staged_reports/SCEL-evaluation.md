---
type: protein-evaluation
gene: "SCEL"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SCEL -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCEL / none |
| Protein Name | Sciellin |
| Protein Size | ~688 aa (77.6 kDa) |
| UniProt ID | O95171 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SCEL.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 10/10 | x1 | **10** | 688 aa |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict ~42 |
| 3D Structure | 1/10 | x3 | **3** | PDB: 0, AF: Yes |
| Regulatory Domains | 2/10 | x2 | **4** | InterPro: 2, Pfam: 0 |
| PPI Network | 4/10 | x3 | **12** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.25** | |
| **Raw Total** | | | **83.2/180** | |
| **Normalized Total** | | | **46.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | not specified |
| UniProt | Membrane | not specified |
| GO-CC | cornified envelope | TAS:UniProtKB |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | extracellular exosome | HDA:UniProtKB |
| GO-CC | perinuclear region of cytoplasm | IDA:BHF-UCL |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Plasma membrane | IF-based (Supported) |
| HPA (IF) | Cytosol | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nucleoplasm (Reliability: Supported)

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

688 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 42 |
| Broad query count | 74 |
| Alias note |  |
| Novelty score | 6/10 |

PubMed strict count ~42 articles. Moderate-to-established field, growing literature. Score: 6/10.

**Key Publications**:

- **PMID:32726565** (2020 Dec 15) -- A Single-Cell Atlas of the Human Healthy Airways. (American journal of respiratory and critical care medicine)
- **PMID:40341648** (2025 May 8) -- Sciellin inhibits senescence and promotes pancreatic cancer progress by activating the notch signaling pathway. (Scientific reports)
- **PMID:37733753** (2023 Nov) -- CBX8 promotes lung adenocarcinoma growth and metastasis through transcriptional repression of CDKN2C and SCEL. (Journal of cellular physiology)
- **PMID:37060824** (2023 May) -- Clinical significance and diagnostic value of QPCT, SCEL and TNFRSF12A in papillary thyroid cancer. (Pathology, research and practice)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 45.2 |
| PDB Entries | 0 |
| AF pLDDT >90% | 2.2% |
| AF pLDDT <50% | 78.8% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 45.2. pLDDT distribution: >90: 2.2%, 70-90: 8.4%, 50-70: 10.6%, <50: 78.8%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR052621 | IPR052621 |
| InterPro | IPR001781 | IPR001781 |

InterPro domains: 2 | Pfam domains: 0. Total catalogued domains: 2.

Functional annotation: May function in the assembly or regulation of proteins in the cornified envelope. The LIM domain may be involved in homotypic or heterotypic associations and may function to localize sciellin to the cornified envelope

**Domain score: 2/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SULF1 | Combined: 0.752 | EXP: 0.000 | DB: 0 |
| SYNPO | Combined: 0.720 | EXP: 0.091 | DB: 0 |
| YIPF3 | Combined: 0.711 | EXP: 0.000 | DB: 0 |
| CYP26A1 | Combined: 0.700 | EXP: 0.046 | DB: 0 |
| ACTN4 | Combined: 0.636 | EXP: 0.000 | DB: 0 |
| NPHS1 | Combined: 0.601 | EXP: 0.000 | DB: 0 |
| SPRR2B | Combined: 0.573 | EXP: 0.000 | DB: 0 |
| LCE3D | Combined: 0.563 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- SULF1 (combined score: 0.75, experimental: 0.00)
- SYNPO (combined score: 0.72, experimental: 0.09)
- YIPF3 (combined score: 0.71, experimental: 0.00)
- CYP26A1 (combined score: 0.70, experimental: 0.05)
- ACTN4 (combined score: 0.64, experimental: 0.00)

High-confidence interactors (score >= 0.7): 4. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 4/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | May function in the assembly or regulation of proteins in the cornified envelope. The LIM domain may be involved in homo | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.25/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (WEAK). Total score 83.2/180 (46.2/100). The protein passes the hard filters but scores are modest. Consider as a backup candidate.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 42 articles 
3. Protein size: 688 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 4 high-confidence
6. Domain architecture: 2 InterPro + 0 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 42 <= 100). Total score: 83.2/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O95171
- HPA: https://www.proteinatlas.org/ENSG00000136155-SCEL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCEL%22
- STRING: https://string-db.org/ (search SCEL)
- IntAct: https://www.ebi.ac.uk/intact/ (search SCEL)
- Harvest packet: SCEL.json
