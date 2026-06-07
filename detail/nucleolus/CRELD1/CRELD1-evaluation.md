---
type: protein-evaluation
gene: "CRELD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CRELD1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CRELD1/IF_images/274_G2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CRELD1/IF_images/274_G2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CRELD1 |
| 蛋白名称 | Protein disulfide isomerase CRELD1 |
| 蛋白大小 | 420 aa |
| UniProt ID | [Q96HD1](https://www.uniprot.org/uniprotkb/Q96HD1) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 51 |
| AlphaFold pLDDT | 81.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 420 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 51篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 81.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **109/183** |  |
| **归一化总分** |  |  | **59.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CRELD1 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Jeffries L et al. (2024). "Biallelic CRELD1 variants cause a multisystem syndrome, including neurodevelopmental phenotypes, cardiac dysrhythmias, and frequent infections". *Genet Med*. PMID: 37947183
2. Perrot A & Rickert-Sperling S (2024). "Human Genetics of Defects of Situs". *Adv Exp Med Biol*. PMID: 38884744
3. Slieker RC et al. (2023). "Identification of biomarkers for glycaemic deterioration in type 2 diabetes". *Nat Commun*. PMID: 37137910
4. Beckert V et al. (2021). "Creld1 regulates myocardial development and function". *J Mol Cell Cardiol*. PMID: 33773996
5. D'Alessandro M et al. (2025). "Biallelic CRELD1 variants cause severe muscle weakness and infantile epilepsy". *Brain Commun*. PMID: 40980404

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

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅51篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 81.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CRELD1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96HD1)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CRELD1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96HD1)


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
| UniProt | Q96HD1 |
| SMART | SM00181;SM00179;SM00261; |
| UniProt Domain [FT] | DOMAIN 153..193; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 305..344; /note="EGF-like 2; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR021852;IPR050751;IPR000742;IPR001881;IPR000152;IPR018097;IPR006212;IPR009030;IPR002049;IPR049883; |
| Pfam | PF11938;PF07645; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163703-CRELD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RER1 | Opencell | false |
| SLC35F6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
