---
type: protein-evaluation
gene: "SC5D"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SC5D -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SC5D / SC5DL |
| Protein Name | Lathosterol oxidase |
| Protein Size | ~299 aa (35.3 kDa) |
| UniProt ID | O75845 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SC5D.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 10/10 | x1 | **10** | 299 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~40 |
| 3D Structure | 5/10 | x3 | **15** | PDB: 0, AF: Yes |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 2, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **118.0/180** | |
| **Normalized Total** | | | **65.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Endoplasmic reticulum membrane | ECO:0000269 |
| GO-CC | endoplasmic reticulum membrane | IDA:UniProtKB |
| GO-CC | membrane | IBA:GO_Central |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Endoplasmic reticulum | IF-based (Approved) |
| HPA (IF) | Plasma membrane | IF-based (Approved) |
| HPA (IF) | Cytosol | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

299 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 40 |
| Broad query count | 55 |
| Alias note | Aliases observed but not used for scoring: SC5DL |
| Novelty score | 8/10 |

PubMed strict count ~40 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:38297130** (2024 Feb) -- 7-Dehydrocholesterol dictates ferroptosis sensitivity. (Nature)
- **PMID:36470484** (2023 Feb 15) -- Characterization and potential function of 7-dehydrocholesterol reductase (dhcr7) and lathosterol 5-desaturase (sc5d) in (Gene)
- **PMID:36167286** (2023 Jan) -- Long noncoding RNA lincsc5d regulates hepatic cholesterol synthesis by modulating sterol C5 desaturase in large yellow c (Comparative biochemistry and physiology. Part B, Biochemistry & molecular biology)
- **PMID:11731337** (2001 Oct 31) -- Molecular cloning and structural analysis of human sterol C5 desaturase. (Biochimica et biophysica acta)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 91.7 |
| PDB Entries | 0 |
| AF pLDDT >90% | 87.3% |
| AF pLDDT <50% | 6.0% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 91.7. pLDDT distribution: >90: 87.3%, 70-90: 3.7%, 50-70: 3.0%, <50: 6.0%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR006694 | IPR006694 |
| InterPro | IPR050307 | IPR050307 |
| Pfam | PF04116 | PF04116 |

InterPro domains: 2 | Pfam domains: 1. Total catalogued domains: 3.

Functional annotation: Catalyzes the penultimate step of the biosynthesis of cholesterol, the dehydrogenation of lathosterol into 7-dehydrocholesterol (7-DHC). Cholesterol is the major sterol component in mammalian membranes and a precursor for bile acid and steroid hormone synthesis (PubMed:10786622, PubMed:38297129). In addition to its essential role in cholesterol biosynthesis, it also indirectly regulates ferroptosis through the production of 7-DHC. By diverting the spread of damage caused by peroxyl radicals from

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| DHCR7 | Combined: 0.998 | EXP: 0.782 | DB: 1 |
| HSD17B7 | Combined: 0.997 | EXP: 0.954 | DB: 0 |
| FDFT1 | Combined: 0.996 | EXP: 0.954 | DB: 0 |
| EBP | Combined: 0.995 | EXP: 0.000 | DB: 1 |
| MSMO1 | Combined: 0.991 | EXP: 0.783 | DB: 0 |
| ERG28 | Combined: 0.989 | EXP: 0.954 | DB: 0 |
| LSS | Combined: 0.989 | EXP: 0.954 | DB: 0 |
| CYP51A1 | Combined: 0.987 | EXP: 0.305 | DB: 0 |

Top STRING interaction partners:
- DHCR7 (combined score: 1.00, experimental: 0.78)
- HSD17B7 (combined score: 1.00, experimental: 0.95)
- FDFT1 (combined score: 1.00, experimental: 0.95)
- EBP (combined score: 0.99, experimental: 0.00)
- MSMO1 (combined score: 0.99, experimental: 0.78)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | Catalyzes the penultimate step of the biosynthesis of cholesterol, the dehydrogenation of lathosterol into 7-dehydrochol | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 118.0/180 (65.6/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 40 articles 
3. Protein size: 299 aa -- ideal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 2 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 40 <= 100). Total score: 118.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75845
- HPA: https://www.proteinatlas.org/ENSG00000109929-SC5D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SC5D%22
- STRING: https://string-db.org/ (search SC5D)
- IntAct: https://www.ebi.ac.uk/intact/ (search SC5D)
- Harvest packet: SC5D.json
