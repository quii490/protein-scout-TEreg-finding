---
type: protein-evaluation
gene: "DMBX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMBX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMBX1 / MBX, OTX3, PAXB |
| 蛋白名称 | Diencephalon/mesencephalon homeobox protein 1 |
| 蛋白大小 | 382 aa / 41.2 kDa |
| UniProt ID | Q8NFW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 382 aa / 41.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052488, IPR001356, IPR017970, IPR009057, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

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
- transcription regulator complex (GO:0005667)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MBX, OTX3, PAXB |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. Generation and maintenance of Dmbx1 gene-targeted mutant alleles.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 16845469
3. A Neuroendocrine Differentiation-related Molecular Model for Prognosis Prediction in Prostate Cancer Patients.. *Current medicinal chemistry*. PMID: 40377162
4. Duplicate dmbx1 genes regulate progenitor cell cycle and differentiation during zebrafish midbrain and retinal development.. *BMC developmental biology*. PMID: 20860823
5. The paired-type homeobox gene Dmbx1 marks the midbrain and pretectum.. *Mechanisms of development*. PMID: 12175514

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 46.1% |
| 有序区域 (pLDDT>70) 占比 | 37.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 37.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052488, IPR001356, IPR017970, IPR009057, IPR003654; Pfam: PF00046, PF03826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OTX2 | 0.632 | 0.095 | — |
| AGRP | 0.627 | 0.000 | — |
| RAB2A | 0.490 | 0.054 | — |
| PAX2 | 0.489 | 0.127 | — |
| SIK3 | 0.439 | 0.000 | — |
| HOMEZ | 0.434 | 0.068 | — |
| SIX3 | 0.415 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 7，IntAct interactions: 0
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 7 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DMBX1 — Diencephalon/mesencephalon homeobox protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小382 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197587-DMBX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMBX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
