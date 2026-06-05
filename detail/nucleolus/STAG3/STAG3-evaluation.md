---
type: protein-evaluation
gene: "STAG3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STAG3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAG3 |
| 蛋白名称 | Cohesin subunit SA-3 |
| 蛋白大小 | 1225 aa / 139.0 kDa |
| UniProt ID | Q9UJ98 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus; Chromosome; Chromosome, centromere |
| 蛋白大小 | 5/10 | ×1 | 5 | 1225 aa / 139.0 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=83 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR039662, IPR056396, IPR020839, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, centromeric region (GO:0000775)
- extracellular space (GO:0005615)
- meiotic cohesin complex (GO:0030893)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- synaptonemal complex (GO:0000795)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 83 |
| PubMed broad count | 118 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. N6-methyladenosine writer METTL16-mediated alternative splicing and translation control are essential for murine spermatogenesis.. *Genome biology*. PMID: 39030605
2. STAG3, a novel gene encoding a protein involved in meiotic chromosome pairing and location of STAG3-related genes flanking the Williams-Beuren syndrome deletion.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 10698974
3. New STAG3 gene variant as a cause of premature ovarian insufficiency.. *Revista colombiana de obstetricia y ginecologia*. PMID: 35503298
4. METTL3/IGF2BP2 axis affects the progression of colorectal cancer by regulating m6A modification of STAG3.. *Scientific reports*. PMID: 37828232
5. STAG3-mediated stabilization of REC8 cohesin complexes promotes chromosome synapsis during meiosis.. *The EMBO journal*. PMID: 24797475

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 58.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 74.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 74.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR039662, IPR056396, IPR020839, IPR013721; Pfam: PF24571, PF21581, PF08514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMC3 | 0.999 | 0.821 | — |
| RAD21 | 0.999 | 0.573 | — |
| REC8 | 0.999 | 0.505 | — |
| RAD21L1 | 0.999 | 0.573 | — |
| SMC1B | 0.999 | 0.522 | — |
| SMC1A | 0.999 | 0.647 | — |
| SGO2 | 0.963 | 0.000 | — |
| STAG1 | 0.962 | 0.000 | — |
| STAG2 | 0.958 | 0.000 | — |
| SYCP3 | 0.921 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| yopM | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CASTOR3P | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, centromere / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. STAG3 — Cohesin subunit SA-3，研究基础较多，新颖性有限。
2. 蛋白大小1225 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 83 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJ98
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066923-STAG3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAG3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJ98
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000066923-STAG3/subcellular

![](https://images.proteinatlas.org/49106/738_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/49106/738_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/49106/750_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/49106/750_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJ98-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
