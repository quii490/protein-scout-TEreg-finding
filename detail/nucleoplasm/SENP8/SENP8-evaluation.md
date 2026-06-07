---
type: protein-evaluation
gene: "SENP8"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SENP8 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SENP8 / DEN1, NEDP1, PRSC2 |
| Protein Name | Sentrin-specific protease 8 |
| Protein Size | ~212 aa (24.1 kDa) |
| UniProt ID | Q96LD8 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SENP8.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 7/10 | x1 | **7** | 212 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~27 |
| 3D Structure | 9/10 | x3 | **27** | PDB: 3, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 3, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **127.0/180** | |
| **Normalized Total** | | | **70.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| GO-CC | cytosol | TAS:Reactome |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Vesicles | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

212 aa -- moderately sized, acceptable for most experimental approaches. Score: 7/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 27 |
| Broad query count | 52 |
| Alias note | Aliases observed but not used for scoring: DEN1, NEDP1, PRSC2 |
| Novelty score | 8/10 |

PubMed strict count ~27 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:36626230** (2023 Feb 15) -- SHP2 deneddylation mediates tumor immunosuppression in colon cancer via the CD47/SIRPα axis. (The Journal of clinical investigation)
- **PMID:36847487** (2023 May) -- Deneddylating enzyme SENP8 regulates neuronal development. (Journal of neurochemistry)
- **PMID:38314144** (2024 Mar) -- Etoposide-induced SENP8 confers a feed-back drug resistance on acute lymphoblastic leukemia cells. (Biochemistry and biophysics reports)
- **PMID:26403403** (2015 Jul-Sep) -- PAPILLARY THYROID CANCER IS CHARACTERIZED BY ALTERED EXPRESSION OF GENES INVOLVED IN THE SUMOYLATION PROCESS. (Journal of biological regulators and homeostatic agents)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 96.7 |
| PDB Entries | 3 |
| AF pLDDT >90% | 95.3% |
| AF pLDDT <50% | 0.0% |

**Structure Assessment**: PDB entries available (3 total): 1XT9 (X-ray, 2.20 A), 2BKQ (X-ray, 2.00 A), 2BKR (X-ray, 1.90 A) AlphaFold prediction available (v6) with mean pLDDT: 96.7. pLDDT distribution: >90: 95.3%, 70-90: 4.7%, 50-70: 0.0%, <50: 0.0%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR044613 | IPR044613 |
| InterPro | IPR038765 | IPR038765 |
| InterPro | IPR003653 | IPR003653 |
| Pfam | PF02902 | PF02902 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: Protease that catalyzes two essential functions in the NEDD8 pathway: processing of full-length NEDD8 to its mature form and deconjugation of NEDD8 from targeted proteins such as cullins or p53

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| NEDD8 | Combined: 0.999 | EXP: 0.986 | DB: 1 |
| ACO2 | Combined: 0.915 | EXP: 0.000 | DB: 1 |
| ACO1 | Combined: 0.914 | EXP: 0.000 | DB: 1 |
| IREB2 | Combined: 0.914 | EXP: 0.000 | DB: 1 |
| CUL1 | Combined: 0.900 | EXP: 0.644 | DB: 0 |
| ACMSD | Combined: 0.896 | EXP: 0.000 | DB: 1 |
| UBA3 | Combined: 0.892 | EXP: 0.000 | DB: 0 |
| SENP3 | Combined: 0.890 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- NEDD8 (combined score: 1.00, experimental: 0.99)
- ACO2 (combined score: 0.92, experimental: 0.00)
- ACO1 (combined score: 0.91, experimental: 0.00)
- IREB2 (combined score: 0.91, experimental: 0.00)
- CUL1 (combined score: 0.90, experimental: 0.64)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 6.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | Protease that catalyzes two essential functions in the NEDD8 pathway: processing of full-length NEDD8 to its mature form | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 127.0/180 (70.6/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 27 articles 
3. Protein size: 212 aa -- acceptable
4. Structure: Experimental PDB available (3 entries)
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 27 <= 100). Total score: 127.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96LD8
- HPA: https://www.proteinatlas.org/ENSG00000166192-SENP8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SENP8%22
- STRING: https://string-db.org/ (search SENP8)
- IntAct: https://www.ebi.ac.uk/intact/ (search SENP8)
- Harvest packet: SENP8.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96LD8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR044613;IPR038765;IPR003653; |
| Pfam | PF02902; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166192-SENP8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKIP1 | Biogrid | false |
| CHN2 | Intact | false |
| COPS2 | Biogrid | false |
| CUL1 | Biogrid | false |
| CUL4A | Biogrid | false |
| NEDD8 | Biogrid | false |
| NSF | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
