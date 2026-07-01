---
type: protein-evaluation
gene: "LTB4R2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LTB4R2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LTB4R2 |
| 蛋白名称 | Leukotriene B4 receptor 2 |
| 蛋白大小 | 358 aa / 37.9 kDa |
| UniProt ID | Q9NPC1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 358 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=23 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=81.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Leukotriene_B4_rcpt |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=57 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=23 broad=145
- AF pLDDT=81.1 PDB=0
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Leukotriene_B4_rcpt
- Pfam: 7tm_1
- PPI degree=57 ChIP: None
38097183: Leukotriene B4 receptor 2 governs macrophage migration during tissue inflammatio | 28658281: Next-generation sequencing of the human TRPV1 gene and the regulating co-players | 34298691: CSNK1A1, KDM2A, and LTB4R2 Are New Druggable Vulnerabilities in Lung Cancer.

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Leukotriene B4 receptor 2

**功能**: Low-affinity receptor for leukotrienes including leukotriene B4. Mediates chemotaxis of granulocytes and macrophages. The response is mediated via G proteins that activate a phosphatidylinositol-calcium second messenger system. The rank order of affinities for the leukotrienes is LTB4 > 12-epi-LTB4 > LTB5 > LTB3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR003981 |
| InterPro | IPR003982 |
| Pfam | PF00001 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LTA4H | STRING | 892 |
| RANBP9 | BioGRID | 1 |
| LTB4R2 | BioGRID | 1 |
| AKT1 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| CSNK2B | BioGRID | 1 |
| CEBPZ | BioGRID | 1 |
| FOLR1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NPC1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000213906-LTB4R2

![](https://images.proteinatlas.org/72921/1501_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/72921/1501_H5_4_red_green.jpg)
![](https://images.proteinatlas.org/72921/1577_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/72921/1577_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/72921/1522_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/72921/1522_H5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 145**

| 41887306 | Characterisation of eicosanoid-regulating genes in Atlantic salmon: insights into the control of pro-inflammatory and an | Fish Shellfish Immunol 2026 |
| 41482602 | LTB4 Activates the MAP Kinase Pathway in Endothelial Cells to Cause Long-Lasting Neutrophil Tethering, MCP-1 and NO Rele | Scand J Immunol 2026 |
| 41381763 | Structure-based identification of compounds with potential as selective BLT1 antagonists. | Sci Rep 2025 |

### 深度机制分析

LTB4R2是一种经典的G蛋白偶联受体（GPCR，358 aa, 37.9 kDa），属于视紫红质类GPCR超家族（GPCR_Rhodpsn, IPR000276），其结构域架构以7次跨膜螺旋束（7tm_1, PF00001）为核心，这是GPCR家族的标志性折叠。AlphaFold预测的pLDDT为81.1，7TM区域的预测置信度较高，但胞外环（ECL）和胞内环（ICL）区域因柔性较高而信度下降。由于无PDB实验结构验证，配体结合口袋的精确构象及其在与白三烯B4（LTB4）结合时的动态变化仍待实验确定。

LTB4R2作为低亲和力LTB4受体，通过G蛋白激活磷脂酰肌醇-钙第二信使系统，介导粒细胞和巨噬细胞的趋化性。其膜定位（Plasma membrane）为经典受体功能，但HPA同时记录的Nucleoplasm定位（Supported级别）则提出了非经典核受体的可能性。在GPCR家族中，已有多例报道某些受体可以在配体刺激下转位至核膜或核质内部，直接参与核内信号调控。PPI网络（BioGRID degree=57）中，LTA4H（STRING评分892）作为LTB4合成通路中的关键水解酶，与RANBP9（核质转运蛋白）和TRIM25（E3泛素连接酶）的互作尤其值得关注——后者是已知的抗病毒先天免疫和RNA结合调控因子。

文献证据指向LTB4R2在巨噬细胞介导的组织炎症中调控细胞迁移（PMID:38097183），以及在肺癌中的可药性脆弱性（PMID:34298691）。与CSNK2B（酪蛋白激酶2调节亚基）的互作加上与CEBPZ（CCAAT增强子结合蛋白）的关联提示LTB4R2的核定位可能通过磷酸化级联间接参与转录调控。在TE调控的语境下，LTB4R2在核质中的存在可能使其作为炎症信号传感器——炎症刺激→LTB4配体→LTB4R2信号→核内转录因子激活→TE去抑制/转录激活通路值得深入探索。GPCR的7TM折叠在pLDDT=81.1时相对可信，这为基于结构的虚拟筛选以鉴定可能影响TE调控的小分子配体提供了出发点。

