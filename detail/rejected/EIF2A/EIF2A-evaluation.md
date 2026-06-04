---
type: protein-evaluation
gene: "EIF2A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF2A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=369，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2A |
| 蛋白名称 | Eukaryotic translation initiation factor 2A |
| 蛋白大小 | 585 aa / 65.0 kDa |
| UniProt ID | Q9BY44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 585 aa / 65.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=369 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.5; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 369 |
| PubMed broad count | 373 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Capillarisenol C, a novel bisphenol from Artemisia capillaris, induces ER stress-mediated cytotoxic autophagy in liver cancer cells.. *Food Chem Toxicol*. PMID: 42203023
2. DUXA is not essential for parthenogenetic blastocyst formation but regulates cell proliferation in porcine embryos.. *Reproduction*. PMID: 42116739
3. Knowledge Discovery and Drug-Repurposing Framework for Pancreatic Ductal Adenocarcinoma: Molecular Networking and Computational Docking.. *Comput Struct Biotechnol J*. PMID: 42093818
4. The nuclear cap-binding complex safeguards stress-resistant protein synthesis and proliferation of stem cells.. *Sci Adv*. PMID: 42054446
5. Exploiting autophagy-targeting natural compounds for potential antimicrobial actions.. *Autophagy*. PMID: 42047332

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 59.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 86.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.5，有序区 86.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2S1 | 0.000 | 0.000 | — |
| EIF3B | 0.000 | 0.000 | — |
| EIF2S3 | 0.000 | 0.000 | — |
| EIF2S2 | 0.000 | 0.000 | — |
| EIF2AK2 | 0.000 | 0.000 | — |
| EIF5B | 0.000 | 0.000 | — |
| RPS6 | 0.000 | 0.000 | — |
| EIF2AK4 | 0.000 | 0.000 | — |
| EIF2AK3 | 0.000 | 0.000 | — |
| RPS19 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9VNX8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8T053 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9XYZ6 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P45975 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P05198 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q6ZWX6 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P68101 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8U1R5 | psi-mi:"MI:0091"(chromatography technology) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P62137 | psi-mi:"MI:0678"(antibody array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 无 | pLDDT=85.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 待确认 |
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
1. EIF2A — Eukaryotic translation initiation factor 2A，研究基础较多，新颖性有限。
2. 蛋白大小585 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 369 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BY44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144895-EIF2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BY44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
