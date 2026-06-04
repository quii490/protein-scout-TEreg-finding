---
type: protein-evaluation
gene: "CARF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARF — REJECTED (研究热度过高 (PubMed strict=102，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARF / ALS2CR8 |
| 蛋白名称 | Calcium-responsive transcription factor |
| 蛋白大小 | 725 aa / 80.7 kDa |
| UniProt ID | Q8N187 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Vesicles; 额外: Nucleoli fibrillar center, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 725 aa / 80.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=102 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=55.5; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR029309; Pfam: PF15299 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- granular component (GO:0001652)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 102 |
| PubMed broad count | 386 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALS2CR8 |

**关键文献**:
1. The CRISPR effector Cam1 mediates membrane depolarization for phage defence.. *Nature*. PMID: 38200316
2. Novel FMRP interaction networks linked to cellular stress.. *The FEBS journal*. PMID: 32525608
3. Fine Mapping and Gene Analysis of restorer-of-fertility Gene CaRf(HZ) in Pepper (Capsicum annuum L.).. *International journal of molecular sciences*. PMID: 35886981
4. CARF is a multi-module regulator of cell proliferation and a molecular bridge between cellular senescence and carcinogenesis.. *Mechanisms of ageing and development*. PMID: 28754531
5. Antiviral signaling of a type III CRISPR-associated deaminase.. *Science (New York, N.Y.)*. PMID: 39666823

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 24.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 58.9% |
| 有序区域 (pLDDT>70) 占比 | 32.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.5），有序残基占 32.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029309; Pfam: PF15299 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BDNF | 0.637 | 0.000 | — |
| MECP2 | 0.509 | 0.000 | — |
| TRPC6 | 0.496 | 0.000 | — |
| CPA5 | 0.477 | 0.000 | — |
| THADA | 0.476 | 0.000 | — |
| NTRK2 | 0.476 | 0.000 | — |
| TMEM260 | 0.475 | 0.000 | — |
| NBEAL1 | 0.474 | 0.000 | — |
| NTF4 | 0.454 | 0.000 | — |
| USF1 | 0.453 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LMO3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CDKN2AIP | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| purCD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Clp1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DHX58 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ZSCAN31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PKM | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |
| EBI-9351778 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5 + PDB: 无 | pLDDT=55.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Vesicles; 额外: Nucleoli fibrillar center, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CARF -- Calcium-responsive transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小725 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 102 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 102 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N187
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138380-CARF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N187
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
