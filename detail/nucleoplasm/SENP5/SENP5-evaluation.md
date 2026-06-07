---
type: protein-evaluation
gene: "SENP5"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SENP5 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SENP5 / none |
| Protein Name | Sentrin-specific protease 5 |
| Protein Size | ~755 aa (86.7 kDa) |
| UniProt ID | Q96HI0 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SENP5.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | Strongly nuclear -- primary localization confirmed by multiple databases |
| Protein Size | 10/10 | x1 | **10** | 755 aa |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict ~43 |
| 3D Structure | 6/10 | x3 | **18** | PDB: 3, AF: Yes |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: 3, Pfam: 2 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.00** | |
| **Raw Total** | | | **144.0/180** | |
| **Normalized Total** | | | **80.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus, nucleolus | ECO:0000269, ECO:0000269 |
| GO-CC | nucleolus | IEA:UniProtKB-SubCell |
| GO-CC | nucleoplasm | TAS:Reactome |
| GO-CC | nucleus | IBA:GO_Central |
| GO-CC | postsynaptic cytosol | IEA:Ensembl |
| GO-CC | presynaptic cytosol | IEA:Ensembl |

**HPA IF Status**: No HPA IF data available.

**Nuclear Score: 10/10.** Strongly nuclear -- primary localization confirmed by multiple databases.

- UniProt annotates: Nucleus, nucleolus

- GO-CC annotations include: nucleolus, nucleoplasm, nucleus

**Nuclear localization score: 10/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

755 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 43 |
| Broad query count | 68 |
| Alias note |  |
| Novelty score | 6/10 |

PubMed strict count ~43 articles. Moderate-to-established field, growing literature. Score: 6/10.

**Key Publications**:

- **PMID:37684630** (2023 Sep 8) -- SENP5 promotes homologous recombination-mediated DNA damage repair in colorectal cancer cells through H2AZ deSUMOylation (Journal of experimental & clinical cancer research : CR)
- **PMID:38615367** (2024 Apr) -- Astragaloside IV combined with ligustrazine ameliorates abnormal mitochondrial dynamics via Drp1 SUMO/deSUMOylation in c (CNS neuroscience & therapeutics)
- **PMID:39433793** (2024 Oct 21) -- Peptidylprolyl isomerase A guides SENP5/GAU1 DNA-lncRNA triplex generation for driving tumorigenesis. (Nature communications)
- **PMID:40404649** (2025 May 22) -- Structural basis for the human SENP5's SUMO isoform discrimination. (Nature communications)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 54.9 |
| PDB Entries | 3 |
| AF pLDDT >90% | 32.2% |
| AF pLDDT <50% | 56.7% |

**Structure Assessment**: PDB entries available (3 total): 9GNN (X-ray, 2.36 A), 9GNV (X-ray, 2.18 A), 9GNX (X-ray, 1.90 A) AlphaFold prediction available (v6) with mean pLDDT: 54.9. pLDDT distribution: >90: 32.2%, 70-90: 3.7%, 50-70: 7.4%, <50: 56.7%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR038765 | IPR038765 |
| InterPro | IPR003653 | IPR003653 |
| InterPro | IPR045577 | IPR045577 |
| Pfam | PF02902 | PF02902 |
| Pfam | PF19722 | PF19722 |

InterPro domains: 3 | Pfam domains: 2. Total catalogued domains: 5.

Functional annotation: Protease that catalyzes two essential functions in the SUMO pathway: processing of full-length SUMO3 to its mature form and deconjugation of SUMO2 and SUMO3 from targeted proteins. Has weak proteolytic activity against full-length SUMO1 or SUMO1 conjugates. Required for cell division

**Domain score: 7/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SUMO2 | Combined: 0.963 | EXP: 0.489 | DB: 0 |
| SUMO1 | Combined: 0.955 | EXP: 0.309 | DB: 0 |
| SUMO3 | Combined: 0.898 | EXP: 0.489 | DB: 0 |
| NPM1 | Combined: 0.871 | EXP: 0.361 | DB: 0 |
| GNL2 | Combined: 0.862 | EXP: 0.068 | DB: 0 |
| RPL37A | Combined: 0.845 | EXP: 0.069 | DB: 0 |
| SAE1 | Combined: 0.761 | EXP: 0.096 | DB: 0 |
| UBE2I | Combined: 0.758 | EXP: 0.095 | DB: 0 |

Top STRING interaction partners:
- SUMO2 (combined score: 0.96, experimental: 0.49)
- SUMO1 (combined score: 0.95, experimental: 0.31)
- SUMO3 (combined score: 0.90, experimental: 0.49)
- NPM1 (combined score: 0.87, experimental: 0.36)
- GNL2 (combined score: 0.86, experimental: 0.07)

High-confidence interactors (score >= 0.7): 13. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Protease that catalyzes two essential functions in the SUMO pathway: processing of full-length SUMO3 to its mature form  | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Strong multi-database consistency. Bonus: +2.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 144.0/180 (80.0/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Strongly nuclear -- primary localization confirmed by multiple databases
2. PubMed count: 43 articles 
3. Protein size: 755 aa -- ideal
4. Structure: Experimental PDB available (3 entries)
5. PPI network: 15 STRING interactions, 13 high-confidence
6. Domain architecture: 3 InterPro + 2 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 10 > 3, PubMed 43 <= 100). Total score: 144.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96HI0
- HPA: https://www.proteinatlas.org/ENSG00000119231-SENP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SENP5%22
- STRING: https://string-db.org/ (search SENP5)
- IntAct: https://www.ebi.ac.uk/intact/ (search SENP5)
- Harvest packet: SENP5.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96HI0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038765;IPR003653;IPR045577; |
| Pfam | PF02902;PF19722; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119231-SENP5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NPM1 | Biogrid, Opencell | true |
| NPM3 | Biogrid, Opencell, Bioplex | true |
| ACTL6B | Bioplex | false |
| CASQ2 | Bioplex | false |
| CBX6 | Bioplex | false |
| DHDH | Bioplex | false |
| DNAJA2 | Bioplex | false |
| DNASE1L1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
