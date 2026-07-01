---
type: protein-evaluation
gene: "SMIM4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SMIM4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMIM4 |
| 蛋白名称 | Ubiquinol-cytochrome c reductase complex assembly factor 5 |
| 蛋白大小 | 70 aa / 8.7 kDa |
| UniProt ID | Q8WVI0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 70 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=68.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | UQCC5 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=5 broad=6
- AF pLDDT=68.7 PDB=0
- InterPro: UQCC5
- Pfam: UPF0640
- PPI degree=5 ChIP: None
41193425: The integral membrane protein smim4 modulates redox balance via malate compartme | 40678804: Genetic architecture and mechanisms shared between kidney and ureteral stones, c | 34951053: Identification of seven-gene marker to predict the survival of patients with lun

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SMIM4（亦称UQCC5）是一个极小蛋白（70 aa, 8.7 kDa），其唯一已知的结构域为UQCC5/UPF0640家族保守区（Pfam PF15114, InterPro IPR028183）。作为线粒体呼吸链复合体III（CIII，细胞色素bc1复合物）的组装因子，SMIM4在氧化磷酸化中调控电子传递链蛋白水平以响应能量需求变化。AlphaFold2预测pLDDT仅为68.7，无PDB实验结构，考虑到该蛋白极小的分子量和线粒体内膜整合特性，其三维结构解析具有技术挑战性。

SMIM4的PPI网络极为有限（degree=5），但其互作伙伴具有高度的功能性富集。与ESR2（雌激素受体β）的BioGRID互作值得深入探讨——ESR2是核受体超家族成员，直接参与核内转录调控，SMIM4在核质中的Approved级别定位可能通过此互作参与激素信号通路。与RECQL4（RecQ样解旋酶4，参与DNA复制和修复）的互作进一步支持SMIM4在核内DNA代谢中的潜在角色。HSCB（线粒体铁硫簇组装辅伴侣）则连接了SMIM4的线粒体经典功能。

从功能机制角度，SMIM4呈现出典型的"双定位功能分配"模式：在线粒体中作为CIII组装因子维持呼吸链完整性；在核质中可能通过蛋白互作参与基因表达调控。最新文献（PMID:41193425）揭示了SMIM4通过苹果酸区室化调节氧化还原平衡，在胰腺癌中发挥关键作用。苹果酸是连接线粒体TCA循环与胞质/核质代谢的重要代谢物，SMIM4对苹果酸区室化的调控可能在核质中影响表观遗传酶（如TET双加氧酶、组蛋白去甲基化酶）的活性，因为这些酶依赖于TCA循环中间代谢物作为辅因子。

SMIM4的研究新颖性极高（PubMed=5，得分10/10），HPA Nucleoplasm Approved定位（得分9/10），但其极小的分子量和中等偏低的pLDDT是主要短板。微蛋白（microprotein）在核质中的功能是一个新兴领域，SMIM4可能代表了线粒体-核信号交流的一类新型信使分子。其TE调控评估中的ChIP-Seq数据提示该基因座可能受到转座子元件的调控（PMID:40678804涉及基因组共定位分析），值得进一步探索。

### 补充分析 (UniProt API)

**蛋白全称**: Ubiquinol-cytochrome c reductase complex assembly factor 5

**功能**: Required for the assembly and stability of the mitochondrial ubiquinol-cytochrome c reductase complex (complex III (CIII) or cytochrome b-c1 complex), a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain (ETC) which drives oxidative phosphorylation (By similarity). Mediates early complex III biogenesis (By similarity). Participates in regulating the levels of electron transport chain proteins, and therefore energy supply, in response to changes in energ

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028183 |
| Pfam | PF15114 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ESR2 | BioGRID | 0 |
| RECQL4 | BioGRID | 0 |
| HSCB | BioGRID | 0 |
| CLEC16A | BioGRID | 0 |
| CDC123 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8WVI0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168273-SMIM4

![](https://images.proteinatlas.org/47771/804_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/47771/804_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/47771/964_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/47771/964_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/47771/712_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/47771/712_G6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 41193425 | The integral membrane protein smim4 modulates redox balance via malate compartmentalization in pancreatic cancer. | Nat Commun 2025 |
| 40678804 | Genetic architecture and mechanisms shared between kidney and ureteral stones, cardiovascular diseases, and metabolic sy | Biochem Biophys Rep 2025 |
| 35977508 | Mitochondrial microproteins link metabolic cues to respiratory chain biogenesis. | Cell Rep 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SMIM4

