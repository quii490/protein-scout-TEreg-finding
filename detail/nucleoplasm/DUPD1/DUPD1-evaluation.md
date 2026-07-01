---
type: protein-evaluation
gene: "DUPD1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## DUPD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DUPD1 |
| 蛋白名称 | Dual specificity phosphatase 29 |
| 蛋白大小 | 220 aa / 25.3 kDa |
| UniProt ID | Q68J44 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 220 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=86.8; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Atypical_DUSP_subfamA; Dual-sp_phosphatase_cat-dom; Prot-tyrosine_phosphatase-li |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=5 broad=8
- AF pLDDT=86.8 PDB=1
- InterPro: Atypical_DUSP_subfamA; Dual-sp_phosphatase_cat-dom; Prot-tyrosine_phosphatase-like
- Pfam: DSPc
- PPI degree=39 ChIP: None
42238898: Identification of highly expressed genes and efficient core promoters specific t | 32639872: Dual-specificity phosphatase 29 is induced during neurogenic skeletal muscle atr | 21199871: Inhibition of MAPK by prolactin signaling through the short form of its receptor

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**双特异性磷酸酶催化机制与核内功能**：DUPD1（Dual specificity phosphatase 29, UniProt Q68J44）属于非典型双特异性磷酸酶亚家族A（InterPro: Atypical_DUSP_subfamA IPR020405），催化结构域为双特异性磷酸酶催化域（Dual-sp_phosphatase_cat-dom IPR000340）。该酶能够同时去磷酸化底物蛋白上的磷酸酪氨酸、磷酸丝氨酸和磷酸苏氨酸残基，偏好磷酸酪氨酸底物（PMID:17498703）。从结构角度看，其Pfam DSPc结构域包含保守的HCX5R催化基序，通过半胱氨酸亲核攻击机制水解磷酸酯键。pLDDT=86.8的中高置信度AlphaFold结构支持催化核心的有序折叠，且PDB=1的晶体结构存在，为高分辨率机制研究提供了结构基础。

**MAPK信号轴与TE沉默的潜在交汇**：DUPD1的核心生物学功能是调节MAPK1/2信号级联（PMIDs:32639872, 21199871）。MAPK通路与表观遗传调控存在已知的交叉节点：ERK1/2可磷酸化组蛋白H3S10和H3S28，直接影响染色质压缩状态，且MEK-ERK信号参与调控L1逆转座子5'UTR启动子活性。因此，DUPD1通过去磷酸化MAPK组分间接影响染色质修饰酶活性的假说具有一定合理性。其作用位点主要在骨骼肌（PMIDs:42238898, 32639872），骨骼肌中LINE-1低水平体细胞逆转座已有报道，提示组织特异性TE调控的潜在关联。

**PPI网络中的核质功能线索**：尽管DUPD1自身的核定位证据仅为5/10（无明确NLS），但其PPI互作伙伴中POLR2G（RNA聚合酶II亚基G, BioGRID score=1）和SRSF11（丝氨酸/精氨酸富集剪接因子11）的存在为核质功能提供了间接支持。POLR2G是Pol II的Rpb7亚基，直接参与转录延伸；SRSF11参与mRNA剪接调控。若DUPD1在核质中去磷酸化这些核蛋白，可能产生转录调控效应。另外，PPI degree=39（BioGRID/STRING）表明该蛋白具有适度的互作网络，可能作为信号枢纽整合多个上游输入。

**TE调控的新颖性维度**：PubMed strict=5的极低文献量和归一化得分68.9/100中新奇性满分（50/50）突显该蛋白在TE领域完全未被探索。磷酸酶在TE调控中的角色长期被低估——已有研究发现PP1和PP2A磷酸酶通过去磷酸化HP1α影响异染色质稳定性，但DUSP家族与TE调控的关系几乎空白。DUPD1作为MAPK通路的负调控因子，可能通过抑制MAPK驱动的染色质开放来间接促进TE区域的异染色质化。

**高风险因素与实验建议**：主要风险在于缺乏核定位的确凿证据（HPA n/a），且DUSP29的经典功能局限在胞质信号转导。实验验证策略应考虑：首先通过共表达分析确认DUPD1的核质分布，随后利用磷酸化蛋白质组学鉴定其核内核底物；若核底物包含染色质修饰因子（如HDAC、HAT、HMT），则DUPD1-TE调控假说将获得关键支撑。


### 补充分析 (UniProt API)

**蛋白全称**: Dual specificity phosphatase 29

**功能**: Dual specificity phosphatase able to dephosphorylate phosphotyrosine, phosphoserine and phosphothreonine residues within the same substrate, with a preference for phosphotyrosine as a substrate (PubMed:17498703). Involved in the modulation of intracellular signaling cascades. In skeletal muscle regulates systemic glucose homeostasis by activating, AMPK, an energy sensor protein kinase (By similarity). Affects MAP kinase signaling though modulation of the MAPK1/2 cascade in skeletal muscle promot

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR020405 |
| InterPro | IPR000340 |
| InterPro | IPR029021 |
| InterPro | IPR016130 |
| InterPro | IPR000387 |
| InterPro | IPR020422 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RB1CC1 | BioGRID | 1 |
| FASN | BioGRID | 1 |
| RCC2 | BioGRID | 1 |
| PSMB5 | BioGRID | 1 |
| RNF40 | BioGRID | 1 |
| ASPA | BioGRID | 1 |
| SRSF11 | BioGRID | 1 |
| POLR2G | BioGRID | 1 |