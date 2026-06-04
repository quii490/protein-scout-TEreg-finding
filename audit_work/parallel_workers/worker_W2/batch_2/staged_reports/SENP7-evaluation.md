---
type: protein-evaluation
gene: "SENP7"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SENP7 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SENP7 / KIAA1707, SSP2, SUSP2 |
| Protein Name | Sentrin-specific protease 7 |
| Protein Size | ~1050 aa (119.7 kDa) |
| UniProt ID | Q9BQF6 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SENP7.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 7/10 | x1 | **7** | 1050 aa |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict ~52 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 2, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 3, Pfam: 1 |
| PPI Network | 8/10 | x3 | **24** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.75** | |
| **Raw Total** | | | **111.8/180** | |
| **Normalized Total** | | | **62.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000250 |
| GO-CC | cytoplasm | ISS:UniProtKB |
| GO-CC | nucleus | IDA:LIFEdb |
| GO-CC | postsynaptic cytosol | IEA:Ensembl |
| GO-CC | presynaptic cytosol | IEA:Ensembl |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Nuclear bodies | IF-based (Supported) |
| HPA (IF) | Centrosome | IF-based (Supported) |
| HPA (IF) | Cytosol | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nucleoplasm, Nuclear bodies (Reliability: Supported)

- GO-CC annotations include: nucleus

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

1050 aa -- large protein, still workable but may require specialized approaches for full-length studies. Score: 7/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 52 |
| Broad query count | 81 |
| Alias note | Aliases observed but not used for scoring: KIAA1707, SSP2, SUSP2 |
| Novelty score | 6/10 |

PubMed strict count ~52 articles. Moderate-to-established field, growing literature. Score: 6/10.

**Key Publications**:

- **PMID:36512624** (2023 Feb 15) -- Deregulation of SPOP in Cancer. (Cancer research)
- **PMID:38677512** (2024 Jun) -- Senp7 deficiency impairs lipid droplets maturation in white adipose tissues via Plin4 deSUMOylation. (The Journal of biological chemistry)
- **PMID:41362746** (2026) -- A SENP7-SIRT1-IL-10 Axis Driven by DeSUMOylation Promotes Breg Differentiation and Immune Evasion in Colorectal Cancer. (International journal of biological sciences)
- **PMID:36417853** (2022 Nov 22) -- SENP7 deSUMOylase-governed transcriptional program coordinates sarcomere assembly and is targeted in muscle atrophy. (Cell reports)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 56.1 |
| PDB Entries | 2 |
| AF pLDDT >90% | 23.4% |
| AF pLDDT <50% | 55.7% |

**Structure Assessment**: PDB entries available (2 total): 3EAY (X-ray, 2.40 A), 7R2E (X-ray, 1.74 A) AlphaFold prediction available (v6) with mean pLDDT: 56.1. pLDDT distribution: >90: 23.4%, 70-90: 13.4%, 50-70: 7.4%, <50: 55.7%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR038765 | IPR038765 |
| InterPro | IPR003653 | IPR003653 |
| InterPro | IPR051947 | IPR051947 |
| Pfam | PF02902 | PF02902 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: Protease that acts as a positive regulator of the cGAS-STING pathway by catalyzing desumoylation of CGAS. Desumoylation of CGAS promotes DNA-binding activity of CGAS, subsequent oligomerization and activation (By similarity). Deconjugates SUMO2 and SUMO3 from targeted proteins, but not SUMO1 (PubMed:18799455). Catalyzes the deconjugation of poly-SUMO2 and poly-SUMO3 chains (PubMed:18799455). Has very low efficiency in processing full-length SUMO proteins to their mature forms (PubMed:18799455)

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SUMO2 | Combined: 0.959 | EXP: 0.602 | DB: 0 |
| SUMO1 | Combined: 0.931 | EXP: 0.403 | DB: 0 |
| RANGAP1 | Combined: 0.901 | EXP: 0.055 | DB: 0 |
| CBX5 | Combined: 0.855 | EXP: 0.617 | DB: 0 |
| SUMO4 | Combined: 0.815 | EXP: 0.602 | DB: 0 |
| SUMO3 | Combined: 0.770 | EXP: 0.537 | DB: 0 |
| UBE2I | Combined: 0.725 | EXP: 0.184 | DB: 0 |
| SAE1 | Combined: 0.691 | EXP: 0.096 | DB: 0 |

Top STRING interaction partners:
- SUMO2 (combined score: 0.96, experimental: 0.60)
- SUMO1 (combined score: 0.93, experimental: 0.40)
- RANGAP1 (combined score: 0.90, experimental: 0.06)
- CBX5 (combined score: 0.85, experimental: 0.62)
- SUMO4 (combined score: 0.81, experimental: 0.60)

High-confidence interactors (score >= 0.7): 7. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 8/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | Protease that acts as a positive regulator of the cGAS-STING pathway by catalyzing desumoylation of CGAS. Desumoylation  | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.75/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 111.8/180 (62.1/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 52 articles 
3. Protein size: 1050 aa -- acceptable
4. Structure: Experimental PDB available (2 entries)
5. PPI network: 15 STRING interactions, 7 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 52 <= 100). Total score: 111.8/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQF6
- HPA: https://www.proteinatlas.org/ENSG00000138468-SENP7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SENP7%22
- STRING: https://string-db.org/ (search SENP7)
- IntAct: https://www.ebi.ac.uk/intact/ (search SENP7)
- Harvest packet: SENP7.json
