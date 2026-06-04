---
type: protein-evaluation
gene: "SCRN2"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SCRN2 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCRN2 / none |
| Protein Name | Secernin-2 |
| Protein Size | ~425 aa (46.6 kDa) |
| UniProt ID | Q96FV2 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SCRN2.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 10/10 | x1 | **10** | 425 aa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict ~6 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 0, AF: Yes |
| Regulatory Domains | 2/10 | x2 | **4** | InterPro: 1, Pfam: 1 |
| PPI Network | 6/10 | x3 | **18** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.25** | |
| **Raw Total** | | | **113.2/180** | |
| **Normalized Total** | | | **62.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| GO-CC | extracellular exosome | HDA:UniProtKB |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Golgi apparatus | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Supported)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

425 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 6 |
| Broad query count | 8 |
| Alias note |  |
| Novelty score | 10/10 |

PubMed strict count ~6 articles. Very high novelty -- minimal prior research. Score: 10/10.

**Key Publications**:

- **PMID:35235319** (2022 Mar 30) -- Discovery of Potent and Selective Inhibitors against Protein-Derived Electrophilic Cofactors. (Journal of the American Chemical Society)
- **PMID:39836524** (2025 Mar) -- Secernin-2 Stabilizes Histone Methyltransferase KMT2C to Suppress Progression and Confer Therapeutic Sensitivity to PARP (Advanced science (Weinheim, Baden-Wurttemberg, Germany))
- **PMID:37020999** (2023) -- Using multi-tissue transcriptome-wide association study to identify candidate susceptibility genes for respiratory infec (Frontiers in genetics)
- **PMID:37901794** (2023) -- Clinical effects of novel susceptibility genes for beta-amyloid: a gene-based association study in the Korean population (Frontiers in aging neuroscience)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 94.4 |
| PDB Entries | 0 |
| AF pLDDT >90% | 88.7% |
| AF pLDDT <50% | 2.1% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 94.4. pLDDT distribution: >90: 88.7%, 70-90: 8.7%, 50-70: 0.5%, <50: 2.1%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR005322 | IPR005322 |
| Pfam | PF03577 | PF03577 |

InterPro domains: 1 | Pfam domains: 1. Total catalogued domains: 2.

**Domain score: 2/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| ARPC3 | Combined: 0.875 | EXP: 0.779 | DB: 0 |
| ARPC4 | Combined: 0.875 | EXP: 0.778 | DB: 0 |
| NCKIPSD | Combined: 0.779 | EXP: 0.761 | DB: 0 |
| ARPC5L | Combined: 0.689 | EXP: 0.575 | DB: 0 |
| ARPC5 | Combined: 0.687 | EXP: 0.575 | DB: 0 |
| ARPC1A | Combined: 0.606 | EXP: 0.505 | DB: 0 |
| ARPC1B | Combined: 0.604 | EXP: 0.505 | DB: 0 |
| ENSP00000491073 | Combined: 0.602 | EXP: 0.505 | DB: 0 |

Top STRING interaction partners:
- ARPC3 (combined score: 0.88, experimental: 0.78)
- ARPC4 (combined score: 0.88, experimental: 0.78)
- NCKIPSD (combined score: 0.78, experimental: 0.76)
- ARPC5L (combined score: 0.69, experimental: 0.57)
- ARPC5 (combined score: 0.69, experimental: 0.57)

High-confidence interactors (score >= 0.7): 3. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 6/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | No functional annotation | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.25/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 113.2/180 (62.9/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 6 articles 
3. Protein size: 425 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 3 high-confidence
6. Domain architecture: 1 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 6 <= 100). Total score: 113.2/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96FV2
- HPA: https://www.proteinatlas.org/ENSG00000141295-SCRN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCRN2%22
- STRING: https://string-db.org/ (search SCRN2)
- IntAct: https://www.ebi.ac.uk/intact/ (search SCRN2)
- Harvest packet: SCRN2.json
