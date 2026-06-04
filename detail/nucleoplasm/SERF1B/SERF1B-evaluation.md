---
type: protein-evaluation
gene: "SERF1B"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SERF1B -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERF1B / FAM2A, SERF1, SMAM1 |
| Protein Name | Small EDRK-rich factor 1 |
| Protein Size | ~110 aa (12.3 kDa) |
| UniProt ID | O75920 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SERF1B.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | Strongly nuclear -- primary localization confirmed by multiple databases |
| Protein Size | 4/10 | x1 | **4** | 110 aa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict ~2 |
| 3D Structure | 2/10 | x3 | **6** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 2, Pfam: 1 |
| PPI Network | 1/10 | x3 | **3** | STRING: 7 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **106.0/180** | |
| **Normalized Total** | | | **58.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm, cytosol | ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | cytosol | IMP:UniProtKB |
| GO-CC | nucleus | IMP:UniProtKB |
| GO-CC | protein-containing complex | IMP:UniProtKB |
| HPA (IF) | Nuclear bodies | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 9/10.** Strongly nuclear -- primary localization confirmed by multiple databases.

- UniProt annotates: Nucleus

- HPA IF detects: Nuclear bodies (Reliability: Approved)

- GO-CC annotations include: nucleus

**Nuclear localization score: 9/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

110 aa -- small protein, at the lower boundary of the workable range. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 2 |
| Broad query count | 2 |
| Alias note | Aliases observed but not used for scoring: FAM2A, SERF1, SMAM1 |
| Novelty score | 10/10 |

PubMed strict count ~2 articles. Very high novelty -- minimal prior research. Score: 10/10.

**Key Publications**:

- **PMID:36446526** (2023 Feb) -- Transcriptome analyses in infertile men reveal germ cell-specific expression and splicing patterns. (Life science alliance)
- **PMID:42107920** (2026 May 6) -- Genetic characterization of DDX11 variants identified in a Chinese family with Warsaw breakage syndrome. (Seizure)

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
| SERF1A | Combined: 0.483 | EXP: 0.000 | DB: 0 |
| GTF2H2C | Combined: 0.479 | EXP: 0.000 | DB: 0 |
| SMN1 | Combined: 0.469 | EXP: 0.000 | DB: 0 |
| GTF2H2 | Combined: 0.451 | EXP: 0.000 | DB: 0 |
| OR5M3 | Combined: 0.425 | EXP: 0.000 | DB: 0 |
| ZNF630 | Combined: 0.418 | EXP: 0.000 | DB: 0 |
| TMEM54 | Combined: 0.404 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- SERF1A (combined score: 0.48, experimental: 0.00)
- GTF2H2C (combined score: 0.48, experimental: 0.00)
- SMN1 (combined score: 0.47, experimental: 0.00)
- GTF2H2 (combined score: 0.45, experimental: 0.00)
- OR5M3 (combined score: 0.42, experimental: 0.00)

High-confidence interactors (score >= 0.7): 0. Total STRING interactions: 7. IntAct entries: 4.

**PPI score: 1/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Positive regulator of amyloid protein aggregation and proteotoxicity (PubMed:20723760, PubMed:22854022, PubMed:31034892) | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 106.0/180 (58.9/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Strongly nuclear -- primary localization confirmed by multiple databases
2. PubMed count: 2 articles 
3. Protein size: 110 aa -- suboptimal
4. Structure: AlphaFold prediction only
5. PPI network: 7 STRING interactions, 0 high-confidence
6. Domain architecture: 2 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 9 > 3, PubMed 2 <= 100). Total score: 106.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75920
- HPA: https://www.proteinatlas.org/ENSG00000205572-SERF1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERF1B%22
- STRING: https://string-db.org/ (search SERF1B)
- IntAct: https://www.ebi.ac.uk/intact/ (search SERF1B)
- Harvest packet: SERF1B.json
