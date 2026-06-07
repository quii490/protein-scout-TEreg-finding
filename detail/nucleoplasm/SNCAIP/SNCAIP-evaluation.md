---
type: protein-evaluation
gene: "SNCAIP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SNCAIP 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNCAIP/IF_images/1331_C9_4_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SNCAIP/IF_images/1331_C9_9_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SNCAIP |
| 蛋白名称 | Synphilin-1 |
| 蛋白大小 | 919 aa |
| UniProt ID | [Q9Y6H5](https://www.uniprot.org/uniprotkb/Q9Y6H5) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 45 |
| AlphaFold pLDDT | 51.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 919 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 45篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 51.6 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **101/183** |  |
| **归一化总分** |  |  | **55.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SNCAIP 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Yao RQ et al. (2021). "Organelle-specific autophagy in inflammatory diseases: a potential therapeutic target underlying the quality control of multiple organelles". *Autophagy*. PMID: 32048886
2. Schmidt C et al. (2024). "PRDM6 promotes medulloblastoma by repressing chromatin accessibility and altering gene expression". *Sci Rep*. PMID: 38992221
3. Larsen K et al. (2015). "Splicing variants of porcine synphilin-1". *Meta Gene*. PMID: 26101749
4. Gialluisi A et al. (2021). "Identification of sixteen novel candidate genes for late onset Parkinson's disease". *Mol Neurodegener*. PMID: 34148545
5. Dwivedi A et al. (2025). "Co-occurrence of Parkinson's disease and Retinitis Pigmentosa: A genetic and in silico analysis". *Neuroscience*. PMID: 39674535

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
2. **研究新颖性**: PubMed仅45篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 51.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SNCAIP)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9Y6H5)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SNCAIP%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9Y6H5)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y6H5 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR040133;IPR032027; |
| Pfam | PF12796;PF16700; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000064692-SNCAIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SNCA | Intact, Biogrid | true |
| CSNK2A1 | Biogrid | false |
| GSK3B | Biogrid | false |
| KALRN | Biogrid | false |
| NUB1 | Biogrid | false |
| PIN1 | Biogrid | false |
| PPHLN1 | Intact | false |
| PPP1CA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
