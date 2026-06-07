---
type: protein-evaluation
gene: "E4F1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## E4F1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/E4F1/IF_images/1526_F11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/E4F1/IF_images/1526_F11_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | E4F1 |
| 蛋白名称 | Transcription factor E4F1 |
| 蛋白大小 | 784 aa |
| UniProt ID | [Q66K89](https://www.uniprot.org/uniprotkb/Q66K89) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 62 |
| AlphaFold pLDDT | 52.4 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Nucleus, nucleoplasm; Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 784 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 62篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 52.4 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **95/183** |  |
| **归一化总分** |  |  | **51.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 E4F1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus, nucleoplasm; Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Sun S et al. (2023). "Transcription factor E4F1 as a regulator of cell life and disease progression". *Sci Adv*. PMID: 37774036
2. Di Michele M et al. (2025). "E4F1 coordinates pyruvate metabolism and the activity of the elongator complex to ensure translation fidelity during brain development". *Nat Commun*. PMID: 39747033
3. Sun S et al. (2025). "Phosphorylation of PA28γ by CK2 kinase facilitates HNSCC tumor formation and progression". *Nat Commun*. PMID: 41372189
4. Zhang L et al. (2025). "Ribosomal protein S3A (RPS3A), as a transcription regulator of colony-stimulating factor 1 (CSF1), promotes glioma progression through regulating the recruitment and autophagy-mediated M2 polarizat...". *Naunyn Schmiedebergs Arch Pharmacol*. PMID: 39560749
5. Lacroix M et al. (2021). "The multifunctional protein E4F1 links P53 to lipid metabolism in adipocytes". *Nat Commun*. PMID: 34857760

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
2. **研究新颖性**: PubMed仅62篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 52.4

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/E4F1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q66K89)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=E4F1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q66K89)


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
| UniProt | Q66K89 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036236;IPR013087; |
| Pfam | PF00096; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167967-E4F1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Intact, Biogrid | true |
| ABT1 | Bioplex | false |
| ANP32A | Intact | false |
| C1QBP | Bioplex | false |
| CDKN2A | Biogrid | false |
| FHL2 | Biogrid | false |
| HMGA2 | Biogrid | false |
| PARP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
