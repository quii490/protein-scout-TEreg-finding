---
type: protein-evaluation
gene: "HR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HR — REJECTED (研究热度过高 (PubMed strict=48199，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HR |
| 蛋白名称 | Lysine-specific demethylase hairless |
| 蛋白大小 | 1189 aa / 127.5 kDa |
| UniProt ID | O43593 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1189 aa / 127.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=48199 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003347, IPR045109; Pfam: PF02373 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- histone deacetylase complex (GO:0000118)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48199 |
| PubMed broad count | 440755 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Classic Thrombophilias and Thrombotic Risk Among Middle-Aged and Older Adults: A Population-Based Cohort Study.. *Journal of the American Heart Association*. PMID: 35112923
2. PD-1 protein and gene expression as prognostic factors in early breast cancer.. *ESMO open*. PMID: 33172959
3. RNA methylation, homologous recombination repair and therapeutic resistance.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 37659205
4. Human Hairless Protein Roles in Skin/Hair and Emerging Connections to Brain and Other Cancers.. *Journal of cellular biochemistry*. PMID: 28543886
5. Autophagy induction enhances homologous recombination-associated CRISPR-Cas9 gene editing.. *Nucleic acids research*. PMID: 40239991

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 55.4% |
| 有序区域 (pLDDT>70) 占比 | 35.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.2），有序残基占 35.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003347, IPR045109; Pfam: PF02373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP27B1 | 0.530 | 0.510 | — |
| HDAC1 | 0.528 | 0.516 | — |
| FAM131C | 0.523 | 0.000 | — |
| JMJD7 | 0.444 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q80Y47 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| CPSF30 | psi-mi:"MI:0018"(two hybrid) | pubmed:18479511|imex:IM-19266 |
| NDR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17012600|imex:IM-19393 |
| RIN4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17012600|imex:IM-19393 |
| RPS2 | psi-mi:"MI:0096"(pull down) | pubmed:19000159|imex:IM-20263 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| Thrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15086341|imex:IM-27315 |
| ENSP00000505181.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZMYND12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 15
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.2 + PDB: 无 | pLDDT=55.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 4 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HR — Lysine-specific demethylase hairless，研究基础较多，新颖性有限。
2. 蛋白大小1189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48199 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 48199 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43593
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168453-HR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43593
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000168453-HR/subcellular

![](https://images.proteinatlas.org/54888/1203_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/54888/1203_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/54888/874_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/54888/874_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/54888/881_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/54888/881_A1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43593-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43593 |
| SMART | SM00558; |
| UniProt Domain [FT] | DOMAIN 946..1157; /note="JmjC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00538" |
| InterPro | IPR003347;IPR045109; |
| Pfam | PF02373; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168453-HR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP23 | Intact | false |
| C11orf1 | Intact | false |
| CNFN | Intact | false |
| CYSRT1 | Intact | false |
| GEMIN4 | Intact | false |
| HDAC1 | Biogrid | false |
| INCA1 | Intact | false |
| KRTAP11-1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
