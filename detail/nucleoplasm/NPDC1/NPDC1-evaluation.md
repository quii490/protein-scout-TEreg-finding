---
type: protein-evaluation
gene: "NPDC1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## NPDC1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPDC1/IF_images/75_F9_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NPDC1/IF_images/75_F9_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NPDC1 |
| 蛋白名称 | Neural proliferation differentiation and control protein 1 |
| 蛋白大小 | 325 aa |
| UniProt ID | [Q9NQX5](https://www.uniprot.org/uniprotkb/Q9NQX5) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 36 |
| AlphaFold pLDDT | 68.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 325 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 36篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 68.4 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NPDC1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Perez-Canamas A et al. (2025). "mGluR4-NPDC1 complex mediates α-synuclein fibril-induced neurodegeneration". *Nat Commun*. PMID: 41444258
2. Perez-Canamas A et al. (2025). "mGluR4-Npdc1 complex mediates α-synuclein fibril-induced neurodegeneration". *bioRxiv*. PMID: 40777374
3. Qin Q et al. (2026). "Glutamine-driven upregulation of NPDC1 promotes colorectal cancer progression through PI3K/AKT signaling". *J Transl Med*. PMID: 41580703
4. Gao H et al. (2020). "miR-762 regulates the proliferation and differentiation of retinal progenitor cells by targeting NPDC1". *Cell Cycle*. PMID: 32544377
5. Njoroge JN et al. (2026). "Large-Scale Proteomic Profiling of Incident Heart Failure and Its Subtypes in Older Adults". *Circ Genom Precis Med*. PMID: 41636061

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
2. **研究新颖性**: PubMed仅36篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 68.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NPDC1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9NQX5)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NPDC1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9NQX5)


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
| UniProt | Q9NQX5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009635; |
| Pfam | PF06809; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107281-NPDC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACY3 | Bioplex | false |
| AQR | Bioplex | false |
| ATP11A | Bioplex | false |
| C3orf52 | Intact | false |
| CYSRT1 | Intact | false |
| DAD1 | Bioplex | false |
| E2F1 | Biogrid | false |
| EMD | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
