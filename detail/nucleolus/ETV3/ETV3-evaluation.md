---
type: protein-evaluation
gene: "ETV3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ETV3 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ETV3/IF_images/69_F2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ETV3/IF_images/69_F2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ETV3 |
| 蛋白名称 | ETS translocation variant 3 |
| 蛋白大小 | 512 aa |
| UniProt ID | [P41162](https://www.uniprot.org/uniprotkb/P41162) |
| HPA 核定位 (IF) | Nucleoli; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 26 |
| AlphaFold pLDDT | 54.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli; Nucleoplasm (Approved); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 512 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 26篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 54.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ETV3 定位：
- **亚细胞定位**: Nucleoli; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Huang S et al. (2022). "Identification of the shared gene signatures and pathways between sarcopenia and type 2 diabetes mellitus". *PLoS One*. PMID: 35271662
2. Villar J et al. (2023). "ETV3 and ETV6 enable monocyte differentiation into dendritic cells by repressing macrophage fate commitment". *Nat Immunol*. PMID: 36543959
3. Adams NM et al. (2026). "Transcription factor Etv3 controls the tolerogenic function of dendritic cells". *Science*. PMID: 41678619
4. Ozkaya N et al. (2024). "Indeterminate DC histiocytosis is distinct from LCH and often associated with other hematopoietic neoplasms". *Blood Adv*. PMID: 39361706
5. Nagel S et al. (2023). "Establishment of the lymphoid ETS-code reveals deregulated ETS genes in Hodgkin lymphoma". *PLoS One*. PMID: 37428779

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli; Nucleoplasm
2. **研究新颖性**: PubMed仅26篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 54.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ETV3)
- [UniProt](https://www.uniprot.org/uniprotkb/P41162)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ETV3%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P41162)


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
| UniProt | P41162 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR036388;IPR036390; |
| Pfam | PF00178; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117036-ETV3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTL6B | Bioplex | false |
| ANGPTL7 | Bioplex | false |
| CIAO2A | Bioplex | false |
| CIB2 | Bioplex | false |
| CLEC11A | Bioplex | false |
| CRYBB3 | Bioplex | false |
| D2HGDH | Bioplex | false |
| EEF1AKMT3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
