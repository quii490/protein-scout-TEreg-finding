---
type: protein-evaluation
gene: "CSTF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 9
---

## CSTF2 (Cleavage stimulation factor subunit 2) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | P33240 |
| **Protein Name** | Cleavage stimulation factor subunit 2 |
| **Aliases** | CSTF2 |
| **Length** | 577 aa |
| **Mass** | 61.0 kDa |
| **AlphaFold mean pLDDT** | 59.8 |
| **AlphaFold pLDDT >90** | 11.4% |
| **AlphaFold pLDDT <50** | 46.1% |
| **PubMed (strict)** | 46 |
| **Function** | One of the multiple factors required for polyadenylation and 3'-end cleavage of mammalian pre-mRNAs. This subunit is directly involved in the binding to pre-mRNAs |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Nucleus

#### GO Cellular Component
- **cleavage body** (IDA:UniProtKB)
- **mRNA cleavage and polyadenylation specificity factor complex** (IDA:UniProtKB)
- **nuclear body** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IMP:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Nuclear bodies
- **Reliability (IF)**: Enhanced
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 46 |

**Key Papers:**
- PMID:37816727 -- CSTF2 mediated mRNA N(6)-methyladenosine modification drives pancreatic ductal adenocarcinoma m(6)A subtypes. (Nature communications, 2023 Oct 10)
- PMID:38166492 -- The role of CSTF2 in cancer: from technology to clinical application. (Cell cycle (Georgetown, Tex.), 2023 Dec-Dec)
- PMID:39972059 -- CSTF2-impeded innate αβ T cell infiltration and activation exacerbate immune evasion of pancreatic cancer. (Cell death and differentiation, 2025 May)
- PMID:35090899 -- Electrostatic Interactions between CSTF2 and pre-mRNA Drive Cleavage and Polyadenylation. (Biophysical journal, 2022 Feb 15)
- PMID:39514400 -- CSTF2 Supports Hypoxia Tolerance in Hepatocellular Carcinoma by Enabling m6A Modification Evasion of PGK1 to Enhance Gly (Cancer research, 2025 Feb 1)


**Research Volume Assessment**: Low (<50 papers), ample research space

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CSTF1 | STRING | 999 |
| CPSF3 | STRING | 999 |
| CPSF2 | STRING | 999 |
| CSTF3 | STRING | 999 |
| CPSF1 | STRING | 998 |
| CPSF4 | STRING | 997 |
| CPSF6 | STRING | 992 |
| PCF11 | STRING | 991 |


### 深度机制分析

CSTF2（Cleavage stimulation factor subunit 2）是mRNA前体3'末端加工机器的核心组分。其结构域架构包含两个关键RNA结合模块和一个C端蛋白-蛋白互作模块：N端RRM型RNA识别基序（UniProt FT: 16-94aa, SMART SM00360, Pfam PF00076）负责直接结合pre-mRNA的U/GU-rich下游序列元件（DSE）；C端（531-577aa）构成与CSTF1/CSTF3互作的对接平台。两者之间的约400个氨基酸区域富含InterPro注释的IPR025742、IPR026896、IPR038192和IPR012677（Nucleotide-binding alpha-beta plait domain），构成多个RNA结合超二级结构单元。AlphaFold v6预测整体pLDDT=59.8，为中等置信度——这在富含RNA结合域的蛋白中并不少见，因为RRM域在未结合RNA时常表现为构象柔性和动态性。实验NMR结构已有4个条目（1P1T, 2J8P, 6Q2I, 6TZE），分别覆盖N端和C端折叠域。

CSTF2的分子机制已通过生物物理和生化手段深入表征：该蛋白通过RRM结构域以静电相互作用驱动的方式结合pre-mRNA的DSE序列（PMID:35090899, Biophysical Journal, 2022），其结合特异性决定了CSTF复合体对poly(A)位点的选择。CSTF2是前体mRNA切割和聚腺苷酸化特异因子（CPSF）与切割刺激因子（CSTF）协同网络中不可或缺的亚基。PPI网络极强地支持这一功能角色：STRING记录的所有高置信度互作均为mRNA 3'加工机器组分——CPSF3（0.999）、CSTF3（0.999）、SYMPK（0.999）、CPSF2（0.999）、CSTF1（0.999）、CPSF1（0.998）、CPSF4（0.997）、CPSF6（0.992）、PCF11（0.991）、FIP1L1（0.990）。这种高度收敛的PPI图谱是典型的核心分子机器亚基的特征。

近年研究揭示了CSTF2在癌症生物学中的重要角色。CSTF2介导的mRNA m6A修饰失调驱动胰腺导管腺癌m6A亚型分类（PMID:37816727, Nature Communications, 2023），而其在肝细胞癌中通过使PGK1逃避m6A修饰以增强糖酵解，支持缺氧耐受（PMID:39514400, Cancer Research, 2025）。最引人注目的是，CSTF2阻碍先天αβ T细胞浸润和活化，加剧胰腺癌的免疫逃避（PMID:39972059, Cell Death and Differentiation, 2025）。这些研究将CSTF2从一个"管家"3'加工因子重新定义为一个有选择性地调控特定靶基因表达和表观转录组的调控因子。

CSTF2的TE调控潜力来源于其多重功能交叠：（1）作为mRNA 3'加工因子，异常的poly(A)位点选择可能导致TE衍生的隐蔽poly(A)信号被异常激活，产生嵌合TE-宿主转录本；（2）通过m6A修饰调控分子间接影响TE转录本的稳定性和翻译；（3）HPA IF定位于核质和核体（Nuclear bodies, Enhanced），核体是mRNA加工和保留的场所，可能也是TE RNA的命运决定位点。PubMed strict=46篇确保了充分的研究空间（非零基础但远未饱和），核定位评分达9/10（最高之一），使其成为TE转录后调控研究中一个机制清晰的强候选因子。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 59.8
- pLDDT >90: 11.4%, 70-90: 22.7%, 50-70: 19.8%, <50: 46.1%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 1P1T | NMR | - | A=8-111 |
| 2J8P | NMR | - | A=531-577 |
| 6Q2I | NMR | - | A=1-107 |
| 6TZE | NMR | - | A=1-107 |

**Structure Assessment**: AlphaFold low confidence (pLDDT 59.8), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR025742 |  |
| IPR026896 |  |
| IPR038192 |  |
| IPR012677 |  |
| IPR035979 |  |
| IPR000504 |  |

| Pfam | Description |
|------|-------------|
| PF14327 |  |
| PF14304 |  |
| PF00076 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CPSF3 | 0.999 | 0.929 | -- |
| CSTF3 | 0.999 | 0.964 | -- |
| SYMPK | 0.999 | 0.96 | -- |
| CPSF2 | 0.999 | 0.907 | -- |
| CSTF1 | 0.999 | 0.91 | -- |
| CPSF1 | 0.998 | 0.878 | -- |
| CPSF4 | 0.997 | 0.764 | -- |
| CPSF6 | 0.992 | 0.4 | -- |
| PCF11 | 0.991 | 0.801 | -- |
| FIP1L1 | 0.99 | 0.902 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| UBQLN1 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16189514|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| BAG6 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| ERG28 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| FEZ1 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16169070|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- ABHD11 (3 experiments)
- AKAP8L (3 experiments)
- ANKRD10 (3 experiments)
- ATP23 (3 experiments)
- BARD1 (8 experiments)
- CDC73 (5 experiments)
- CEACAM6 (3 experiments)
- CNOT2 (3 experiments)
- CPSF2 (2 experiments)
- CTBP2 (3 experiments)

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 9/10 | x4 | 36 | Clear nuclear localization, multi-db cross-validated |
| Protein Size | 10/10 | x1 | 10 | Medium (577 aa), convenient for biochemical experiments |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=46 papers), only limited foundational research |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 59.8), 11% high confidence, 46% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **123.5/180** | |
| **Normalized Total** | | | **67.5/100** | |

### 9. Final Decision

**SCORED: 67.5/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 46 papers, Extremely high research novelty
- Medium (577 aa), convenient for biochemical experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P33240
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CSTF2%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P33240
- STRING: https://string-db.org/cgi/network?identifiers=CSTF2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CSTF2

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000101811-CSTF2/subcellular

![](https://images.proteinatlas.org/427/23_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/427/23_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/427/2_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/427/2_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/427/3_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/427/3_A5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P33240 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 16..94; /note="RRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR025742;IPR026896;IPR038192;IPR012677;IPR035979;IPR000504; |
| Pfam | PF14327;PF14304;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101811-CSTF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BARD1 | Intact, Biogrid | true |
| CDC73 | Intact, Biogrid | true |
| CPSF2 | Intact, Biogrid | true |
| CPSF6 | Biogrid, Opencell | true |
| SYMPK | Intact, Biogrid | true |
| UBQLN2 | Intact, Biogrid | true |
| AKAP8L | Intact | false |
| ATP23 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
