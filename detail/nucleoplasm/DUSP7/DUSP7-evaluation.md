---
type: protein-evaluation
gene: "DUSP7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP7 / PYST2 |
| 蛋白名称 | Dual specificity protein phosphatase 7 |
| 蛋白大小 | 419 aa / 45.0 kDa |
| UniProt ID | Q16829 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 45.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.0; PDB: 4Y2E |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PYST2 |

**关键文献**:
1. MAP4K Family Kinases and DUSP Family Phosphatases in T-Cell Signaling and Systemic Lupus Erythematosus.. *Cells*. PMID: 31766293
2. Let-7c-5p Down Regulates the Proliferation of Colorectal Cancer Through the MAPK-ERK-Signaling Pathway.. *Biochemical genetics*. PMID: 38095736
3. Linc-RoR promotes MAPK/ERK signaling and confers estrogen-independent growth of breast cancer.. *Molecular cancer*. PMID: 29041978
4. The Phosphatase Dusp7 Drives Meiotic Resumption and Chromosome Alignment in Mouse Oocytes.. *Cell reports*. PMID: 27783954
5. Dual specificity phosphatase 7 drives the formation of cardiac mesoderm in mouse embryonic stem cells.. *PloS one*. PMID: 36227898

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 37.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 28.9% |
| 有序区域 (pLDDT>70) 占比 | 64.0% |
| 可用 PDB 条目 | 4Y2E |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.0，有序区 64.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036873; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.927 | 0.114 | — |
| MAPK14 | 0.927 | 0.737 | — |
| MAPK9 | 0.920 | 0.114 | — |
| MAPK1 | 0.916 | 0.657 | — |
| DUSP9 | 0.900 | 0.837 | — |
| MAPK3 | 0.830 | 0.335 | — |
| MAPK12 | 0.753 | 0.175 | — |
| MAPK11 | 0.751 | 0.175 | — |
| MAPK13 | 0.749 | 0.175 | — |
| SPOP | 0.708 | 0.538 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 4Y2E | pLDDT=74.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DUSP7 — Dual specificity protein phosphatase 7，非常新颖，仅有少数基础研究。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16829
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164086-DUSP7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16829
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16829-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16829 |
| SMART | SM00195;SM00450; |
| UniProt Domain [FT] | DOMAIN 68..187; /note="Rhodanese"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00173"; DOMAIN 244..387; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR008343;IPR029021;IPR001763;IPR036873;IPR000387;IPR020422; |
| Pfam | PF00782;PF00581; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164086-DUSP7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAPK1 | Intact, Biogrid | true |
| SPOP | Intact, Biogrid | true |
| EGLN3 | Intact | false |
| GHR | Intact | false |
| MAPK14 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
