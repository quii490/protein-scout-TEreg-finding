---
type: protein-evaluation
gene: "DHRS7B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHRS7B — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHRS7B / SDR32C1 |
| 蛋白名称 | Peroxisomal reductase activating PPAR-gamma |
| 蛋白大小 | 325 aa / 35.1 kDa |
| UniProt ID | Q6IAN0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Plasma membrane, Cell Junctions, Cytosol; UniProt: Peroxisome membrane; Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 325 aa / 35.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036291, IPR020904, IPR002347; Pfam: PF00106 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions, Cytosol | Approved |
| UniProt | Peroxisome membrane; Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- peroxisomal membrane (GO:0005778)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.8 |
| 高置信度残基 (pLDDT>90) 占比 | 84.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 93.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.8，有序区 93.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036291, IPR020904, IPR002347; Pfam: PF00106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SARDH | 0.719 | 0.051 | — |
| GNPAT | 0.604 | 0.000 | — |
| DHRS1 | 0.582 | 0.066 | — |
| TLCD1 | 0.581 | 0.077 | — |
| TMEM11 | 0.538 | 0.000 | — |
| FDX1 | 0.528 | 0.256 | — |
| AGPS | 0.524 | 0.091 | — |
| TYSND1 | 0.524 | 0.047 | — |
| NATD1 | 0.517 | 0.102 | — |
| MEIOB | 0.500 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED19 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BABAM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| NMES1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| PDGFRB | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| ARHGAP31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.8 + PDB: 无 | pLDDT=92.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome membrane; Endoplasmic reticulum membran / Plasma membrane, Cell Junctions, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DHRS7B — Peroxisomal reductase activating PPAR-gamma，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小325 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IAN0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109016-DHRS7B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHRS7B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IAN0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000109016-DHRS7B/subcellular

![](https://images.proteinatlas.org/16873/133_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16873/133_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16873/134_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16873/134_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16873/135_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16873/135_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IAN0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
