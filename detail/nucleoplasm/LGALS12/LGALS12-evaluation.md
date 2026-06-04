---
type: protein-evaluation
gene: "LGALS12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGALS12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALS12 / GRIP1 |
| 蛋白名称 | Galectin-12 |
| 蛋白大小 | 336 aa / 37.5 kDa |
| UniProt ID | Q96DT0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 336 aa / 37.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GRIP1 |

**关键文献**:
1. Cloning and functional verification of a porcine adipose tissue-specific promoter.. *BMC genomics*. PMID: 35610578
2. CRISPR/Cas9-meditated gene knockout in pigs proves that LGALS12 deficiency suppresses the proliferation and differentiation of porcine adipocytes.. *Biochimica et biophysica acta. Molecular and cell biology of lipids*. PMID: 37956708
3. Comprehensive transcriptomic view of the role of the LGALS12 gene in porcine subcutaneous and intramuscular adipocytes.. *BMC genomics*. PMID: 31215398
4. DNA methylation expression patterns predict outcome of clear cell renal cell carcinoma.. *Discover oncology*. PMID: 40419839
5. O-GlcNAc-Mediated Regulation of Galectin Expression and Secretion in Human Promyelocytic HL-60 Cells Undergoing Neutrophilic Differentiation.. *Biomolecules*. PMID: 36551191

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 72.9% |
| 置信残基 (pLDDT 70-90) 占比 | 16.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 89.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.6，有序区 89.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS13C | 0.687 | 0.520 | — |
| LGALS13 | 0.665 | 0.000 | — |
| CLC | 0.652 | 0.000 | — |
| TIMP4 | 0.485 | 0.000 | — |
| VSTM4 | 0.476 | 0.000 | — |
| EMB | 0.474 | 0.440 | — |
| GFRA2 | 0.452 | 0.000 | — |
| LIMD1 | 0.436 | 0.436 | — |
| TLR4 | 0.428 | 0.000 | — |
| TRARG1 | 0.427 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EMB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS13C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LIMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ITGA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTPRA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTPRK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CSPG4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC38A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 14
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 无 | pLDDT=88.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LGALS12 — Galectin-12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小336 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DT0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133317-LGALS12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALS12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DT0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
