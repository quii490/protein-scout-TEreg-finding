---
type: protein-evaluation
gene: "PHF21B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PHF21B 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PHF21B/IF_images/1386_E12_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PHF21B/IF_images/1386_E12_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PHF21B |
| 蛋白名称 | PHD finger protein 21B |
| 蛋白大小 | 531 aa |
| UniProt ID | [Q96EK2](https://www.uniprot.org/uniprotkb/Q96EK2) |
| HPA 核定位 (IF) | Nucleoli fibrillar center; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 8 |
| AlphaFold pLDDT | 59.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli fibrillar center; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 531 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 8篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.8 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PHF21B 定位：
- **亚细胞定位**: Nucleoli fibrillar center; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Mitz AR et al. (2024). "Evidence for common mechanisms of pathology between SHANK3 and other genes of Phelan-McDermid syndrome". *Clin Genet*. PMID: 38414139
2. Basu A et al. (2020). "Phf21b imprints the spatiotemporal epigenetic switch essential for neural stem cell differentiation". *Genes Dev*. PMID: 32820037
3. Li Q et al. (2017). "PHF21B overexpression promotes cancer stem cell-like traits in prostate cancer cells by activating the Wnt/β-catenin signaling pathway". *J Exp Clin Cancer Res*. PMID: 28645312
4. Wang J et al. (2025). "From molecular chaos to precision medicine in the treatment of cardiac hypertrophy: A rational use of natural products by integrating artificial intelligence and multi-omics data". *Pharmacol Res*. PMID: 40754044
5. Li C et al. (2021). "hsa_circ_0003222 accelerates stemness and progression of non-small cell lung cancer by sponging miR-527". *Cell Death Dis*. PMID: 34433810

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TFCP2 | validated two hybrid | 26871637 | — | — |
| BANP | validated two hybrid | 26871637 | — | — |
| RCOR3 | validated two hybrid | 26871637 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 3 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center; Nucleoplasm
2. **研究新颖性**: PubMed仅8篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 59.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PHF21B)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96EK2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PHF21B%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96EK2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




