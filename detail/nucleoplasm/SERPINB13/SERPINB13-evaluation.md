---
type: protein-evaluation
gene: "SERPINB13"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SERPINB13 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERPINB13 / PI13 |
| Protein Name | Serpin B13 |
| Protein Size | ~391 aa (44.3 kDa) |
| UniProt ID | Q9UIV8 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SERPINB13.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 10/10 | x1 | **10** | 391 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~19 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 0, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 6, Pfam: 1 |
| PPI Network | 7/10 | x3 | **21** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.50** | |
| **Raw Total** | | | **126.5/180** | |
| **Normalized Total** | | | **70.3/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | not specified |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | cytosol | IDA:HPA |
| GO-CC | extracellular exosome | HDA:UniProtKB |
| GO-CC | extracellular space | IBA:GO_Central |
| GO-CC | lysosomal lumen | TAS:Reactome |
| GO-CC | nuclear speck | IDA:HPA |
| GO-CC | nucleoplasm | IDA:UniProtKB |
| HPA (IF) | Nuclear speckles | IF-based (Approved) |
| HPA (IF) | Cytosol | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nuclear speckles (Reliability: Approved)

- GO-CC annotations include: nuclear speck, nucleoplasm

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

391 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 19 |
| Broad query count | 40 |
| Alias note | Aliases observed but not used for scoring: PI13 |
| Novelty score | 9/10 |

PubMed strict count ~19 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:40247093** (2025 Apr 17) -- Investigating immune cell infiltration and gene expression features in pterygium pathogenesis. (Scientific reports)
- **PMID:33827974** (2021 Apr 7) -- SerpinB13 antibodies promote β cell development and resistance to type 1 diabetes. (Science translational medicine)
- **PMID:31373692** (2019 Nov) -- Shared gene signature between pterygium and meibomian gland dysfunction uncovered through gene-expression meta-analysis. (Annals of human genetics)
- **PMID:21723253** (2011 Jul 22) -- SERPINB13 is a novel RUNX1 target gene. (Biochemical and biophysical research communications)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 86.8 |
| PDB Entries | 0 |
| AF pLDDT >90% | 67.8% |
| AF pLDDT <50% | 8.4% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 86.8. pLDDT distribution: >90: 67.8%, 70-90: 21.2%, 50-70: 2.6%, <50: 8.4%.

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

Functional annotation: May play a role in the proliferation or differentiation of keratinocytes

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| CTSG | Combined: 0.922 | EXP: 0.045 | DB: 1 |
| CTSK | Combined: 0.918 | EXP: 0.052 | DB: 1 |
| CTSL | Combined: 0.885 | EXP: 0.052 | DB: 1 |
| SERPINB3 | Combined: 0.779 | EXP: 0.000 | DB: 0 |
| RUNX1 | Combined: 0.765 | EXP: 0.000 | DB: 1 |
| CTSV | Combined: 0.758 | EXP: 0.052 | DB: 1 |
| CBFB | Combined: 0.750 | EXP: 0.000 | DB: 1 |
| KRT6A | Combined: 0.649 | EXP: 0.041 | DB: 0 |

Top STRING interaction partners:
- CTSG (combined score: 0.92, experimental: 0.04)
- CTSK (combined score: 0.92, experimental: 0.05)
- CTSL (combined score: 0.89, experimental: 0.05)
- SERPINB3 (combined score: 0.78, experimental: 0.00)
- RUNX1 (combined score: 0.77, experimental: 0.00)

High-confidence interactors (score >= 0.7): 7. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 7/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | May play a role in the proliferation or differentiation of keratinocytes | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 126.5/180 (70.3/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 19 articles 
3. Protein size: 391 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 7 high-confidence
6. Domain architecture: 6 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 19 <= 100). Total score: 126.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIV8
- HPA: https://www.proteinatlas.org/ENSG00000197641-SERPINB13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERPINB13%22
- STRING: https://string-db.org/ (search SERPINB13)
- IntAct: https://www.ebi.ac.uk/intact/ (search SERPINB13)
- Harvest packet: SERPINB13.json
