---
type: protein-evaluation
gene: "PDLIM5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PDLIM5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PDLIM5/IF_images/131_F8_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PDLIM5/IF_images/131_F8_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PDLIM5 |
| 蛋白名称 | PDZ and LIM domain protein 5 |
| 蛋白大小 | 596 aa |
| UniProt ID | [Q96HC4](https://www.uniprot.org/uniprotkb/Q96HC4) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 68 |
| AlphaFold pLDDT | 64.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Postsynaptic density; Presynapse; Postsynapse; Cytoplasm, cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 596 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 68篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 64.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **96/183** |  |
| **归一化总分** |  |  | **52.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PDLIM5 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Postsynaptic density; Presynapse; Postsynapse; Cytoplasm, cytosol
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Nie P et al. (2024). "Targeting p97-Npl4 interaction inhibits tumor T(reg) cell development to enhance tumor immunity". *Nat Immunol*. PMID: 39107403
2. Chou EL et al. (2022). "Aortic Cellular Diversity and Quantitative Genome-Wide Association Study Trait Prioritization Through Single-Nuclear RNA Sequencing of the Aneurysmal Human Aorta". *Arterioscler Thromb Vasc Biol*. PMID: 36172868
3. Gan P et al. (2024). "RBPMS regulates cardiomyocyte contraction and cardiac function through RNA alternative splicing". *Cardiovasc Res*. PMID: 37890031
4. Huang X et al. (2020). "An Overview of the Cytoskeleton-Associated Role of PDLIM5". *Front Physiol*. PMID: 32848888
5. Fu Y et al. (2024). "Expression of PDLIM5 Spliceosomes and Regulatory Functions on Myogenesis in Pigs". *Cells*. PMID: 38667334

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
2. **研究新颖性**: PubMed仅68篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 64.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PDLIM5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96HC4)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PDLIM5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96HC4)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




