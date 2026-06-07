---
type: protein-evaluation
gene: "ODAM"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ODAM 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ODAM/IF_images/1816_E2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ODAM/IF_images/1816_E2_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ODAM |
| 蛋白名称 | Odontogenic ameloblast-associated protein |
| 蛋白大小 | 279 aa |
| UniProt ID | [A1E959](https://www.uniprot.org/uniprotkb/A1E959) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 66 |
| AlphaFold pLDDT | 42.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Secreted; Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 279 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 66篇 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT: 42.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **90/183** |  |
| **归一化总分** |  |  | **49.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ODAM 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Secreted; Cytoplasm; Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zhao C et al. (2024). "Gradient-Based Instance-Specific Visual Explanations for Object Specification and Object Discrimination". *IEEE Trans Pattern Anal Mach Intell*. PMID: 38517727
2. Wang R et al. (2025). "The impact of dosage timing for inhaled corticosteroids in asthma: a randomised three-way crossover trial". *Thorax*. PMID: 40234005
3. Cai H et al. (2024). "CRISPR/Cas9 model of prostate cancer identifies Kmt2c deficiency as a metastatic driver by Odam/Cabs1 gene cluster expression". *Nat Commun*. PMID: 38453924
4. Waterson P & Robertson M (2022). "Forty years of Organisational Design and Management (ODAM)". *Ergonomics*. PMID: 35102812
5. Zhu S et al. (2022). "The versatile roles of odontogenic ameloblast-associated protein in odontogenesis, junctional epithelium regeneration and periodontal disease". *Front Physiol*. PMID: 36117697

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
2. **研究新颖性**: PubMed仅66篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 42.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ODAM)
- [UniProt](https://www.uniprot.org/uniprotkb/A1E959)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ODAM%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/A1E959)


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
| UniProt | A1E959 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026802; |
| Pfam | PF15424; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000109205-ODAM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID5A | Intact | false |
| BRAF | Intact | false |
| FHL2 | Intact | false |
| HGS | Intact | false |
| MED25 | Intact | false |
| POGZ | Intact | false |
| SDCBP | Intact | false |
| SNRPC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
