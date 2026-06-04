---
type: protein-evaluation
gene: "RERGL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RERGL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RERGL |
| 蛋白名称 | Ras-related and estrogen-regulated growth inhibitor-like protein |
| 蛋白大小 | 205 aa / 23.9 kDa |
| UniProt ID | Q9H628 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 23.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR051065, IPR001806; Pfam: PF00071 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.5/180** | |
| **归一化总分** | | | **73.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Spatial Proteomics for Further Exploration of Missing Proteins: A Case Study of the Ovary.. *Journal of proteome research*. PMID: 36108145
2. Revealing the impact of TOX3 on osteoarthritis: insights from bioinformatics.. *Frontiers in medicine*. PMID: 38020130
3. Genomic insights into growth traits in German Black Pied cattle: a dual-purpose breed at risk.. *Animal : an international journal of animal bioscience*. PMID: 40424954
4. Transcriptional Changes in the Ovaries of Perch from Chernobyl.. *Environmental science & technology*. PMID: 32686935
5. Distinguishing colorectal adenoma from hyperplastic polyp by WNT2 expression.. *Journal of clinical laboratory analysis*. PMID: 34477243

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 28.8% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 14.6% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=76.9，有序区 66.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR051065, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITSN2 | 0.540 | 0.497 | — |
| ITSN1 | 0.535 | 0.497 | — |
| FHL5 | 0.513 | 0.110 | — |
| MAP3K7CL | 0.452 | 0.110 | — |
| FLYWCH1 | 0.443 | 0.097 | — |
| PIK3C2G | 0.437 | 0.000 | — |
| TMEM74B | 0.410 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=76.9 + PDB: 无 | pLDDT=76.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 7 + 0 interactions | 数据有限 |

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
1. RERGL — Ras-related and estrogen-regulated growth inhibitor-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H628
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111404-RERGL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RERGL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H628
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
