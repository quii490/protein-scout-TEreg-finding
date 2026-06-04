---
type: protein-evaluation
gene: "CLPTM1L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLPTM1L — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=190，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLPTM1L |
| 蛋白名称 | Lipid scramblase CLPTM1L |
| 蛋白大小 | 538 aa / 62.2 kDa |
| UniProt ID | Q96KA5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 538 aa / 62.2 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=190 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=78.4; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 190 |
| PubMed broad count | 199 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Novel Genetic Risk Loci for Pancreatic Ductal Adenocarcinoma Identified in a Genome-wide Study of African Ancestry Individuals.. *medRxiv*. PMID: 42078392
2. Integrative screening identifies functional variants and VNTRs underlying GWAS signals at the 5p15.33 multi-cancer susceptibility locus.. *medRxiv*. PMID: 41867231
3. Erk5-mediated microglial ferroptosis drives ischemic white matter damage via the Nfatc4-Clptm1l axis.. *Proc Natl Acad Sci U S A*. PMID: 41512030
4. Exploring the association between DNA methylation and pancreatic cancer susceptibility through epigenome-wide Mendelian randomization and multi-omics data integration.. *Epigenetics*. PMID: 41368819
5. Association of pre-and postnatal mercury exposure with cardiometabolic risk factors in children: the role of the telomere length and telomerase reverse transcriptase polymorphisms.. *Environ Int*. PMID: 41205373

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.9% |
| 置信残基 (pLDDT 70-90) 占比 | 63.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.4，有序区 80.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERT | 0.000 | 0.000 | — |
| RNASEH2A | 0.000 | 0.000 | — |
| NR5A2 | 0.000 | 0.000 | — |
| DMRT1 | 0.000 | 0.000 | — |
| ATF7IP | 0.000 | 0.000 | — |
| SLC6A18 | 0.000 | 0.000 | — |
| ETNK1 | 0.000 | 0.000 | — |
| CHRNA3 | 0.000 | 0.000 | — |
| HYKK | 0.000 | 0.000 | — |
| LPCAT1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96KA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P32189 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9H3M0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96KA5-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 3 / 20 = 15%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 15%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 无 | pLDDT=78.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLPTM1L -- Lipid scramblase CLPTM1L，研究基础较多，新颖性有限。
2. 蛋白大小538 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 190 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KA5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000049656-CLPTM1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLPTM1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KA5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
