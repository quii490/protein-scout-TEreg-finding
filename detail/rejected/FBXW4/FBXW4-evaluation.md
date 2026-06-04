---
type: protein-evaluation
gene: "FBXW4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXW4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXW4 / FBW4, SHFM3 |
| 蛋白名称 | F-box/WD repeat-containing protein 4 |
| 蛋白大小 | 412 aa / 46.3 kDa |
| UniProt ID | P57775 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 46.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR052301, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBW4, SHFM3 |

**关键文献**:
1. Pivotal Role of FBXW4 in Glioma Progression and Prognosis.. *Genetics research*. PMID: 39377096
2. Elucidating the role of FBXW4 in osteoporosis: integrating bioinformatics and machine learning for advanced insight.. *BMC pharmacology & toxicology*. PMID: 39881357
3. FBXW4 Is Highly Expressed and Associated With Poor Survival in Acute Myeloid Leukemia.. *Frontiers in oncology*. PMID: 32175272
4. Identification of hypertrophy-modulating Cullin-RING ubiquitin ligases in primary cardiomyocytes.. *Frontiers in physiology*. PMID: 36969608
5. The novel ubiquitin ligase complex, SCF(Fbxw4), interacts with the COP9 signalosome in an F-box dependent manner, is mutated, lost and under-expressed in human cancers.. *PloS one*. PMID: 23658844

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 77.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.5，有序区 92.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR052301, IPR015943, IPR036322; Pfam: PF12937, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.933 | 0.782 | — |
| POLL | 0.925 | 0.000 | — |
| CUL1 | 0.911 | 0.818 | — |
| LBX1 | 0.894 | 0.000 | — |
| CCT5 | 0.885 | 0.775 | — |
| CCT3 | 0.863 | 0.730 | — |
| CCT4 | 0.861 | 0.676 | — |
| CCT8 | 0.859 | 0.730 | — |
| CCT7 | 0.843 | 0.692 | — |
| TXNDC9 | 0.819 | 0.814 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| CDC37 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| ECSIT | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| MAST1 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| RNF32 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22632967|imex:IM-17368 |
| CCT6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDCL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 无 | pLDDT=90.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXW4 — F-box/WD repeat-containing protein 4，非常新颖，仅有少数基础研究。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57775
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107829-FBXW4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXW4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57775
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
