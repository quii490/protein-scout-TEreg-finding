---
type: protein-evaluation
gene: "UPP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## UPP1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Enhanced)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/UPP1/IF_images/856_B7_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/UPP1/IF_images/856_B7_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UPP1 |
| 蛋白名称 | Uridine phosphorylase 1 |
| 蛋白大小 | 310 aa |
| UniProt ID | [Q16831](https://www.uniprot.org/uniprotkb/Q16831) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Enhanced |
| PubMed 总数 | 93 |
| AlphaFold pLDDT | 94.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoplasm (Enhanced); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 310 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 93篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 94.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **96/183** |  |
| **归一化总分** |  |  | **52.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 UPP1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Enhanced
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Nwosu ZC et al. (2023). "Uridine-derived ribose fuels glucose-restricted pancreatic cancer". *Nature*. PMID: 37198494
2. Lai K et al. (2023). "Uridine Alleviates Sepsis-Induced Acute Lung Injury by Inhibiting Ferroptosis of Macrophage". *Int J Mol Sci*. PMID: 36982166
3. Du W et al. (2024). "UPP1 enhances bladder cancer progression and gemcitabine resistance through AKT". *Int J Biol Sci*. PMID: 38385072
4. Li Y et al. (2024). "UPP1 promotes lung adenocarcinoma progression through the induction of an immunosuppressive microenvironment". *Nat Commun*. PMID: 38331898
5. Xiao J et al. (2026). "Uridine depletion impairs CD8⁺ T cell antitumor activity through N-glycosylation". *Cell Metab*. PMID: 41468885

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

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅93篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 94.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/UPP1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q16831)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=UPP1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q16831)


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
| UniProt | Q16831 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018016;IPR000845;IPR035994;IPR010059; |
| Pfam | PF01048; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183696-UPP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A2ML1 | Bioplex | false |
| ARMCX5 | Bioplex | false |
| BBS2 | Bioplex | false |
| BRCA2 | Bioplex | false |
| CCR1 | Bioplex | false |
| CTPS2 | Bioplex | false |
| CUL7 | Bioplex | false |
| FDFT1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
