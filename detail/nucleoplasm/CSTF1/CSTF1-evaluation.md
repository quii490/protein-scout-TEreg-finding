---
type: protein-evaluation
gene: "CSTF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSTF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSTF1 |
| 蛋白名称 | Cleavage stimulation factor subunit 1 |
| 蛋白大小 | 431 aa / 48.4 kDa |
| UniProt ID | Q05048 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 431 aa / 48.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 6B3X |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR044633, IPR032028, IPR038184, IPR015943, IPR019 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.5/180** | |
| **归一化总分** | | | **81.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mRNA cleavage stimulating factor complex (GO:0005848)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 13 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Computational and functional prioritization identifies genes that rescue behavior and reduce tau protein in fly and human cell models of Alzheimer disease.. *American journal of human genetics*. PMID: 40215969
2. Gene expression investigation of four key regulators of polyadenylation and alternative adenylation in the periphery of late-onset Alzheimer's disease patients.. *Gene*. PMID: 37981081
3. CAPTURE of the Human U2 snRNA Genes Expands the Repertoire of Associated Factors.. *Biomolecules*. PMID: 35625631
4. Assessing associations between the AURKA-HMMR-TPX2-TUBG1 functional module and breast cancer risk in BRCA1/2 mutation carriers.. *PloS one*. PMID: 25830658
5. p53 inhibits mRNA 3' processing through its interaction with the CstF/BARD1 complex.. *Oncogene*. PMID: 21383700

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 75.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 6B3X |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=90.4，有序区 91.4%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044633, IPR032028, IPR038184, IPR015943, IPR019775; Pfam: PF16699, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTF2 | 0.999 | 0.910 | — |
| CSTF3 | 0.999 | 0.971 | — |
| CPSF2 | 0.998 | 0.954 | — |
| BARD1 | 0.997 | 0.833 | — |
| CSTF2T | 0.996 | 0.938 | — |
| CPSF3 | 0.982 | 0.664 | — |
| BRCA1 | 0.974 | 0.510 | — |
| CPSF4 | 0.974 | 0.572 | — |
| CPSF1 | 0.966 | 0.000 | — |
| FIP1L1 | 0.941 | 0.520 | — |

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
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 6B3X | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CSTF1 -- Cleavage stimulation factor subunit 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小431 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05048
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101138-CSTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSTF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05048
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF1/IF_images/A-431_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF1/IF_images/A-431_1.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF1/CSTF1-PAE.png]]
