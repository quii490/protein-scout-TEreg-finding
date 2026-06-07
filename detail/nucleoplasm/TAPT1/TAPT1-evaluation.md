---
type: protein-evaluation
gene: "TAPT1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TAPT1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TAPT1/IF_images/547_B6_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TAPT1/IF_images/547_B6_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TAPT1 |
| 蛋白名称 | Transmembrane anterior posterior transformation protein 1 homolog |
| 蛋白大小 | 567 aa |
| UniProt ID | [Q6NXT6](https://www.uniprot.org/uniprotkb/Q6NXT6) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 12 |
| AlphaFold pLDDT | 71.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, cilium |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 567 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 12篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 71.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **126/183** |  |
| **归一化总分** |  |  | **68.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TAPT1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, cilium basal body; Membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang B et al. (2022). "Transmembrane anterior posterior transformation 1 regulates BMP signaling and modulates the protein stability of SMAD1/5". *J Biol Chem*. PMID: 36370851
2. Dang TT et al. (2020). "miR614 Expression Enhances Breast Cancer Cell Motility". *Int J Mol Sci*. PMID: 33374314
3. Etich J et al. (2023). "TAPT1-at the crossroads of extracellular matrix and signaling in Osteogenesis imperfecta". *EMBO Mol Med*. PMID: 37292039
4. Godfrey L et al. (2021). "H3K79me2/3 controls enhancer-promoter interactions and activation of the pan-cancer stem cell marker PROM1/CD133 in MLL-AF4 leukemia cells". *Leukemia*. PMID: 32242051
5. Nabavizadeh N et al. (2023). "A progeroid syndrome caused by a deep intronic variant in TAPT1 is revealed by RNA/SI-NET sequencing". *EMBO Mol Med*. PMID: 36652330

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
2. **研究新颖性**: PubMed仅12篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 71.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TAPT1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q6NXT6)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TAPT1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q6NXT6)


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
| UniProt | Q6NXT6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008010; |
| Pfam | PF05346; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169762-TAPT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LRRC59 | Biogrid | false |
| SEC61B | Biogrid | false |
| SMAD1 | Biogrid | false |
| SMURF1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
