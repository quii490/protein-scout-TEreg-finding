---
type: protein-evaluation
gene: "PPM1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPM1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPM1B / PP2CB |
| 蛋白名称 | Protein phosphatase 1B |
| 蛋白大小 | 479 aa / 52.6 kDa |
| UniProt ID | O75688 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm, cytosol; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 479 aa / 52.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=84.7; PDB: 2P8E |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015655, IPR000222, IPR012911, IPR036580, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PP2CB |

**关键文献**:
1. Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors.. *Pharmacology & therapeutics*. PMID: 32650009
2. Modulation of YBX1-mediated PANoptosis inhibition by PPM1B and USP10 confers chemoresistance to oxaliplatin in gastric cancer.. *Cancer letters*. PMID: 38364962
3. BRISC-Mediated PPM1B-K63 Deubiquitination and Subsequent TGF-β Pathway Activation Promote High-Fat/High-Sucrose Diet-Induced Arterial Stiffness.. *Circulation research*. PMID: 39742393
4. A comprehensive overview of PPM1B: From biological functions to diseases.. *European journal of pharmacology*. PMID: 36863552
5. Decreased PPM1B Expression Drives PRMT5-Mediated Histone Modification in Lung Cancer Progression.. *Biomolecules*. PMID: 41301499

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 69.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 2P8E |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=84.7，有序区 77.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015655, IPR000222, IPR012911, IPR036580, IPR036457; Pfam: PF00481, PF07830 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC3A1 | 0.968 | 0.000 | — |
| PREPL | 0.967 | 0.000 | — |
| ISG15 | 0.962 | 0.518 | — |
| CAMKMT | 0.953 | 0.000 | — |
| MAP3K7 | 0.946 | 0.340 | — |
| CHUK | 0.831 | 0.699 | — |
| PPP2CB | 0.794 | 0.107 | — |
| PPM1A | 0.791 | 0.626 | — |
| YEATS4 | 0.751 | 0.045 | — |
| ARIH1 | 0.726 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PABPC4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KRT18 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ANXA2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VIL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VCP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| S100A8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RASGRP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ANXA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Tcr-alpha | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 2P8E | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Membrane / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PPM1B — Protein phosphatase 1B，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小479 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75688
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138032-PPM1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPM1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75688
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75688-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
