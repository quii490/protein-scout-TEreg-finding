---
type: protein-evaluation
gene: "DDX55"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 9
---

## DDX55 (ATP-dependent RNA helicase DDX55) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q8NHQ9 |
| **Protein Name** | ATP-dependent RNA helicase DDX55 |
| **Aliases** | KIAA1595 |
| **Length** | 600 aa |
| **Mass** | 68.5 kDa |
| **AlphaFold mean pLDDT** | 84.4 |
| **AlphaFold pLDDT >90** | 53.0% |
| **AlphaFold pLDDT <50** | 7.0% |
| **PubMed (strict)** | 10 |
| **Function** | Probable ATP-binding RNA helicase. Has ATPase activity and is involved in the maturation of precursor large subunit rRNAs (PubMed:33048000) |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus, nucleoplasm

#### GO Cellular Component
- **cytosol** (IDA:HPA)
- **membrane** (HDA:UniProtKB)
- **nucleolus** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)

#### HPA Subcellular Localization
- **Main location**: Nucleoli
- **Additional locations**: Nucleoplasm; Cytosol
- **Reliability (IF)**: Enhanced
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 10 |

**Key Papers:**
- PMID:35514200 -- DDX55 promotes hepatocellular carcinoma progression by interacting with BRD4 and participating in exosome-mediated cell- (Cancer science, 2022 Sep)
- PMID:41225606 -- Integrative analysis of RNA binding proteins identifies DDX55 as a novel regulator of 3'UTR isoform diversity. (Genome biology, 2025 Nov 12)
- PMID:40114746 -- Identification of a novel FOXO3‑associated prognostic model in hepatocellular carcinoma. (Oncology letters, 2025 May)
- PMID:40654921 -- Integrative analysis of RNA binding proteins identifies DDX55 as a novel regulator of 3'UTR isoform diversity. (bioRxiv : the preprint server for biology, 2025 May 8)
- PMID:33425256 -- Lead DEAD/H box helicase biomarkers with the therapeutic potential identified by integrated bioinformatic approaches in  (Computational and structural biotechnology journal, 2021)


**Research Volume Assessment**: Very low (<10 papers), nearly unstudied, excellent candidate for exploring novel nuclear protein function

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 84.4
- pLDDT >90: 53.0%, 70-90: 31.3%, 50-70: 8.7%, <50: 7.0%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| None | -- | -- | -- |

**Structure Assessment**: AlphaFold moderate quality (pLDDT 84.4), ordered region 84%

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR011545 |  |
| IPR014001 |  |
| IPR001650 |  |
| IPR027417 |  |
| IPR000629 |  |
| IPR014014 |  |
| IPR025313 |  |

| Pfam | Description |
|------|-------------|
| PF13959 |  |
| PF00270 |  |
| PF00271 |  |

**Domain Assessment**: Limited domain annotation, but AlphaFold predicts identifiable fold domains

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| FTSJ3 | 0.984 | 0.866 | -- |
| BOP1 | 0.984 | 0.937 | -- |
| WDR12 | 0.977 | 0.88 | -- |
| GTPBP4 | 0.972 | 0.907 | -- |
| NOL12 | 0.962 | 0.941 | -- |
| NOC3L | 0.962 | 0.886 | -- |
| NIFK | 0.962 | 0.918 | -- |
| NOC2L | 0.957 | 0.886 | -- |
| NOP2 | 0.951 | 0.798 | -- |
| RSL24D1 | 0.949 | 0.833 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| ENSP00000238146.3 | psi-mi:"MI:1314"(proximity-dependent bio | imex:IM-30059|pubmed:3925 | psi-mi:"MI:2364"(proximity) | -- |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21145461|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent bio | pubmed:29568061|imex:IM-2 | psi-mi:"MI:2364"(proximity) | -- |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| FGF8 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| KRTAP10-8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:2541 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- AGTRAP (3 experiments)
- KRTAP10-8 (3 experiments)
- PICK1 (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 9/10 | x4 | 36 | Clear nuclear localization, multi-db cross-validated |
| Protein Size | 10/10 | x1 | 10 | Medium (600 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=10 papers), nearly unstudied, huge exploration space |
| 3D Structure | 7/10 | x3 | 21 | High quality (pLDDT 84.4), 53% high confidence, 7% disordered |
| Regulatory Domains | 6/10 | x2 | 12 | Limited domain annotation, but AlphaFold predicts identifiab |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **139.5/180** | |
| **Normalized Total** | | | **76.2/100** | |

### 9. Final Decision

**SCORED: 76.2/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 10 papers, Extremely high research novelty
- Medium (600 aa), convenient for biochemical experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHQ9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22DDX55%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHQ9
- STRING: https://string-db.org/cgi/network?identifiers=DDX55&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/DDX55

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000111364-DDX55/subcellular

![](https://images.proteinatlas.org/39962/1000_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/39962/1000_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/39962/1003_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/39962/1003_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/39962/1276_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/39962/1276_H6_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NHQ9 |
| SMART | SM00487;SM01178;SM00490; |
| UniProt Domain [FT] | DOMAIN 40..223; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 254..402; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011545;IPR014001;IPR001650;IPR027417;IPR000629;IPR014014;IPR025313; |
| Pfam | PF13959;PF00270;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111364-DDX55/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTRAP | Intact | false |
| CALM2 | Opencell | false |
| CALM3 | Opencell | false |
| CRLF3 | Bioplex | false |
| DDX56 | Biogrid | false |
| FGFBP1 | Bioplex | false |
| H1-4 | Bioplex | false |
| H2BC8 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
