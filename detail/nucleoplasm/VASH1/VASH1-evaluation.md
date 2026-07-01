---
type: protein-evaluation
gene: "VASH1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## VASH1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VASH1 |
| 蛋白名称 | Tubulinyl-Tyr carboxypeptidase 1 |
| 蛋白大小 | 365 aa / 41.0 kDa |
| UniProt ID | Q7L8A9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Centrosome; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 365 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=92 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=78.3; PDB=14 |
| 调控结构域 | 4/10 | x2 | 8.0 | VASH1 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=18 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Basal body; Centrosome; Cytosol; Nucleoplasm (Approved)
- PubMed strict=92 broad=261
- AF pLDDT=78.3 PDB=14
- InterPro: VASH1
- Pfam: Vasohibin
- PPI degree=18 ChIP: None
37716348: Microtubule detyrosination by VASH1/SVBP is regulated by the conformational stat | 40179877: MicroRNA mechanisms instructing Purkinje cell specification. | 34995817: MiR-143-3p facilitates motility and invasiveness of endometriotic stromal cells 

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

VASH1（Vasohibin-1）是一个365 aa的微管去酪氨酸化酶，其核心结构域为Vasohibin家族保守区（Pfam PF14822, InterPro IPR028131），负责催化α-微管蛋白C端酪氨酸残基的切除。该蛋白需要辅因子SVBP（Small Vasohibin-Binding Protein）的协助才能发挥完整酶活性。AlphaFold2预测pLDDT=78.3，PDB数据库中已有14个实验结构（得分9/10），大部分为VASH1-SVBP复合物与微管或抑制剂的共晶结构，结构解析度极高，为该蛋白的理性药物设计奠定了坚实基础。

VASH1的PPI网络规模较小（degree=18），但互作伙伴涵盖了重要的分子伴侣系统。与HSPA8、HSPA6、HSPA1L等多个Hsp70家族成员的BioGRID互作提示VASH1的折叠和稳定性受到分子伴侣网络的严格调控。DHPS（脱氧hypusine合酶）的互作则暗示VASH1可能与翻译调控存在交叉对话。遗憾的是这些互作缺乏高置信度实验评分，需要co-IP或交联质谱等方法的验证。

VASH1的酶学机制已得到深入研究：PMID:29146869、31171830、31235910、31235911、31270470等多篇文献系统阐明了其催化微管去酪氨酸化的分子机制。这种翻译后修饰调控微管动力学、有丝分裂纺锤体长度和定位，对染色体精确分离至关重要（PMID:31171830）。VASH1在核质中的Approved级别定位尤其耐人寻味——核质中存在微管蛋白池，VASH1可能通过调控核内微管蛋白的酪氨酸化状态影响核骨架动态或转录因子转运。最新研究（PMID:42312425）发现FGF13缺失通过抑制VASH1介导的微管去酪氨酸化改善紫杉醇诱导的神经性疼痛，凸显VASH1在疾病中的核心角色。

作为经典微管调控因子的核质定位蛋白，VASH1提供了一个有趣的范式——同一酶活性在不同亚细胞区室（胞质微管 vs 核质微管蛋白池）可能产生截然不同的功能输出。92篇PubMed文献（得分7/10）表明研究已有较深积累，但核质中VASH1的特异性底物和功能仍有待挖掘。VASH1在基底小体（Basal body）和中心体（Centrosome）的额外定位进一步支持其在微管组织中心的协调功能。

### 补充分析 (UniProt API)

**蛋白全称**: Tubulinyl-Tyr carboxypeptidase 1

**功能**: Tyrosine carboxypeptidase that removes the C-terminal tyrosine residue of alpha-tubulin, thereby regulating microtubule dynamics and function (PubMed:29146869, PubMed:31171830, PubMed:31235910, PubMed:31235911, PubMed:31270470). Critical for spindle function and accurate chromosome segregation during mitosis since microtubule detyrosination regulates mitotic spindle length and postioning (PubMed:31171830). Acts as an angiogenesis inhibitor: inhibits migration, proliferation and network formation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028131 |
| Pfam | PF14822 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CCDC23 | BioGRID | 0 |
| DHPS | BioGRID | 0 |
| HSPA8 | BioGRID | 0 |
| HSPA6 | BioGRID | 0 |
| HSPA1L | BioGRID | 0 |
| AMY1C | BioGRID | 0 |
| RAB6B | BioGRID | 0 |
| C9orf142 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7L8A9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000071246-VASH1

![](https://images.proteinatlas.org/653/2167_D1_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2167_D1_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_14_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000071246-VASH1

![](https://images.proteinatlas.org/653/2167_D1_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2167_D1_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_14_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000071246-VASH1

![](https://images.proteinatlas.org/653/2167_D1_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2167_D1_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/653/2120_A1_14_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 261**

| 42312425 | FGF13 Deficiency Ameliorates Paclitaxel-Induced Neuropathic Pain by Inhibiting VASH1-Mediated Microtubule Detyrosination | Adv Sci (Weinh) 2026 |
| 41815567 | Comprehensive analysis for the role of macrophage-driven genes in abdominal aortic aneurysm. | Cardiovasc Diagn Ther 2026 |
| 41803714 | A nine-gene diagnostic model for IgA nephropathy based on multi-cohort machine learning: integrating gene expression and | Ren Fail 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/VASH1

