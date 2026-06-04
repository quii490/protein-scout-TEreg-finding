---
type: protein-evaluation
gene: "SEPTIN10"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: rejected
---

## SEPTIN10 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEPTIN10 / SEPT10 |
| Protein Name | Septin-10 |
| Protein Size | ~454 aa (52.6 kDa) |
| UniProt ID | Q9P0V9 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SEPTIN10.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | No credible nuclear localization |
| Protein Size | 10/10 | x1 | **10** | 454 aa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict ~7 |
| 3D Structure | 4/10 | x3 | **12** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 3, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.75** | |
| **Raw Total** | | | **108.8/180** | |
| **Normalized Total** | | | **60.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Cytoplasm, cytoskeleton | ECO:0000250 |
| UniProt | Cell projection, cilium, flagellum | ECO:0000250 |
| GO-CC | cell division site | IBA:GO_Central |
| GO-CC | microtubule cytoskeleton | IBA:GO_Central |
| GO-CC | motile cilium | IEA:UniProtKB-SubCell |
| GO-CC | septin complex | IBA:GO_Central |
| GO-CC | septin ring | IBA:GO_Central |
| HPA (IF) | Actin filaments | IF-based (Supported) |
| HPA (IF) | Microtubules | IF-based (Supported) |
| HPA (IF) | Annulus | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 0/10.** No credible nuclear localization.

- No nuclear annotation found in UniProt, HPA, or GO-CC databases.

**Nuclear localization score: 0/10.** RULE: Nuclear <=3 -> REJECTED. This gene FAILS the nuclear localization threshold.

### 4. Protein Size Assessment

454 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 7 |
| Broad query count | 12 |
| Alias note | Aliases observed but not used for scoring: SEPT10 |
| Novelty score | 10/10 |

PubMed strict count ~7 articles. Very high novelty -- minimal prior research. Score: 10/10.

**Key Publications**:

- **PMID:38242197** (2024 Mar 1) -- SEPTIN10-mediated crosstalk between cytoskeletal networks controls mechanotransduction and oncogenic YAP/TAZ signaling. (Cancer letters)
- **PMID:33485349** (2021 Jan 23) -- HELQ and EGR3 expression correlate with IGHV mutation status and prognosis in chronic lymphocytic leukemia. (Journal of translational medicine)
- **PMID:39025256** (2024 Oct) -- Novel lipid-interaction motifs within the C-terminal domain of Septin10 from Schistosoma mansoni. (Biochimica et biophysica acta. Biomembranes)
- **PMID:16617321** (2006 Jun) -- Deregulated expression of fat and muscle genes in B-cell chronic lymphocytic leukemia with high lipoprotein lipase expre (Leukemia)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 80.7 |
| PDB Entries | 0 |
| AF pLDDT >90% | 50.0% |
| AF pLDDT <50% | 12.1% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 80.7. pLDDT distribution: >90: 50.0%, 70-90: 29.5%, 50-70: 8.4%, <50: 12.1%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR030379 | IPR030379 |
| InterPro | IPR027417 | IPR027417 |
| InterPro | IPR016491 | IPR016491 |
| Pfam | PF00735 | PF00735 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: Filament-forming cytoskeletal GTPase. May play a role in cytokinesis (Potential)

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SEPTIN7 | Combined: 0.979 | EXP: 0.895 | DB: 1 |
| SEPTIN11 | Combined: 0.979 | EXP: 0.835 | DB: 1 |
| SEPTIN4 | Combined: 0.979 | EXP: 0.853 | DB: 1 |
| SEPTIN1 | Combined: 0.977 | EXP: 0.886 | DB: 1 |
| SEPTIN2 | Combined: 0.975 | EXP: 0.902 | DB: 1 |
| SEPTIN5 | Combined: 0.975 | EXP: 0.931 | DB: 1 |
| SEPTIN9 | Combined: 0.963 | EXP: 0.799 | DB: 1 |
| SEPTIN8 | Combined: 0.963 | EXP: 0.873 | DB: 1 |

Top STRING interaction partners:
- SEPTIN7 (combined score: 0.98, experimental: 0.90)
- SEPTIN11 (combined score: 0.98, experimental: 0.83)
- SEPTIN4 (combined score: 0.98, experimental: 0.85)
- SEPTIN1 (combined score: 0.98, experimental: 0.89)
- SEPTIN2 (combined score: 0.97, experimental: 0.90)

High-confidence interactors (score >= 0.7): 13. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | Filament-forming cytoskeletal GTPase. May play a role in cytokinesis (Potential) | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.75/3.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED. Nuclear localization score 0/10 is at or below the auto-rejection threshold of 3/10. The protein's localization evidence places it primarily outside the nucleus, making it unsuitable for a nuclear-protein-focused study. No nuclear localization signal detected in any database.

**Core Observations**:
1. Nuclear localization: No credible nuclear localization
2. PubMed count: 7 articles 
3. Protein size: 454 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 13 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: REJECTED. Nuclear localization score (0/10) is at or below the 3/10 auto-rejection threshold. Nuclear score <= 3 triggers automatic REJECTED status.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0V9
- HPA: https://www.proteinatlas.org/ENSG00000186522-SEPTIN10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEPTIN10%22
- STRING: https://string-db.org/ (search SEPTIN10)
- IntAct: https://www.ebi.ac.uk/intact/ (search SEPTIN10)
- Harvest packet: SEPTIN10.json
