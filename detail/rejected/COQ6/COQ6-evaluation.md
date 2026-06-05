---
type: protein-evaluation
gene: "COQ6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ6 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ6 |
| 蛋白名称 | Ubiquinone biosynthesis monooxygenase COQ6, mitochondrial |
| 蛋白大小 | 468 aa / 50.9 kDa |
| UniProt ID | Q9Y2Z9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane; Golgi apparatus; Cell projecti |
| 蛋白大小 | 10/10 | x1 | 10 | 468 aa / 50.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=83.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.0/180** | |
| **归一化总分** | | | **33.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Mitochondrion inner membrane; Golgi apparatus; Cell projection | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 153 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Mitochondrial NAD kinase Pos5 is required for CoQ biosynthesis in yeasts.. *PLoS One*. PMID: 41926382
2. The effect of SIRT1 knockdown on the gene expression of CoQ10 biosynthetic enzymes.. *J Clin Biochem Nutr*. PMID: 41841111
3. Consanguinity-linked genetic variants in Algerian patients with steroid-resistant nephrotic syndrome: a familial study.. *Pediatr Nephrol*. PMID: 41612037
4. Severe Neurological Presentation in Siblings With COQ5-Related Primary Coenzyme Q10 Deficiency: Expanding Clinical and Molecular Spectrum.. *JIMD Rep*. PMID: 41199775
5. Ovariectomy Enhances Carcass Performance and Meat Quality by Modulating Muscle Development and Lipid Metabolism in Wuding Hens.. *Animals (Basel)*. PMID: 41227511

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 57.1% |
| 置信残基 (pLDDT 70-90) 占比 | 26.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.9，有序区 84.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ3 | 0.000 | 0.000 | — |
| COQ5 | 0.000 | 0.000 | — |
| COQ4 | 0.000 | 0.000 | — |
| COQ7 | 0.000 | 0.000 | — |
| COQ9 | 0.000 | 0.000 | — |
| COQ2 | 0.000 | 0.000 | — |
| COQ8B | 0.000 | 0.000 | — |
| COQ8A | 0.000 | 0.000 | — |
| PDSS2 | 0.000 | 0.000 | — |
| PDSS1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P06634 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P19882 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10592 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11484 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P07259 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P16140 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y2Z9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q05516 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9VMQ5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P25303 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 无 | pLDDT=83.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane; Golgi apparatus; Cel / 暂无HPA定位数据 | 待确认 |
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
1. COQ6 -- Ubiquinone biosynthesis monooxygenase COQ6, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2Z9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119723-COQ6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2Z9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2Z9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
