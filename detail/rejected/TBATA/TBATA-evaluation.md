---
type: protein-evaluation
gene: "TBATA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBATA — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBATA / C10orf27, SPATIAL |
| 蛋白名称 | Protein TBATA |
| 蛋白大小 | 351 aa / 39.5 kDa |
| UniProt ID | Q96M53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 39.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037394; Pfam: PF15256 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf27, SPATIAL |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. Tbata modulates thymic stromal cell proliferation and thymus function.. *The Journal of experimental medicine*. PMID: 20937703
3. Spatial gene's (Tbata) implication in neurite outgrowth and dendrite patterning in hippocampal neurons.. *Molecular and cellular neurosciences*. PMID: 24361585
4. Peptides presented by HLA class I molecules in the human thymus.. *Journal of proteomics*. PMID: 24029068
5. Spatial (Tbata) expression in mature medullary thymic epithelial cells.. *European journal of immunology*. PMID: 19918778

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 13.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 33.6% |
| 低置信 (pLDDT<50) 占比 | 37.9% |
| 有序区域 (pLDDT>70) 占比 | 28.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 28.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037394; Pfam: PF15256 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCLN | 0.743 | 0.000 | — |
| DENND3 | 0.673 | 0.000 | — |
| PRSS16 | 0.614 | 0.000 | — |
| PAXBP1 | 0.485 | 0.000 | — |
| SLC46A2 | 0.465 | 0.000 | — |
| NUP98 | 0.458 | 0.000 | — |
| SUN5 | 0.447 | 0.000 | — |
| PSMB11 | 0.440 | 0.000 | — |
| FOXN1 | 0.435 | 0.000 | — |
| SMIM19 | 0.435 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIH1D2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 1
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TBATA — Protein TBATA，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96M53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166220-TBATA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBATA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96M53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96M53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
