---
type: protein-evaluation
gene: "SFMBT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SFMBT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SFMBT1 / RU1 |
| 蛋白名称 | Scm-like with four MBT domains protein 1 |
| 蛋白大小 | 866 aa / 98.1 kDa |
| UniProt ID | Q9UHJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 866 aa / 98.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004092, IPR047352, IPR047351, IPR050548, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RU1 |

**关键文献**:
1. iNPH-the mystery resolving.. *EMBO molecular medicine*. PMID: 33555136
2. SFMBT1 facilitates colon cancer cell metastasis and drug resistance combined with HMG20A.. *Cell death discovery*. PMID: 35577773
3. MicroRNA-218 inhibits EMT, migration and invasion by targeting SFMBT1 and DCUN1D1 in cervical cancer.. *Oncotarget*. PMID: 27285984
4. Genome-wide Screening Identifies SFMBT1 as an Oncogenic Driver in Cancer with VHL Loss.. *Molecular cell*. PMID: 32023483
5. SFMBT1 functions with LSD1 to regulate expression of canonical histone genes and chromatin-related factors.. *Genes & development*. PMID: 23592795

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 33.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 69.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004092, IPR047352, IPR047351, IPR050548, IPR001660; Pfam: PF02820, PF00536, PF12140 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCOR1 | 0.869 | 0.682 | — |
| YY1 | 0.796 | 0.089 | — |
| PSMB8 | 0.778 | 0.000 | — |
| KDM1A | 0.762 | 0.488 | — |
| HMG20A | 0.751 | 0.711 | — |
| PSMB9 | 0.736 | 0.000 | — |
| HDAC1 | 0.671 | 0.617 | — |
| L3MBTL3 | 0.657 | 0.368 | — |
| ZMYM2 | 0.635 | 0.587 | — |
| RYBP | 0.614 | 0.045 | — |

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
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SFMBT1 — Scm-like with four MBT domains protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小866 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163935-SFMBT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SFMBT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
