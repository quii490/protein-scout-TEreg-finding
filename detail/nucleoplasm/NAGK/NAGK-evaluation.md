---
type: protein-evaluation
gene: "NAGK"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## NAGK 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAGK/IF_images/1801_H3_19_cr59c4bdce05b18_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NAGK/IF_images/1801_H3_3_cr59c4bdce061c5_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NAGK |
| 蛋白名称 | N-acetyl-D-glucosamine kinase |
| 蛋白大小 | 344 aa |
| UniProt ID | [Q9UJ70](https://www.uniprot.org/uniprotkb/Q9UJ70) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 57 |
| AlphaFold pLDDT | 94.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 344 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 57篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 94.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **112/183** |  |
| **归一化总分** |  |  | **61.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NAGK 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Llácer JL et al. (2008). "Arginine and nitrogen storage". *Curr Opin Struct Biol*. PMID: 19013524
2. Su H et al. (2025). "Targeting PGM3 abolishes SREBP-1 activation-hexosamine synthesis feedback regulation to effectively suppress brain tumor growth". *Sci Adv*. PMID: 40249802
3. Stafford CA et al. (2022). "Phosphorylation of muramyl peptides by NAGK is required for NOD2 activation". *Nature*. PMID: 36002575
4. Sharif SR et al. (2016). "N-Acetyl-D-Glucosamine Kinase Interacts with Dynein-Lis1-NudE1 Complex and Regulates Cell Division". *Mol Cells*. PMID: 27646688
5. Celik A et al. (2024). "An Uncommon Phosphorylation Mode Regulates the Activity and Protein Interactions of N-Acetylglucosamine Kinase". *J Am Chem Soc*. PMID: 38733353

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅57篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 94.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NAGK)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9UJ70)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NAGK%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9UJ70)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


