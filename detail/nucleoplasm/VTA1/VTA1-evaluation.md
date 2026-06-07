---
type: protein-evaluation
gene: "VTA1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## VTA1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VTA1/IF_images/1134_H11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VTA1/IF_images/1134_H11_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VTA1 |
| 蛋白名称 | Vacuolar protein sorting-associated protein VTA1 homolog |
| 蛋白大小 | 307 aa |
| UniProt ID | [Q9NP79](https://www.uniprot.org/uniprotkb/Q9NP79) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 21 |
| AlphaFold pLDDT | 78.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm; Endosome membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 307 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 21篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **119/183** |  |
| **归一化总分** |  |  | **65.0/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 VTA1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Endosome membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Hou J et al. (2024). "Integrated multi-omics analyses identify anti-viral host factors and pathways controlling SARS-CoV-2 infection". *Nat Commun*. PMID: 38168026
2. Hurley JH (2010). "The ESCRT complexes". *Crit Rev Biochem Mol Biol*. PMID: 20653365
3. Hurley JH & Yang D (2008). "MIT domainia". *Dev Cell*. PMID: 18194647
4. Tam PJ & Lingwood CA (2007). "Membrane cytosolic translocation of verotoxin A1 subunit in target cells". *Microbiology (Reading)*. PMID: 17660434
5. Yang D & Hurley JH (2010). "Structural role of the Vps4-Vta1 interface in ESCRT-III recycling". *Structure*. PMID: 20696398

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
2. **研究新颖性**: PubMed仅21篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/VTA1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9NP79)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=VTA1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9NP79)


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
| UniProt | Q9NP79 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR044538;IPR039431;IPR023175;IPR041212; |
| Pfam | PF04652;PF18097; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000009844-VTA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHMP1A | Intact, Biogrid, Bioplex | true |
| CHMP1B | Intact, Biogrid | true |
| CHMP2A | Biogrid, Bioplex | true |
| CHMP5 | Intact, Biogrid, Bioplex | true |
| VPS4A | Biogrid, Bioplex | true |
| BEX3 | Biogrid | false |
| C4orf3 | Bioplex | false |
| CBS | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
