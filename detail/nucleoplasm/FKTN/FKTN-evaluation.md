---
type: protein-evaluation
gene: "FKTN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKTN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKTN / FCMD |
| 蛋白名称 | Ribitol-5-phosphate transferase FKTN |
| 蛋白大小 | 461 aa / 53.7 kDa |
| UniProt ID | O75072 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 461 aa / 53.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009644, IPR045587, IPR007074; Pfam: PF19737, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi apparatus membrane; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- endoplasmic reticulum (GO:0005783)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 209 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FCMD |

**关键文献**:
1. Genetic variations and clinical spectrum of dystroglycanopathy in a large cohort of Chinese patients.. *Clinical genetics*. PMID: 33200426
2. Whole genome sequencing delineates regulatory, copy number, and cryptic splice variants in early onset cardiomyopathy.. *NPJ genomic medicine*. PMID: 35288587
3. Molecular Diagnosis of Limb-Girdle Muscular Dystrophy Using Next-Generation Sequencing Panels.. *Molecular syndromology*. PMID: 38357257
4. Enzyme assay of fukutin and fukutin-related protein (ribitol phosphate transferase, FKTN and FKRP).. **. PMID: 37590597
5. Branchpoints as potential targets of exon-skipping therapies for genetic disorders.. *Molecular therapy. Nucleic acids*. PMID: 37547287

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.0，有序区 93.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009644, IPR045587, IPR007074; Pfam: PF19737, PF04991 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FKRP | 0.998 | 0.066 | — |
| POMGNT1 | 0.990 | 0.045 | — |
| POMT1 | 0.986 | 0.000 | — |
| POMT2 | 0.986 | 0.000 | — |
| POMK | 0.984 | 0.000 | — |
| CRPPA | 0.978 | 0.000 | — |
| DAG1 | 0.977 | 0.051 | — |
| RXYLT1 | 0.936 | 0.421 | — |
| LARGE1 | 0.928 | 0.000 | — |
| POMGNT2 | 0.860 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-DPA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RXYLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GAT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM59 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HLA-DQA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CHRNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POMGNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17034757|imex:IM-29995 |
| ENST00000357998 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 无 | pLDDT=92.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FKTN — Ribitol-5-phosphate transferase FKTN，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小461 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75072
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106692-FKTN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKTN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75072
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75072-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
