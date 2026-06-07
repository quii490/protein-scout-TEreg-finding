---
type: protein-evaluation
gene: "CEP152"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CEP152 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP152/IF_images/487_C1_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP152/IF_images/487_C1_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CEP152 |
| 蛋白名称 | Centrosomal protein of 152 kDa |
| 蛋白大小 | 1710 aa |
| UniProt ID | [O94986](https://www.uniprot.org/uniprotkb/O94986) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 69 |
| AlphaFold pLDDT | 60.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtu |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1710 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 69篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 60.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **91/183** |  |
| **归一化总分** |  |  | **49.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CEP152 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Avidor-Reiss T & Gopalakrishnan J (2013). "Building a centriole". *Curr Opin Cell Biol*. PMID: 23199753
2. Kasera H et al. (2025). "PLK4 Homodimerization is Required for CEP152 Centrosome Localization and Spindle Organization". *J Mol Biol*. PMID: 40222413
3. Wang T et al. (2024). "Dual roles of CCDC102A in governing centrosome duplication and cohesion". *Cell Rep*. PMID: 38280197
4. Gürkaşlar HK & Hoffmann I (2025). "Binding of CEP152 to PLK4 stimulates kinase activity to promote centriole assembly". *Mol Biol Cell*. PMID: 40372713
5. Klos Dehring DA et al. (2013). "Deuterosome-mediated centriole biogenesis". *Dev Cell*. PMID: 24075808

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
2. **研究新颖性**: PubMed仅69篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 60.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CEP152)
- [UniProt](https://www.uniprot.org/uniprotkb/O94986)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CEP152%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O94986)


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
| UniProt | O94986 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051235;IPR057659;IPR057664; |
| Pfam | PF25770;PF25769; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103995-CEP152/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PLK4 | Intact, Biogrid | true |
| ACTR3 | Biogrid | false |
| ALMS1 | Biogrid | false |
| CDK5RAP2 | Biogrid | false |
| CENPJ | Biogrid | false |
| CEP128 | Biogrid | false |
| CEP131 | Intact | false |
| CEP135 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
