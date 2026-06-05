---
type: protein-evaluation
gene: "PROX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PROX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PROX2 |
| 蛋白名称 | Prospero homeobox protein 2 |
| 蛋白大小 | 592 aa / 65.6 kDa |
| UniProt ID | Q3B8N5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 592 aa / 65.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023082, IPR037131, IPR009057, IPR039350; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

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
| PubMed strict count | 9 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ABCD4 is associated with mammary gland development in mammals.. *BMC genomics*. PMID: 38764031
2. Characterization of a novel prospero-related homeobox gene, Prox2.. *Molecular genetics and genomics : MGG*. PMID: 16470382
3. Identification and expression pattern of zebrafish prox2 during embryonic development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 19035352
4. MLE functions as a transcriptional regulator of the roX2 gene.. *The Journal of biological chemistry*. PMID: 15358781
5. Circadian gene expression in mouse renal proximal tubule.. *American journal of physiology. Renal physiology*. PMID: 36727945

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.9 |
| 高置信度残基 (pLDDT>90) 占比 | 29.7% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 58.4% |
| 有序区域 (pLDDT>70) 占比 | 37.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.9），有序残基占 37.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023082, IPR037131, IPR009057, IPR039350; Pfam: PF05044 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VRTN | 0.726 | 0.000 | — |
| AREL1 | 0.598 | 0.000 | — |
| SYNDIG1L | 0.541 | 0.000 | — |
| YLPM1 | 0.521 | 0.000 | — |
| RPS6KL1 | 0.517 | 0.000 | — |
| SWI5 | 0.455 | 0.000 | — |
| CATSPER1 | 0.454 | 0.000 | — |
| IFT80 | 0.446 | 0.000 | — |
| HEATR4 | 0.446 | 0.000 | — |
| NBPF6 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GSK3A | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| GSK3B | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.9 + PDB: 无 | pLDDT=59.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. PROX2 — Prospero homeobox protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小592 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3B8N5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119608-PROX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PROX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3B8N5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3B8N5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
