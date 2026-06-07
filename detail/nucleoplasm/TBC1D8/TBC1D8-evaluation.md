---
type: protein-evaluation
gene: "TBC1D8"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TBC1D8 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TBC1D8/IF_images/1872_H7_13_cr5b51eeb390ef8_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TBC1D8/IF_images/1872_H7_7_cr5b51eeb39153e_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TBC1D8 |
| 蛋白名称 | TBC1 domain family member 8 |
| 蛋白大小 | 1140 aa |
| UniProt ID | [O95759](https://www.uniprot.org/uniprotkb/O95759) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 10 |
| AlphaFold pLDDT | 78.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1140 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 10篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TBC1D8 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Liu YJ et al. (2022). "An analysis of the significance of the Tre2/Bub2/CDC 16 (TBC) domain protein family 8 in colorectal cancer". *Sci Rep*. PMID: 35918393
2. Chen M et al. (2019). "TBC1D8 Amplification Drives Tumorigenesis through Metabolism Reprogramming in Ovarian Cancer". *Theranostics*. PMID: 30809301
3. Mutai H et al. (2022). "Whole exome analysis of patients in Japan with hearing loss reveals high heterogeneity among responsible and novel candidate genes". *Orphanet J Rare Dis*. PMID: 35248088
4. Kouri N et al. (2021). "Latent trait modeling of tau neuropathology in progressive supranuclear palsy". *Acta Neuropathol*. PMID: 33635380
5. Yang JO et al. (2020). "Characteristics of Genetic Variations Associated With Lennox-Gastaut Syndrome in Korean Families". *Front Genet*. PMID: 33584793

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
2. **研究新颖性**: PubMed仅10篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TBC1D8)
- [UniProt](https://www.uniprot.org/uniprotkb/O95759)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D8%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O95759)


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
| UniProt | O95759 |
| SMART | SM00568;SM00164; |
| UniProt Domain [FT] | DOMAIN 145..212; /note="GRAM 1"; DOMAIN 285..353; /note="GRAM 2"; DOMAIN 505..692; /note="Rab-GAP TBC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00163" |
| InterPro | IPR011992;IPR004182;IPR011993;IPR000195;IPR035969;IPR036009;IPR036016; |
| Pfam | PF02893;PF00566; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204634-TBC1D8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CD70 | Bioplex | false |
| COMTD1 | Bioplex | false |
| FAM174A | Bioplex | false |
| GPR45 | Bioplex | false |
| GZMH | Bioplex | false |
| RAB4A | Biogrid | false |
| TRAF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
