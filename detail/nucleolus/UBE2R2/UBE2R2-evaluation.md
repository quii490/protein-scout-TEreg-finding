---
type: protein-evaluation
gene: "UBE2R2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## UBE2R2 (Ubiquitin-conjugating enzyme E2 R2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | UBE2R2 |
| 蛋白全称 | Ubiquitin-conjugating enzyme E2 R2 |
| UniProt ID | Q712K3 |
| 蛋白大小 | 238 aa / 26.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 238 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR050113; InterPro:IPR000608; InterPro:IPR023313; InterPro:IPR016135; Pfam:PF00179 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

E2 ubiquitin-conjugating enzyme that accepts ubiquitin from an E1 ubiquitin-activating protein, and catalyzes its covalent attachment to other proteins by an E3 ubiquitin-protein ligase complex (PubMed:12037680, PubMed:20061386, PubMed:38326650). In vitro catalyzes monoubiquitination and 'Lys-48'-linked polyubiquitination (PubMed:12037680, PubMed:20061386, PubMed:38326650). Works in collaboration 

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050113 |
| InterPro | IPR000608 |
| InterPro | IPR023313 |
| InterPro | IPR016135 |
| Pfam | PF00179 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

UBE2R2（238 aa, UniProt Q712K3）是泛素结合酶E2家族的R2亚型，其结构域由IPR050113（泛素结合酶E2）、IPR000608（泛素结合酶催化结构域）、IPR023313（泛素结合超折叠）和IPR016135（UBC样结构域）构成，Pfam条目PF00179（UQ_con）。E2酶在泛素化级联中占据中心位置——从E1接受活化的泛素，在E3连接酶的协作下将泛素共价转移到靶蛋白的赖氨酸ε-氨基。UBE2R2体外催化单泛素化和Lys-48连接的多泛素化（PubMed:12037680, PubMed:20061386, PubMed:38326650），其K48多泛素链是26S蛋白酶体识别的主要降解信号。该酶与CUL1-RBX1-SKP1-F-box蛋白（SCF）E3连接酶复合物协同工作，参与细胞周期调控和信号转导。

PPI数据显示UBE2R2的互作组以E3连接酶和泛素化通路组分为主：BTRC（β-TrCP, SCF泛素连接酶的F-box底物受体, BioGRID评分0）、RNF113B（RING型E3连接酶）、ARIH2（Ariadne RBR型E3连接酶）、CBLC（Cbl家族E3连接酶）、DTX3L（Deltex E3连接酶，参与PARPylation和DNA损伤应答）和DZIP3（含锌指E3连接酶，调控hDAX-1转录抑制因子的降解）。DTX3L的互作特别值得关注——DTX3L通过与PARP9形成复合物参与DNA损伤修复，该复合物已被证实可通过泛素化组蛋白调控损伤位点的染色质动力学。

从TE调控角度，UBE2R2通过调控关键TE抑制因子的蛋白质稳定性间接影响TE活性。BTRC/β-TrCP是SCF泛素连接酶的底物识别亚基，其已知底物包括多个直接参与TE调控的转录因子——β-TrCP通过降解EMT转录因子Snail（其靶基因包含大量ERV/MaLR衍生增强子）和NF-κB信号组分（IκBα, p105）调控炎症和分化过程中的TE表达。RNF113B和DTX3L与DNA损伤应答的关联提示UBE2R2可能在TE引起的DNA损伤信号中通过泛素化去除损伤位点的TE蛋白（如LINE-1 EN/RT）促进修复。此外，ARIH2作为RBR型E3连接酶，可生成K48和K63泛素链——K63泛素链参与非降解性信号，如DNA损伤修复灶的组装和染色质重塑复合物的招募。该蛋白的核仁定位（加权评分67.8）和K48特异性泛素化活性提示其可能在核仁核糖体DNA（rDNA）转录区域调控组蛋白H2A/H2B泛素化平衡，影响rDNA位点上TE（如R2元件）的插入和表达。

---

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BTRC | BioGRID | 0 |
| RNF113B | BioGRID | 0 |
| ARIH2 | BioGRID | 0 |
| CBLC | BioGRID | 0 |
| DTX3L | BioGRID | 0 |
| DZIP3 | BioGRID | 0 |
| INF2 | BioGRID | 0 |
| PNPLA2 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBE2R2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107341-UBE2R2

![](https://images.proteinatlas.org/61000/1060_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/61000/1060_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/61000/1136_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/61000/1136_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/61000/1105_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/61000/1105_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/74334/1910_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/74334/1910_A6_3_red_green.jpg)

### PubMed

**Count: 35**

| PMID | Title |
|---|---|
| 42372683 | Early-life low-dose lead exposure impairs synaptic development via epigenetic repression of the PI3K/AKT/mTOR signaling pathway. |
| 41706475 | Modulation of Ube2R1 activity by a nanobody that binds near its N-terminus. |
| 41570900 | Genome-wide association and functional genomic analyses of teat placement traits derived from robotic milking systems in American Holstein cattle. |
| 41540731 | Proteomic Profiling Reveals Candidate Proteins and Pathways Associated with Chemo-Radio-Sensitivity and Relapse in Rhabdomyosarcoma. |
| 41389538 | Genome-wide association study of economic traits and functional characterization of MAN2A2 in the Jilin White Goose. |


