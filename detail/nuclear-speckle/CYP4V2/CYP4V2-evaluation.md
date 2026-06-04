---
type: protein-evaluation
gene: "CYP4V2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP4V2 — REJECTED (研究热度过高 (PubMed strict=195，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP4V2 |
| 蛋白名称 | Cytochrome P450 4V2 |
| 蛋白大小 | 525 aa / 60.7 kDa |
| UniProt ID | Q6ZWL3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear speckles; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 525 aa / 60.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=195 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=90.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.5/180** | |
| **归一化总分** | | | **40.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 195 |
| PubMed broad count | 201 |
| 别名(未计入scoring) |  |

**关键文献**:
1. ZVS101e: AAV-mediated gene replacement therapy for Bietti crystalline corneoretinal dystrophy (BCD).. *Asia Pac J Ophthalmol (Phila)*. PMID: 42025802
2. Fundus Autofluorescence as a Sensitive Biomarker of Disease Progression in Bietti Crystalline Dystrophy.. *Ophthalmol Sci*. PMID: 42022046
3. Development and Validation of a Quantitative LC-MS/MS Method for Measuring CYP4V2 Enzyme Activity via 12-Hydroxylauric Acid in rAAV-hCYP4V2 Gene Therapy Products.. *Molecules*. PMID: 42123783
4. Ageratina adenophora aqueous extract impairs Ascaris suum egg embryonation and infectivity via disruption of metabolic and detoxification pathways.. *Front Vet Sci*. PMID: 42100221
5. Bietti crystalline dystrophy in Türkiye: A genetic crossroads between Asia and Europe.. *Graefes Arch Clin Exp Ophthalmol*. PMID: 42008154

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 77.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 2.7% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POR | 0.000 | 0.000 | — |
| GFM1 | 0.000 | 0.000 | — |
| NDOR1 | 0.000 | 0.000 | — |
| AACS | 0.000 | 0.000 | — |
| MTRR | 0.000 | 0.000 | — |
| LSS | 0.000 | 0.000 | — |
| SC5D | 0.000 | 0.000 | — |
| DIP2C | 0.000 | 0.000 | — |
| GATC | 0.000 | 0.000 | — |
| SQLE | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q6ZWL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O43716 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O60524-3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-21019856 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 6
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 无 | pLDDT=90.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 25 + 6 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CYP4V2 -- Cytochrome P450 4V2，研究基础较多，新颖性有限。
2. 蛋白大小525 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 195 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 195 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZWL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145476-CYP4V2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP4V2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZWL3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
