---
type: protein-evaluation
gene: "SEPTIN3"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SEPTIN3 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEPTIN3 / SEP3, SEPT3 |
| Protein Name | Neuronal-specific septin-3 |
| Protein Size | ~358 aa (40.7 kDa) |
| UniProt ID | Q9UH03 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SEPTIN3.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 10/10 | x1 | **10** | 358 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~11 |
| 3D Structure | 8/10 | x3 | **24** | PDB: 4, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 4, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **144.0/180** | |
| **Normalized Total** | | | **80.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | not specified |
| UniProt | Cytoplasm, cytoskeleton | ECO:0000250 |
| UniProt | Synapse | ECO:0000250 |
| GO-CC | cell division site | IBA:GO_Central |
| GO-CC | microtubule cytoskeleton | IBA:GO_Central |
| GO-CC | presynapse | ISS:UniProtKB |
| GO-CC | septin complex | ISS:UniProtKB |
| GO-CC | septin ring | IBA:GO_Central |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Plasma membrane | IF-based (Approved) |
| HPA (IF) | Actin filaments | IF-based (Approved) |
| HPA (IF) | Primary cilium | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

358 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 11 |
| Broad query count | 18 |
| Alias note | Aliases observed but not used for scoring: SEP3, SEPT3 |
| Novelty score | 9/10 |

PubMed strict count ~11 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:39088289** (2024 Aug 1) -- Autoimmune Movement Disorders. (Continuum (Minneapolis, Minn.))
- **PMID:41340014** (2025 Dec) -- Revealing Causal Protein Biomarkers and Potential Therapeutic Targets for Histologic-Specific Lung Cancer. (Journal of cellular and molecular medicine)
- **PMID:40562343** (2025 Oct) -- Circadian rhythm disruption exacerbates neurodegeneration and alters proteomic profiles in a 6-OHDA induced Parkinson's  (Experimental neurology)
- **PMID:38686040** (2024) -- SEPT3 as a Potential Molecular Target of Triple-Negative Breast Cancer. (International journal of general medicine)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 81.5 |
| PDB Entries | 4 |
| AF pLDDT >90% | 54.7% |
| AF pLDDT <50% | 13.7% |

**Structure Assessment**: PDB entries available (4 total): 3SOP (X-ray, 2.88 A), 4Z51 (X-ray, 1.86 A), 4Z54 (X-ray, 1.83 A), 6UQQ (X-ray, 2.75 A) AlphaFold prediction available (v6) with mean pLDDT: 81.5. pLDDT distribution: >90: 54.7%, 70-90: 22.9%, 50-70: 8.7%, <50: 13.7%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR030379 | IPR030379 |
| InterPro | IPR027417 | IPR027417 |
| InterPro | IPR016491 | IPR016491 |
| InterPro | IPR008114 | IPR008114 |
| Pfam | PF00735 | PF00735 |

InterPro domains: 4 | Pfam domains: 1. Total catalogued domains: 5.

Functional annotation: Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential)

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SEPTIN4 | Combined: 0.995 | EXP: 0.898 | DB: 1 |
| SEPTIN5 | Combined: 0.989 | EXP: 0.898 | DB: 1 |
| SEPTIN7 | Combined: 0.988 | EXP: 0.913 | DB: 1 |
| SEPTIN2 | Combined: 0.980 | EXP: 0.917 | DB: 1 |
| SEPTIN11 | Combined: 0.978 | EXP: 0.861 | DB: 1 |
| SEPTIN6 | Combined: 0.977 | EXP: 0.839 | DB: 1 |
| SEPTIN1 | Combined: 0.962 | EXP: 0.900 | DB: 1 |
| SEPTIN9 | Combined: 0.962 | EXP: 0.861 | DB: 1 |

Top STRING interaction partners:
- SEPTIN4 (combined score: 0.99, experimental: 0.90)
- SEPTIN5 (combined score: 0.99, experimental: 0.90)
- SEPTIN7 (combined score: 0.99, experimental: 0.91)
- SEPTIN2 (combined score: 0.98, experimental: 0.92)
- SEPTIN11 (combined score: 0.98, experimental: 0.86)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential) | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 144.0/180 (80.0/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 11 articles 
3. Protein size: 358 aa -- ideal
4. Structure: Experimental PDB available (4 entries)
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 4 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 11 <= 100). Total score: 144.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UH03
- HPA: https://www.proteinatlas.org/ENSG00000100167-SEPTIN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEPTIN3%22
- STRING: https://string-db.org/ (search SEPTIN3)
- IntAct: https://www.ebi.ac.uk/intact/ (search SEPTIN3)
- Harvest packet: SEPTIN3.json
