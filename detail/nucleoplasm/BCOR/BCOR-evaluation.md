---
type: protein-evaluation
gene: "BCOR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCOR — REJECTED (研究热度过高 (PubMed strict=536，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCOR / KIAA1575 |
| 蛋白名称 | BCL-6 corepressor |
| 蛋白大小 | 1755 aa / 192.2 kDa |
| UniProt ID | Q6W2J9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1755 aa / 192.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=536 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=39.6; PDB: 2N1L, 3BIM, 4HPL, 6B7G, 8HCU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR031628, IPR047144, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BCOR complex (GO:0140261)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 536 |
| PubMed broad count | 1008 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1575 |

**关键文献**:
1. Genomic Classification and Clinical Outcome in Rhabdomyosarcoma: A Report From an International Consortium.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 34166060
2. Epigenetic regulation of noncanonical menin targets modulates menin inhibitor response in acute myeloid leukemia.. *Blood*. PMID: 39158067
3. Genotypic and Phenotypic Characteristics of Acute Promyelocytic Leukemia Translocation Variants.. *Hematology/oncology and stem cell therapy*. PMID: 32473106
4. What is new in acute myeloid leukemia classification?. *Blood research*. PMID: 38616211
5. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 39.6 |
| 高置信度残基 (pLDDT>90) 占比 | 7.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 86.0% |
| 有序区域 (pLDDT>70) 占比 | 12.6% |
| 可用 PDB 条目 | 2N1L, 3BIM, 4HPL, 6B7G, 8HCU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=39.6），有序残基占 12.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR031628, IPR047144, IPR032365; Pfam: PF12796, PF15808, PF16553 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCGF1 | 0.999 | 0.989 | — |
| BCL6 | 0.999 | 0.983 | — |
| RNF2 | 0.995 | 0.849 | — |
| RING1 | 0.994 | 0.835 | — |
| MLLT3 | 0.994 | 0.978 | — |
| KDM2B | 0.986 | 0.851 | — |
| CBX8 | 0.971 | 0.604 | — |
| RYBP | 0.960 | 0.841 | — |
| PCGF2 | 0.958 | 0.523 | — |
| BMI1 | 0.958 | 0.523 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP7 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| proS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Rnf2 | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| Kdm2b | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| fabB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GOLGA2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CRY1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27254|pubmed:23133559 |
| ENSP00000505761.1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-25601|pubmed:27505670 |
| EBI-10049836 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-25601|pubmed:27505670 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=39.6 + PDB: 2N1L, 3BIM, 4HPL, 6B7G, 8HCU | pLDDT=39.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BCOR — BCL-6 corepressor，研究基础较多，新颖性有限。
2. 蛋白大小1755 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 536 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=39.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 536 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6W2J9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183337-BCOR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCOR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6W2J9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
