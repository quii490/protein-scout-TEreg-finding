---
type: protein-evaluation
gene: "EIF3J"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3J — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3J |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit J |
| 蛋白大小 | 258 aa / 29.1 kDa |
| UniProt ID | O75822 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 29.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 58 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Deletion of the translation initiation factor eIF3j promotes the synthesis of amylase and kojic acid in the fungus Aspergillus oryzae.. *Mycologia*. PMID: 42118908
2. Site-specific propynylation modification of apigeninidin enhances anti-cervical cancer activity by targeting PARP-1.. *Bioorg Chem*. PMID: 41653678
3. miR-101/METTL3 axis induces autophagy by interrupting FOXG1/EIF3J-AS1 binding in gliomas.. *Cell Death Dis*. PMID: 41390674
4. Yeast Eukaryotic Initiation Factor 4B Remodels the MRNA Entry Site on the Small Ribosomal Subunit.. *Biochemistry*. PMID: 39847343
5. LncRNA EIF3J-DT promotes chemoresistance in oral squamous cell carcinoma.. *Oral Dis*. PMID: 38817073

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 31.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 22.5% |
| 低置信 (pLDDT<50) 占比 | 30.2% |
| 有序区域 (pLDDT>70) 占比 | 47.3% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 47.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3I | 0.000 | 0.000 | — |
| EIF3D | 0.000 | 0.000 | — |
| EIF3C | 0.000 | 0.000 | — |
| EIF3K | 0.000 | 0.000 | — |
| EIF3E | 0.000 | 0.000 | — |
| EIF3G | 0.000 | 0.000 | — |
| EIF3A | 0.000 | 0.000 | — |
| EIF3B | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF3H | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q7K550 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O75822 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8T0N1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:O75821 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P55884 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13347 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9VD72 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VU87 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF3J — Eukaryotic translation initiation factor 3 subunit J，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75822
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104131-EIF3J/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3J
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75822
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
