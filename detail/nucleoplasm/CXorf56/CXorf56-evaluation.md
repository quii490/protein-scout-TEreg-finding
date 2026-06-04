---
type: protein-evaluation
gene: "CXorf56"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CXorf56 (STING ER exit protein) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q9H5V9 |
| **Protein Name** | STING ER exit protein |
| **Aliases** | CXorf56 |
| **Length** | 222 aa |
| **Mass** | 25.6 kDa |
| **AlphaFold mean pLDDT** | 76.1 |
| **AlphaFold pLDDT >90** | 36.9% |
| **AlphaFold pLDDT <50** | 7.7% |
| **PubMed (strict)** | 7 |
| **Function** | Molecular adapter that stimulates membrane curvature formation and subsequent endoplasmic reticulum exit site (ERES) establishment by recruiting PI3K complex I, leading to COPII vesicle-mediated transport (PubMed:32690950). Promotes endoplasmic reticulum (ER) exit of cGAMP-activated STING1 oligomers |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm; Endoplasmic reticulum membrane; Nucleus

#### GO Cellular Component
- **cell body** (ISS:UniProtKB)
- **centrosome** (IDA:HPA)
- **cytoplasm** (IDA:UniProtKB)
- **endoplasmic reticulum** (IDA:UniProtKB)
- **endoplasmic reticulum membrane** (IDA:UniProt)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Centrosome
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

No data (Pending cell analysis), nuclear localization based on UniProt + GO + HPA annotations.

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 7 |

**Key Papers:**
- PMID:29374277 -- CXorf56, a dendritic neuronal protein, identified as a new candidate gene for X-linked intellectual disability. (European journal of human genetics : EJHG, 2018 Apr)
- PMID:37156759 -- Inhibition of CXorf56 promotes PARP inhibitor-induced cytotoxicity in triple-negative breast cancer. (NPJ breast cancer, 2023 May 8)
- PMID:31822863 -- Novel clinical and genetic insight into CXorf56-associated intellectual disability. (European journal of human genetics : EJHG, 2020 Mar)
- PMID:31198491 -- A Fragment of Apolipoprotein E4 Leads to the Downregulation of a CXorf56 Homologue, a Novel ER-Associated Protein, and A (Oxidative medicine and cellular longevity, 2019)
- PMID:33673493 -- The Role of the Reanalysis of Genetic Test Results in the Diagnosis of Dysmorphic Syndrome Caused by Inherited xq24 Dele (Genes, 2021 Feb 27)


**Research Volume Assessment**: Very low (<10 papers), nearly unstudied, excellent candidate for exploring novel nuclear protein function

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 76.1
- pLDDT >90: 36.9%, 70-90: 23.0%, 50-70: 32.4%, <50: 7.7%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 8C6J | EM | 2.80 A | j=1-222 |
| 9FMD | EM | 3.30 A | 56=1-222 |

**Structure Assessment**: High-quality AlphaFold prediction (pLDDT 76.1), fold confidence high, PDB 2 entries verified

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR029704 |  |
| IPR057965 |  |

| Pfam | Description |
|------|-------------|
| PF25809 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| PPIL1 | 0.853 | 0.291 | -- |
| UPF3B | 0.821 | 0.0 | -- |
| CDC40 | 0.817 | 0.0 | -- |
| SRRM1 | 0.814 | 0.0 | -- |
| SLU7 | 0.814 | 0.0 | -- |
| ALYREF | 0.81 | 0.0 | -- |
| SYF2 | 0.807 | 0.0 | -- |
| DDX39B | 0.803 | 0.0 | -- |
| DRG1 | 0.802 | 0.797 | -- |
| GRN | 0.799 | 0.797 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| NFKBIL1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| STEEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| LMNA | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:31046837|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| RPRD1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| PIBF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |
| HAT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- HAT1 (3 experiments)
- KIF9 (3 experiments)
- PIBF1 (3 experiments)
- RPRD1B (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (222 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=7 papers), nearly unstudied, huge exploration space |
| 3D Structure | 9/10 | x3 | 27 | Good quality (pLDDT 76.1), 36% high confidence, 7% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **138.0/180** | |
| **Normalized Total** | | | **75.4/100** | |

### 9. Final Decision

**SCORED: 75.4/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 7 papers, Extremely high research novelty
- Medium (222 aa), convenient for biochemical experiments
- Sufficient structural data (PDB experimental + AlphaFold)

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5V9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CXorf56%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5V9
- STRING: https://string-db.org/cgi/network?identifiers=CXorf56&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CXorf56
