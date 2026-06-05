---
type: protein-evaluation
gene: "GNA15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNA15 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNA15 / GNA16 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit alpha-15 |
| 蛋白大小 | 374 aa / 43.5 kDa |
| UniProt ID | P30679 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 43.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000654, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- heterotrimeric G-protein complex (GO:0005834)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNA16 |

**关键文献**:
1. Gα15 in early onset of pancreatic ductal adenocarcinoma.. *Scientific reports*. PMID: 34290274
2. Gene structure of murine Gna11 and Gna15: tandemly duplicated Gq class G protein alpha subunit genes.. *Genomics*. PMID: 8838318
3. Identification and validation of apoptosis-related genes in acute myocardial infarction based on integrated bioinformatics methods.. *PeerJ*. PMID: 39650552
4. Identification of a Diagnosis and Therapeutic Inflammatory Response-Related Gene Signature Associated with Esophageal Adenocarcinoma.. *Critical reviews in eukaryotic gene expression*. PMID: 37602454
5. Multiomics profiling identifies the poor prognostic role of a tumor cluster with GNA15 overexpression in triple-negative breast cancer.. *Frontiers in immunology*. PMID: 41058682

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000654, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLCB2 | 0.976 | 0.071 | — |
| PLCB3 | 0.948 | 0.071 | — |
| PLCB1 | 0.947 | 0.071 | — |
| PLCB4 | 0.940 | 0.071 | — |
| RXFP4 | 0.927 | 0.115 | — |
| BDKRB2 | 0.921 | 0.115 | — |
| S1PR4 | 0.892 | 0.115 | — |
| GRK2 | 0.878 | 0.370 | — |
| GNB5 | 0.839 | 0.413 | — |
| GNA14 | 0.832 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FECH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APPBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MLF1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| Hacd3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| MLF2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| E9KL47 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| PSMD2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNA15 — Guanine nucleotide-binding protein subunit alpha-15，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P30679
- Protein Atlas: https://www.proteinatlas.org/ENSG00000060558-GNA15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNA15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P30679
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P30679-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
