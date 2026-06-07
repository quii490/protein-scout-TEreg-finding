---
type: protein-evaluation
gene: "P3H3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## P3H3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/P3H3/IF_images/512_B11_3_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/P3H3/IF_images/512_B11_7_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | P3H3 |
| 蛋白名称 | Prolyl 3-hydroxylase 3 |
| 蛋白大小 | 736 aa |
| UniProt ID | [Q8IVL6](https://www.uniprot.org/uniprotkb/Q8IVL6) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 81.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: Endoplasmic reticulum |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 736 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 81.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 P3H3 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Khan MM et al. (2024). "Dextromethorphan inhibits collagen and collagen-like cargo secretion to ameliorate lung fibrosis". *Sci Transl Med*. PMID: 39693409
2. Li Y et al. (2018). "Collagen prolyl hydroxylase 3 has a tumor suppressive activity in human lung cancer". *Exp Cell Res*. PMID: 29277505
3. Tian Y et al. (2023). "Identifying Immune Cell Infiltration and Hub Genes During the Myocardial Remodeling Process After Myocardial Infarction". *J Inflamm Res*. PMID: 37456781
4. Li Q et al. (2024). "Role of ZNF334 in cervical cancer: implications for EMT reversal and tumor suppression". *Med Oncol*. PMID: 38954116
5. Lin Y et al. (2024). "Identification of cuproptosis-related genes and immune infiltration in dilated cardiomyopathy". *Int J Cardiol*. PMID: 38168558

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| kra92_human | validated two hybrid | 32296183 | — | — |
| B2B | two hybrid array | 32296183 | — | — |
| kr123_human | two hybrid array | 32296183 | — | — |
| KRT31 | validated two hybrid | 32296183 | — | — |
| TRIM63 | two hybrid prey pooling approach | 31391242 | — | — |
| TRIM55 | two hybrid prey pooling approach | 31391242 | — | — |
| SPRED1 | two hybrid array | 32814053 | — | — |
| HTT | two hybrid array | 32814053 | — | — |
| OPTN | two hybrid array | 32814053 | — | — |
| UBQLN1 | two hybrid pooling approach | 32814053 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Endoplasmic reticulum

**IntAct 查询记录**: IntAct: 14 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 81.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/P3H3)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IVL6)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=P3H3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IVL6)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IVL6 |
| SMART | SM00702; |
| UniProt Domain [FT] | DOMAIN 561..675; /note="Fe2OG dioxygenase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00805" |
| InterPro | IPR056585;IPR005123;IPR039575;IPR006620;IPR044862;IPR011990; |
| Pfam | PF13640;PF23557; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110811-P3H3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADAMTS4 | Bioplex | false |
| ALPP | Bioplex | false |
| C1QTNF9 | Bioplex | false |
| C1QTNF9B | Bioplex | false |
| C1orf54 | Bioplex | false |
| CA6 | Bioplex | false |
| CBLN4 | Bioplex | false |
| CFC1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
