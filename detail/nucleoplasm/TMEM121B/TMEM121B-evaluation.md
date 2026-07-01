---
type: protein-evaluation
gene: "TMEM121B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM121B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM121B |
| 蛋白名称 | Transmembrane protein 121B |
| 蛋白大小 | 578 aa / 58.4 kDa |
| UniProt ID | Q9BXQ6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 578 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=59.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CECR6; CECR6/TMEM121 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=2 broad=2
- AF pLDDT=59.3 PDB=0
- InterPro: CECR6; CECR6/TMEM121
- Pfam: CECR6_TMEM121
- PPI degree=0 ChIP: None
38703760: Gut-brain bidirectional determination in regulating the residual feed intake of  | 39120548: Exploring the relationship between anal fistula and colorectal cancer based on M

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TMEM121B是一个研究极度匮乏的核膜相关跨膜蛋白，578个氨基酸的蛋白骨架含有CECR6/TMEM121保守结构域（IPR032776/PF14997），该结构域家族的功能至今完全未知。AlphaFold预测pLDDT仅59.3且无PDB结构，结合PPI degree=0的极端孤立互作网络，TMEM121B代表了NEW核蛋白中信息最稀薄、新颖性最高的一类。HPA Approved的Nucleoplasm定位加上Plasma membrane和Vesicles的多重定位提示该蛋白可能在核膜与质膜之间动态穿梭——这是内体循环或核膜物质转运蛋白的经典特征。

在结构预测方面，pLDDT=59.3的低置信度暗示TMEM121B含有大量内在无序区域（IDR）或高度柔性的loop区段。跨膜预测（基于TMEM命名家族）表明该蛋白至少含有一个跨膜α-螺旋，极可能嵌入内体膜、核膜或质膜。CECR6_TMEM121（PF14997）结构域的具体拓扑结构未知，但其在进化中的保守性（从无脊椎动物到脊椎动物均存在同源基因）提示不可忽视的基础细胞生物学功能。

从TE调控研究角度看，TMEM121B的优势与挑战同样突出。优势在于极度新颖（PubMed=2，得分10/10），意味着该蛋白几乎完全未被功能性研究覆盖——任何发现都可能是首创性的。挑战在于缺少任何PPI伙伴、功能注释或疾病关联作为研究切入线索。唯一的文献关联来自GWAS/MR研究：TMEM121B所在位点与直肠癌（PMID:39120548）及鸭饲料效率（PMID:38703760）相关，但这些关联的分子机制完全未知。

TMEM121B的综合评分（71.6/100）主要受其高新颖性和核定位特异性支撑。作为核质膜的潜在组分，TMEM121B可能参与核孔复合体构成、核-质物质转运或核膜内体接触位点的形成。建议的实验验证策略为：（1）CRISPR敲除后进行转录组/蛋白质组学分析以获取功能性线索；（2）免疫共沉淀-质谱（Co-IP/MS）鉴定互作蛋白；（3）超分辨率显微镜确定核膜vs核质的精确亚细胞定位。两个PubMed文献为0的蛋白之一（PubMed=2）——TMEM121B是真正的"暗蛋白质"（dark protein），其功能发现将具有重大基础细胞生物学意义。

**蛋白全称**: Transmembrane protein 121B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026624 |
| InterPro | IPR032776 |
| Pfam | PF14997 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 121B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026624 |
| InterPro | IPR032776 |
| Pfam | PF14997 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BXQ6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000183307-TMEM121B

![](https://images.proteinatlas.org/68790/1416_D12_6_red_green.jpg)
![](https://images.proteinatlas.org/68790/1416_D12_8_red_green.jpg)
![](https://images.proteinatlas.org/68790/1374_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/68790/1374_E3_4_red_green.jpg)
![](https://images.proteinatlas.org/68790/1376_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/68790/1376_E3_3_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 39120548 | Exploring the relationship between anal fistula and colorectal cancer based on Mendelian randomization and bioinformatic | J Cell Mol Med 2024 |
| 38703760 | Gut-brain bidirectional determination in regulating the residual feed intake of small-sized meat ducks. | Poult Sci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM121B

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LHFPL4 | STRING | 413 |
| TMEM121B | STRING | 413 |
| SLC35E4 | STRING | 507 |
| ATP5MGL | STRING | 540 |
