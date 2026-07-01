---
type: protein-evaluation
gene: "VAMP5"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## VAMP5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VAMP5 |
| 蛋白名称 | Vesicle-associated membrane protein 5 |
| 蛋白大小 | 116 aa / 12.8 kDa |
| UniProt ID | O95183 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 116 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=34 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Synaptobrevin-like; V_SNARE_CC; Vamp5 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=169 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=34 broad=45
- AF pLDDT=79.8 PDB=0
- InterPro: Synaptobrevin-like; V_SNARE_CC; Vamp5
- Pfam: Synaptobrevin
- PPI degree=169 ChIP: None
39909380: Topology-driven discovery of transmembrane protein S-palmitoylation. | 38674369: Exploring the Role of Extracellular Vesicles in the Pathogenesis of Tuberculosis | 40624080: Vesicle-associated membrane protein 5 is an intrinsic defense factor for embryon

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Vesicle-associated membrane protein 5

**功能**: May participate in trafficking events that are associated with myogenesis, such as myoblast fusion and/or GLUT4 trafficking

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001388 |
| InterPro | IPR042855 |
| InterPro | IPR042166 |
| InterPro | IPR042581 |
| Pfam | PF00957 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MDC1 | BioGRID | 0 |
| ATP4A | BioGRID | 0 |
| STX1A | BioGRID | 0 |
| STX4 | BioGRID | 0 |
| STX16 | BioGRID | 0 |
| SNAP23 | BioGRID | 0 |
| SNAP29 | BioGRID | 0 |
| LMNA | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95183-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168899-VAMP5

![](https://images.proteinatlas.org/35082/1612_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/35082/1612_B8_3_red_green.jpg)
![](https://images.proteinatlas.org/35082/1878_B8_31_red_green.jpg)
![](https://images.proteinatlas.org/35082/1878_B8_32_red_green.jpg)

### PubMed 文献

**PubMed count: 45**

| 42257837 | Targeting VAMP5 suppresses PLK1-driven growth of gliomas with high NDRG4 expression. | J Neurooncol 2026 |
| 41855695 | Integrative transcriptomic and machine learning analysis identifies core immune genes and pathways driving graft-versus- | Leuk Res 2026 |
| 41851715 | The Galectin-3-binding protein promotes angiogenesis in pancreatic cancer via simultaneous upregulation of VEGFA and dir | Cell Commun Signal 2026 |

### 深度机制分析

VAMP5（116 aa, 12.8 kDa）是囊泡相关膜蛋白（VAMP）/synaptobrevin家族的成员，属于SNARE蛋白超家族。SNARE蛋白以约60个氨基酸的保守卷曲螺旋（coiled-coil）SNARE基序为特征，通过四个SNARE基序（通常来自不同SNARE亚家族）的平行组装形成四螺旋束，将囊泡膜拉近靶膜以驱动膜融合。VAMP5结构域架构极为精简：N端含有一个Synaptobrevin样结构域（IPR001388），核心为V_SNARE卷曲螺旋（IPR042855），C端带有跨膜锚定螺旋。AlphaFold预测pLDDT=79.8，SNARE卷曲螺旋区域的预测置信度高（该区域趋向于形成稳定的α-螺旋）。

VAMP5的已知功能主要与肌生成和GLUT4（葡萄糖转运蛋白）运输相关，参与成肌细胞融合和胰岛素响应的GLUT4囊泡向质膜转运。然而，HPA将其定位为Nucleoplasm; Plasma membrane（Approved级别），质膜定位符合其作为v-SNARE参与GLUT4囊泡融合的经典功能，而核质定位则提出了非经典核内功能的假说。与其他v-SNARE蛋白不同，VAMP5的核质定位可能是SNARE蛋白中的一个相对独特现象。

PPI网络极为丰富（BioGRID degree=169），包括多种syntaxin（STX1A、STX4、STX16）和SNAP蛋白（SNAP23、SNAP29）等经典SNARE伴侣。值得特别关注的是与LMNA（核纤层蛋白A/C）和MDC1（DNA损伤检查点介质）的互作——LMNA是核纤层的主要结构组分，维持核的机械稳定性和染色质组织；MDC1是DNA双链断裂应答的关键支架蛋白。这两个互作将VAMP5与核结构维持和DNA损伤修复直接联系起来。

文献提示VAMP5是多功能蛋白——PLK1驱动的胶质瘤生长受VAMP5靶向抑制（PMID:42257837），胚胎发育中VAMP5是固有防御因子（PMID:40624080）。在TE调控方面，VAMP5最值得关注的假设是"核膜-核质SNARE轴"：VAMP5是否参与内核膜（INM）附近的膜融合事件，从而影响核纤层相关的异染色质组织？若VAMP5与LMNA的互作具有功能性后果，VAMP5可能通过调控核纤层组装来间接影响LAD（核纤层相关结构域）中的TE表达。DNA损伤修复与TE去抑制之间的关联是另一个有前景的方向——持续的DNA损伤可导致重复序列的去抑制，VAMP5-MDC1互作是否参与DNA损伤应答中的重复序列调控值得探索。

