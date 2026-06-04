---
type: protein-evaluation
gene: "CERS5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CERS5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear membrane (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/CERS5/IF_images/2102_E3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/CERS5/IF_images/2102_E3_6_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CERS5 |
| 蛋白名称 | Ceramide synthase 5 |
| 蛋白大小 | 392 aa |
| UniProt ID | [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) |
| HPA 核定位 (IF) | Nuclear membrane |
| HPA 可靠性 | Approved |
| PubMed 总数 | 61 |
| AlphaFold pLDDT | 84.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nuclear membrane (Approved); UniProt: Endoplasmic reticulum membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 392 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 61篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 84.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **99/183** |  |
| **归一化总分** |  |  | **54.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CERS5 定位：
- **亚细胞定位**: Nuclear membrane
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Hammerschmidt P et al. (2019). "CerS6-Derived Sphingolipids Interact with Mff and Promote Mitochondrial Fragmentation in Obesity". *Cell*. PMID: 31150623
2. Liu Q et al. (2025). "Comprehensive profiling of lipid metabolic reprogramming expands precision medicine for HCC". *Hepatology*. PMID: 38899975
3. Zhu Q et al. (2024). "PAQR4 regulates adipocyte function and systemic metabolic health by mediating ceramide levels". *Nat Metab*. PMID: 38961186
4. Reese L et al. (2024). "Loss of ceramide synthase 5 inhibits the development of experimentally induced aortic valve stenosis". *Acta Physiol (Oxf)*. PMID: 38546351
5. Zhang S et al. (2022). "High expression of ceramide synthase 5 predicts a poor prognosis in gastric cancer". *Transl Cancer Res*. PMID: 36237237

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear membrane
2. **研究新颖性**: PubMed仅61篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 84.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CERS5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8N5B7)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERS5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8N5B7)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




