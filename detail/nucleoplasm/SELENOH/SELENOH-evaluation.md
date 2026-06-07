---
type: protein-evaluation
gene: "SELENOH"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SELENOH -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOH / C11orf31, SELH |
| Protein Name | Selenoprotein H |
| Protein Size | ~122 aa (13.5 kDa) |
| UniProt ID | Q8IZQ5 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SELENOH.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 4/10 | x1 | **4** | 122 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~21 |
| 3D Structure | 0/10 | x3 | **0** | PDB: 0, AF: No |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 3, Pfam: 1 |
| PPI Network | 7/10 | x3 | **21** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.50** | |
| **Raw Total** | | | **91.5/180** | |
| **Normalized Total** | | | **50.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| GO-CC | Golgi apparatus | IBA:GO_Central |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Nucleoli | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 5/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nucleoplasm, Nucleoli (Reliability: Approved)

**Nuclear localization score: 5/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

122 aa -- small protein, at the lower boundary of the workable range. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 21 |
| Broad query count | 32 |
| Alias note | Aliases observed but not used for scoring: C11orf31, SELH |
| Novelty score | 8/10 |

PubMed strict count ~21 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:27645994** (2016 Nov 11) -- Selenoprotein Gene Nomenclature. (The Journal of biological chemistry)
- **PMID:28917051** (2018) -- Selenocysteine-Mediated Expressed Protein Ligation of SELENOM. (Methods in molecular biology (Clifton, N.J.))
- **PMID:36958417** (2023 Jul) -- The role of selenium in shaping mice brain metabolome and selenoproteome through the gut-brain axis by combining metabol (The Journal of nutritional biochemistry)
- **PMID:35553364** (2023 Apr) -- Selenoprotein Gene mRNA Expression Evaluation During Renal Ischemia-Reperfusion Injury in Rats and Ebselen Intervention  (Biological trace element research)

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
| InterPro | IPR011893 | IPR011893 |
| InterPro | IPR052674 | IPR052674 |
| InterPro | IPR036249 | IPR036249 |
| Pfam | PF10262 | PF10262 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: May be involved in a redox-related process

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SELENOT | Combined: 0.886 | EXP: 0.000 | DB: 0 |
| SELENOK | Combined: 0.880 | EXP: 0.000 | DB: 0 |
| SELENOV | Combined: 0.854 | EXP: 0.061 | DB: 0 |
| SELENOF | Combined: 0.843 | EXP: 0.000 | DB: 0 |
| SELENOO | Combined: 0.833 | EXP: 0.000 | DB: 0 |
| SELENOW | Combined: 0.828 | EXP: 0.000 | DB: 0 |
| SELENOS | Combined: 0.823 | EXP: 0.000 | DB: 0 |
| SEPHS2 | Combined: 0.821 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- SELENOT (combined score: 0.89, experimental: 0.00)
- SELENOK (combined score: 0.88, experimental: 0.00)
- SELENOV (combined score: 0.85, experimental: 0.06)
- SELENOF (combined score: 0.84, experimental: 0.00)
- SELENOO (combined score: 0.83, experimental: 0.00)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 7/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | May be involved in a redox-related process | -- |
| Structure | AF + PDB | Limited | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 91.5/180 (50.8/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 21 articles 
3. Protein size: 122 aa -- suboptimal
4. Structure: No structural data available
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 5 > 3, PubMed 21 <= 100). Total score: 91.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZQ5
- HPA: https://www.proteinatlas.org/ENSG00000211450-SELENOH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SELENOH%22
- STRING: https://string-db.org/ (search SELENOH)
- IntAct: https://www.ebi.ac.uk/intact/ (search SELENOH)
- Harvest packet: SELENOH.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZQ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011893;IPR052674;IPR036249; |
| Pfam | PF10262; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000211450-SELENOH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARIH1 | Biogrid | false |
| KPNA4 | Opencell | false |
| PPM1G | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
