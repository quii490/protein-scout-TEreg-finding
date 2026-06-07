---
type: protein-evaluation
gene: "NINL"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## NINL 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NINL/IF_images/1293_H4_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NINL/IF_images/1293_H4_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NINL |
| 蛋白名称 | Ninein-like protein |
| 蛋白大小 | 1382 aa |
| UniProt ID | [Q9Y2I6](https://www.uniprot.org/uniprotkb/Q9Y2I6) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 34 |
| AlphaFold pLDDT | 65.7 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1382 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 34篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 65.7 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **111/183** |  |
| **归一化总分** |  |  | **60.7/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NINL 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Haley GE et al. (2010). "Effects of epsilon4 on object recognition in the non-demented elderly". *Curr Aging Sci*. PMID: 20044903
2. Haley GE et al. (2012). "Novel image-novel location object recognition task sensitive to age-related cognitive decline in nondemented elderly". *Age (Dordr)*. PMID: 21234692
3. Stevens DA et al. (2022). "Antiviral function and viral antagonism of the rapidly evolving dynein activating adaptor NINL". *Elife*. PMID: 36222652
4. Bachmann-Gagescu R et al. (2015). "The Ciliopathy Protein CC2D2A Associates with NINL and Functions in RAB8-MICAL3-Regulated Vesicle Trafficking". *PLoS Genet*. PMID: 26485645
5. Siva A et al. (2025). "Synthetic cargo adaptors reveal molecular features that can enhance dynein activation". *bioRxiv*. PMID: 40501990

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
2. **研究新颖性**: PubMed仅34篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 65.7

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NINL)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9Y2I6)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NINL%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9Y2I6)


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
| UniProt | Q9Y2I6 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 7..42; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 41..76; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 196..231; /note="EF-hand 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 233..268; /note="EF-hand 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR011992;IPR018247;IPR002048; |
| Pfam | PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101004-NINL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LZTS2 | Intact, Biogrid | true |
| MCM10 | Intact, Biogrid | true |
| RCOR3 | Intact, Biogrid | true |
| RGS2 | Intact, Biogrid | true |
| ACTR1A | Biogrid | false |
| AHI1 | Biogrid | false |
| ARHGAP21 | Biogrid | false |
| AURKB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
