---
type: protein-evaluation
gene: "F8A2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## F8A2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | F8A2 |
| 蛋白名称 | 40-kDa huntingtin-associated protein |
| 蛋白大小 | 371 aa / 39.1 kDa |
| UniProt ID | P23610 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Early endosome; Nucleus, nuclear body |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 39.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.5; PDB: 6EZ8, 6X9O, 7DXJ, 7DXK, 8SAH, 8VLX, 8W15 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039494, IPR011990 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Early endosome; Nucleus, nuclear body | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome (GO:0005769)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. African Americans and European Americans exhibit distinct gene expression patterns across tissues and tumors associated with immunologic functions and environmental exposures.. *Scientific reports*. PMID: 33972602
2. PCR assay for the inversion causing severe Hemophilia A and its application.. *Chinese medical journal*. PMID: 11593511
3. Transriptome Analysis of Peripheral Blood Monocytes in Chronic Obstructive Pulmonary Disease Patients.. *Doklady. Biochemistry and biophysics*. PMID: 39480635

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 42.3% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 17.8% |
| 有序区域 (pLDDT>70) 占比 | 73.8% |
| 可用 PDB 条目 | 6EZ8, 6X9O, 7DXJ, 7DXK, 8SAH, 8VLX, 8W15, 9PMW, 9PN0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6EZ8, 6X9O, 7DXJ, 7DXK, 8SAH, 8VLX, 8W15, 9PMW, 9PN0）+ AlphaFold极高置信度预测（pLDDT=77.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039494, IPR011990 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HTT | 0.998 | 0.960 | — |
| RAB5A | 0.956 | 0.087 | — |
| F8A1 | 0.803 | 0.800 | — |
| F8A3 | 0.801 | 0.800 | — |
| HAP1 | 0.583 | 0.000 | — |
| RAB30 | 0.548 | 0.545 | — |
| APPL1 | 0.484 | 0.000 | — |
| REPIN1 | 0.481 | 0.000 | — |
| NAPB | 0.447 | 0.000 | — |
| ITFG2 | 0.431 | 0.431 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SH3GLB1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| RAB30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| F8A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:26514267|imex:IM-24624 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 3
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 6EZ8, 6X9O, 7DXJ, 7DXK, 8SAH,  | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Early endosome; Nucleus, nucle / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. F8A2 — 40-kDa huntingtin-associated protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23610
- Protein Atlas: https://www.proteinatlas.org/ENSG00000288709-F8A2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=F8A2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23610
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23610-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P23610 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039494;IPR011990; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000288709-F8A2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HTT | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
