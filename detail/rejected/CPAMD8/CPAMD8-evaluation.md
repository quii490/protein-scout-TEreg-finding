---
type: protein-evaluation
gene: "CPAMD8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPAMD8 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPAMD8 |
| 蛋白名称 | C3 and PZP-like alpha-2-macroglobulin domain-containing protein 8 |
| 蛋白大小 | 1885 aa / 206.7 kDa |
| UniProt ID | Q8IZJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Focal adhesion sites; UniProt: Secreted; Cell membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 1885 aa / 206.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 10 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites | Uncertain |
| UniProt | Secreted; Cell membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 43 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Clinical and Surgical Implications of Genotype-Phenotype Correlations in Congenital Ectopia Lentis: A Real-World Cohort Study.. *Invest Ophthalmol Vis Sci*. PMID: 42126156
2. A Rare Case of Childhood Glaucoma Resulting from Anterior Segment Dysgenesis Associated with a Homozygous Mutation in the CPAMD8 Gene.. *Genes (Basel)*. PMID: 42074612
3. Unraveling quantitative trait loci (QTL) overlapping epigenomic regulatory regions associated with feeding behavior in pigs.. *Front Genet*. PMID: 42039699
4. Integrating clinical and genetic insights in anterior segment dysgenesis with glaucoma: A contemporary review.. *Eur J Ophthalmol*. PMID: 41936534
5. Ophthalmological phenotype associated with biallelic CPAMD8 variants: first report in Mexican patients.. *Ophthalmic Genet*. PMID: 41917731

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 53.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 70.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FURIN | 0.000 | 0.000 | — |
| TRIM58 | 0.000 | 0.000 | — |
| GAA | 0.000 | 0.000 | — |
| ADAMTSL4 | 0.000 | 0.000 | — |
| GPATCH3 | 0.000 | 0.000 | — |
| PRSS48 | 0.000 | 0.000 | — |
| IQCC | 0.000 | 0.000 | — |
| MYOC | 0.000 | 0.000 | — |
| PROSER3 | 0.000 | 0.000 | — |
| P3H2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q6DN03 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q99878 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q8IZJ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 3
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted; Cell membrane / Focal adhesion sites | 一致 |
| PPI | STRING + IntAct | 10 + 3 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPAMD8 -- C3 and PZP-like alpha-2-macroglobulin domain-containing protein 8，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1885 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160111-CPAMD8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPAMD8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (uncertain)。来源: https://www.proteinatlas.org/ENSG00000160111-CPAMD8/subcellular

![](https://images.proteinatlas.org/31329/1457_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31329/1457_B3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/31329/1483_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31329/1483_B3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/31329/1830_D8_31_cr5ba8ac10ddf65_blue_red_green.jpg)
![](https://images.proteinatlas.org/31329/1830_D8_46_cr5ba8ac10ddf64_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZJ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
