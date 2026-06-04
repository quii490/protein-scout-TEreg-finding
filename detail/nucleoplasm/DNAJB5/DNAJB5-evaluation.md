---
type: protein-evaluation
gene: "DNAJB5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJB5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB5 |
| 蛋白名称 | DnaJ heat shock protein family (Hsp40) member B5 |
| 蛋白大小 | 382 aa / 43.0 kDa |
| UniProt ID | A0A7I2RN43 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 382 aa / 43.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 21 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A genome-wide CRISPR/Cas9 screen reveals novel positive regulators of FTY720 sensitivity in acute lymphoblastic leukemia cells.. *BMC Res Notes*. PMID: 41578398
2. A transient protein folding response targets aggregation in the early phase of TDP-43-mediated neurodegeneration.. *Nat Commun*. PMID: 38374041
3. Identification and validation of a new prognostic signature based on cancer-associated fibroblast-driven genes in breast cancer.. *World J Clin Cases*. PMID: 38322675
4. Genetic diversity, population structure, and selective signature of sheep in the northeastern Tarim Basin.. *Front Genet*. PMID: 38028584
5. Downregulation of miR-26 promotes invasion and metastasis via targeting interleukin-22 in cutaneous T-cell lymphoma.. *Cancer Sci*. PMID: 35133054

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 23.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 27.2% |
| 有序区域 (pLDDT>70) 占比 | 65.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.2，有序区 65.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSPH1 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| DNAJB4 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| P2RX6 | 0.000 | 0.000 | — |
| DNAJB1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 无 | pLDDT=73.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DNAJB5 -- DnaJ heat shock protein family (Hsp40) member B5，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小382 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A7I2RN43
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137094-DNAJB5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A7I2RN43
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
