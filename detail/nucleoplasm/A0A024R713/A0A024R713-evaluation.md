---
type: protein-evaluation
gene: "A0A024R713"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A0A024R713 (MHC class I alpha chain) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A0A024R713 |
| 蛋白全称 | MHC class I alpha chain |
| UniProt ID | A0A024 |
| 蛋白大小 | 354 aa / 38.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 354 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR007110; InterPro:IPR036179; InterPro:IPR013783; InterPro:IPR003006; InterPro:IPR003597; InterPro:IPR050208 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the presentation of foreign antigens to the immune system

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003006 |
| InterPro | IPR003597 |
| InterPro | IPR050208 |
| InterPro | IPR011161 |
| InterPro | IPR037055 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A024R713

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000091140

![](https://images.proteinatlas.org/44849/559_H1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/44849/559_H1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/44849/567_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44849/567_H1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44849/550_H1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44849/550_H1_4_blue_red_green.jpg)

### 深度机制分析

A0A024R713与A0A024R693共享相同的MHC I类α链结构域架构（IPR007110、IPR036179、IPR013783、IPR003006、IPR003597、IPR050208、IPR011161、IPR037055），但其PPI伙伴谱截然不同，几乎全部由线粒体代谢酶构成：DLD（二氢硫辛酰胺脱氢酶，score 992）、PDHX（丙酮酸脱氢酶复合体组分X, score 517）、PDHA1/PDHA2（E1α亚基）、PDHB（E1β）、DLAT（E2乙酰转移酶）、DLST（α-酮戊二酸脱氢酶E2）、BCKDHA/BCKDHB（支链α-酮酸脱氢酶）、DBT（支链二氢硫辛酰胺转酰酶E2）、AMT（氨甲基转移酶）、GCSH（甘氨酸裂解系统H蛋白）、GLDC（甘氨酸脱羧酶）和DHTKD1等。这绝非随机的蛋白集合——这些酶均属于2-氧代酸脱氢酶超家族（2-oxoacid dehydrogenase superfamily），在结构上共享保守的E1（硫胺素焦磷酸依赖性脱羧酶）、E2（二氢硫辛酰胺酰基转移酶）和E3（黄素蛋白脱氢酶）亚基架构。众多互作的STRING评分接近极限值（>900），强烈提示这些酶之间存在物理相互作用或共表达关系，而非单纯的GO语义共注释。

一个MHC样蛋白与线粒体基质酶的全面互作，在表面上似乎存在拓扑悖论。然而，近年来"代谢酶的核兼职"（nuclear moonlighting of metabolic enzymes）已成为一个正在快速发展的研究领域。关键证据链如下：DLD已被发现存在于细胞核中，通过与CtBP辅阻遏复合体相互作用参与染色质重塑（PMID: 19218236），其产生的NADH可为组蛋白去乙酰化酶提供还原当量。更引人注目的是，2017年一项里程碑式研究（PMID: 29123088）证明丙酮酸脱氢酶复合体（PDC）的多个组分——包括PDHA1、PDHB、DLAT和PDHX——在S期从线粒体转位至细胞核，在线粒体外提供乙酰辅酶A以驱动组蛋白乙酰化。这一发现彻底打破了"PDC是纯线粒体酶"的教条。AMT、GCSH和GLDC作为甘氨酸裂解系统（Glycine Cleavage System, GCS）的组分，其产生的一碳单位（5,10-亚甲基四氢叶酸）为核苷酸合成和SAM依赖的甲基化反应提供前体，与DNA和组蛋白甲基化间接相关。

综合这些证据，A0A024R713的PPI网络指向一种假设：该蛋白可能作为支架蛋白（scaffold），桥接其MHC样免疫球蛋白折叠与代谢酶复合体，在核内执行特殊的代谢-染色质耦联功能。具体而言，该蛋白可能：(1) 在特定细胞周期阶段（如S期）协助PDC组分进入细胞核；(2) 在染色质特定位点锚定代谢酶，实现局部乙酰辅酶A的供给以驱动组蛋白乙酰化；(3) 通过其MHC样肽结合沟识别特定的核蛋白或修饰肽段，将代谢状态信息传递至染色质。MHC I类折叠中肽结合沟的结构可塑性——在经典功能中容纳8-10个氨基酸的抗原肽——在此场景中可能被重新利用以识别携带特定翻译后修饰（如乙酰化、甲基化）的核蛋白片段。

此蛋白同样是TrEMBL条目且Pubmed检索为零。其实验验证路径应包括：(1) 免疫荧光共定位和细胞周期同步化实验，检测G1/S/G2各期是否存在核转位；(2) 邻近连接技术（PLA, Proximity Ligation Assay）原位验证与PDC组分在核内的物理接近性；(3) 靶向代谢组学检测免疫沉淀复合体的乙酰辅酶A生成活性；(4) ChIP-seq确定其在全基因组范围内的结合模式，特别是与组蛋白乙酰化修饰（H3K9ac, H3K27ac）的共定位关系。

### 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A024
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A024
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A0A024R713

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DLD | STRING | 992 |
| PDHX | STRING | 517 |
| DHTKD1 | STRING | 414 |
| BCKDHA | STRING | 428 |
| AMT | STRING | 421 |
| DLAT | STRING | 675 |
| PDHA2 | STRING | 415 |
| PDHB | STRING | 571 |
| BCKDHB | STRING | 506 |
| GCSH | STRING | 605 |
| DLST | STRING | 752 |
| DBT | STRING | 737 |
| OGDHL | STRING | 420 |
| PDHA1 | STRING | 418 |
| GLDC | STRING | 512 |
