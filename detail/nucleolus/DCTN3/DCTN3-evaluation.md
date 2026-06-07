---
type: protein-evaluation
gene: "DCTN3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## DCTN3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DCTN3/IF_images/527_H9_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DCTN3/IF_images/527_H9_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DCTN3 |
| 蛋白名称 | Dynactin subunit 3 |
| 蛋白大小 | 186 aa |
| UniProt ID | [O75935](https://www.uniprot.org/uniprotkb/O75935) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Supported |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 88.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Supported); UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chromosome, centromer |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 186 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 88.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **130/183** |  |
| **归一化总分** |  |  | **71.0/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DCTN3 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spindle; Cleavage furrow
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Balay SD et al. (2021). "The expression, localisation and interactome of pigeon CRY2". *Sci Rep*. PMID: 34645873
2. Zhao T et al. (2024). "A proteome-wide association study identifies putative causal proteins for breast cancer risk". *Br J Cancer*. PMID: 39468330
3. Zhu Z et al. (2024). "Whole-genome resequencing revealed the population structure and selection signal of 4 indigenous Chinese laying ducks". *Poult Sci*. PMID: 38781766
4. Su X et al. (2021). "Study on the Prognostic Values of Dynactin Genes in Low-Grade Glioma". *Technol Cancer Res Treat*. PMID: 33896271
5. Kuźma-Kozakiewicz M et al. (2016). "Alteration of Motor Protein Expression Involved in Bidirectional Transport in Peripheral Blood Mononuclear Cells of Patients with Amyotrophic Lateral Sclerosis". *Neurodegener Dis*. PMID: 26954557

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PBX2 | two hybrid | 14667819 | — | — |
| q9vhl3_drome | two hybrid | 14605208 | — | — |
| q9vlx3_drome | two hybrid | 14605208 | — | — |
| UbcE2M | two hybrid | 14605208 | — | — |
| PSMG1 | two hybrid | 14605208 | — | — |
| q9vf05_drome | two hybrid | 14605208 | — | — |
| cnn | two hybrid | 14605208 | — | — |
| q9vbm3_drome | two hybrid | 14605208 | — | — |
| Cpr64Ad | two hybrid | 14605208 | — | — |
| ATXN1 | two hybrid | 16713569 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 88.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DCTN3)
- [UniProt](https://www.uniprot.org/uniprotkb/O75935)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DCTN3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O75935)


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
| UniProt | O75935 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009991; |
| Pfam | PF07426; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137100-DCTN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Biogrid, Opencell | true |
| DCTN1 | Intact, Biogrid | true |
| DCTN2 | Intact, Biogrid, Opencell | true |
| DYNC1I2 | Biogrid, Opencell | true |
| ACTG1 | Opencell | false |
| ACTR1A | Biogrid | false |
| ACTR1B | Biogrid | false |
| CAPZA2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
