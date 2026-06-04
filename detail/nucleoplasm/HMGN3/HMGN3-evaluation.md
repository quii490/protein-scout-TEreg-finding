---
type: protein-evaluation
gene: "HMGN3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## HMGN3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMGN3/IF_images/299_E11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMGN3/IF_images/299_E11_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HMGN3 |
| 蛋白名称 | High mobility group nucleosome-binding domain-containing protein 3 |
| 蛋白大小 | 99 aa |
| UniProt ID | [Q15651](https://www.uniprot.org/uniprotkb/Q15651) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 18 |
| AlphaFold pLDDT | 65.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 99 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 18篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 65.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **121/183** |  |
| **归一化总分** |  |  | **66.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 HMGN3 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang N et al. (2025). "Cellular hierarchy framework based on single-cell and bulk RNA sequencing reveals fatty acid metabolic biomarker MYDGF as a therapeutic target for ccRCC". *Front Immunol*. PMID: 40539074
2. Haws W et al. (2023). "Analyses of binding partners and functional domains for the developmentally essential protein Hmx3a/HMX3". *Sci Rep*. PMID: 36670152
3. Geng X et al. (2025). "Chromatin structural gene expression stratifies cardiac cell populations in health and disease". *Epigenetics*. PMID: 41117190
4. Seefelder M & Kochanek S (2021). "A meta-analysis of transcriptomic profiles of Huntington's disease patients". *PLoS One*. PMID: 34111223
5. Sorin S et al. (2022). "HMGN3 represses transcription of epithelial regulators to promote migration of cholangiocarcinoma in a SNAI2-dependent manner". *FASEB J*. PMID: 35635715

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
2. **研究新颖性**: PubMed仅18篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 65.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/HMGN3)
- [UniProt](https://www.uniprot.org/uniprotkb/Q15651)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=HMGN3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q15651)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




