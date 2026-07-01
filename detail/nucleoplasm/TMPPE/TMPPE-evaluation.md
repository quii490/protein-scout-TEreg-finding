---
type: protein-evaluation
gene: "TMPPE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMPPE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMPPE |
| 蛋白名称 | Transmembrane protein with metallophosphoesterase domain |
| 蛋白大小 | 453 aa / 49.5 kDa |
| UniProt ID | Q6ZT21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 453 aa / 49.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004843, IPR029052, IPR051158; Pfam: PF00149 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genome-wide meta-analyses of stratified depression in Generation Scotland and UK Biobank.. *Translational psychiatry*. PMID: 29317602

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 95.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.4，有序区 95.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004843, IPR029052, IPR051158; Pfam: PF00149 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC66A3 | 0.598 | 0.000 | — |
| TMEM41A | 0.588 | 0.000 | — |
| ZNF319 | 0.491 | 0.000 | — |
| LYSMD4 | 0.474 | 0.000 | — |
| DOLPP1 | 0.460 | 0.000 | — |
| YIPF4 | 0.451 | 0.000 | — |
| C5orf51 | 0.451 | 0.000 | — |
| UNC50 | 0.432 | 0.000 | — |
| FNDC3A | 0.416 | 0.000 | — |
| INKA1 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HTR3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC22A9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC6A15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RY12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYZL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SFXN5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CNR2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SMAGP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SCN3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLAMF6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 无 | pLDDT=91.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TMPPE — Transmembrane protein with metallophosphoesterase domain，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小453 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

TMPPE的核心结构域为金属磷酸酯酶结构域（Metallophosphoesterase domain, PF00149），属于钙调磷酸酶样磷酸酯酶超家族（IPR004843, IPR029052）。该结构域采用经典的α/β折叠，依赖双核金属离子（通常为Mn²⁺或Fe³⁺）催化磷酸酯键水解。AlphaFold v6预测结构具有极高置信度（pLDDT=91.4，有序区95.1%），表明结构域折叠可靠，但其PAE仍需关注长距离域间取向的不确定性。值得注意的是，金属磷酸酯酶超家族与DNA修复磷酸酯酶（如Mre11核酸酶家族）在进化上存在同源关系，暗示TMPPE的催化口袋可能天然适配含磷底物，包括磷酸化蛋白、核酸或磷脂底物。然而，UniProt虽将其注释为跨膜蛋白（Membrane），HPA IF却清晰显示核质定位（Nucleoplasm, Approved），这种双重定位的矛盾提示TMPPE可能存在膜锚定形态与核内可溶形态之间的动态分配。

PPI网络分析进一步复杂化了TMPPE的机制推断。STRING预测的10个互作伙伴（SLC66A3 score=0.598, TMEM41A score=0.588等）全部定位于膜系统，涉及溶质转运与内质网/高尔基体运输功能，并未指向任何染色质相关因子或转录调控蛋白。IntAct实验验证的15个互作同样偏向膜蛋白与转运体（HTR3C, SLC22A9, SLC6A15等），其中以共免疫沉淀（anti tag coimmunoprecipitation, PMID:28514442）和双杂交筛选（two hybrid array, PMID:32296183）为主要方法学。BioGRID中列出的ATP1B3、TMEM30A等伙伴也均为质膜或内体膜蛋白，进一步印证TMPPE的互作组集中于膜生物学而非染色质环境。这种PPI图谱与核定位之间的矛盾，可能说明TMPPE在核质中以单体或低聚体形式发挥催化功能，而膜定位形态则参与不同的蛋白复合体——这是一种典型的"兼职蛋白"（moonlighting protein）行为模式。

从现有文献角度，TMPPE几乎是完全未被探索的蛋白。PubMed严格检索仅命中1篇文献（PMID:29317602），内容为抑郁症全基因组关联研究的荟萃分析，并未针对TMPPE开展任何功能性研究。这种极端的研究空白（PubMed=1, ≤20）既提供了高度的创新性红利，也带来了功能注释缺失的巨大风险。结合其金属磷酸酯酶催化核心和454 aa的适中大小（49.5 kDa），TMPPE在理论上具备作为核内磷酸酯信号调控节点的潜力，但缺乏任何染色质/TE调控相关的直接证据——无论是结构域层面、PPI层面还是文献层面。

综合审评结论：TMPPE的结构预测质量极高（pLDDT=91.4），磷酸酯酶催化核心在进化上与核酸加工酶相关，核定位有HPA approved级别证据支撑，但这些有利因素被完全缺乏核内功能注释的现实严重削弱。若该蛋白确实在核质中执行催化功能，最可能的底物类型为磷酸化蛋白（类似于磷酸酶）或低分子量含磷代谢物，而非染色质DNA。TE调控的间接可能性存在——例如通过去磷酸化某个转录抑制因子而间接影响TE转录——但这种推测需要大规模的互作组重注释和体外酶活验证才有望被证实。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ATP1B3 | BioGRID | 0 |
| ASGR2 | BioGRID | 0 |
| IDS | BioGRID | 0 |
| TMEM30A | BioGRID | 0 |
| P2RY12 | BioGRID | 0 |
| POMK | BioGRID | 0 |
| BSCL2 | BioGRID | 0 |
| FAM189A2 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZT21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188167-TMPPE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMPPE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZT21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188167-TMPPE/subcellular

![](https://images.proteinatlas.org/27019/604_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/27019/604_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/27019/607_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/27019/607_C12_4_red_green.jpg)
![](https://images.proteinatlas.org/27019/609_C12_4_red_green.jpg)
![](https://images.proteinatlas.org/27019/609_C12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZT21-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZT21 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004843;IPR029052;IPR051158; |
| Pfam | PF00149; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188167-TMPPE/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CD79A | Intact | false |
| CLDND2 | Intact | false |
| CLRN1 | Intact | false |
| CNR2 | Intact | false |
| CYB561 | Intact | false |
| FIS1 | Intact | false |
| FXYD6 | Intact | false |
| GPR152 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
