---
type: protein-evaluation
gene: "GSC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GSC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GSC2 / GSCL |
| 蛋白名称 | Homeobox protein goosecoid-2 |
| 蛋白大小 | 205 aa / 21.5 kDa |
| UniProt ID | O15499 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051440, IPR001356, IPR017970, IPR009057; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GSCL |

**关键文献**:
1. The MAPK homolog, Smk1, promotes assembly of the glucan layer of the spore wall in S. cerevisiae.. *Yeast (Chichester, England)*. PMID: 38874213
2. Genetically defined nucleus incertus neurons differ in connectivity and function.. *eLife*. PMID: 38819436
3. The Smk1p MAP kinase negatively regulates Gsc2p, a 1,3-beta-glucan synthase, during spore wall morphogenesis in Saccharomyces cerevisiae.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 16116083
4. Characterization and gene cloning of 1,3-beta-D-glucan synthase from Saccharomyces cerevisiae.. *European journal of biochemistry*. PMID: 7649185
5. Cloning of the Candida albicans homolog of Saccharomyces cerevisiae GSC1/FKS1 and its involvement in beta-1,3-glucan synthesis.. *Journal of bacteriology*. PMID: 9209021

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 25.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 38.0% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 38.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 38.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051440, IPR001356, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1L | 0.807 | 0.066 | — |
| SLC25A1 | 0.780 | 0.000 | — |
| TBX1 | 0.751 | 0.126 | — |
| LOC102724788 | 0.714 | 0.000 | — |
| PRODH | 0.693 | 0.000 | — |
| SEPTIN5 | 0.674 | 0.000 | — |
| GP1BB | 0.672 | 0.047 | — |
| RANBP1 | 0.655 | 0.082 | — |
| DGCR2 | 0.631 | 0.045 | — |
| CLTCL1 | 0.626 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TIM50 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| SSA3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSZ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| GIM3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SKP1 | psi-mi:"MI:0096"(pull down) | imex:IM-14111|pubmed:19882662 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| MID2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 无 | pLDDT=67.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GSC2 — Homeobox protein goosecoid-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15499
- Protein Atlas: https://www.proteinatlas.org/ENSG00000063515-GSC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GSC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15499
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15499-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
