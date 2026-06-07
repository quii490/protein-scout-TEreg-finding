---
type: protein-evaluation
gene: "OPHN1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## OPHN1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/OPHN1/IF_images/57_A3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/OPHN1/IF_images/57_A3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | OPHN1 |
| 蛋白名称 | Oligophrenin-1 |
| 蛋白大小 | 694 aa |
| UniProt ID | [A0A7P0Z4E9](https://www.uniprot.org/uniprotkb/A0A7P0Z4E9) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 97 |
| AlphaFold pLDDT | 78.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cell projection, dendrite; Cell projection, dendritic spine; Cytoplasm; Presynapse |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 694 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 97篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **89/183** |  |
| **归一化总分** |  |  | **48.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 OPHN1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cell projection, dendrite; Cell projection, dendritic spine; Cytoplasm; Presynapse
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zhou H et al. (2024). "Whole exome sequencing analysis of 167 men with primary infertility". *BMC Med Genomics*. PMID: 39267058
2. Bennett JA et al. (2018). "Uterine PEComas: A Morphologic, Immunohistochemical, and Molecular Analysis of 32 Tumors". *Am J Surg Pathol*. PMID: 30001237
3. des Portes V (2013). "X-linked mental deficiency". *Handb Clin Neurol*. PMID: 23622180
4. Houy S et al. (2015). "Oligophrenin-1 Connects Exocytotic Fusion to Compensatory Endocytosis in Neuroendocrine Cells". *J Neurosci*. PMID: 26245966
5. Liu J et al. (2022). "Androgen deprivation‑induced OPHN1 amplification promotes castration‑resistant prostate cancer". *Oncol Rep*. PMID: 34738630

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

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅97篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/OPHN1)
- [UniProt](https://www.uniprot.org/uniprotkb/A0A7P0Z4E9)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=OPHN1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/A0A7P0Z4E9)


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
| UniProt | O60890 |
| SMART | SM00233;SM00324; |
| UniProt Domain [FT] | DOMAIN 265..368; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 380..564; /note="Rho-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00172" |
| InterPro | IPR027267;IPR004148;IPR047234;IPR047267;IPR011993;IPR001849;IPR047225;IPR008936;IPR000198; |
| Pfam | PF16746;PF00169;PF00620; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000079482-OPHN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC42 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
