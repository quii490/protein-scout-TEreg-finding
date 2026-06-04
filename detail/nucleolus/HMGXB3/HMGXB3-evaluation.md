---
type: protein-evaluation
gene: "HMGXB3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## HMGXB3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/HMGXB3/IF_images/78_D5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/HMGXB3/IF_images/78_D5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HMGXB3 |
| 蛋白名称 | N/A |
| 蛋白大小 | 0 aa |
| UniProt ID | [N/A](https://www.uniprot.org/uniprotkb/N/A) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 3 |
| AlphaFold pLDDT | N/A |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: N/A |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 0 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 3篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: N/A |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **118/183** |  |
| **归一化总分** |  |  | **64.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 HMGXB3 定位：
- **亚细胞定位**: Nucleoli
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
1. Collins JE et al. (2019). "Common and distinct transcriptional signatures of mammalian embryonic lethality". *Nat Commun*. PMID: 31243271
2. Woo HH & Chambers SK (2021). "Regulation of closely juxtaposed proto-oncogene c-fms and HMGXB3 gene expression by mRNA 3' end polymorphism in breast cancer cells". *RNA*. PMID: 34155128
3. Tan D et al. (2014). "The ROQ domain of Roquin recognizes mRNA constitutive-decay element and double-stranded RNA". *Nat Struct Mol Biol*. PMID: 25026078
4. Li X et al. (2025). "Validation of male-specific markers confirmed an XY/XX-type sex determination system in Chinese dark sleeper (Odontobutis sinensis)". *Genomics*. PMID: 40348286
5. Zhang G et al. (2021). "Circular RNA EGLN3 silencing represses renal cell carcinoma progression through the miR-1224-3p/HMGXB3 axis". *Acta Histochem*. PMID: 34274607

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| q5ni33_fratt | two hybrid pooling approach | 20711500 | — | — |
| tuf | two hybrid pooling approach | 20711500 | — | — |
| DISC1 | two hybrid fragment pooling approach | 31413325 | — | — |
| Hoxa11 | two hybrid array | 20211142 | — | — |
| EBI-54261929 | clash | 23622248 | — | — |
| EBI-54264679 | clash | 23622248 | — | — |
| EBI-54261765 | clash | 23622248 | — | — |
| EBI-21019856 | clash | 23622248 | — | — |
| hsamir6153p | clash | 23622248 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Nucleus

**IntAct 查询记录**: IntAct: 9 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅3篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = N/A

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/HMGXB3)
- [UniProt](https://www.uniprot.org/uniprotkb/N/A)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=HMGXB3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/N/A)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




