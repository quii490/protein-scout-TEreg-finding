---
type: protein-evaluation
gene: "ELK4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ELK4 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELK4/IF_images/296_B11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELK4/IF_images/296_B11_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ELK4 |
| 蛋白名称 | ETS domain-containing protein Elk-4 |
| 蛋白大小 | 431 aa |
| UniProt ID | [P28324](https://www.uniprot.org/uniprotkb/P28324) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 97 |
| AlphaFold pLDDT | 59.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 431 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 97篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **83/183** |  |
| **归一化总分** |  |  | **45.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ELK4 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zheng K et al. (2023). "IGF1R-phosphorylated PYCR1 facilitates ELK4 transcriptional activity and sustains tumor growth under hypoxia". *Nat Commun*. PMID: 37777542
2. Zhu Z et al. (2023). "ELK4 Promotes Colorectal Cancer Progression by Activating the Neoangiogenic Factor LRG1 in a Noncanonical SP1/3-Dependent Manner". *Adv Sci (Weinh)*. PMID: 37786278
3. Huang M et al. (2024). "Single-cell transcriptomes and chromatin accessibility of endothelial cells unravel transcription factors associated with dysregulated angiogenesis in systemic sclerosis". *Ann Rheum Dis*. PMID: 38754983
4. Lin H et al. (2023). "Reprogramming of cis-regulatory networks during skeletal muscle atrophy in male mice". *Nat Commun*. PMID: 37853001
5. Zheng Y et al. (2025). "The role of ELK4 up-regulation in macrophage polarization and its mechanism in connective tissue disease-associated interstitial lung disease". *Int Immunopharmacol*. PMID: 40663811

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
3. **结构质量**: AlphaFold pLDDT = 59.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ELK4)
- [UniProt](https://www.uniprot.org/uniprotkb/P28324)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ELK4%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P28324)


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
| UniProt | P28324 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR036388;IPR036390; |
| Pfam | PF00178; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158711-ELK4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Biogrid | false |
| DOK4 | Biogrid | false |
| SIRT7 | Intact | false |
| SRF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
