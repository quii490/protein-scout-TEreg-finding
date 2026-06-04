---
type: protein-evaluation
gene: "EFHC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFHC2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFHC2 |
| 蛋白名称 | EF-hand domain-containing family member C2 |
| 蛋白大小 | 749 aa / 87.4 kDa |
| UniProt ID | Q5JST6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskel |
| 蛋白大小 | 10/10 | ×1 | 10 | 749 aa / 87.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 18 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Theory of Mind: A Brief Review of Candidate Genes.. *Genes (Basel)*. PMID: 38927653
2. Study on Potential Differentially Expressed Genes in Idiopathic Pulmonary Fibrosis by Bioinformatics and Next-Generation Sequencing Data Analysis.. *Biomedicines*. PMID: 38137330
3. Clinical exome sequencing findings in 1589 patients.. *Am J Med Genet A*. PMID: 36964972
4. Sex differences in the intergenerational link between maternal and neonatal whole blood DNA methylation: a genome-wide analysis in 2 birth cohorts.. *Clin Epigenetics*. PMID: 36966332
5. The Role of Chromosome X in Intraocular Pressure Variation and Sex-Specific Effects.. *Invest Ophthalmol Vis Sci*. PMID: 32926103

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 63.0% |
| 中等置信 (pLDDT 50-70) 占比 | 18.0% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 79.0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=79.4，有序区 79.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PACRG | 0.000 | 0.000 | — |
| ENKUR | 0.000 | 0.000 | — |
| CFAP161 | 0.000 | 0.000 | — |
| TEKT2 | 0.000 | 0.000 | — |
| EFHB | 0.000 | 0.000 | — |
| CFAP45 | 0.000 | 0.000 | — |
| TEKT1 | 0.000 | 0.000 | — |
| CFAP20 | 0.000 | 0.000 | — |
| GPR82 | 0.000 | 0.000 | — |
| EFHC1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8IYI6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5JST6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O60568 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96HB5-4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q5JST6-1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O95833 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q13882 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 无 | pLDDT=79.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EFHC2 — EF-hand domain-containing family member C2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小749 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JST6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183690-EFHC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFHC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JST6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
