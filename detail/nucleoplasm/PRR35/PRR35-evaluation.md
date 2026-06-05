---
type: protein-evaluation
gene: "PRR35"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR35 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR35 / C16orf11 |
| 蛋白名称 | Proline-rich protein 35 |
| 蛋白大小 | 571 aa / 59.4 kDa |
| UniProt ID | P0CG20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Cytokinetic bridge, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 571 aa / 59.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039363, IPR039064; Pfam: PF15269 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytokinetic bridge, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf11 |

**关键文献**:
1. Molecular Fingerprints of Borderline Changes in Kidney Allografts Are Influenced by Donor Category.. *Frontiers in immunology*. PMID: 32269565
2. NMR structure verifies the eponymous zinc finger domain of transcription factor ZNF750.. *Journal of structural biology: X*. PMID: 37655311

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.4 |
| 高置信度残基 (pLDDT>90) 占比 | 4.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 21.4% |
| 低置信 (pLDDT<50) 占比 | 68.8% |
| 有序区域 (pLDDT>70) 占比 | 9.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.4），有序残基占 9.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039363, IPR039064; Pfam: PF15269 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NHLRC4 | 0.815 | 0.000 | — |
| OR51A4 | 0.710 | 0.000 | — |
| OR51L1 | 0.707 | 0.000 | — |
| OR52J3 | 0.694 | 0.000 | — |
| OR51A2 | 0.680 | 0.000 | — |
| KBTBD12 | 0.676 | 0.000 | — |
| RRP36 | 0.647 | 0.000 | — |
| SPATA48 | 0.615 | 0.000 | — |
| TOGARAM1 | 0.611 | 0.000 | — |
| VWC2 | 0.609 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1R13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LZTS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP10-7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBASH3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBXN11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CARD10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000386499.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT31 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| APPL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.4 + PDB: 无 | pLDDT=49.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Cytokinetic bridge, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PRR35 — Proline-rich protein 35，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小571 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0CG20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161992-PRR35/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR35
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0CG20
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0CG20-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000161992-PRR35/subcellular

![](https://images.proteinatlas.org/69297/1947_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/69297/1947_G1_6_red_green.jpg)
![](https://images.proteinatlas.org/69297/1972_G2_15_cr5e15ac98b134c_red_green.jpg)
![](https://images.proteinatlas.org/69297/1972_G2_7_cr5e15ac98afb9c_red_green.jpg)
![](https://images.proteinatlas.org/69297/2048_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/69297/2048_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
