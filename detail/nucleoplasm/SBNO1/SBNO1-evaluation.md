---
type: protein-evaluation
gene: "SBNO1"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SBNO1 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SBNO1 / MOP3 |
| Protein Name | Protein strawberry notch homolog 1 |
| Protein Size | ~1393 aa (154.3 kDa) |
| UniProt ID | A3KN83 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SBNO1.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Primarily nuclear with experimental support |
| Protein Size | 4/10 | x1 | **4** | 1393 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~13 |
| 3D Structure | 3/10 | x3 | **9** | PDB: 0, AF: Yes |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: 5, Pfam: 3 |
| PPI Network | 4/10 | x3 | **12** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.50** | |
| **Raw Total** | | | **116.5/180** | |
| **Normalized Total** | | | **64.7/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus | ECO:0000250 |
| GO-CC | nucleus | ISS:UniProtKB |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 8/10.** Primarily nuclear with experimental support.

- UniProt annotates: Nucleus

- HPA IF detects: Nucleoplasm (Reliability: Approved)

- GO-CC annotations include: nucleus

**Nuclear localization score: 8/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

1393 aa -- very large protein, may present challenges for recombinant expression and structural biology. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 13 |
| Broad query count | 19 |
| Alias note | Aliases observed but not used for scoring: MOP3 |
| Novelty score | 9/10 |

PubMed strict count ~13 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:32636717** (2020) -- The plasma peptides of sepsis. (Clinical proteomics)
- **PMID:36695974** (2023 Feb) -- Study of Strawberry Notch homolog 1 and 2 expression in human glioblastoma. (Journal of neuro-oncology)
- **PMID:36057539** (2022 Sep) -- Involvement of strawberry notch homologue 1 in neurite outgrowth of cortical neurons. (Development, growth & differentiation)
- **PMID:20503374** (2010 Jun) -- Expression of strawberry notch family genes during zebrafish embryogenesis. (Developmental dynamics : an official publication of the American Association of Anatomists)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 67.3 |
| PDB Entries | 0 |
| AF pLDDT >90% | 17.9% |
| AF pLDDT <50% | 31.6% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 67.3. pLDDT distribution: >90: 17.9%, 70-90: 42.6%, 50-70: 7.9%, <50: 31.6%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR027417 | IPR027417 |
| InterPro | IPR057332 | IPR057332 |
| InterPro | IPR026937 | IPR026937 |
| InterPro | IPR026741 | IPR026741 |
| InterPro | IPR039187 | IPR039187 |
| Pfam | PF13872 | PF13872 |
| Pfam | PF13871 | PF13871 |
| Pfam | PF25373 | PF25373 |

InterPro domains: 5 | Pfam domains: 3. Total catalogued domains: 8.

Functional annotation: Plays a crucial role in the regulation of neural stem cells (NSCs) proliferation. Enhances the phosphorylation of GSK3B through the PI3K-Akt signaling pathway, thereby upregulating the Wnt/beta-catenin signaling pathway and promoting the proliferation of NSCs. Improves ischemic stroke recovery while inhibiting neuroinflammation through small extracellular vesicles (sEVs)-mediated mechanism. Enhances the secretion of sEVs from NSCs, which in turn inhibit both the MAPK and NF-kappaB pathways in mi

**Domain score: 7/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| RASGEF1A | Combined: 0.812 | EXP: 0.000 | DB: 0 |
| RIOK1 | Combined: 0.810 | EXP: 0.000 | DB: 0 |
| RIOX1 | Combined: 0.796 | EXP: 0.000 | DB: 0 |
| TGFBRAP1 | Combined: 0.790 | EXP: 0.000 | DB: 0 |
| RIF1 | Combined: 0.660 | EXP: 0.000 | DB: 0 |
| PDS5A | Combined: 0.636 | EXP: 0.000 | DB: 0 |
| CDK2AP1 | Combined: 0.626 | EXP: 0.000 | DB: 0 |
| PBDC1 | Combined: 0.618 | EXP: 0.220 | DB: 0 |

Top STRING interaction partners:
- RASGEF1A (combined score: 0.81, experimental: 0.00)
- RIOK1 (combined score: 0.81, experimental: 0.00)
- RIOX1 (combined score: 0.80, experimental: 0.00)
- TGFBRAP1 (combined score: 0.79, experimental: 0.00)
- RIF1 (combined score: 0.66, experimental: 0.00)

High-confidence interactors (score >= 0.7): 4. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 4/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Plays a crucial role in the regulation of neural stem cells (NSCs) proliferation. Enhances the phosphorylation of GSK3B  | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 116.5/180 (64.7/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Primarily nuclear with experimental support
2. PubMed count: 13 articles 
3. Protein size: 1393 aa -- suboptimal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 4 high-confidence
6. Domain architecture: 5 InterPro + 3 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 8 > 3, PubMed 13 <= 100). Total score: 116.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/A3KN83
- HPA: https://www.proteinatlas.org/ENSG00000139697-SBNO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SBNO1%22
- STRING: https://string-db.org/ (search SBNO1)
- IntAct: https://www.ebi.ac.uk/intact/ (search SBNO1)
- Harvest packet: SBNO1.json
