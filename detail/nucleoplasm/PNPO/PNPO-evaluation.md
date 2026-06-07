---
type: protein-evaluation
gene: "PNPO"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PNPO 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PNPO/IF_images/237_F6_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PNPO/IF_images/237_F6_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PNPO |
| 蛋白名称 | Pyridoxine-5'-phosphate oxidase |
| 蛋白大小 | 151 aa |
| UniProt ID | [A0A286YFL3](https://www.uniprot.org/uniprotkb/A0A286YFL3) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 98 |
| AlphaFold pLDDT | N/A |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 151 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 98篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: N/A |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **84/183** |  |
| **归一化总分** |  |  | **45.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PNPO 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; 

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
1. Adam MP et al. (1993). "PNPO Deficiency". **. PMID: 35737815
2. Deng Z et al. (2025). "PNPO-Mediated Oxidation of DVL3 Promotes Multiple Myeloma Malignancy and Osteoclastogenesis by Activating the Wnt/β-Catenin Pathway". *Adv Sci (Weinh)*. PMID: 39656865
3. Sekine H et al. (2024). "PNPO-PLP axis senses prolonged hypoxia in macrophages by regulating lysosomal activity". *Nat Metab*. PMID: 38822028
4. Sekine H et al. (2024). "Author Correction: PNPO-PLP axis senses prolonged hypoxia in macrophages by regulating lysosomal activity". *Nat Metab*. PMID: 39592844
5. Li X et al. (2024). "Targeting PNPO to suppress tumor growth via inhibiting autophagic flux and to reverse paclitaxel resistance in ovarian cancer". *Apoptosis*. PMID: 38615082



### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅98篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = N/A

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PNPO)
- [UniProt](https://www.uniprot.org/uniprotkb/A0A286YFL3)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PNPO%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/A0A286YFL3)


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
| UniProt | Q9NVS9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000659;IPR019740;IPR011576;IPR019576;IPR012349; |
| Pfam | PF10590;PF01243; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108439-PNPO/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LIME1 | Intact | false |
| MTERF1 | Intact, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
