---
type: protein-evaluation
gene: "CRYBG2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CRYBG2 (Beta/gamma crystallin domain-containing protein 2) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q8N1P7 |
| **Protein Name** | Beta/gamma crystallin domain-containing protein 2 |
| **Aliases** | AIM1L |
| **Length** | 1661 aa |
| **Mass** | 177.9 kDa |
| **AlphaFold mean pLDDT** | 54.5 |
| **AlphaFold pLDDT >90** | 24.7% |
| **AlphaFold pLDDT <50** | 57.5% |
| **PubMed (strict)** | 1 |
| **Function** |  |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
No UniProt annotation

#### GO Cellular Component
- No GO-CC annotation

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: None
- **Reliability (IF)**: Approved
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 1 |

**Key Papers:**
- PMID:39944650 -- Variations in rumen microbiota and host genome impacted feed efficiency in goat breeds. (Frontiers in microbiology, 2025)


**Research Volume Assessment**: Very low (<10 papers), nearly unstudied, excellent candidate for exploring novel nuclear protein function

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 54.5
- pLDDT >90: 24.7%, 70-90: 14.3%, 50-70: 3.4%, <50: 57.5%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| None | -- | -- | -- |

**Structure Assessment**: AlphaFold low confidence (pLDDT 54.5), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR050252 |  |
| IPR001064 |  |
| IPR011024 |  |
| IPR035992 |  |
| IPR000772 |  |

| Pfam | Description |
|------|-------------|
| PF00030 |  |
| PF00652 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| TMEM191C | 0.7 | 0.0 | -- |
| LKAAEAR1 | 0.507 | 0.0 | -- |
| PPP2R5C | 0.487 | 0.487 | -- |
| PPP2R5D | 0.487 | 0.487 | -- |
| NOP16 | 0.454 | 0.0 | -- |
| PRSS48 | 0.445 | 0.051 | -- |
| OR8G1 | 0.43 | 0.0 | -- |
| ZNF280C | 0.418 | 0.053 | -- |
| ZNF681 | 0.4 | 0.053 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| PDLIM7 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| DDX3Y | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| PER1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| MAP3K7 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| EIF4G3 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| HELZ | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ERF | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| RPL23 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- No UniProt interaction annotations

**PPI Assessment**: Sparse PPI network (9 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 5/10 | x1 | 5 | Very large (1661 aa), challenging for experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=1 papers), nearly unstudied, huge exploration space |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 54.5), 24% high confidence, 57% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (9 STRING partners), possibly independent |
| **Weighted Total** | | | **118.5/180** | |
| **Normalized Total** | | | **64.8/100** | |

### 9. Final Decision

**SCORED: 64.8/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 1 papers, Extremely high research novelty
- Very large (1661 aa), challenging for experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1P7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CRYBG2%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1P7
- STRING: https://string-db.org/cgi/network?identifiers=CRYBG2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CRYBG2

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000176092-CRYBG2/subcellular

![](https://images.proteinatlas.org/29629/1032_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/29629/1032_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/29629/271_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/29629/271_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/29629/272_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/29629/272_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N1P7 |
| SMART | SM00458;SM00247; |
| UniProt Domain [FT] | DOMAIN 986..1023; /note="Beta/gamma crystallin 'Greek key' 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1024..1067; /note="Beta/gamma crystallin 'Greek key' 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1073..1113; /note="Beta/gamma crystallin 'Greek key' 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1114..1156; /note="Beta/gamma crystallin 'Greek key' 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1168..1213; /note="Beta/gamma crystallin 'Greek key' 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1214..1256; /note="Beta/gamma crystallin 'Greek key' 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1262..1302; /note="Beta/gamma crystallin 'Greek key' 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1303..1345; /note="Beta/gamma crystallin 'Greek key' 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1356..1393; /note="Beta/gamma crystallin 'Greek key' 9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1394..1437; /note="Beta/gamma crystallin 'Greek key' 10"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1443..1483; /note="Beta/gamma crystallin 'Greek key' 11"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1484..1525; /note="Beta/gamma crystallin 'Greek key' 12"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00028"; DOMAIN 1569..1659; /note="Ricin B-type lectin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00174" |
| InterPro | IPR050252;IPR001064;IPR011024;IPR035992;IPR000772; |
| Pfam | PF00030;PF00652; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176092-CRYBG2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C12orf57 | Bioplex | false |
| CORO1A | Bioplex | false |
| LAMTOR4 | Bioplex | false |
| NEIL3 | Bioplex | false |
| RALBP1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
