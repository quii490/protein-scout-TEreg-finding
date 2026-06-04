---
type: protein-evaluation
gene: "NFKBIE"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## NFKBIE 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center; Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NFKBIE/IF_images/30_B5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NFKBIE/IF_images/30_B5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NFKBIE |
| 蛋白名称 | NF-kappa-B inhibitor epsilon |
| 蛋白大小 | 500 aa |
| UniProt ID | [O00221](https://www.uniprot.org/uniprotkb/O00221) |
| HPA 核定位 (IF) | Nucleoli fibrillar center; Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 65 |
| AlphaFold pLDDT | 61.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli fibrillar center; Nucleoplasm (Supported); UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 500 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 65篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 61.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **100/183** |  |
| **归一化总分** |  |  | **54.6/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NFKBIE 定位：
- **亚细胞定位**: Nucleoli fibrillar center; Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Jain P & Wang M (2025). "High-risk MCL: recognition and treatment". *Blood*. PMID: 39786418
2. Bordini J et al. (2024). "IκBε deficiency accelerates disease development in chronic lymphocytic leukemia". *Leukemia*. PMID: 38575671
3. Bonato A et al. (2024). "NFKBIE mutations are selected by the tumor microenvironment and contribute to immune escape in chronic lymphocytic leukemia". *Leukemia*. PMID: 38486128
4. Chen SH et al. (2024). "Ultrahigh frequency transcutaneous electrical nerve stimulation for neuropathic pain alleviation and neuromodulation". *Neurotherapeutics*. PMID: 38368171
5. Thorvaldsdottir B et al. (2025). "ATM aberrations in chronic lymphocytic leukemia: del(11q) rather than ATM mutations is an adverse-prognostic biomarker". *Leukemia*. PMID: 40275070

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| NFKB2 | tandem affinity purification | 14743216 | — | — |
| FBXW11 | tandem affinity purification | 14743216 | — | — |
| REL | tandem affinity purification | 14743216 | — | — |
| EBI-359405 | tandem affinity purification | 14743216 | — | — |
| ANKHD1 | tandem affinity purification | 14743216 | — | — |
| CHUK | tandem affinity purification | 14743216 | — | — |
| ANKRD28 | tandem affinity purification | 14743216 | — | — |
| PPP6R2 | tandem affinity purification | 14743216 | — | — |
| PPP6R1 | tandem affinity purification | 14743216 | — | — |
| PPP6C | tandem affinity purification | 14743216 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center; Nucleoplasm
2. **研究新颖性**: PubMed仅65篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 61.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NFKBIE)
- [UniProt](https://www.uniprot.org/uniprotkb/O00221)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NFKBIE%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O00221)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




