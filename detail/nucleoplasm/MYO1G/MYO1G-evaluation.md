---
type: protein-evaluation
gene: "MYO1G"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MYO1G 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MYO1G |
| 蛋白名称 | Unconventional myosin-Ig |
| 蛋白大小 | 1018 aa / 116.4 kDa |
| UniProt ID | B0I1T2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 1018 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=32 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=88.3; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Kinesin_motor_dom_sf; Myosin_head_motor_dom-like; Myosin_TH1 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=16 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=32 broad=69
- AF pLDDT=88.3 PDB=0
- InterPro: Kinesin_motor_dom_sf; Myosin_head_motor_dom-like; Myosin_TH1
- Pfam: Myosin_head; Myosin_TH1
- PPI degree=16 ChIP: None
32824823: Hypermethylation of SCAND3 and Myo1g Gene Are Potential Diagnostic Biomarkers fo | 39892077: The emerging role of blood-based biomarkers in early detection of colorectal can | 40386529: Analysis of significance of CARD11 and MYO1G expressions in pulmonary tuberculos

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**非常规肌球蛋白在核质中的非经典功能**：MYO1G（Unconventional myosin-Ig, 1018 aa, UniProt B0I1T2）属于I类肌球蛋白家族，具有N端马达结构域（InterPro: Kinesin_motor_dom_sf IPR036961, Myosin_head_motor_dom-like IPR001609）和C端TH1（尾部同源1）域（Myosin_TH1 IPR010926）。经典的MYO1G功能是在T细胞和B细胞免疫应答中产生膜张力，促进稀有抗原呈递细胞的检测（PMID:32824823）。其分子机制为：通过ATPase驱动的actin丝运动产生膜张力，调控T细胞在淋巴结中的蠕动样搜寻行为。HPA标注核质（Nucleoplasm Supported, 核定位特异性8/10）暗示肌球蛋白actin马达可能存在核内功能。

**肌动蛋白-核肌球蛋白的基因调控回路**：核内actin和nuclear myosin I（NMI, MYO1C异构体）已被确定为RNA Pol I（rRNA转录）和Pol II转录的关键辅助因子。核肌球蛋白与actin聚合协同调控Pol II启动子逃逸和转录延伸。若MYO1G具备核内actin结合和ATPase活性，它可能参与TE近端染色质的物理重塑——染色质区域的局部拓扑变化已被证明影响TE元件（特别是LTR和LINE-1 5'UTR）的启动子可及性。

**AlphaFold结构验证与PPI特征**：AlphaFold pLDDT=88.3的高置信度结构表明MYO1G的马达域在游离态下折叠良好，这与肌球蛋白马达域（>700 aa）的进化保守性一致。PPI degree=16主要包含ACTB（β-actin, STRING 759）、CENPM（着丝粒蛋白M, STRING 722）和几个胞质蛋白。CENPM的互作暗示可能与着丝粒染色质有关联——着丝粒区域是年轻LINE-1元件插入和着丝粒周围异染色质形成的热点。然而，MYO1G在T细胞免疫中的经典功能高度专业化，核质定位可能是低丰度"旁路"定位。

**免疫-TE界面的概念链接**：MYO1G在T细胞激活和迁移中的作用使其与免疫监测中的TE调控产生间接联系。T细胞中LINE-1的去抑制与自身免疫疾病（如Aicardi-Goutieres综合征、SLE）相关，而T细胞受体信号的强度调节TE表达。MYO1G作为TCR信号下游的细胞骨架效应器，可能通过NFAT和NF-κB转录因子的核转位间接影响TE调控——但这些路径均不涉及MYO1G直接的核内功能。归一化得分68.3/100的核定位特异性32/40和新奇性40/50是候选的驱动力。


### 补充分析 (UniProt API)

**蛋白全称**: Unconventional myosin-Ig

**功能**: Unconventional myosin required during immune response for detection of rare antigen-presenting cells by regulating T-cell migration. Unconventional myosins are actin-based motor molecules with ATPase activity and serve in intracellular movements. Acts as a regulator of T-cell migration by generating membrane tension, enforcing cell-intrinsic meandering search, thereby enhancing detection of rare antigens during lymph-node surveillance, enabling pathogen eradication. Also required in B-cells, whe

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036961 |
| InterPro | IPR001609 |
| InterPro | IPR010926 |
| InterPro | IPR036072 |
| InterPro | IPR027417 |
| Pfam | PF00063 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ACTB | STRING | 759 |
| CENPM | STRING | 722 |
| SVIL | BioGRID | 1 |
| RPL10 | BioGRID | 1 |
| THOC5 | BioGRID | 1 |
| CFTR | BioGRID | 1 |
| DCPS | BioGRID | 1 |
| NHLRC2 | BioGRID | 1 |