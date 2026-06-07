---
type: protein-evaluation
gene: "ELP2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## ELP2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP2/IF_images/1898_D1_20_cr5ba362bc94e90_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP2/IF_images/1898_D1_3_cr5ba362bc94ea1_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ELP2 |
| 蛋白名称 | Elongator complex protein 2 |
| 蛋白大小 | 826 aa |
| UniProt ID | [Q6IA86](https://www.uniprot.org/uniprotkb/Q6IA86) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 82 |
| AlphaFold pLDDT | 89.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 826 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 82篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 89.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **90/183** |  |
| **归一化总分** |  |  | **49.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 ELP2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Nucleus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Tian J et al. (2022). "Aberrant RNA Splicing Is a Primary Link between Genetic Variation and Pancreatic Cancer Risk". *Cancer Res*. PMID: 35363263
2. Xia C et al. (2023). "ELP2-NLRP3-GSDMD/GSDME-mediated pyroptosis is induced by TNF-α in MC3T3-E1 cells during osteogenic differentiation". *J Cell Mol Med*. PMID: 37830762
3. Wang Y et al. (2013). "The Arabidopsis elongator complex subunit2 epigenetically regulates plant immune responses". *Plant Cell*. PMID: 23435660
4. Wang C et al. (2015). "Arabidopsis Elongator subunit 2 positively contributes to resistance to the necrotrophic fungal pathogens Botrytis cinerea and Alternaria brassicicola". *Plant J*. PMID: 26216741
5. Russo A et al. (2021). "ELP2 compound heterozygous variants associated with cortico-cerebellar atrophy, nodular heterotopia and epilepsy: Phenotype expansion and review of the literature". *Eur J Med Genet*. PMID: 34653680

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
2. **研究新颖性**: PubMed仅82篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 89.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/ELP2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q6IA86)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=ELP2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q6IA86)


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
| UniProt | Q6IA86 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037289;IPR015943;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134759-ELP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELP1 | Intact, Biogrid | true |
| ELP3 | Biogrid | false |
| ELP4 | Biogrid | false |
| ELP6 | Biogrid | false |
| FKBP5 | Opencell | false |
| JAK1 | Biogrid | false |
| RPA2 | Biogrid | false |
| STAT3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
