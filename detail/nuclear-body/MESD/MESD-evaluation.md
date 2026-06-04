---
type: protein-evaluation
gene: "MESD"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## MESD 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear bodies (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/MESD/IF_images/523_A9_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/MESD/IF_images/523_A9_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MESD |
| 蛋白名称 | LRP chaperone MESD |
| 蛋白大小 | 234 aa |
| UniProt ID | [Q14696](https://www.uniprot.org/uniprotkb/Q14696) |
| HPA 核定位 (IF) | Nuclear bodies |
| HPA 可靠性 | Supported |
| PubMed 总数 | 56 |
| AlphaFold pLDDT | 67.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nuclear bodies (Supported); UniProt: Endoplasmic reticulum |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 234 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 56篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 67.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **106/183** |  |
| **归一化总分** |  |  | **57.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 MESD 定位：
- **亚细胞定位**: Nuclear bodies
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ; 

![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/MESD/MESD-PAE.png]]

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Jovanovic M & Marini JC (2024). "Update on the Genetics of Osteogenesis Imperfecta". *Calcif Tissue Int*. PMID: 39127989
2. Calvier L et al. (2022). "Interplay of Low-Density Lipoprotein Receptors, LRPs, and Lipoproteins in Pulmonary Hypertension". *JACC Basic Transl Sci*. PMID: 35257044
3. Ghosh DK et al. (2023). "Mutant MESD links cellular stress to type I collagen aggregation in osteogenesis imperfecta type XX". *Matrix Biol*. PMID: 36526215
4. Moosa S et al. (2019). "Autosomal-Recessive Mutations in MESD Cause Osteogenesis Imperfecta". *Am J Hum Genet*. PMID: 31564437
5. Price MN et al. (2021). "Four families of folate-independent methionine synthases". *PLoS Genet*. PMID: 33534785

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| HOGA1 | cross-linking study | 30021884 | — | — |
| SYNE2 | cross-linking study | 30021884 | — | — |
| ASH1L | cross-linking study | 30021884 | — | — |
| H2BC21 | cross-linking study | 30021884 | — | — |
| NCL | cross-linking study | 30021884 | — | — |
| H1FX | cross-linking study | 30021884 | — | — |
| GEM | two hybrid prey pooling approach | 32296183 | — | — |
| COX14 | two hybrid prey pooling approach | 32296183 | — | — |
| BORCS8 | two hybrid prey pooling approach | 32296183 | — | — |
| CYP4F11 | two hybrid prey pooling approach | 32296183 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Endoplasmic reticulum, plasma membrane

**IntAct 查询记录**: IntAct: 74 实验验证互作

**评价**: —


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear bodies
2. **研究新颖性**: PubMed仅56篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 67.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/MESD)
- [UniProt](https://www.uniprot.org/uniprotkb/Q14696)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=MESD%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q14696)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MESD-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/MESD/MESD-PAE.png]]




