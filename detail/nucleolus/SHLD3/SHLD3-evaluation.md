---
type: protein-evaluation
gene: "SHLD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHLD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHLD3 / FLJ26957, RINN1 |
| 蛋白名称 | Shieldin complex subunit 3 |
| 蛋白大小 | 250 aa / 28.8 kDa |
| UniProt ID | Q6ZNX1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nucleoli; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 250 aa / 28.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.5; PDB: 6K07, 6K08, 6KTO, 6M7A, 6M7B, 6VE5, 6WW9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039996 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **147.5/180** | |
| **归一化总分** | | | **81.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- site of double-strand break (GO:0035861)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FLJ26957, RINN1 |

**关键文献**:
1. The shieldin complex mediates 53BP1-dependent DNA repair.. *Nature*. PMID: 30022168
2. CDH1 binds MAD2L2 in a Rev1-like pattern.. *Biochemical and biophysical research communications*. PMID: 32811646
3. MAD2L2 dimerization and TRIP13 control shieldin activity in DNA repair.. *Nature communications*. PMID: 34521823
4. 53BP1-RIF1-shieldin counteracts DSB resection through CST- and Polα-dependent fill-in.. *Nature*. PMID: 30022158
5. CHAMP1 binds to REV7/FANCV and promotes homologous recombination repair.. *Cell reports*. PMID: 36044844

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.5 |
| 高置信度残基 (pLDDT>90) 占比 | 45.6% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 6K07, 6K08, 6KTO, 6M7A, 6M7B, 6VE5, 6WW9, 6WWA, 7L9P |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6K07, 6K08, 6KTO, 6M7A, 6M7B, 6VE5, 6WW9, 6WWA, 7L9P）+ AlphaFold极高置信度预测（pLDDT=78.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039996 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHLD2 | 0.999 | 0.900 | — |
| MAD2L2 | 0.998 | 0.939 | — |
| SHLD1 | 0.994 | 0.000 | — |
| TRIP13 | 0.917 | 0.900 | — |
| TP53BP1 | 0.710 | 0.439 | — |
| C20orf96 | 0.648 | 0.000 | — |
| KIZ | 0.558 | 0.000 | — |
| TRAPPC13 | 0.536 | 0.000 | — |
| RIF1 | 0.519 | 0.000 | — |
| USP28 | 0.476 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.5 + PDB: 6K07, 6K08, 6KTO, 6M7A, 6M7B,  | pLDDT=78.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SHLD3 — Shieldin complex subunit 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小250 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZNX1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253251-SHLD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHLD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZNX1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
