---
type: protein-evaluation
gene: "SCHIP1"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SCHIP1 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCHIP1 / none |
| Protein Name | Schwannomin-interacting protein 1 |
| Protein Size | ~487 aa (53.5 kDa) |
| UniProt ID | P0DPB3 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SCHIP1.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 10/10 | x1 | **10** | 487 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~26 |
| 3D Structure | 2/10 | x3 | **6** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 2, Pfam: 1 |
| PPI Network | 7/10 | x3 | **21** | STRING: 13 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **108.0/180** | |
| **Normalized Total** | | | **60.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| GO-CC | cell junction | IBA:GO_Central |
| GO-CC | cytoplasm | IEA:UniProtKB-SubCell |
| GO-CC | plasma membrane | IBA:GO_Central |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Nuclear bodies | IF-based (Approved) |
| HPA (IF) | Plasma membrane | IF-based (Approved) |
| HPA (IF) | Cell Junctions | IF-based (Approved) |
| HPA (IF) | Cytosol | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nucleoplasm, Nuclear bodies (Reliability: Approved)

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

487 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 26 |
| Broad query count | 42 |
| Alias note |  |
| Novelty score | 8/10 |

PubMed strict count ~26 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:26954546** (2016 Mar 7) -- Drosophila Schip1 Links Expanded and Tao-1 to Regulate Hippo Signaling. (Developmental cell)
- **PMID:28787085** (2018 Feb) -- Homozygous nonsense mutation in SCHIP1/IQCJ-SCHIP1 causes a neurodevelopmental brain malformation syndrome. (Clinical genetics)
- **PMID:17045569** (2006 Dec 1) -- IQCJ-SCHIP1, a novel fusion transcript encoding a calmodulin-binding IQ motif protein. (Biochemical and biophysical research communications)
- **PMID:25807495** (2015) -- Schip1 is a novel podocyte foot process protein that mediates actin cytoskeleton rearrangements and forms a complex with (PloS one)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 60.3 |
| PDB Entries | 0 |
| AF pLDDT >90% | 15.0% |
| AF pLDDT <50% | 47.6% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 60.3. pLDDT distribution: >90: 15.0%, 70-90: 18.3%, 50-70: 19.1%, <50: 47.6%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR039045 | IPR039045 |
| InterPro | IPR015649 | IPR015649 |
| Pfam | PF10148 | PF10148 |

InterPro domains: 2 | Pfam domains: 1. Total catalogued domains: 3.

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| IQCJ | Combined: 0.985 | EXP: 0.000 | DB: 0 |
| NF2 | Combined: 0.971 | EXP: 0.314 | DB: 0 |
| GHITM | Combined: 0.860 | EXP: 0.000 | DB: 0 |
| TAOK2 | Combined: 0.761 | EXP: 0.069 | DB: 0 |
| TAOK1 | Combined: 0.750 | EXP: 0.069 | DB: 0 |
| NRGN | Combined: 0.712 | EXP: 0.000 | DB: 0 |
| SCOC | Combined: 0.627 | EXP: 0.627 | DB: 0 |
| GAP43 | Combined: 0.580 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- IQCJ (combined score: 0.98, experimental: 0.00)
- NF2 (combined score: 0.97, experimental: 0.31)
- GHITM (combined score: 0.86, experimental: 0.00)
- TAOK2 (combined score: 0.76, experimental: 0.07)
- TAOK1 (combined score: 0.75, experimental: 0.07)

High-confidence interactors (score >= 0.7): 6. Total STRING interactions: 13. IntAct entries: 15.

**PPI score: 7/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | No functional annotation | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 108.0/180 (60.0/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 26 articles 
3. Protein size: 487 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 13 STRING interactions, 6 high-confidence
6. Domain architecture: 2 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 26 <= 100). Total score: 108.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P0DPB3
- HPA: https://www.proteinatlas.org/ENSG00000151967-SCHIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCHIP1%22
- STRING: https://string-db.org/ (search SCHIP1)
- IntAct: https://www.ebi.ac.uk/intact/ (search SCHIP1)
- Harvest packet: SCHIP1.json
