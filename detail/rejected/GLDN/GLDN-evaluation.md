---
type: protein-evaluation
gene: "GLDN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLDN — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLDN / COLM |
| 蛋白名称 | Gliomedin |
| 蛋白大小 | 551 aa / 59.0 kDa |
| UniProt ID | Q6ZMI3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles, Plasma membrane; UniProt: Cell membrane; Cell projection, axon; Secreted; Secreted, ex |
| 蛋白大小 | 10/10 | ×1 | 10 | 551 aa / 59.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=72.7; PDB: 5YBY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008160, IPR003112, IPR050605; Pfam: PF01391, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane | Supported |
| UniProt | Cell membrane; Cell projection, axon; Secreted; Secreted, extracellular space, extracellular matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cell surface (GO:0009986)
- collagen trimer (GO:0005581)
- extracellular space (GO:0005615)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COLM |

**关键文献**:
1. Phenotypic spectrum and genomics of undiagnosed arthrogryposis multiplex congenita.. *Journal of medical genetics*. PMID: 33820833
2. Identification and Mapping of Human Lymph Node Stromal Cell Subsets by Combining Single-Cell RNA Sequencing with Spatial Transcriptomics.. *European journal of immunology*. PMID: 40498289
3. Expanding MNS1 Heterotaxy Phenotype.. *American journal of medical genetics. Part A*. PMID: 39233552
4. Flavobacterium johnsoniae gldN and gldO are partially redundant genes required for gliding motility and surface localization of SprB.. *Journal of bacteriology*. PMID: 20038590
5. Type IX Secretion System Effectors and Virulence of the Model Flavobacterium columnare Strain MS-FC-4.. *Applied and environmental microbiology*. PMID: 34818105

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.3% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 27.6% |
| 有序区域 (pLDDT>70) 占比 | 54.1% |
| 可用 PDB 条目 | 5YBY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=72.7，有序区 54.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008160, IPR003112, IPR050605; Pfam: PF01391, PF02191 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFASC | 0.998 | 0.000 | — |
| NRCAM | 0.996 | 0.000 | — |
| SPTBN4 | 0.807 | 0.000 | — |
| CNTNAP1 | 0.734 | 0.000 | — |
| CNTN1 | 0.683 | 0.000 | — |
| ANK3 | 0.657 | 0.000 | — |
| TNFAIP8L3 | 0.605 | 0.000 | — |
| HSPG2 | 0.578 | 0.000 | — |
| HAPLN2 | 0.565 | 0.000 | — |
| MYOC | 0.563 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CLU | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 5YBY | pLDDT=72.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, axon; Secreted; Se / Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLDN — Gliomedin，非常新颖，仅有少数基础研究。
2. 蛋白大小551 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZMI3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186417-GLDN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLDN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZMI3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
