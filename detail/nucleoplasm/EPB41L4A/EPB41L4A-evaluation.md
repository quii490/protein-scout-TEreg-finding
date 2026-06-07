---
type: protein-evaluation
gene: "EPB41L4A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## EPB41L4A 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPB41L4A/IF_images/1523_D7_5_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPB41L4A/IF_images/1523_D7_6_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EPB41L4A |
| 蛋白名称 | N/A |
| 蛋白大小 | 0 aa |
| UniProt ID | [N/A](https://www.uniprot.org/uniprotkb/N/A) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 52 |
| AlphaFold pLDDT | N/A |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 0 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 52篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: N/A |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **98/183** |  |
| **归一化总分** |  |  | **53.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EPB41L4A 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: N/A

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Alazami AM et al. (2015). "Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families". *Cell Rep*. PMID: 25558065
2. Wang Z et al. (2024). "EPB41L4A-AS1 is required to maintain basal autophagy to modulates Aβ clearance". *NPJ Aging*. PMID: 38704365
3. Li M et al. (2025). "lncRNA EPB41L4A-AS1: A promising therapeutic target for aging and age-related diseases". *Mech Ageing Dev*. PMID: 41067507
4. Yan Y et al. (2023). "EPB41L4A-AS1 and UNC5B-AS1 have diagnostic and prognostic significance in osteosarcoma". *J Orthop Surg Res*. PMID: 36998043
5. Yang F & Lv S (2022). "LncRNA EPB41L4A-AS1 Regulates Cell Proliferation, Apoptosis and Metastasis in Breast Cancer". *Ann Clin Lab Sci*. PMID: 35181612

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
2. **研究新颖性**: PubMed仅52篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = N/A

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EPB41L4A)
- [UniProt](https://www.uniprot.org/uniprotkb/N/A)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EPB41L4A%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/N/A)
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | two hybrid pooling approach | 20711500 |
| — | protein kinase assay | 23602568 |
| — | protein kinase assay | 23602568 |
| — | two hybrid array | 25814554 |
| — | anti tag coimmunoprecipitation | 33961781 |
| — | anti tag coimmunoprecipitation | 33961781 |
| — | anti tag coimmunoprecipitation | 33961781 |
| — | anti tag coimmunoprecipitation | 33961781 |
| — | anti tag coimmunoprecipitation | 33961781 |
| — | anti tag coimmunoprecipitation | 33961781 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| TAAR1 | 0.813 |
| PCNX2 | 0.494 |
| DYNLL2 | 0.465 |
| KIAA1755 | 0.460 |
| ALAD | 0.451 |
| CCT5 | 0.429 |
| MAB21L3 | 0.428 |
| ARHGEF37 | 0.424 |
| SLC6A7 | 0.414 |
| CTNNB1 | 0.409 |

**GO-CC 复合体/定位核查**:
- UniProt GO-CC 未列出可解析复合体/细胞组分条目。

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCS5 |
| SMART | SM00295;SM01195;SM01196; |
| UniProt Domain [FT] | DOMAIN 11..299; /note="FERM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00084" |
| InterPro | IPR030696;IPR019749;IPR000798;IPR014847;IPR014352;IPR035963;IPR019748;IPR019747;IPR000299;IPR018979;IPR018980;IPR011993;IPR029071; |
| Pfam | PF08736;PF09380;PF00373;PF09379; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129595-EPB41L4A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DVL3 | Biogrid | false |
| UNC119 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
