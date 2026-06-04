---
type: protein-evaluation
gene: "DHX37"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHX37 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX37 |
| 蛋白名称 | Probable ATP-dependent RNA helicase DHX37 |
| 蛋白大小 | 1157 aa / 129.5 kDa |
| UniProt ID | Q8IY37 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX37/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX37/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus, nucleolus; Cytoplasm; Nucleus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1157 aa / 129.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Approved |
| UniProt | Nucleus, nucleolus; Cytoplasm; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 62 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Phenylalanyl-tRNA synthetase FARS-1/FARSA balances longevity and immunity by downregulating endogenous mitochondrial double-stranded RNAs.. *Mol Cell*. PMID: 42184833
2. DHX37 protein and mRNA expression patterns in breast and ovarian cancer and their prognostic implications.. *Histochem Cell Biol*. PMID: 42151440
3. A Comprehensive Analysis of Variations in Sex Characteristics Across OMIM.. *Am J Med Genet A*. PMID: 41466375
4. Comprehensively identifying and validating the implications of NR5A1 and DHX37 variants for 46,XY disorders of sex development diagnosis.. *BMC Med Genomics*. PMID: 42057034
5. DHX37 and tumor growth: a novel avenue for melanoma research.. *J Transl Med*. PMID: 42045937

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.1% |
| 置信残基 (pLDDT 70-90) 占比 | 30.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 71.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX37/DHX37-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=75.9，有序区 71.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP14A | 0.000 | 0.000 | — |
| UTP3 | 0.000 | 0.000 | — |
| WDR46 | 0.000 | 0.000 | — |
| FCF1 | 0.000 | 0.000 | — |
| NOC4L | 0.000 | 0.000 | — |
| EMG1 | 0.000 | 0.000 | — |
| NOL6 | 0.000 | 0.000 | — |
| NOP14 | 0.000 | 0.000 | — |
| UTP20 | 0.000 | 0.000 | — |
| UTP11 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8IY37 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NY93 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q6NZL1 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 无 | pLDDT=75.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm; Nucleus membrane / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DHX37 — Probable ATP-dependent RNA helicase DHX37，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1157 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY37
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150990-DHX37/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX37
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY37
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX37/DHX37-PAE.png]]




