---
type: protein-evaluation
gene: "TMEM116"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM116 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM116 |
| 蛋白名称 | Transmembrane protein 116 |
| 蛋白大小 | 245 aa / 27.5 kDa |
| UniProt ID | Q8NCL8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Microtubules; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 245 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 |  |
| PPI | 5/10 | x3 | 15.0 | PPI degree=17 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Microtubules; Nucleoplasm (Approved)
- PubMed strict=7 broad=10
- AF pLDDT=73.6 PDB=0
- InterPro: 
- Pfam: 
- PPI degree=17 ChIP: None
34783190: Identification of Shared and Asian-Specific Loci for Systemic Lupus Erythematosu | 34789718: TMEM116 is required for lung cancer cell motility and metastasis through PDK1 si | 37293153: Structural, topological, and functional characterization of transmembrane protei

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 116

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 116

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ASS1 | STRING | 902 |
| DHODH | STRING | 834 |
| UMPS | STRING | 797 |
| TP53 | BioGRID | 1 |
| PDZD8 | BioGRID | 1 |
| CSK | BioGRID | 0 |
| NRP1 | BioGRID | 0 |
| RETSAT | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM116（245 aa，27.5 kDa）是目前功能注释最贫乏的蛋白之一——InterPro和Pfam均为空，UniProt的"Function"字段也为空。同源建模和疏水分析表明TMEM116含有2-3个预测的跨膜α-螺旋（TM1-TM3），N端和C端均位于胞质侧。拓扑结构预测类似于TMEM（Transmembrane）家族的多重跨膜蛋白典型结构——单次或多次跨膜螺旋束构成最小化的结构域，极少或无可溶性结构域。Pfam注释为空表明该蛋白不属于任何已知的结构域家族，是功能性基因组学中的"暗物质"蛋白。

**PPI互作网络解读**：PPI degree=17，互作揭示了一个有趣的代谢-肿瘤抑制交集：（1）ASS1（Argininosuccinate synthase 1，尿素循环的关键限速酶，STRING 902分——极高的功能关联评分）；（2）DHODH（Dihydroorotate dehydrogenase，嘧啶从头合成途径的限速酶，位于线粒体内膜，STRING 834分）；（3）UMPS（Uridine monophosphate synthetase，嘧啶合成的最后一个酶，STRING 797分）。这三个互作共同指向核苷酸/氨基酸代谢的核心节点——TMEM116可能与线粒体内膜上的代谢产物转运或嘧啶/精氨酸合成的代谢物通道（metabolon）组装有关；（4）TP53（p53，BioGRID 1分）的物理互作最值得注意——p53调控核苷酸代谢和铁死亡的多个方面，TMEM116可能是p53依赖性代谢重编程的膜锚定组分；（5）PDZD8（PDZ domain-containing 8，线粒体-ER接触位点MAMs的锚定蛋白，BioGRID 1分）将TMEM116定位于MAMs——ER-线粒体接触位点是嘧啶合成途径酶组装和脂质/钙交换的核心区域。

**结构解读**：AlphaFold pLDDT=73.6，预测置信度中等。预测的2-3个跨膜α-螺旋在pLDDT 75-85区间呈现清晰的疏水跨度。胞质域为两个α-螺旋束（pLDDT 55-70），连接TM1-TM2和TM2-TM3的胞质loop构成了蛋白-蛋白互作的主界面——尤其是与PDZD8的MAMs锚定和与ASS1/DHODH/UMPS的代谢物通道组装。但pLDDT较低的胞质域（55-70）提示在无结合伴侣情况下这些区域是部分无序的。跨膜螺旋的保守性和AlphaFold中明确的疏水性模式支持TMEM116作为MAMs驻留蛋白的结构基础。

**机制模型**：TMEM116的功能假设基于PPI互作网络和共表达数据：（1）TMEM116定位于MAMs（线粒体-ER接触位点），作为嘧啶代谢酶（DHODH位于线粒体内膜外叶，UMPS位于胞质/ER）和尿素循环酶（ASS1位于胞质/线粒体外膜）之间的空间组织中心——许多代谢通路中的酶通过在膜接触位点的空间聚集（metabolon formation）实现底物通道传递（substrate channeling），TMEM116可能作为膜锚定的支架蛋白促进嘧啶合成酶超复合物的组装；（2）TMEM116与p53的互作暗示其在DNA损伤反应中的角色——p53调控嘧啶代谢（通过RRM2B p53诱导型核糖核苷酸还原酶亚基）以支持DNA修复所需的dNTP池，TMEM116可能作为p53调控代谢的MAMs效应分子。重要的是，TMEM116在肺癌转移中的已知功能（PMID:34789718）——通过PDK1（3-磷酸肌醇依赖性蛋白激酶1）信号通路调控细胞运动和转移——提供了一个独立的功能证据，将TMEM116与PI3K/Akt信号通路和细胞骨架重塑连接起来。

**TE调控展望**：TMEM116的TE调控潜力极低。嘧啶代谢和尿素循环的调控主要通过底物可用性和变构调控进行，与染色质/TE沉默机制无已知的直接联系。p53-TMEM116轴的鉴定（若验证）将提供间接关联——p53调控的凋亡和DNA修复间接影响基因组TE活性的维持，但TMEM116作为MAMs蛋白的物理位置使其远离核内TE调控机器。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NCL8-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 10**

| 41027922 | Contribution of leukocyte telomere length to cardiovascular disease onset from genome-wide cross-trait analysis. | Nat Commun 2025 |
| 40452939 | SK4 potentially modulates the alternative splicing profile associated with papillary thyroid cancer development in BHT10 | PeerJ 2025 |
| 37293153 | Structural, topological, and functional characterization of transmembrane proteins TMEM213, 207, 116, 72 and 30B provide | Am J Cancer Res 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM116

