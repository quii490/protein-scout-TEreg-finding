---
type: protein-evaluation
gene: "CNOT6L"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 4
---

## CNOT6L (CCR4-NOT transcription complex subunit 6-like) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q96LI5 |
| **Protein Name** | CCR4-NOT transcription complex subunit 6-like |
| **Aliases** | CCR4B |
| **Length** | 555 aa |
| **Mass** | 63.0 kDa |
| **AlphaFold mean pLDDT** | 90.0 |
| **AlphaFold pLDDT >90** | 77.3% |
| **AlphaFold pLDDT <50** | 5.6% |
| **PubMed (strict)** | 36 |
| **Function** | Has 3'-5' poly(A) exoribonuclease activity for synthetic poly(A) RNA substrate. Catalytic component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repre |

### 2. 核定位证据

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **CCR4-NOT complex** (IDA:UniProtKB)
- **cytoplasm** (IDA:UniProtKB)
- **cytosol** (IDA:HPA)
- **nucleus** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Cytosol
- **Additional locations**: 无
- **Reliability (IF)**: Supported
- **IF Display Images Available**: YES

HPA IF 可显示图像可用，可靠性: Supported。

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 可显示图像可用，可靠性: Supported。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 36 |

**Key Papers:**
- PMID:35385705 -- Deadenylase-dependent mRNA decay of GDF15 and FGF21 orchestrates food intake and energy expenditure. (Cell metabolism, 2022 Apr 5)
- PMID:30389976 -- Crystal Structure of Human Nocturnin Catalytic Domain. (Scientific reports, 2018 Nov 2)
- PMID:40023604 -- CNOT6L deadenylase suppresses cardiac remodeling in heart failure through downregulation of tenascin-C mRNA. (The Journal of pharmacology and experimental therapeutics, 2025 Feb)
- PMID:40598799 -- The E3 ubiquitin ligase, RNF219, suppresses CNOT6L expression to exhibit antiproliferative activity. (FEBS open bio, 2025 Nov)
- PMID:39433858 -- High expression of CNOT6L contributes to the negative development of type 2 diabetes. (Scientific reports, 2024 Oct 21)


**Research Volume Assessment**: 较低（<50篇），研究空间充足

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 90.0
- pLDDT >90: 77.3%, 70-90: 12.6%, 50-70: 4.5%, <50: 5.6%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 3NGN | X-ray | 2.40 A | A=158-555 |
| 3NGO | X-ray | 2.20 A | A=158-555 |
| 3NGQ | X-ray | 1.80 A | A=158-555 |
| 5DV2 | X-ray | 2.07 A | A=158-555 |
| 5DV4 | X-ray | 1.80 A | A=158-555 |
| 7VOI | X-ray | 4.38 A | C=1-555 |

**Structure Assessment**: PDB实验结构（6个条目）+ AlphaFold高质量预测，结构可信度极高

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR050410 |  |
| IPR034967 |  |
| IPR036691 |  |
| IPR005135 |  |
| IPR001611 |  |
| IPR003591 |  |
| IPR032675 |  |

| Pfam | Description |
|------|-------------|
| PF03372 |  |
| PF13855 |  |

**Domain Assessment**: 结构域注释有限，但AlphaFold预测有可辨识折叠域

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CNOT9 | 0.999 | 0.888 | -- |
| CNOT7 | 0.999 | 0.994 | -- |
| CNOT1 | 0.999 | 0.992 | -- |
| CNOT2 | 0.999 | 0.92 | -- |
| CNOT3 | 0.999 | 0.901 | -- |
| CNOT6 | 0.999 | 0.783 | -- |
| CNOT8 | 0.999 | 0.921 | -- |
| CNOT10 | 0.998 | 0.803 | -- |
| CNOT11 | 0.997 | 0.83 | -- |
| TNKS1BP1 | 0.991 | 0.806 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| BTG2 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| Cnot3 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| mviM1 | psi-mi:"MI:0398"(two hybrid pooling appr | imex:IM-13779|pubmed:2071 | psi-mi:"MI:0915"(physical asso | -- |
| Rc3h1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| Rc3h2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ANXA2R | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| CNOT11 | psi-mi:"MI:2222"(inference by socio-affi | pubmed:unassigned1312 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- CNOT1 (6 experiments)
- CNOT10 (4 experiments)
- CNOT11 (4 experiments)
- CNOT2 (5 experiments)
- CNOT3 (4 experiments)
- CNOT6 (3 experiments)
- CNOT7 (10 experiments)
- CNOT8 (6 experiments)
- CNOT9 (3 experiments)
- TNKS1BP1 (4 experiments)

**PPI Assessment**: PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 4/10 | x4 | 16 | 核定位证据较弱 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（555 aa），生化实验操作便利 |
| 研究新颖性 | 8/10 | x5 | 40 | 非常新颖（PubMed=36篇），仅有少量基础研究 |
| 三维结构 | 10/10 | x3 | 30 | 高质量预测（pLDDT 90.0），77%高置信度，5%无序 |
| 调控结构域 | 6/10 | x2 | 12 | 结构域注释有限，但AlphaFold预测有可辨识折叠域 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **120.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 9. Final Decision

**SCORED: 65.6/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 36 篇，研究新颖性极高
- 中等大小（555 aa），生化实验操作便利
- 结构数据充分（PDB实验结构+AlphaFold）

**Weaknesses:**
- 核定位证据较弱，需HPA IF验证
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96LI5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CNOT6L%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96LI5
- STRING: https://string-db.org/cgi/network?identifiers=CNOT6L&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CNOT6L

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000138767-CNOT6L/subcellular

![](https://images.proteinatlas.org/42688/1967_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42688/1967_D10_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/42688/477_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42688/477_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42688/479_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42688/479_H1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96LI5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
