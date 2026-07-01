---
type: protein-evaluation
gene: "NLRP10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NLRP10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NLRP10 |
| 蛋白名称 | NACHT, LRR and PYD domains-containing protein 10 |
| 蛋白大小 | 655 aa / 75.0 kDa |
| UniProt ID | Q86W26 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 655 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=30 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=73.4; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | DAPIN; DEATH-like_dom_sf; NACHT_NTPase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=15 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=30 broad=61
- AF pLDDT=73.4 PDB=1
- InterPro: DAPIN; DEATH-like_dom_sf; NACHT_NTPase
- Pfam: NACHT; PYRIN; WHD_NOD2
- PPI degree=15 ChIP: None
39351983: Molecular mechanisms of emerging inflammasome complexes and their activation and | 36941399: Epithelial Nlrp10 inflammasome mediates protection against intestinal autoinflam | 39424623: NLRP10 maintains epidermal homeostasis by promoting keratinocyte survival and P6

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: NACHT, LRR and PYD domains-containing protein 10

**功能**: Inhibits autoprocessing of CASP1, CASP1-dependent IL1B secretion, PYCARD aggregation and PYCARD-mediated apoptosis but not apoptosis induced by FAS or BID (PubMed:15096476). Displays anti-inflammatory activity (PubMed:20393137). Required for immunity against C.albicans infection (By similarity). Involved in the innate immune response by contributing to pro-inflammatory cytokine release in response to invasive bacterial infection (PubMed:22672233). Contributes to T-cell-mediated inflammatory resp

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004020 |
| InterPro | IPR011029 |
| InterPro | IPR007111 |
| InterPro | IPR050637 |
| InterPro | IPR041075 |
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PYCARD | STRING | 784 |
| CASP1 | STRING | 748 |
| BECN1 | STRING | 715 |
| AR | BioGRID | 1 |
| EGFR | BioGRID | 1 |
| STK26 | BioGRID | 1 |
| UBE4B | BioGRID | 1 |
| TBC1D22B | BioGRID | 0 |


### 深度机制分析

**结构域架构**：NLRP10（655 aa，75.0 kDa）是NLRP（NACHT, LRR and PYD domains-containing）家族的非典型成员，含有三个经典的结构域模块：（1）N端DAPIN/PYD（Pyrin domain，IPR004020，DEATH-like_dom_sf IPR011029）——属于死亡结构域超家族，介导同型蛋白-蛋白互作，是炎症小体（inflammasome）组装的信号枢纽；（2）中央NACHT_NTPase结构域（IPR007111，IPR027417，NACHT PF02463）——ATPase活性驱动蛋白寡聚化，形成炎症小体的结构骨架；（3）C端LRR结构域（IPR050637）——可能参与配体识别和自身抑制（autoinhibition）。NLRP10特殊之处在于它是NLRP家族中唯一缺乏LRR-完整性的成员（仅有部分LRR或LRR-like序列），这使其处于NLRP家族中进化上的独特位置。

**PPI互作网络解读**：PPI degree=15，核心互作为PYCARD/ASC（STRING 784分，炎症小体适配器）、CASP1（Caspase-1，STRING 748分，炎症小体的效应蛋白酶）。这一PYD-PYD（NLRP10-PYCARD）互作模块是炎症小体组装的经典通路。与EGFR（BioGRID 1分）和AR（雄激素受体，BioGRID 1分）的互作提示NLRP10可能与非经典的炎症信号通路交叉，而与BECN1（Beclin-1，STRING 715分）的互作连接了炎症小体信号和自噬调控。

**结构解读**：AlphaFold pLDDT=73.4（1个PDB结构验证），PYD域的pLDDT >85，形成经典的六α-螺旋束（Death domain fold），其酸性表面（helix-2/helix-3界面）负责PYCARD的PYD识别和炎症小体成核。NACHT域的pLDDT（60-75）反映了其在无核苷酸结合状态下的构象柔性；ATP结合后Walker A/B基序会经历显著的构象重排，驱动NACHT域闭合和寡聚化。LRR-like区域的pLDDT较低（<60），这与NLRP10被认为缺乏完整LRR结构域的特征一致。

**机制模型**：NLRP10作为炎症小体信号的抑制性调控因子（而非经典的模式识别受体），通过以下机制运作：（1）不直接识别病原相关分子模式（PAMP）或损伤相关分子模式（DAMP），而是作为"诱饵受体"或"竞争性抑制剂"通过PYD-PYD互作侵占PYCARD/ASC，阻止其他NLRP成员（如NLRP1、NLRP3）的炎症小体组装和CASP1激活（PMID:15096476）；（2）同时具有抗炎活性（PMID:20393137），在角质形成细胞的表皮稳态维持中发挥关键作用（PMID:39424623）；（3）NLRP10在核质中的定位（Approved）提示可能存在非经典核内炎症小体功能——在细胞核内，NLRP10可能通过AR互作参与雄激素受体靶基因的转录调控，将炎症信号与核受体信号整合。

**TE调控展望**：NLRP10的TE调控潜力主要体现在炎症小体信号与TE激活的交叉调控上。LINE-1和ERV的异常表达可激活cGAS-STING和NLRP3炎症小体通路，导致炎症因子（IL-1β、IL-18）释放。NLRP10作为炎症小体的抑制因子可能在限制TE驱动的慢性炎症中发挥"制动器"作用。PMID:42362760（2026年最新研究）发现NLRP10在脂滴上的定位和寡聚化受C端赖氨酸残基调控，暗示其在代谢应激与TE炎症反应之间的潜在桥梁功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q86W26-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000182261-NLRP10

![](https://images.proteinatlas.org/39498/413_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/39498/413_F12_3_red_green.jpg)
![](https://images.proteinatlas.org/39498/420_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/39498/420_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/39498/417_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/39498/417_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/40101/539_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/40101/539_G3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 61**

| 42362760 | C-terminal lysine residues localise NLRP10 at lipid droplets and govern NLRP10 oligomer formation. | EMBO Rep 2026 |
| 42304038 | The effect of Staphylococcus aureus targeting ROS-dependent mitochondrial damage activating NLRP10 in inducing skin and  | Sci Rep 2026 |
| 42185668 | Endothelial Dysfunction in Vascular Inflammation: The Role of NLRP3, NLRP10, AIM2, TLR9, and PANoptosis. | Handb Exp Pharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NLRP10

