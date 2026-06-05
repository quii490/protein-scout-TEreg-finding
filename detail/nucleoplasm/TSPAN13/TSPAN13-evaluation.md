---
type: protein-evaluation
gene: "TSPAN13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSPAN13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSPAN13 / NET6, TM4SF13 |
| 蛋白名称 | Tetraspanin-13 |
| 蛋白大小 | 204 aa / 22.1 kDa |
| UniProt ID | O95857 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 204 aa / 22.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018499, IPR000301; Pfam: PF00335 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NET6, TM4SF13 |

**关键文献**:
1. Tetraspanin 13 Enhances Immune Evasion in Breast Cancer by Promoting MHC-I Degradation.. *Cancer research*. PMID: 41218148
2. The role of tetraspanins pan-cancer.. *iScience*. PMID: 35992081
3. Single-Cell Sequencing Combined with Transcriptome Sequencing to Explore the Molecular Mechanisms Related to Skin Photoaging.. *Journal of inflammation research*. PMID: 39713718
4. Tetraspanin-enriched microdomains play an important role in pathogenesis in the protozoan parasite Entamoeba histolytica.. *PLoS pathogens*. PMID: 39361713
5. DUSP6 protein action and related hub genes prevention of sepsis-induced lung injury were screened by WGCNA and Venn.. *International journal of biological macromolecules*. PMID: 39197622

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.0 |
| 高置信度残基 (pLDDT>90) 占比 | 69.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.0，有序区 93.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018499, IPR000301; Pfam: PF00335 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| B4E171_HUMAN | 0.778 | 0.000 | — |
| ANKMY2 | 0.647 | 0.000 | — |
| BZW2 | 0.615 | 0.000 | — |
| TSPAN17 | 0.577 | 0.000 | — |
| ITGB1 | 0.566 | 0.000 | — |
| TSPAN1 | 0.557 | 0.000 | — |
| TSPAN11 | 0.539 | 0.000 | — |
| TSPAN5 | 0.534 | 0.000 | — |
| TSPAN15 | 0.513 | 0.000 | — |
| TSPAN6 | 0.487 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GLP1R | psi-mi:"MI:1320"(membrane yeast two hybrid) | pubmed:23864651|imex:IM-30241 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.0 + PDB: 无 | pLDDT=90.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSPAN13 — Tetraspanin-13，非常新颖，仅有少数基础研究。
2. 蛋白大小204 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95857
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106537-TSPAN13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPAN13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95857
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000106537-TSPAN13/subcellular

![](https://images.proteinatlas.org/7426/1199_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/7426/1199_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/7426/1232_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/7426/1232_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/7426/1253_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/7426/1253_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95857-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
