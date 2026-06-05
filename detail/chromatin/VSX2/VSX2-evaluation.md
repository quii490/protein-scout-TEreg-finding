---
type: protein-evaluation
gene: "VSX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VSX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VSX2 / CHX10, HOX10 |
| 蛋白名称 | Visual system homeobox 2 |
| 蛋白大小 | 361 aa / 39.4 kDa |
| UniProt ID | P58304 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 39.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023339, IPR001356, IPR017970, IPR009057, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 237 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHX10, HOX10 |

**关键文献**:
1. Dynamic molecular and cellular characteristics of VSX2-positive retinal progenitor cells in human retinal organoids.. *Stem cell research & therapy*. PMID: 41152974
2. Functional analysis of the Vsx2 super-enhancer uncovers distinct cis-regulatory circuits controlling Vsx2 expression during retinogenesis.. *Development (Cambridge, England)*. PMID: 35831950
3. A framework to identify functional interactors that contribute to disrupted early retinal development in Vsx2 ocular retardation J mice.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 37259952
4. Microphthalmia and disrupted retinal development due to a LacZ knock-in/knock-out allele at the Vsx2 locus.. *bioRxiv : the preprint server for biology*. PMID: 38895315
5. Microphthalmia and Disrupted Retinal Development Due to a LacZ Knock-in/Knock-Out Allele at the Vsx2 Locus.. *Eye and brain*. PMID: 39610658

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 32.1% |
| 低置信 (pLDDT<50) 占比 | 41.6% |
| 有序区域 (pLDDT>70) 占比 | 26.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.2），有序残基占 26.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023339, IPR001356, IPR017970, IPR009057, IPR003654; Pfam: PF00046, PF03826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIX3 | 0.867 | 0.000 | — |
| ATOH7 | 0.820 | 0.000 | — |
| NXNL1 | 0.816 | 0.000 | — |
| RHO | 0.802 | 0.045 | — |
| POU4F2 | 0.792 | 0.000 | — |
| MFRP | 0.790 | 0.000 | — |
| RCVRN | 0.782 | 0.000 | — |
| POU4F1 | 0.754 | 0.000 | — |
| GDF3 | 0.752 | 0.000 | — |
| SIX6 | 0.729 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PolZ2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Q4V6W6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpS26 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PTPMT1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cv | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10600 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11034 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mst98Ca | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ATPsynbeta | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11248 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.2 + PDB: 无 | pLDDT=60.2, v6 | 仅预测 |
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

**推荐等级**: ⭐⭐

**核心优势**:
1. VSX2 — Visual system homeobox 2，研究基础较多，新颖性有限。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58304
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119614-VSX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VSX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58304
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58304-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
