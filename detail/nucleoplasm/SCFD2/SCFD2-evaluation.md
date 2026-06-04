---
type: protein-evaluation
gene: "SCFD2"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SCFD2 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCFD2 / STXBP1L1 |
| Protein Name | Sec1 family domain-containing protein 2 |
| Protein Size | ~684 aa (75.1 kDa) |
| UniProt ID | Q8WU76 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SCFD2.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 10/10 | x1 | **10** | 684 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~12 |
| 3D Structure | 0/10 | x3 | **0** | PDB: 0, AF: No |
| Regulatory Domains | 3/10 | x2 | **6** | InterPro: 3, Pfam: 1 |
| PPI Network | 9/10 | x3 | **27** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.50** | |
| **Raw Total** | | | **104.5/180** | |
| **Normalized Total** | | | **58.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| HPA (IF) | Nucleoplasm | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

684 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 12 |
| Broad query count | 14 |
| Alias note | Aliases observed but not used for scoring: STXBP1L1 |
| Novelty score | 9/10 |

PubMed strict count ~12 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:34587239** (2022 Jan 8) -- t(4;12)(q12;p13) ETV6-rearranged AML without eosinophilia does not involve PDGFRA: relevance for imatinib insensitivity. (Blood advances)
- **PMID:35681031** (2022 Jun 9) -- PSPC1 is a potential prognostic marker for hormone-dependent breast cancer patients and modulates RNA processing of ESR1 (Scientific reports)
- **PMID:39232998** (2025 Jan) -- Lipidomic and transcriptomic characteristics of boar seminal plasma extracellular vesicles associated with sperm motilit (Biochimica et biophysica acta. Molecular and cell biology of lipids)
- **PMID:32213542** (2020 Jun 1) -- PSF Promotes ER-Positive Breast Cancer Progression via Posttranscriptional Regulation of ESR1 and SCFD2. (Cancer research)

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
| InterPro | IPR001619 | IPR001619 |
| InterPro | IPR027482 | IPR027482 |
| InterPro | IPR036045 | IPR036045 |
| Pfam | PF00995 | PF00995 |

InterPro domains: 3 | Pfam domains: 1. Total catalogued domains: 4.

Functional annotation: May be involved in protein transport

**Domain score: 3/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| STX18 | Combined: 0.900 | EXP: 0.821 | DB: 0 |
| RINT1 | Combined: 0.889 | EXP: 0.771 | DB: 0 |
| SCFD1 | Combined: 0.876 | EXP: 0.687 | DB: 0 |
| ZW10 | Combined: 0.876 | EXP: 0.788 | DB: 0 |
| USE1 | Combined: 0.863 | EXP: 0.828 | DB: 0 |
| NBAS | Combined: 0.858 | EXP: 0.784 | DB: 0 |
| BNIP1 | Combined: 0.800 | EXP: 0.756 | DB: 0 |
| SEC22B | Combined: 0.784 | EXP: 0.777 | DB: 0 |

Top STRING interaction partners:
- STX18 (combined score: 0.90, experimental: 0.82)
- RINT1 (combined score: 0.89, experimental: 0.77)
- SCFD1 (combined score: 0.88, experimental: 0.69)
- ZW10 (combined score: 0.88, experimental: 0.79)
- USE1 (combined score: 0.86, experimental: 0.83)

High-confidence interactors (score >= 0.7): 10. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 9/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | May be involved in protein transport | -- |
| Structure | AF + PDB | Limited | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 104.5/180 (58.1/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 12 articles 
3. Protein size: 684 aa -- ideal
4. Structure: No structural data available
5. PPI network: 15 STRING interactions, 10 high-confidence
6. Domain architecture: 3 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 12 <= 100). Total score: 104.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WU76
- HPA: https://www.proteinatlas.org/ENSG00000184178-SCFD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCFD2%22
- STRING: https://string-db.org/ (search SCFD2)
- IntAct: https://www.ebi.ac.uk/intact/ (search SCFD2)
- Harvest packet: SCFD2.json
