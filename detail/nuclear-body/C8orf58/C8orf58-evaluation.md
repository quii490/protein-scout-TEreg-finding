---
type: protein-evaluation
gene: "C8orf58"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C8orf58 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C8orf58 |
| 蛋白名称 | Uncharacterized protein C8orf58 |
| 蛋白大小 | 365 aa / 39.7 kDa |
| UniProt ID | Q8NAV2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 365 aa / 39.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027958; Pfam: PF15552 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 4 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Whole Exome Sequencing Study in a Family with Type 2 Diabetes Mellitus.. *International journal of general medicine*. PMID: 34815695

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 7.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 26.3% |
| 低置信 (pLDDT<50) 占比 | 56.4% |
| 有序区域 (pLDDT>70) 占比 | 17.3% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 17.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027958; Pfam: PF15552 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NPIPB15 | 0.480 | 0.000 | — |
| FAM122B | 0.475 | 0.000 | — |
| CCAR2 | 0.471 | 0.000 | — |
| BIN3 | 0.439 | 0.000 | — |
| ZNF707 | 0.436 | 0.000 | — |
| TMEM196 | 0.418 | 0.000 | — |
| PDLIM2 | 0.417 | 0.000 | — |
| SORBS3 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000289989.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| metG1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CENPH | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FCN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 4
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 无 | pLDDT=54.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 8 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C8orf58 — Uncharacterized protein C8orf58，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小365 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NAV2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000241852-C8orf58/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C8orf58
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NAV2
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:27:48

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000241852-C8orf58/subcellular

![](https://images.proteinatlas.org/28286/2265_A11_10_red_green.jpg)
![](https://images.proteinatlas.org/28286/2265_A11_33_red_green.jpg)
![](https://images.proteinatlas.org/28286/301_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/28286/301_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/28286/303_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/28286/303_D6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NAV2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
