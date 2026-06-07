---
type: protein-evaluation
gene: "MAJIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAJIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAJIN / C11orf85 |
| 蛋白名称 | Membrane-anchored junction protein |
| 蛋白大小 | 176 aa / 20.1 kDa |
| UniProt ID | Q3KP22 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus inner membrane; Chromosome, telomere |
| 蛋白大小 | 8/10 | ×1 | 8 | 176 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 6GNX, 6GNY, 6J08 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027816; Pfam: PF15077 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus inner membrane; Chromosome, telomere | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf85 |

**关键文献**:
1. The meiotic TERB1-TERB2-MAJIN complex tethers telomeres to the nuclear envelope.. *Nature communications*. PMID: 30718482
2. Distinct TERB1 Domains Regulate Different Protein Interactions in Meiotic Telomere Movement.. *Cell reports*. PMID: 29141207
3. The TERB1-TERB2-MAJIN complex of mouse meiotic telomeres dates back to the common ancestor of metazoans.. *BMC evolutionary biology*. PMID: 32408858
4. Telomeric function and regulation during male meiosis in mice and humans.. *Andrology*. PMID: 38511802
5. Comprehensive Analysis Identifies Hyaluronan Mediated Motility Receptor and Cell Division Cycle 25C as Potential Prognostic Biomarkers in Head and Neck Squamous Cell Carcinoma.. *Cancer control : journal of the Moffitt Cancer Center*. PMID: 39323031

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 7.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 51.7% |
| 低置信 (pLDDT<50) 占比 | 26.1% |
| 有序区域 (pLDDT>70) 占比 | 22.2% |
| 可用 PDB 条目 | 6GNX, 6GNY, 6J08 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 22.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027816; Pfam: PF15077 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERB2 | 0.999 | 0.929 | — |
| TERB1 | 0.991 | 0.000 | — |
| CCDC155 | 0.861 | 0.000 | — |
| SUN1 | 0.815 | 0.000 | — |
| TERF1 | 0.775 | 0.000 | — |
| SUN2 | 0.686 | 0.000 | — |
| HORMAD1 | 0.626 | 0.000 | — |
| HORMAD2 | 0.609 | 0.000 | — |
| CDK2 | 0.550 | 0.000 | — |
| SPDYA | 0.521 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PRKAB2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TRIM69 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TERB2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COL8A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SYT17 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNX11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CRYBB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 6GNX, 6GNY, 6J08 | pLDDT=60.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Chromosome, telomere / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAJIN — Membrane-anchored junction protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3KP22
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168070-MAJIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAJIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3KP22
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3KP22-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3KP22 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027816; |
| Pfam | PF15077; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168070-MAJIN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CRYBB3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
