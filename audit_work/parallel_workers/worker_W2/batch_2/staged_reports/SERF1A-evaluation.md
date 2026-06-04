---
type: protein-evaluation
gene: "SERF1A"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SERF1A -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERF1A / FAM2A, SERF1, SMAM1 |
| Protein Name | Small EDRK-rich factor 1 |
| Protein Size | ~110 aa (12.3 kDa) |
| UniProt ID | O75920 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SERF1A.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Primarily nuclear with experimental support |
| Protein Size | 4/10 | x1 | **4** | 110 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~17 |
| 3D Structure | 2/10 | x3 | **6** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 2, Pfam: 1 |
| PPI Network | 5/10 | x3 | **15** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.50** | |
| **Raw Total** | | | **108.5/180** | |
| **Normalized Total** | | | **60.3/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm, cytosol | ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | cytosol | IMP:UniProtKB |
| GO-CC | nucleus | IMP:UniProtKB |
| GO-CC | protein-containing complex | IMP:UniProtKB |
| HPA (IF) | Nuclear bodies | IF-based (Uncertain) |

**HPA IF Status**: IF images available; reliability: Uncertain.

**Nuclear Score: 8/10.** Primarily nuclear with experimental support.

- UniProt annotates: Nucleus

- HPA IF detects: Nuclear bodies (Reliability: Uncertain)

- GO-CC annotations include: nucleus

**Nuclear localization score: 8/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

110 aa -- small protein, at the lower boundary of the workable range. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 17 |
| Broad query count | 25 |
| Alias note | Aliases observed but not used for scoring: FAM2A, SERF1, SMAM1 |
| Novelty score | 9/10 |

PubMed strict count ~17 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:38272228** (2024 Mar) -- The disordered protein SERF promotes α-Synuclein aggregation through liquid-liquid phase separation. (The Journal of biological chemistry)
- **PMID:31794729** (2020 Feb 14) -- Structural Fuzziness of the RNA-Organizing Protein SERF Determines a Toxic Gain-of-interaction. (Journal of molecular biology)
- **PMID:35713792** (2022 Oct) -- Backbone resonance assignments and dynamics of S. cerevisiae SERF. (Biomolecular NMR assignments)
- **PMID:36071912** (2022 Sep) -- Investigation on the Effects of Modifying Genes on the Spinal Muscular Atrophy Phenotype. (Global medical genetics)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 62.6 |
| PDB Entries | 0 |
| AF pLDDT >90% | 0.0% |
| AF pLDDT <50% | 24.5% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 62.6. pLDDT distribution: >90: 0.0%, 70-90: 37.3%, 50-70: 38.2%, <50: 24.5%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR007513 | IPR007513 |
| InterPro | IPR040211 | IPR040211 |
| Pfam | PF04419 | PF04419 |

InterPro domains: 2 | Pfam domains: 1. Total catalogued domains: 3.

Functional annotation: Positive regulator of amyloid protein aggregation and proteotoxicity (PubMed:20723760, PubMed:22854022, PubMed:31034892). Induces conformational changes in amyloid proteins, such as APP, HTT, and SNCA, driving them into compact formations preceding the formation of aggregates (PubMed:20723760, PubMed:22854022, PubMed:31034892)

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| NDUFAF3 | Combined: 0.919 | EXP: 0.000 | DB: 0 |
| SMN1 | Combined: 0.885 | EXP: 0.000 | DB: 0 |
| NAIP | Combined: 0.872 | EXP: 0.000 | DB: 0 |
| SMN2 | Combined: 0.843 | EXP: 0.000 | DB: 0 |
| GPKOW | Combined: 0.724 | EXP: 0.000 | DB: 0 |
| C1S | Combined: 0.720 | EXP: 0.000 | DB: 0 |
| BDP1 | Combined: 0.689 | EXP: 0.000 | DB: 0 |
| GTF2H2 | Combined: 0.616 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- NDUFAF3 (combined score: 0.92, experimental: 0.00)
- SMN1 (combined score: 0.89, experimental: 0.00)
- NAIP (combined score: 0.87, experimental: 0.00)
- SMN2 (combined score: 0.84, experimental: 0.00)
- GPKOW (combined score: 0.72, experimental: 0.00)

High-confidence interactors (score >= 0.7): 6. Total STRING interactions: 15. IntAct entries: 4.

**PPI score: 5/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Positive regulator of amyloid protein aggregation and proteotoxicity (PubMed:20723760, PubMed:22854022, PubMed:31034892) | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 108.5/180 (60.3/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Primarily nuclear with experimental support
2. PubMed count: 17 articles 
3. Protein size: 110 aa -- suboptimal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 6 high-confidence
6. Domain architecture: 2 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 8 > 3, PubMed 17 <= 100). Total score: 108.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75920
- HPA: https://www.proteinatlas.org/ENSG00000172058-SERF1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERF1A%22
- STRING: https://string-db.org/ (search SERF1A)
- IntAct: https://www.ebi.ac.uk/intact/ (search SERF1A)
- Harvest packet: SERF1A.json
