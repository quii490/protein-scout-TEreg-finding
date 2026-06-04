---
type: protein-evaluation
gene: "CTNNAL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTNNAL1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTNNAL1 |
| 蛋白名称 | Alpha-catulin |
| 蛋白大小 | 734 aa / 81.9 kDa |
| UniProt ID | Q9UBT7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton; Cell membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 734 aa / 81.9 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.1; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR036723, IPR001033, IPR030045, IPR006077; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 52 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Associations of TCF12, CTNNAL1 and WNT10B gene polymorphisms with litter size in pigs.. *Animal reproduction science*. PMID: 23820070
2. Genetic variants in RET, ARHGEF3 and CTNNAL1, and relevant interaction networks, contribute to the risk of Hirschsprung disease.. *Aging*. PMID: 32139661
3. Regulation of Cancer Stem Cells and Epithelial-Mesenchymal Transition by CTNNAL1 in Lung Cancer and Glioblastoma.. *Biomedicines*. PMID: 37239133
4. Identification and chromosomal localization of CTNNAL1, a novel protein homologous to alpha-catenin.. *Genomics*. PMID: 9806841
5. CTNNAL1 participates in the regulation of mucus overproduction in HDM-induced asthma mouse model through the YAP-ROCK2 pathway.. *Journal of cellular and molecular medicine*. PMID: 35092120

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.1 |
| 高置信度残基 (pLDDT>90) 占比 | 65.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.1，有序区 83.5%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036723, IPR001033, IPR030045, IPR006077; Pfam: PF01044 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTL7A | 0.950 | 0.050 | — |
| ACTL7B | 0.936 | 0.050 | — |
| DMD | 0.923 | 0.829 | — |
| AKAP13 | 0.864 | 0.292 | — |
| DTNA | 0.808 | 0.328 | — |
| UTRN | 0.771 | 0.637 | — |
| SNTG2 | 0.754 | 0.729 | — |
| SNTB2 | 0.727 | 0.628 | — |
| ADRA1D | 0.666 | 0.625 | — |
| CTNNB1 | 0.657 | 0.296 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.1 + PDB: 无 | pLDDT=84.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTNNAL1 -- Alpha-catulin，非常新颖，仅有少数基础研究。
2. 蛋白大小734 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBT7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119326-CTNNAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTNNAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBT7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
