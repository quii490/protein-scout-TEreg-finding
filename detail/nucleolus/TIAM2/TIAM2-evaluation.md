---
type: protein-evaluation
gene: "TIAM2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TIAM2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center; Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TIAM2/IF_images/108_G9_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TIAM2/IF_images/108_G9_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TIAM2 |
| 蛋白名称 | Rho guanine nucleotide exchange factor TIAM2 |
| 蛋白大小 | 1701 aa |
| UniProt ID | [Q8IVF5](https://www.uniprot.org/uniprotkb/Q8IVF5) |
| HPA 核定位 (IF) | Nucleoli fibrillar center; Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 31 |
| AlphaFold pLDDT | 56.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli fibrillar center; Nucleoplasm (Supported); UniProt: Cytoplasm; Cell projection, lamellipodium; Cell projection, filopodium; Cell projection, growth cone |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1701 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 31篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 56.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **112/183** |  |
| **归一化总分** |  |  | **61.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TIAM2 定位：
- **亚细胞定位**: Nucleoli fibrillar center; Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Cell projection, lamellipodium; Cell projection, filopodium; Cell projection, growth cone; Cell projection, neuron projection
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Dent LG et al. (2024). "Environmentally dependent and independent control of 3D cell shape". *Cell Rep*. PMID: 38636520
2. Makrufardi F et al. (2025). "Extreme temperatures modulate gene expression in the airway epithelium of the lungs in mice and asthma patients". *Front Med (Lausanne)*. PMID: 40313552
3. Cheng S et al. (2022). "TIAM2 promotes proliferation and invasion of osteosarcoma cells by activating the JAK2/STAT3 signaling pathway". *J Bone Oncol*. PMID: 36419799
4. Liu X et al. (2019). "Conformational Dynamics and Cooperativity Drive the Specificity of a Protein-Ligand Interaction". *Biophys J*. PMID: 31146922
5. Jintian Z et al. (2024). "The analysis on Tiam2 for expression in esophageal carcinoma: A descriptive study". *Medicine (Baltimore)*. PMID: 39093764

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center; Nucleoplasm
2. **研究新颖性**: PubMed仅31篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 56.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TIAM2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8IVF5)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TIAM2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8IVF5)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




