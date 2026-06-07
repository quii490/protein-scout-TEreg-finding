---
type: protein-evaluation
gene: "SDCBP2"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SDCBP2 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SDCBP2 / SITAC18 |
| Protein Name | Syntenin-2 |
| Protein Size | ~292 aa (31.6 kDa) |
| UniProt ID | Q9H190 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SDCBP2.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | Strongly nuclear -- primary localization confirmed by multiple databases |
| Protein Size | 10/10 | x1 | **10** | 292 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~13 |
| 3D Structure | 4/10 | x3 | **12** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 3, Pfam: 1 |
| PPI Network | 7/10 | x3 | **21** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.75** | |
| **Raw Total** | | | **131.8/180** | |
| **Normalized Total** | | | **73.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Nucleus, nucleolus | ECO:0000269, ECO:0000269 |
| UniProt | Nucleus, nucleoplasm | ECO:0000269 |
| UniProt | Cell membrane | ECO:0000269 |
| UniProt | Nucleus speckle | ECO:0000269 |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | cytosol | IDA:HPA |
| GO-CC | extracellular exosome | HDA:UniProtKB |
| GO-CC | Golgi apparatus | IDA:HPA |
| GO-CC | nuclear speck | IDA:UniProtKB |
| GO-CC | nucleolus | IDA:UniProtKB |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | plasma membrane | IDA:UniProtKB |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Golgi apparatus | IF-based (Supported) |
| HPA (IF) | Cytosol | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 9/10.** Strongly nuclear -- primary localization confirmed by multiple databases.

- UniProt annotates: Nucleus, nucleolus, Nucleus, nucleoplasm, Nucleus speckle

- HPA IF detects: Nucleoplasm (Reliability: Supported)

- GO-CC annotations include: nuclear speck, nucleolus, nucleoplasm

**Nuclear localization score: 9/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

292 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 13 |
| Broad query count | 24 |
| Alias note | Aliases observed but not used for scoring: SITAC18 |
| Novelty score | 9/10 |

PubMed strict count ~13 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:36209503** (2022 Nov) -- SDCBP-AS1 destabilizes β-catenin by regulating ubiquitination and SUMOylation of hnRNP K to suppress gastric tumorigenic (Cancer communications (London, England))
- **PMID:32636717** (2020) -- The plasma peptides of sepsis. (Clinical proteomics)
- **PMID:37714445** (2023 Dec) -- Targeting SDCBP2 in acute myeloid leukemia. (Cellular signalling)
- **PMID:41409290** (2025) -- SDCBP2 promotes tumor progression and is a novel ferroptosis-related prognostic biomarker in lung adenocarcinoma. (Frontiers in immunology)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 81.2 |
| PDB Entries | 0 |
| AF pLDDT >90% | 55.8% |
| AF pLDDT <50% | 14.7% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 81.2. pLDDT distribution: >90: 55.8%, 70-90: 21.6%, 50-70: 7.9%, <50: 14.7%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR051230 | IPR051230 |
| InterPro | IPR001478 | IPR001478 |
| InterPro | IPR036034 | IPR036034 |
| Pfam | PF00595 | PF00595 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: Binds phosphatidylinositol 4,5-bisphosphate (PIP2). May play a role in the organization of nuclear PIP2, cell division and cell survival (PubMed:15961997)

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| CD63 | Combined: 0.992 | EXP: 0.000 | DB: 0 |
| SDC1 | Combined: 0.923 | EXP: 0.000 | DB: 0 |
| PDCD6IP | Combined: 0.798 | EXP: 0.143 | DB: 0 |
| CD9 | Combined: 0.786 | EXP: 0.000 | DB: 0 |
| CD81 | Combined: 0.780 | EXP: 0.000 | DB: 0 |
| TSG101 | Combined: 0.777 | EXP: 0.000 | DB: 0 |
| B4E171_HUMAN | Combined: 0.721 | EXP: 0.000 | DB: 0 |
| CD6 | Combined: 0.720 | EXP: 0.052 | DB: 0 |

Top STRING interaction partners:
- CD63 (combined score: 0.99, experimental: 0.00)
- SDC1 (combined score: 0.92, experimental: 0.00)
- PDCD6IP (combined score: 0.80, experimental: 0.14)
- CD9 (combined score: 0.79, experimental: 0.00)
- CD81 (combined score: 0.78, experimental: 0.00)

High-confidence interactors (score >= 0.7): 9. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 7/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Binds phosphatidylinositol 4,5-bisphosphate (PIP2). May play a role in the organization of nuclear PIP2, cell division a | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.75/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 131.8/180 (73.2/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Strongly nuclear -- primary localization confirmed by multiple databases
2. PubMed count: 13 articles 
3. Protein size: 292 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 9 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 9 > 3, PubMed 13 <= 100). Total score: 131.8/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H190
- HPA: https://www.proteinatlas.org/ENSG00000125775-SDCBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SDCBP2%22
- STRING: https://string-db.org/ (search SDCBP2)
- IntAct: https://www.ebi.ac.uk/intact/ (search SDCBP2)
- Harvest packet: SDCBP2.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H190 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 108..187; /note="PDZ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 192..267; /note="PDZ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR051230;IPR001478;IPR036034; |
| Pfam | PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125775-SDCBP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TIFA | Intact, Biogrid | true |
| ADAP1 | Intact | false |
| AKAP17A | Intact | false |
| AP1M1 | Intact | false |
| ARF4 | Intact | false |
| C1orf35 | Intact | false |
| CHCHD1 | Intact | false |
| CRCT1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
