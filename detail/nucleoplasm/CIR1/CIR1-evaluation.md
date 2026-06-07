---
type: protein-evaluation
gene: "CIR1"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CIR1 (Corepressor of RBPJ and splicing regulator) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q86X95 |
| **Protein Name** | Corepressor of RBPJ and splicing regulator |
| **Aliases** | CIR; CIR1 |
| **Length** | 450 aa |
| **Mass** | 52.3 kDa |
| **AlphaFold mean pLDDT** | 59.7 |
| **AlphaFold pLDDT >90** | 11.1% |
| **AlphaFold pLDDT <50** | 44.4% |
| **PubMed (strict)** | 30 |
| **Function** | May modulate splice site selection during alternative splicing of pre-mRNAs (By similarity). Regulates transcription and acts as corepressor for RBPJ. Recruits RBPJ to the Sin3-histone deacetylase complex (HDAC). Required for RBPJ-mediated repression of transcription |

### 2. 核定位证据

#### UniProt Subcellular Location
Nucleus speckle; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome

#### GO Cellular Component
- **centrosome** (IEA:UniProtKB-SubCell)
- **nuclear speck** (IDA:HPA)
- **nucleus** (IDA:UniProtKB)
- **protein-containing complex** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nuclear speckles
- **Additional locations**: 无
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 30 |

**Key Papers:**
- PMID:40787456 -- The kinase Bud32 regulates iron homeostasis in fungal pathogen Cryptococcus neoformans. (Frontiers in immunology, 2025)
- PMID:36656038 -- Factors Influencing the Nitrogen-Source Dependent Flucytosine Resistance in Cryptococcus Species. (mBio, 2023 Feb 28)
- PMID:32580959 -- A Transcriptional Regulatory Map of Iron Homeostasis Reveals a New Control Circuit for Capsule Formation in Cryptococcus (Genetics, 2020 Aug)
- PMID:9771976 -- Up-regulation of CIR1/CROC1 expression upon cell immortalization and in tumor-derived human cell lines. (Oncogene, 1998 Sep 10)
- PMID:17587236 -- Constitutive expression of CIR1 (RVE2) affects several circadian-regulated processes and seed germination in Arabidopsis (The Plant journal : for cell and molecular biology, 2007 Aug)


**Research Volume Assessment**: 较低（<50篇），研究空间充足

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 59.7
- pLDDT >90: 11.1%, 70-90: 22.9%, 50-70: 21.6%, <50: 44.4%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 6ZYM | EM | 3.40 A | 9=1-450 |
| 8I0W | EM | 3.40 A | 4=1-450 |

**Structure Assessment**: AlphaFold低置信度（pLDDT 59.7），作为新颖蛋白属正常现象

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR040014 |  |
| IPR019339 |  |

| Pfam | Description |
|------|-------------|
| PF10197 |  |

**Domain Assessment**: 结构域注释稀疏，作为新颖蛋白属正常

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| RBPJ | 0.989 | 0.261 | -- |
| SAP30 | 0.965 | 0.27 | -- |
| SNW1 | 0.954 | 0.852 | -- |
| RBPJL | 0.937 | 0.08 | -- |
| NCOR2 | 0.936 | 0.257 | -- |
| HDAC2 | 0.927 | 0.23 | -- |
| HDAC1 | 0.921 | 0.191 | -- |
| FRG1 | 0.901 | 0.8 | -- |
| CWC25 | 0.871 | 0.817 | -- |
| CWC15 | 0.861 | 0.8 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| rp9 | psi-mi:"MI:0018"(two hybrid) | pubmed:15652350 | psi-mi:"MI:0915"(physical asso | -- |
| SRSF2 | psi-mi:"MI:0416"(fluorescence microscopy | pubmed:15652350 | psi-mi:"MI:0403"(colocalizatio | -- |
| U2AF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15652350 | psi-mi:"MI:0915"(physical asso | -- |
| SRSF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15652350 | psi-mi:"MI:0915"(physical asso | -- |
| RBPJ | psi-mi:"MI:0018"(two hybrid) | pubmed:9874765|mint:MINT- | psi-mi:"MI:0915"(physical asso | -- |
| SAP30 | psi-mi:"MI:0018"(two hybrid) | pubmed:9874765|mint:MINT- | psi-mi:"MI:0915"(physical asso | -- |
| HDAC1 | psi-mi:"MI:0416"(fluorescence microscopy | pubmed:9874765|mint:MINT- | psi-mi:"MI:0403"(colocalizatio | -- |
| HDAC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9874765|mint:MINT- | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- CEP76 (3 experiments)
- SRSF1 (3 experiments)
- SRSF2 (4 experiments)
- U2AF1 (4 experiments)
- DPPA4 (3 experiments)
- MB21D2 (3 experiments)

**PPI Assessment**: PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 7/10 | x4 | 28 | 主要核定位，部分胞质信号 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（450 aa），生化实验操作便利 |
| 研究新颖性 | 8/10 | x5 | 40 | 非常新颖（PubMed=30篇），仅有少量基础研究 |
| 三维结构 | 6/10 | x3 | 18 | 中等质量（pLDDT 59.7），11%高置信度，44%无序 |
| 调控结构域 | 4/10 | x2 | 8 | 结构域注释稀疏，作为新颖蛋白属正常 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **114.5/180** | |
| **归一化总分** | | | **62.6/100** | |

### 9. Final Decision

**SCORED: 62.6/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 30 篇，研究新颖性极高
- 中等大小（450 aa），生化实验操作便利
- AlphaFold结构可用

**Weaknesses:**
- 核定位需HPA进一步确认
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q86X95
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CIR1%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X95
- STRING: https://string-db.org/cgi/network?identifiers=CIR1&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CIR1

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000138433-CIR1/subcellular

![](https://images.proteinatlas.org/15784/1272_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/15784/1272_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/15784/128_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/15784/128_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/15784/129_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/15784/129_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86X95-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86X95 |
| SMART | SM01083; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040014;IPR019339; |
| Pfam | PF10197; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138433-CIR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SRSF1 | Intact, Biogrid | true |
| SRSF2 | Intact, Biogrid | true |
| U2AF1 | Intact, Biogrid | true |
| CEP76 | Intact | false |
| NEK6 | Biogrid | false |
| RP9 | Biogrid | false |
| SNW1 | Biogrid | false |
| STK4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
