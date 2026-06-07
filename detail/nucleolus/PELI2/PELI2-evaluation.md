---
type: protein-evaluation
gene: "PELI2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PELI2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm; Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PELI2/IF_images/1028_C3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PELI2/IF_images/1028_C3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PELI2 |
| 蛋白名称 | E3 ubiquitin-protein ligase pellino homolog 2 |
| 蛋白大小 | 420 aa |
| UniProt ID | [Q9HAT8](https://www.uniprot.org/uniprotkb/Q9HAT8) |
| HPA 核定位 (IF) | Nucleoplasm; Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 11 |
| AlphaFold pLDDT | 89.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoplasm; Nucleoli (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 420 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 11篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 89.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **136/183** |  |
| **归一化总分** |  |  | **74.3/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PELI2 定位：
- **亚细胞定位**: Nucleoplasm; Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ritchie C & Li L (2024). "PELI2 is a negative regulator of STING signaling that is dynamically repressed during viral infection". *Mol Cell*. PMID: 38917796
2. Liu J et al. (2025). "PELI2 inhibits colorectal cancer development through MAPK signaling pathway". *Mol Med*. PMID: 40500708
3. Xu Y et al. (2024). "PELI2 regulates early B-cell progenitor differentiation and related leukemia via the IL-7R expression". *Haematologica*. PMID: 38058209
4. Masuda T et al. (2022). "Identification of a drug-response gene in multiple myeloma through longitudinal single-cell transcriptome sequencing". *iScience*. PMID: 35992084
5. Cristea I et al. (2023). "A Pellino-2 variant is associated with constitutive NLRP3 inflammasome activation in a family with ocular pterygium-digital keloid dysplasia". *FEBS Lett*. PMID: 36776133

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| IRAK4 | two hybrid | 12860405 | — | — |
| IRAK1 | coimmunoprecipitation | 12860405 | — | — |
| Irak1 | anti tag coimmunoprecipitation | 12370331 | — | — |
| UBQLN4 | two hybrid array | 16713569 | — | — |
| ERO1A | two hybrid | 21988832 | — | — |
| THAP7 | two hybrid | 21988832 | — | — |
| CREB3L3 | two hybrid | 21988832 | — | — |
| FRYL | two hybrid | 21988832 | — | — |
| PICALM | two hybrid | 21988832 | — | — |
| LAMC3 | two hybrid | 21988832 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 31 实验验证互作

**评价**: —


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm; Nucleoli
2. **研究新颖性**: PubMed仅11篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 89.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PELI2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9HAT8)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PELI2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9HAT8)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HAT8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 15..202; /note="FHA; atypical" |
| InterPro | IPR006800;IPR048334;IPR048335; |
| Pfam | PF04710;PF20723; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139946-PELI2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IRAK1 | Intact, Biogrid | true |
| IRAK4 | Intact, Biogrid | true |
| CCNF | Biogrid | false |
| CLEC17A | Intact | false |
| DVL2 | Biogrid | false |
| HYAL2 | Intact | false |
| IRS1 | Biogrid | false |
| LZTFL1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
