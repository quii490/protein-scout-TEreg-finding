---
type: protein-evaluation
gene: "DNAJA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJA3 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJA3 |
| 蛋白名称 | DnaJ homolog subfamily A member 3, mitochondrial |
| 蛋白大小 | 480 aa / 52.5 kDa |
| UniProt ID | Q96EY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; 额外: Vesicles; UniProt: Mitochondrion matrix; Cytoplasm, cytosol; Postsynaptic cell  |
| 蛋白大小 | 10/10 | x1 | 10 | 480 aa / 52.5 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=48 篇 (<=60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=74.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Vesicles | Supported |
| UniProt | Mitochondrion matrix; Cytoplasm, cytosol; Postsynaptic cell membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 96 |
| 别名(未计入scoring) |  |

**关键文献**:
1. mtHsp70 overexpression enhances neuroprotection through ATF5-dependent UPRmt signaling after traumatic brain injury.. *Exp Neurol*. PMID: 41999829
2. Gut Microbiota-Derived Propionate Governs Hepatic N2 Neutrophils in Wilson's Disease.. *Cell Mol Gastroenterol Hepatol*. PMID: 41850677
3. Clinical utility of genome sequencing in rare diseases: lessons from a single-center study of 1,452 Korean families.. *NPJ Genom Med*. PMID: 41354729
4. Investigating the Mechanisms of Mitochondrial Dysfunction in Ischemic Stroke and Predicting Therapeutics Through Machine Learning and Integrated Bioinformatics.. *Curr Med Chem*. PMID: 41088987
5. DNAJA3 interacts with ASFV MGF360-14L protein and reduces MGF360-14L antagonistic role on Beta interferon production.. *Int J Biol Macromol*. PMID: 40233912

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 40.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 26.7% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.2，有序区 63.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA9 | 0.000 | 0.000 | — |
| HSPA8 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| GRPEL1 | 0.000 | 0.000 | — |
| GRPEL2 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| CLPP | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 无 | pLDDT=74.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion matrix; Cytoplasm, cytosol; Postsyna / Mitochondria; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DNAJA3 -- DnaJ homolog subfamily A member 3, mitochondrial，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小480 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103423-DNAJA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
