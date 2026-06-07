---
type: protein-evaluation
gene: "SERPINB10"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SERPINB10 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERPINB10 / PI10 |
| Protein Name | Serpin B10 |
| Protein Size | ~397 aa (45.4 kDa) |
| UniProt ID | P48595 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SERPINB10.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Primarily nuclear with experimental support |
| Protein Size | 10/10 | x1 | **10** | 397 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~18 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 0, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 6, Pfam: 1 |
| PPI Network | 3/10 | x3 | **9** | STRING: 9 interactions |
| Cross-Validation Bonus | -- | -- | **+0.25** | |
| **Raw Total** | | | **121.2/180** | |
| **Normalized Total** | | | **67.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus | not specified |
| UniProt | Cytoplasm | not specified |
| GO-CC | cytosol | IDA:HPA |
| GO-CC | extracellular space | IBA:GO_Central |
| GO-CC | ficolin-1-rich granule membrane | TAS:Reactome |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | plasma membrane | TAS:Reactome |
| GO-CC | secretory granule membrane | TAS:Reactome |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Cytosol | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 8/10.** Primarily nuclear with experimental support.

- UniProt annotates: Nucleus

- HPA IF detects: Nucleoplasm (Reliability: Supported)

- GO-CC annotations include: nucleoplasm

**Nuclear localization score: 8/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

397 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 18 |
| Broad query count | 35 |
| Alias note | Aliases observed but not used for scoring: PI10 |
| Novelty score | 9/10 |

PubMed strict count ~18 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:38686450** (2024 Jul) -- The effects of inhaled corticosteroids on healthy airways. (Allergy)
- **PMID:40349036** (2025 May 10) -- SERPINB10 promotes macrophage M2 polarization and airway inflammation in asthma. (Respiratory research)
- **PMID:30382768** (2019 Jan 1) -- Epithelial SERPINB10, a novel marker of airway eosinophilia in asthma, contributes to allergic airway inflammation. (American journal of physiology. Lung cellular and molecular physiology)
- **PMID:35526531** (2022) -- Increased SERPINB10 Expression in Induced Sputum Was Associated with Airway Type 2 Inflammation in Asthma. (International archives of allergy and immunology)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 88.7 |
| PDB Entries | 0 |
| AF pLDDT >90% | 74.1% |
| AF pLDDT <50% | 8.1% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 88.7. pLDDT distribution: >90: 74.1%, 70-90: 15.1%, 50-70: 2.8%, <50: 8.1%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR023795 | IPR023795 |
| InterPro | IPR023796 | IPR023796 |
| InterPro | IPR000215 | IPR000215 |
| InterPro | IPR036186 | IPR036186 |
| InterPro | IPR042178 | IPR042178 |
| Pfam | PF00079 | PF00079 |

InterPro domains: 6 | Pfam domains: 1. Total catalogued domains: 7.

Functional annotation: Protease inhibitor that may play a role in the regulation of protease activities during hematopoiesis and apoptosis induced by TNF. May regulate protease activities in the cytoplasm and in the nucleus

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| CTSG | Combined: 0.924 | EXP: 0.045 | DB: 1 |
| LYG2 | Combined: 0.521 | EXP: 0.051 | DB: 0 |
| BPIFB1 | Combined: 0.472 | EXP: 0.000 | DB: 0 |
| SERPINB4 | Combined: 0.453 | EXP: 0.000 | DB: 0 |
| CRISP3 | Combined: 0.442 | EXP: 0.000 | DB: 0 |
| SLC14A1 | Combined: 0.406 | EXP: 0.000 | DB: 0 |
| AGO2 | Combined: 0.404 | EXP: 0.000 | DB: 0 |
| IVNS1ABP | Combined: 0.402 | EXP: 0.045 | DB: 0 |

Top STRING interaction partners:
- CTSG (combined score: 0.92, experimental: 0.04)
- LYG2 (combined score: 0.52, experimental: 0.05)
- BPIFB1 (combined score: 0.47, experimental: 0.00)
- SERPINB4 (combined score: 0.45, experimental: 0.00)
- CRISP3 (combined score: 0.44, experimental: 0.00)

High-confidence interactors (score >= 0.7): 1. Total STRING interactions: 9. IntAct entries: 2.

**PPI score: 3/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Protease inhibitor that may play a role in the regulation of protease activities during hematopoiesis and apoptosis indu | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.25/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 121.2/180 (67.4/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Primarily nuclear with experimental support
2. PubMed count: 18 articles 
3. Protein size: 397 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 9 STRING interactions, 1 high-confidence
6. Domain architecture: 6 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 8 > 3, PubMed 18 <= 100). Total score: 121.2/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P48595
- HPA: https://www.proteinatlas.org/ENSG00000242550-SERPINB10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERPINB10%22
- STRING: https://string-db.org/ (search SERPINB10)
- IntAct: https://www.ebi.ac.uk/intact/ (search SERPINB10)
- Harvest packet: SERPINB10.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P48595 |
| SMART | SM00093; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023795;IPR023796;IPR000215;IPR036186;IPR042178;IPR042185; |
| Pfam | PF00079; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000242550-SERPINB10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KLK10 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
