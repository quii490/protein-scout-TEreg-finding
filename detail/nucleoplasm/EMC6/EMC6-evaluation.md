---
type: protein-evaluation
gene: "EMC6"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## EMC6 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EMC6/IF_images/1272_F12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EMC6/IF_images/1272_F12_5_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EMC6 |
| 蛋白名称 | ER membrane protein complex subunit 6 |
| 蛋白大小 | 110 aa |
| UniProt ID | [Q9BV81](https://www.uniprot.org/uniprotkb/Q9BV81) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 13 |
| AlphaFold pLDDT | 82.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Endoplasmic reticulum membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 110 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 13篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 82.6 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 EMC6 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; 

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

### 研究现状补充

**关键文献**:
1. Whittsette AL et al. (2022). "The endoplasmic reticulum membrane complex promotes proteostasis of GABA(A) receptors". *iScience*. PMID: 35938049
2. Li R et al. (2019). "Ad5-EMC6 mediates antitumor activity in gastric cancer cells through the mitochondrial apoptosis pathway". *Biochem Biophys Res Commun*. PMID: 30982575
3. Hegde RS (2022). "The Function, Structure, and Origins of the ER Membrane Protein Complex". *Annu Rev Biochem*. PMID: 35287476
4. Güngör B et al. (2022). "The ER membrane complex (EMC) can functionally replace the Oxa1 insertase in mitochondria". *PLoS Biol*. PMID: 35231030
5. Shen X et al. (2016). "EMC6/TMEM93 suppresses glioblastoma proliferation by modulating autophagy". *Cell Death Dis*. PMID: 26775697



### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅13篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 82.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/EMC6)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9BV81)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=EMC6%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9BV81)


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
| UniProt | Q9BV81 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008504;IPR029008; |
| Pfam | PF07019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127774-EMC6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EMC2 | Biogrid, Bioplex | true |
| EMC7 | Biogrid, Bioplex | true |
| EMC8 | Biogrid, Bioplex | true |
| MMGT1 | Intact, Biogrid | true |
| AQP6 | Intact | false |
| AQP9 | Intact | false |
| CD79A | Intact | false |
| EBP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
