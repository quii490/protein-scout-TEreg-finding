---
type: protein-evaluation
gene: "FOXN2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## FOXN2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN2/IF_images/63_H3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FOXN2/IF_images/63_H3_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FOXN2 |
| 蛋白名称 | Forkhead box protein N2 |
| 蛋白大小 | 431 aa |
| UniProt ID | [P32314](https://www.uniprot.org/uniprotkb/P32314) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 20 |
| AlphaFold pLDDT | 60.3 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 431 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 20篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 60.3 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **128/183** |  |
| **归一化总分** |  |  | **69.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 FOXN2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Song Y et al. (2024). "Bmi1 facilitates the progression of cholangiocarcinoma by inhibiting Foxn2 expression dependent on a histone H2A ubiquitination manner". *Cancer Lett*. PMID: 38705565
2. Katoh M & Katoh M (2004). "Human FOX gene family (Review)". *Int J Oncol*. PMID: 15492844
3. Liu XH et al. (2021). "FOXN2 suppresses the proliferation and invasion of human hepatocellular carcinoma cells". *Eur Rev Med Pharmacol Sci*. PMID: 33577027
4. Wu YH et al. (2023). "MicroRNA-188-5p inhibits hepatocellular carcinoma proliferation and migration by targeting forkhead box N2". *BMC Cancer*. PMID: 37277714
5. Nagel S et al. (2017). "Identification of a tumor suppressor network in T-cell leukemia". *Leuk Lymphoma*. PMID: 28142295

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
2. **研究新颖性**: PubMed仅20篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 60.3

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/FOXN2)
- [UniProt](https://www.uniprot.org/uniprotkb/P32314)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=FOXN2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P32314)


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
| UniProt | P32314 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047403;IPR001766;IPR047119;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170802-FOXN2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXW11 | Intact, Biogrid | true |
| RFX1 | Intact, Biogrid, Bioplex | true |
| BTRC | Biogrid | false |
| DHX16 | Bioplex | false |
| RIOK2 | Bioplex | false |
| USP7 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
