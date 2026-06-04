---
type: protein-evaluation
gene: "SERGEF"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SERGEF -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERGEF / DELGEF, GNEFR |
| Protein Name | Secretion-regulating guanine nucleotide exchange factor |
| Protein Size | ~458 aa (49.0 kDa) |
| UniProt ID | Q9UGK8 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SERGEF.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | Strongly nuclear -- primary localization confirmed by multiple databases |
| Protein Size | 10/10 | x1 | **10** | 458 aa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict ~7 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 0, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 4, Pfam: 1 |
| PPI Network | 5/10 | x3 | **15** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.75** | |
| **Raw Total** | | | **140.8/180** | |
| **Normalized Total** | | | **78.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | cytosol | IDA:HPA |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA (IF) | Nucleoplasm | IF-based (Supported) |
| HPA (IF) | Cytosol | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 10/10.** Strongly nuclear -- primary localization confirmed by multiple databases.

- UniProt annotates: Nucleus

- HPA IF detects: Nucleoplasm (Reliability: Supported)

- GO-CC annotations include: nucleoplasm, nucleus

**Nuclear localization score: 10/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

458 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 7 |
| Broad query count | 13 |
| Alias note | Aliases observed but not used for scoring: DELGEF, GNEFR |
| Novelty score | 10/10 |

PubMed strict count ~7 articles. Very high novelty -- minimal prior research. Score: 10/10.

**Key Publications**:

- **PMID:33381146** (2020) -- Aberrantly Methylated-Differentially Expressed Genes Identify Novel Atherosclerosis Risk Subtypes. (Frontiers in genetics)
- **PMID:41300787** (2025 Nov 6) -- Genome-Wide Association Study of First-Parity Reproductive Traits in Suzi Pig. (Genes)
- **PMID:27035928** (2016 May) -- A robust biomarker of differential correlations improves the diagnosis of cytologically indeterminate thyroid cancers. (International journal of molecular medicine)
- **PMID:29206233** (2017) -- Genome-wide admixture and association study of subclinical atherosclerosis in the Women's Interagency HIV Study (WIHS). (PloS one)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 85.2 |
| PDB Entries | 0 |
| AF pLDDT >90% | 72.7% |
| AF pLDDT <50% | 17.2% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 85.2. pLDDT distribution: >90: 72.7%, 70-90: 8.5%, 50-70: 1.5%, <50: 17.2%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR058923 | IPR058923 |
| InterPro | IPR009091 | IPR009091 |
| InterPro | IPR000408 | IPR000408 |
| InterPro | IPR051625 | IPR051625 |
| Pfam | PF25390 | PF25390 |

InterPro domains: 4 | Pfam domains: 1. Total catalogued domains: 5.

Functional annotation: Probable guanine nucleotide exchange factor (GEF), which may be involved in the secretion process

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| DPH3 | Combined: 0.999 | EXP: 0.984 | DB: 0 |
| EXOC2 | Combined: 0.912 | EXP: 0.510 | DB: 0 |
| USH1C | Combined: 0.772 | EXP: 0.068 | DB: 0 |
| EEF2 | Combined: 0.684 | EXP: 0.000 | DB: 0 |
| PRMT6 | Combined: 0.587 | EXP: 0.292 | DB: 0 |
| RABIF | Combined: 0.576 | EXP: 0.000 | DB: 0 |
| HEATR9 | Combined: 0.571 | EXP: 0.000 | DB: 0 |
| CCDC115 | Combined: 0.563 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- DPH3 (combined score: 1.00, experimental: 0.98)
- EXOC2 (combined score: 0.91, experimental: 0.51)
- USH1C (combined score: 0.77, experimental: 0.07)
- EEF2 (combined score: 0.68, experimental: 0.00)
- PRMT6 (combined score: 0.59, experimental: 0.29)

High-confidence interactors (score >= 0.7): 3. Total STRING interactions: 15. IntAct entries: 11.

**PPI score: 5/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Probable guanine nucleotide exchange factor (GEF), which may be involved in the secretion process | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.75/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 140.8/180 (78.2/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Strongly nuclear -- primary localization confirmed by multiple databases
2. PubMed count: 7 articles 
3. Protein size: 458 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 3 high-confidence
6. Domain architecture: 4 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 10 > 3, PubMed 7 <= 100). Total score: 140.8/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UGK8
- HPA: https://www.proteinatlas.org/ENSG00000129158-SERGEF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERGEF%22
- STRING: https://string-db.org/ (search SERGEF)
- IntAct: https://www.ebi.ac.uk/intact/ (search SERGEF)
- Harvest packet: SERGEF.json
