---
type: protein-evaluation
gene: "P3H2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## P3H2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/P3H2/IF_images/1941_A2_3_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/P3H2/IF_images/1941_A2_4_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | P3H2 |
| 蛋白名称 | Prolyl 3-hydroxylase 2 |
| 蛋白大小 | 708 aa |
| UniProt ID | [Q8IVL5](https://www.uniprot.org/uniprotkb/Q8IVL5) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 56 |
| AlphaFold pLDDT | 83.4 |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Endoplasmic reticulum; Sarcoplasmic reticulum; Golgi apparatus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 708 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 56篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 83.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **109/183** |  |
| **归一化总分** |  |  | **59.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 P3H2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum; Sarcoplasmic reticulum; Golgi apparatus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Aypek H et al. (2022). "Loss of the collagen IV modifier prolyl 3-hydroxylase 2 causes thin basement membrane nephropathy". *J Clin Invest*. PMID: 35499085
2. Khan MM et al. (2024). "Dextromethorphan inhibits collagen and collagen-like cargo secretion to ameliorate lung fibrosis". *Sci Transl Med*. PMID: 39693409
3. Guo X et al. (2025). "Iron metabolism and preeclampsia: new insights from bioinformatics analysis". *J Matern Fetal Neonatal Med*. PMID: 40592741
4. Pignata P et al. (2021). "Prolyl 3-Hydroxylase 2 Is a Molecular Player of Angiogenesis". *Int J Mol Sci*. PMID: 33918807
5. Hudson DM et al. (2015). "Post-translationally abnormal collagens of prolyl 3-hydroxylase-2 null mice offer a pathobiological mechanism for the high myopia linked to human LEPREL1 mutations". *J Biol Chem*. PMID: 25645914

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
2. **研究新颖性**: PubMed仅56篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 83.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/P3H2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IVL5)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=P3H2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IVL5)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




