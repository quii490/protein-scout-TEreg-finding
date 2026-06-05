---
type: protein-evaluation
gene: "C2CD6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C2CD6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C2CD6 / ALS2CR11, C2CD6 |
| 蛋白名称 | Cation channel sperm-associated targeting subunit tau |
| 蛋白大小 | 1820 aa / 209.1 kDa |
| UniProt ID | Q53TS8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Principal piece; 额外: Acrosome, Equatorial segment; UniProt: Cell projection, cilium, flagellum membrane |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1820 aa / 209.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=39.7; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR031462, IPR048363; Pfam: PF15729 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Principal piece; 额外: Acrosome, Equatorial segment | Approved |
| UniProt | Cell projection, cilium, flagellum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CatSper complex (GO:0036128)
- sperm principal piece (GO:0097228)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALS2CR11, C2CD6 |

**关键文献**:
1. C2CD6 regulates targeting and organization of the CatSper calcium channel complex in sperm flagella.. *Development (Cambridge, England)*. PMID: 34919125
2. Globozoospermia: A Case Report and Systematic Review of Literature.. *The world journal of men's health*. PMID: 36047070
3. Exome sequencing reveals novel causes as well as new candidate genes for human globozoospermia.. *Human reproduction (Oxford, England)*. PMID: 31985809
4. Male infertility and perfluoroalkyl and poly-fluoroalkyl substances: evidence for alterations in phosphorylation of proteins and fertility-related functional attributes in bull spermatozoa†.. *Biology of reproduction*. PMID: 38847481
5. C2cd6-encoded CatSperτ targets sperm calcium channel to Ca(2+) signaling domains in the flagellar membrane.. *Cell reports*. PMID: 34998468

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 39.7 |
| 高置信度残基 (pLDDT>90) 占比 | 2.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 83.3% |
| 有序区域 (pLDDT>70) 占比 | 7.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/C2CD6/C2CD6-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=39.7），有序残基占 7.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR031462, IPR048363; Pfam: PF15729 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C7orf61 | 0.678 | 0.000 | — |
| EFCAB9 | 0.626 | 0.000 | — |
| SPATA16 | 0.596 | 0.000 | — |
| TSACC | 0.568 | 0.000 | — |
| C22orf23 | 0.540 | 0.000 | — |
| TMEM237 | 0.522 | 0.000 | — |
| FLACC1 | 0.517 | 0.000 | — |
| CCDC62 | 0.507 | 0.000 | — |
| ZPBP | 0.488 | 0.000 | — |
| GKAP1 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TEX11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCM6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNRD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HNRNPD | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| VPS52 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=39.7 + PDB: 无 | pLDDT=39.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum membrane / Principal piece; 额外: Acrosome, Equatorial segment | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C2CD6 — Cation channel sperm-associated targeting subunit tau，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1820 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=39.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53TS8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155754-C2CD6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C2CD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53TS8
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-02 12:43:33


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/C2CD6/C2CD6-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Principal piece (approved)。来源: https://www.proteinatlas.org/ENSG00000155754-C2CD6/subcellular

![](https://images.proteinatlas.org/45406/2239_E11_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/45406/2239_E11_25_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
