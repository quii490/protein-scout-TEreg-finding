---
type: protein-evaluation
gene: "SEPHS2"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SEPHS2 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEPHS2 / SPS2 |
| Protein Name | Selenide, water dikinase 2 |
| Protein Size | ~448 aa (47.3 kDa) |
| UniProt ID | Q99611 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SEPHS2.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 10/10 | x1 | **10** | 448 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~40 |
| 3D Structure | 0/10 | x3 | **0** | PDB: 0, AF: No |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 5, Pfam: 2 |
| PPI Network | 9/10 | x3 | **27** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **104.0/180** | |
| **Normalized Total** | | | **57.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | cytosol | TAS:Reactome |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

448 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 40 |
| Broad query count | 61 |
| Alias note | Aliases observed but not used for scoring: SPS2 |
| Novelty score | 8/10 |

PubMed strict count ~40 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:32694795** (2020 Jul) -- Selenium detoxification is required for cancer-cell survival. (Nature metabolism)
- **PMID:27645994** (2016 Nov 11) -- Selenoprotein Gene Nomenclature. (The Journal of biological chemistry)
- **PMID:40750759** (2025 Aug 2) -- METTL5 regulates SEPHS2-mediated selenoprotein synthesis to promote multiple myeloma survival and progression. (Cell death & disease)
- **PMID:39728918** (2024 Dec 27) -- Target protein identification in live cells and organisms with a non-diffusive proximity tagging system. (eLife)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Not available |
| Mean pLDDT | N/A |
| PDB Entries | 0 |
| AF pLDDT >90% | N/A% |
| AF pLDDT <50% | N/A% |

**Structure Assessment**: No experimental PDB structures available. No AlphaFold prediction available.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR010918 | IPR010918 |
| InterPro | IPR036676 | IPR036676 |
| InterPro | IPR016188 | IPR016188 |
| InterPro | IPR036921 | IPR036921 |
| InterPro | IPR004536 | IPR004536 |
| Pfam | PF00586 | PF00586 |
| Pfam | PF02769 | PF02769 |

InterPro domains: 5 | Pfam domains: 2. Total catalogued domains: 7.

Functional annotation: Selenophosphate synthase that generates the selenium donor for selenocysteine biosynthesis by catalyzing formation of selenophosphate from selenide and ATP

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SEPSECS | Combined: 0.993 | EXP: 0.000 | DB: 1 |
| SCLY | Combined: 0.983 | EXP: 0.000 | DB: 1 |
| TXNRD3 | Combined: 0.979 | EXP: 0.000 | DB: 1 |
| TXNRD1 | Combined: 0.973 | EXP: 0.000 | DB: 1 |
| TXNRD2 | Combined: 0.971 | EXP: 0.000 | DB: 1 |
| SEPHS1 | Combined: 0.924 | EXP: 0.226 | DB: 1 |
| PSTK | Combined: 0.915 | EXP: 0.000 | DB: 0 |
| SELENOT | Combined: 0.877 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- SEPSECS (combined score: 0.99, experimental: 0.00)
- SCLY (combined score: 0.98, experimental: 0.00)
- TXNRD3 (combined score: 0.98, experimental: 0.00)
- TXNRD1 (combined score: 0.97, experimental: 0.00)
- TXNRD2 (combined score: 0.97, experimental: 0.00)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 11.

**PPI score: 9/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | Selenophosphate synthase that generates the selenium donor for selenocysteine biosynthesis by catalyzing formation of se | -- |
| Structure | AF + PDB | Limited | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 104.0/180 (57.8/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 40 articles 
3. Protein size: 448 aa -- ideal
4. Structure: No structural data available
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 5 InterPro + 2 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 40 <= 100). Total score: 104.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q99611
- HPA: https://www.proteinatlas.org/ENSG00000179918-SEPHS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEPHS2%22
- STRING: https://string-db.org/ (search SEPHS2)
- IntAct: https://www.ebi.ac.uk/intact/ (search SEPHS2)
- Harvest packet: SEPHS2.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99611 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010918;IPR036676;IPR016188;IPR036921;IPR004536; |
| Pfam | PF00586;PF02769; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179918-SEPHS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PRDX6 | Biogrid | false |
| SEPHS1 | Intact, Biogrid, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
