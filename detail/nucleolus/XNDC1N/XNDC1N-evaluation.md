---
type: protein-evaluation
gene: "XNDC1N"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## XNDC1N 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XNDC1N |
| 蛋白名称 | Protein XNDC1N |
| 蛋白大小 | 234 aa / 26.0 kDa |
| UniProt ID | Q6ZNB5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoli; 额外: Mitotic chromosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 234 aa / 26.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008979, IPR002706; Pfam: PF01834 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Mitotic chromosome | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 16.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 20.9% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.1，有序区 64.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008979, IPR002706; Pfam: PF01834 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 无 | pLDDT=76.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. XNDC1N — Protein XNDC1N，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小234 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZNB5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000254469-XNDC1N/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XNDC1N
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZNB5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000254469-XNDC1N/subcellular

![](https://images.proteinatlas.org/51121/1130_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51121/1130_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51121/1143_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51121/1143_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51121/1320_F1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51121/1320_F1_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZNB5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
