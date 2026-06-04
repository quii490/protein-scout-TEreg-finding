---
type: protein-evaluation
gene: "LZIC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LZIC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LZIC |
| 蛋白名称 | Protein LZIC |
| 蛋白大小 | 190 aa / 21.5 kDa |
| UniProt ID | Q8WZA0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009428, IPR036911; Pfam: PF06384 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular cloning and characterization of LZIC, a novel gene encoding ICAT homologous protein with leucine zipper domain.. *International journal of molecular medicine*. PMID: 11712074
2. Leucine zipper and ICAT domain containing (LZIC) protein regulates cell cycle transitions in response to ionizing radiation.. *Cell cycle (Georgetown, Tex.)*. PMID: 30973299
3. LZIC regulates neuronal survival during zebrafish development.. *Developmental biology*. PMID: 15932753
4. Genome‑wide investigation of the clinical implications and molecular mechanism of long noncoding RNA LINC00668 and protein‑coding genes in hepatocellular carcinoma.. *International journal of oncology*. PMID: 31432149
5. Analysis of fifteen positional candidate genes for Schnyder crystalline corneal dystrophy.. *Molecular vision*. PMID: 16163269

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 59.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.1，有序区 77.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009428, IPR036911; Pfam: PF06384 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPR157 | 0.664 | 0.069 | — |
| NMNAT1 | 0.568 | 0.000 | — |
| TMEM144 | 0.557 | 0.000 | — |
| KTI12 | 0.546 | 0.000 | — |
| SLC25A33 | 0.537 | 0.000 | — |
| SLC45A1 | 0.519 | 0.000 | — |
| CLSTN1 | 0.516 | 0.000 | — |
| DCTPP1 | 0.514 | 0.069 | — |
| LRIF1 | 0.489 | 0.000 | — |
| KCTD9 | 0.487 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 无 | pLDDT=78.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LZIC — Protein LZIC，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WZA0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162441-LZIC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LZIC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WZA0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
