---
type: protein-evaluation
gene: "CTU1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTU1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTU1 |
| 蛋白名称 | Cytoplasmic tRNA 2-thiolation protein 1 |
| 蛋白大小 | 348 aa / 36.5 kDa |
| UniProt ID | Q7Z7A3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 348 aa / 36.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 22 |
| 别名(未计入scoring) |  |

**关键文献**:
1. RBAD: The first database dedicated alterations of blood RNA in individuals with Alzheimer's disease and their clinical relevance.. *Neural Regen Res*. PMID: 40145964
2. De Novo Design of Efficient NIR-II-Activated Heavy-Atom-Free Type-I Photosensitizer for Anti-Tumor Photoimmunotherapy.. *Adv Mater*. PMID: 40465313
3. mTORC1 cooperates with tRNA wobble modification to sustain the protein synthesis machinery.. *Nat Commun*. PMID: 40328729
4. The conserved wobble uridine tRNA thiolase Ctu1 is required for angiogenesis and embryonic development.. *PLoS One*. PMID: 39705244
5. The thiolation of uridine 34 in tRNA, which controls protein translation, depends on a [4Fe-4S] cluster in the archaeum Methanococcus maripaludis.. *Sci Rep*. PMID: 37005440

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.1 |
| 高置信度残基 (pLDDT>90) 占比 | 59.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 83.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.1，有序区 83.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| URM1 | 0.000 | 0.000 | — |
| CTU2 | 0.000 | 0.000 | — |
| MOCS3 | 0.000 | 0.000 | — |
| ELP3 | 0.000 | 0.000 | — |
| FTSJ3 | 0.000 | 0.000 | — |
| GPI | 0.000 | 0.000 | — |
| NFS1 | 0.000 | 0.000 | — |
| DDX56 | 0.000 | 0.000 | — |
| MPST | 0.000 | 0.000 | — |
| WDR74 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9VWQ7 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P53088 | psi-mi:"MI:0089"(protein array) | pubmed:- |
| uniprotkb:Q9FZK5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q7JWW5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q7Z7A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q05AW7 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.1 + PDB: 无 | pLDDT=84.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTU1 -- Cytoplasmic tRNA 2-thiolation protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z7A3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142544-CTU1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTU1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z7A3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z7A3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
