---
type: protein-evaluation
gene: "LYPD1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LYPD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LYPD1 |
| 蛋白名称 | Ly6/PLAUR domain-containing protein 1 |
| 蛋白大小 | 141 aa / 15.2 kDa |
| UniProt ID | Q8N2G4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 141 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=21 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=76.0; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | LY6_UPA_recep-like; Snake_toxin-like_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=59 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=21 broad=43
- AF pLDDT=76.0 PDB=1
- InterPro: LY6_UPA_recep-like; Snake_toxin-like_sf
- Pfam: UPAR_LY6
- PPI degree=59 ChIP: None
17488974: GPR39 splice variants versus antisense gene LYPD1: expression and regulation in  | 36963497: Identification of GPI-anchored protein LYPD1 as an essential factor for odontobl | 37251737: GATA6 regulates anti-angiogenic properties in human cardiac fibroblasts via modu

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ly6/PLAUR domain-containing protein 1

**功能**: Believed to act as a modulator of nicotinic acetylcholine receptors (nAChRs) activity. In vitro increases receptor desensitization and decreases affinity for ACh of alpha-4:beta-2-containing nAChRs. May play a role in the intracellular trafficking of alpha-4:beta-2 and alpha-7-containing nAChRs and may inhibit their expression at the cell surface. May be involved in the control of anxiety

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016054 |
| InterPro | IPR045860 |
| Pfam | PF00021 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

LYPD1是Ly6/PLAUR(LY6-Urokinase Plasminogen Activator Receptor)超家族成员，编码一个141 aa的GPI锚定膜蛋白前体。其核心功能域为LY6_UPA_recep-like结构域(IPR016054/PF00021)，该结构域采用"三指"(Three-Finger)折叠拓扑——3个β-发夹环从中心疏水核心辐射而出，形似蛇毒神经毒素结构(Snake_toxin-like_sf)。在nAChRs调控中，LYPD1的三个指环结构通过空间位阻或变构效应调节α4β2和α7亚型nAChR的受体脱敏速率和ACh亲和力(UniProt功能注释)。

HPA显示其定位于Nucleoplasm、Plasma membrane和Vesicles(Approved)，这种三位一体定位模式与GPI锚定蛋白的转运/再分配机制一致。在核质中的意外出现(原本预期主要在质膜)可能反映以下机制：GPI锚定蛋白在胞内GPI锚定生物合成后先聚集在内质网-高尔基体中间区室，部分LYPD1可能在锚定失败后以可溶形式进入核质，或是核质中存在某种GPI-独立剪接变体。

PPI证据中与TUBA4A和TUBA1A(微管α-微管蛋白)的互作(BioGRID)最值得注意。在神经元中，nAChR囊泡沿微管进行顺向运输至突触前膜，LYPD1作为nAChR的伴侣蛋白可能与微管蛋白直接结合，参与受体的胞内运输与质膜靶向。LYPD1在肺腺癌中通过激活PI3K/AKT信号通路促进肿瘤进展(PMID:42303101)，这暗示其核质功能超越传统的nAChR伴侣角色。

pLDDT=76.0，PDB=1，反映了该三指折叠结构的实验证据。然而，LYPD1仅141 aa且富含二硫键(Cys残基占比约10%)的核心结构域使得定点突变或功能研究在可操作残基选择上受限。核质定位功能的最直接验证途径应聚焦于：核质LYPD1是否与核内ACh受体信号存在功能性耦合，或是否作为甲基化修饰的底物参与基因表达调控。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N2G4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000150551-LYPD1

![](https://images.proteinatlas.org/68333/1984_C11_4_cr5e5903e44d642_red_green.jpg)
![](https://images.proteinatlas.org/68333/1984_C11_6_cr5e5903e44ea50_red_green.jpg)
![](https://images.proteinatlas.org/68333/1899_G12_6_cr5e7244cec1b52_red_green.jpg)
![](https://images.proteinatlas.org/68333/1899_G12_29_cr5e7244cec2c16_red_green.jpg)
![](https://images.proteinatlas.org/68333/1913_K9_1_red_green.jpg)
![](https://images.proteinatlas.org/68333/1913_K9_3_red_green.jpg)

### PubMed 文献

**PubMed count: 43**

| 42303101 | LYPD1 promotes the progression of lung adenocarcinoma through activating the PI3K/AKT signaling pathway. | Arch Biochem Biophys 2026 |
| 41270577 | Increased vulnerability to noise exposure of low spontaneous rate type 1C spiral ganglion neuron synapses with inner hai | Hear Res 2026 |
| 40502816 | Exploring T-cell bispecific antibodies in gynecologic malignancy. | Gynecol Oncol Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LYPD1

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SPINK7 | physical | Huttlin EL (2017) |
| SPSB3 | physical | Huttlin EL (2017) |
| VWDE | physical | Huttlin EL (2017) |
| PCSK5 | physical | Huttlin EL (2017) |
| NPTX1 | physical | Huttlin EL (2017) |
| TUBA4A | physical | Huttlin EL (2017) |
| TUBA1A | physical | Huttlin EL (2017) |
| EOGT | physical | Huttlin EL (2017) |
| WNT5A | physical | Huttlin EL (2017) |
| ZNF146 | physical | Huttlin EL (2017) |

