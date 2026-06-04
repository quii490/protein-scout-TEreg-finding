---
type: protein-evaluation
gene: "EFNB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFNB1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=206，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFNB1 |
| 蛋白名称 | Ephrin-B1 |
| 蛋白大小 | 346 aa / 38.0 kDa |
| UniProt ID | P98172 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Plasma membrane; UniProt: Cell membrane; Membrane raft; Cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 346 aa / 38.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=206 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.7; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.5/180** | |
| **归一化总分** | | | **36.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cell membrane; Membrane raft; Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 206 |
| PubMed broad count | 616 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Clinical and Neurodevelopmental Course in a Case of EFNB1-Related Craniofrontonasal Syndrome With Unrepaired Craniosynostosis.. *Mol Genet Genomic Med*. PMID: 42026842
2. From brown to white: Brown adipose tissue endothelial cells whiten in culture conditions.. *Mol Metab*. PMID: 41831567
3. Evidence-based classification of genes implicated in craniosynostosis disorders using the ClinGen curation framework.. *Genet Med*. PMID: 42059179
4. Spatial Transcriptomics Reveals Injured Cells, Signature Genes, and Communication Patterns in the Cyst Microenvironment of Polycystic Kidney Disease.. *J Am Soc Nephrol*. PMID: 41071604
5. Distinct Involvement of X-Inactivation in Organogenesis.. *J Dent Res*. PMID: 41846522

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 31.5% |
| 有序区域 (pLDDT>70) 占比 | 53.5% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=70.7，有序区 53.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPHB1 | 0.000 | 0.000 | — |
| EPHB3 | 0.000 | 0.000 | — |
| EPHB6 | 0.000 | 0.000 | — |
| EPHB4 | 0.000 | 0.000 | — |
| EPHB2 | 0.000 | 0.000 | — |
| EPHA4 | 0.000 | 0.000 | — |
| EPHA1 | 0.000 | 0.000 | — |
| NCK2 | 0.000 | 0.000 | — |
| RGS3 | 0.000 | 0.000 | — |
| EPHA10 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P98172 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q62083 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O08992 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q925T6 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q6P7B6 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P27348 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9HC96 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P70424 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:- |
| uniprotkb:P04626 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:- |
| uniprotkb:Q86W74-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 无 | pLDDT=70.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Membrane raft; Cell membrane; Nucle / Plasma membrane | 一致 |
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
1. EFNB1 — Ephrin-B1，研究基础较多，新颖性有限。
2. 蛋白大小346 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 206 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P98172
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090776-EFNB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFNB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P98172
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
