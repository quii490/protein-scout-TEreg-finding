---
type: protein-evaluation
gene: "DCAF16"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 5
---

## DCAF16 (DDB1- and CUL4-associated factor 16) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q9NXF7 |
| **Protein Name** | DDB1- and CUL4-associated factor 16 |
| **Aliases** | C4orf30 |
| **Length** | 216 aa |
| **Mass** | 24.2 kDa |
| **AlphaFold mean pLDDT** | 38.2 |
| **AlphaFold pLDDT >90** | 0% |
| **AlphaFold pLDDT <50** | 94.0% |
| **PubMed (strict)** | 38 |
| **Function** | Functions as a substrate recognition component for CUL4-DDB1 E3 ubiquitin-protein ligase complex, which mediates ubiquitination and proteasome-dependent degradation of nuclear proteins |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus

#### GO Cellular Component
- **Cul4-RING E3 ubiquitin ligase complex** (IDA:UniProtKB)
- **nucleoplasm** (TAS:Reactome)

#### HPA Subcellular Localization
- **Main location**: Plasma membrane; Cytosol
- **Additional locations**: None
- **Reliability (IF)**: Approved
- **IF Display Images Available**: YES

HPA IF display images available, reliability: Approved.

### 3. HPA Immunofluorescence

No data (Pending cell analysis), nuclear localization based on UniProt + GO + HPA annotations.

HPA IF display images available, reliability: Approved.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 38 |

**Key Papers:**
- PMID:38383787 -- Targeted protein degradation via intramolecular bivalent glues. (Nature, 2024 Mar)
- PMID:34411892 -- Developments of CRBN-based PROTACs as potential therapeutic agents. (European journal of medicinal chemistry, 2021 Dec 5)
- PMID:31209349 -- Electrophilic PROTACs that degrade nuclear proteins by engaging DCAF16. (Nature chemical biology, 2019 Jul)
- PMID:40960846 -- Discovery of BRD9 Molecular Glue Degraders That Spare Cardiomyocytes. (Journal of the American Chemical Society, 2025 Oct 1)
- PMID:40626960 -- Rational Design of CDK12/13 and BRD4 Molecular Glue Degraders. (Angewandte Chemie (International ed. in English), 2025 Sep 15)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 38.2
- pLDDT >90: 0%, 70-90: 0%, 50-70: 6.0%, <50: 94.0%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 8G46 | EM | 2.20 A | B=1-216 |
| 8OV6 | EM | 3.77 A | B=1-216 |

**Structure Assessment**: AlphaFold low confidence (pLDDT 38.2), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR028216 |  |

| Pfam | Description |
|------|-------------|
| PF15349 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| DDB1 | 0.97 | 0.443 | -- |
| CUL4A | 0.965 | 0.619 | -- |
| DCAF15 | 0.959 | 0.0 | -- |
| CRBN | 0.956 | 0.0 | -- |
| CUL4B | 0.951 | 0.42 | -- |
| DCAF5 | 0.937 | 0.0 | -- |
| DET1 | 0.936 | 0.0 | -- |
| DDA1 | 0.924 | 0.184 | -- |
| DCAF12 | 0.917 | 0.0 | -- |
| DTL | 0.914 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| tat | psi-mi:"MI:0007"(anti tag coimmunoprecip | imex:IM-17346|pubmed:2219 | psi-mi:"MI:0914"(association) | -- |
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| lcrF | psi-mi:"MI:0398"(two hybrid pooling appr | imex:IM-13779|pubmed:2071 | psi-mi:"MI:0915"(physical asso | -- |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| ZBTB44 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- tat (2 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 5/10 | x4 | 20 | Nucleo-cytoplasmic distribution, possibly shuttling protein |
| Protein Size | 10/10 | x1 | 10 | Medium (216 aa), convenient for biochemical experiments |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=38 papers), only limited foundational research |
| 3D Structure | 4/10 | x3 | 12 | Moderate quality (pLDDT 38.2), 0% high confidence, 94% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **100.5/180** | |
| **Normalized Total** | | | **54.9/100** | |

### 9. Final Decision

**SCORED: 54.9/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 38 papers, Extremely high research novelty
- Medium (216 aa), convenient for biochemical experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization evidence weak, HPA IF validation needed
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXF7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22DCAF16%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXF7
- STRING: https://string-db.org/cgi/network?identifiers=DCAF16&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/DCAF16
