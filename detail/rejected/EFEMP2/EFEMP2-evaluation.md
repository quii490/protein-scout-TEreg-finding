---
type: protein-evaluation
gene: "EFEMP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFEMP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFEMP2 |
| 蛋白名称 | EGF-containing fibulin-like extracellular matrix protein 2 |
| 蛋白大小 | 443 aa / 49.4 kDa |
| UniProt ID | O95967 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted, extracellular space, extracellular matrix; Secrete |
| 蛋白大小 | 10/10 | ×1 | 10 | 443 aa / 49.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=96 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.0/180** | |
| **归一化总分** | | | **39.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Secreted, extracellular space, extracellular matrix; Secreted, extracellular space, extracellular ma... | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 96 |
| PubMed broad count | 177 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Beyond the genome: a rare case report of cutis laxa.. *AME Case Rep*. PMID: 41676178
2. Integrative gene target mapping, RNA sequencing, in silico molecular docking, ADMET profiling and molecular dynamics simulation study of marine derived molecules for type 1 diabetes mellitus.. *Mol Divers*. PMID: 41533020
3. Fibulin-4 is required for the mechanical stability of tendons.. *Cell Tissue Res*. PMID: 41231259
4. Integrative multi-omics analysis identifies AEBP1 and EFEMP2 as key regulators of immune heterogeneity and therapeutic response in glioblastoma.. *Discov Oncol*. PMID: 41026376
5. Proteome-driven transcriptomic dissection of EMT networks in bladder cancer based on the VIM and CDH2 protein macromolecules influence: From molecular-protein subtyping to therapeutic target prioritization.. *Int J Biol Macromol*. PMID: 40419050

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 12.9% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=82.4，有序区 85.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELN | 0.000 | 0.000 | — |
| LOX | 0.000 | 0.000 | — |
| ATP6V0A2 | 0.000 | 0.000 | — |
| FBN1 | 0.000 | 0.000 | — |
| ADAMTS2 | 0.000 | 0.000 | — |
| FBLN5 | 0.000 | 0.000 | — |
| MFAP2 | 0.000 | 0.000 | — |
| PYCR1 | 0.000 | 0.000 | — |
| MFAP5 | 0.000 | 0.000 | — |
| ALG2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O95967 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BUY5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8TCX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BQY4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96FE5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NRQ2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96EQ0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8NEC5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9HB75 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O15162 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 无 | pLDDT=82.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted, extracellular space, extracellular matri / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EFEMP2 — EGF-containing fibulin-like extracellular matrix protein 2，研究基础较多，新颖性有限。
2. 蛋白大小443 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 96 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95967
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172638-EFEMP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFEMP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95967
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
