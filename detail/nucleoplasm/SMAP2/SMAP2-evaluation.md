---
type: protein-evaluation
gene: "SMAP2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SMAP2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SMAP2/IF_images/2060_C5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SMAP2/IF_images/2060_C5_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMAP2 |
| 蛋白名称 | Stromal membrane-associated protein 2 |
| 蛋白大小 | 429 aa |
| UniProt ID | [Q8WU79](https://www.uniprot.org/uniprotkb/Q8WU79) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 14 |
| AlphaFold pLDDT | 62.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 429 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 14篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 62.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SMAP2 定位：
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
1. Zhang J et al. (2021). "Genome-wide investigation of the AP2/ERF superfamily and their expression under salt stress in Chinese willow (Salix matsudana)". *PeerJ*. PMID: 33954030
2. Tanabe K et al. (2008). "A SMAP gene family encoding ARF GTPase-activating proteins and its implication in membrane trafficking". *Methods Enzymol*. PMID: 18413247
3. Matsudaira T et al. (2013). "SMAP2 regulates retrograde transport from recycling endosomes to the Golgi". *PLoS One*. PMID: 23861959
4. Funaki T et al. (2011). "Localization of SMAP2 to the TGN and its function in the regulation of TGN protein transport". *Cell Struct Funct*. PMID: 21368446
5. Natsume W et al. (2006). "SMAP2, a novel ARF GTPase-activating protein, interacts with clathrin and clathrin assembly protein and functions on the AP-1-positive early endosome/trans-Golgi network". *Mol Biol Cell*. PMID: 16571680

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
2. **研究新颖性**: PubMed仅14篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 62.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SMAP2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8WU79)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SMAP2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8WU79)


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
| UniProt | Q8WU79 |
| SMART | SM00105; |
| UniProt Domain [FT] | DOMAIN 13..137; /note="Arf-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00288" |
| InterPro | IPR051718;IPR037278;IPR001164;IPR038508; |
| Pfam | PF01412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000084070-SMAP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP2B1 | Biogrid | false |
| BHLHE40 | Intact | false |
| C1orf94 | Intact | false |
| CLINT1 | Biogrid | false |
| CRX | Intact | false |
| DAB1 | Intact | false |
| DAZAP2 | Intact | false |
| FAM168A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
