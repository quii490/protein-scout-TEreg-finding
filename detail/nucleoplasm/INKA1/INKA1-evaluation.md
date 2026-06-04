---
type: protein-evaluation
gene: "INKA1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## INKA1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/INKA1/IF_images/487_B10_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/INKA1/IF_images/487_B10_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | INKA1 |
| 蛋白名称 | PAK4-inhibitor INKA1 |
| 蛋白大小 | 287 aa |
| UniProt ID | [Q96EL1](https://www.uniprot.org/uniprotkb/Q96EL1) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 6 |
| AlphaFold pLDDT | 57.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Nucleus; Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 287 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 6篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 57.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **123/183** |  |
| **归一化总分** |  |  | **67.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 INKA1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus; Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Kaufmann KB et al. (2021). "A latent subset of human hematopoietic stem cells resists regenerative stress to preserve stemness". *Nat Immunol*. PMID: 33958784
2. Jeon H et al. (2022). "inka1b expression in the head mesoderm is dispensable for facial cartilage development". *Gene Expr Patterns*. PMID: 35811016
3. Yamada S et al. (2022). "Inka2, a novel Pak4 inhibitor, regulates actin dynamics in neuronal development". *PLoS Genet*. PMID: 36301793
4. Lin Y et al. (2024). "Identification of cuproptosis-related genes and immune infiltration in dilated cardiomyopathy". *Int J Cardiol*. PMID: 38168558
5. Church RJ et al. (2025). "Blood toxicogenomics reveals potential biomarkers for management of idiosyncratic drug-induced liver injury". *Front Genet*. PMID: 40201567

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
2. **研究新颖性**: PubMed仅6篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 57.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/INKA1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96EL1)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=INKA1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96EL1)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




