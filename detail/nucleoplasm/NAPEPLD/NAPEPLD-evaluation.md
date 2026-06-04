---
type: protein-evaluation
gene: "NAPEPLD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NAPEPLD — REJECTED (研究热度过高 (PubMed strict=183，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAPEPLD / C7orf18 |
| 蛋白名称 | N-acyl-phosphatidylethanolamine-hydrolyzing phospholipase D |
| 蛋白大小 | 393 aa / 45.6 kDa |
| UniProt ID | Q6IQ20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Golgi apparatus membrane; Early endosome membrane; Nucleus e |
| 蛋白大小 | 10/10 | ×1 | 10 | 393 aa / 45.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=183 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.3; PDB: 4QN9, 8P90, 8P96, 8PC4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001279, IPR024884, IPR036866; Pfam: PF12706 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Uncertain |
| UniProt | Golgi apparatus membrane; Early endosome membrane; Nucleus envelope; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- early endosome (GO:0005769)
- early endosome membrane (GO:0031901)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- hippocampal mossy fiber to CA3 synapse (GO:0098686)
- neuron projection (GO:0043005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 183 |
| PubMed broad count | 313 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf18 |

**关键文献**:
1. Microglial morphological/inflammatory phenotypes and endocannabinoid signaling in a preclinical model of periodontitis and depression.. *Journal of neuroinflammation*. PMID: 39245706
2. Canine NAPEPLD-associated models of human myelin disorders.. *Scientific reports*. PMID: 29643404
3. Deciphering the interaction between N-palmitoyl-D-glucosamine and the endocannabinoidome.. *Scientific reports*. PMID: 40596256
4. Gene expression profiling reveals the genomic changes caused by MLN4924 and the sensitizing effects of NAPEPLD knockdown in pancreatic cancer.. *Cell cycle (Georgetown, Tex.)*. PMID: 34874801
5. Fluorescence-Based NAPE-PLD Activity Assay.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 36152191

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 77.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 4QN9, 8P90, 8P96, 8PC4 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4QN9, 8P90, 8P96, 8PC4）+ AlphaFold高质量预测（pLDDT=87.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001279, IPR024884, IPR036866; Pfam: PF12706 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAAH | 0.931 | 0.000 | — |
| MGLL | 0.920 | 0.000 | — |
| PLD2 | 0.918 | 0.000 | — |
| DAGLA | 0.894 | 0.000 | — |
| DAGLB | 0.890 | 0.000 | — |
| GDE1 | 0.854 | 0.000 | — |
| ABHD4 | 0.853 | 0.000 | — |
| ABHD6 | 0.821 | 0.000 | — |
| NAAA | 0.816 | 0.000 | — |
| FAAH2 | 0.807 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CLEC4M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000417955 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.3 + PDB: 4QN9, 8P90, 8P96, 8PC4 | pLDDT=87.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Early endosome membrane; / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. NAPEPLD — N-acyl-phosphatidylethanolamine-hydrolyzing phospholipase D，研究基础较多，新颖性有限。
2. 蛋白大小393 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 183 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 183 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IQ20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161048-NAPEPLD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAPEPLD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IQ20
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
