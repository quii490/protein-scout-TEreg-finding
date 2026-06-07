---
type: protein-evaluation
gene: "TTC14"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TTC14 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TTC14/IF_images/100_G7_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TTC14/IF_images/100_G7_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TTC14 |
| 蛋白名称 | Tetratricopeptide repeat protein 14 |
| 蛋白大小 | 770 aa |
| UniProt ID | [Q96N46](https://www.uniprot.org/uniprotkb/Q96N46) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 5 |
| AlphaFold pLDDT | 62.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 770 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 5篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 62.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TTC14 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang H et al. (2023). "Identification and study of cuproptosis-related genes in prognostic model of multiple myeloma". *Hematology*. PMID: 37610069
2. Zhang T et al. (2025). "Integrated single-cell RNA-seq and bulk RNA-seq analysis to investigate key adipogenesis genes in adipose-derived stem cells". *PLoS One*. PMID: 41325391
3. Wang J et al. (2016). "Comparative Study of Autoantibody Responses between Lung Adenocarcinoma and Benign Pulmonary Nodules". *J Thorac Oncol*. PMID: 26896032
4. David D et al. (2015). "Clinical Severity of PGK1 Deficiency Due To a Novel p.E120K Substitution Is Exacerbated by Co-inheritance of a Subclinical Translocation t(3;14)(q26.33;q12), Disrupting NUBPL Gene". *JIMD Rep*. PMID: 25814383
5. Jia M et al. (2023). "[Bioinformatics analysis and validation of key genes in transformation of idiopathic membranous nephropathy to end-stage renal disease and traditional Chinese medicines for prevention and treatment]". *Zhongguo Zhong Yao Za Zhi*. PMID: 36872244

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 未检索到实验验证互作

**评价**: 待补充 IntAct/STRING/GO-CC 数据。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅5篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 62.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TTC14)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96N46)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TTC14%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96N46)


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
| UniProt | Q96N46 |
| SMART | SM00028; |
| UniProt Domain [FT] | DOMAIN 126..208; /note="S1 motif"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00180" |
| InterPro | IPR012340;IPR003029;IPR011990;IPR019734;IPR039190; |
| Pfam | PF13414; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163728-TTC14/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDK10 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
