---
type: protein-evaluation
gene: "RABGEF1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## RABGEF1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RABGEF1/IF_images/60_D2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RABGEF1/IF_images/60_D2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RABGEF1 |
| 蛋白名称 | Rab5 GDP/GTP exchange factor |
| 蛋白大小 | 491 aa |
| UniProt ID | [Q9UJ41](https://www.uniprot.org/uniprotkb/Q9UJ41) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Supported |
| PubMed 总数 | 70 |
| AlphaFold pLDDT | 77.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Supported); UniProt: Cytoplasm; Early endosome; Recycling endosome |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 491 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 70篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 77.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **99/183** |  |
| **归一化总分** |  |  | **54.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 RABGEF1 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Early endosome; Recycling endosome
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Huang TX et al. (2024). "ATP6V0A1-dependent cholesterol absorption in colorectal cancer cells triggers immunosuppressive signaling to inactivate memory CD8(+) T cells". *Nat Commun*. PMID: 38971819
2. Yamano K et al. (2018). "Endosomal Rab cycles regulate Parkin-mediated mitophagy". *Elife*. PMID: 29360040
3. Li R et al. (2024). "GPRASP1 loss-of-function links to arteriovenous malformations by endothelial activating GPR4 signals". *Brain*. PMID: 37787182
4. Chen D et al. (2024). "Guanine nucleotide exchange factor RABGEF1 facilitates TNF-induced necroptosis by targeting cIAP1". *Biochem Biophys Res Commun*. PMID: 38377943
5. Marichal T et al. (2016). "Guanine nucleotide exchange factor RABGEF1 regulates keratinocyte-intrinsic signaling to maintain skin homeostasis". *J Clin Invest*. PMID: 27820702

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| KXD1 | pull down | 16189514 | — | — |
| AP1G1 | two hybrid | 15143060 | — | — |
| UBB | affinity chromatography technology | 15143060 | — | — |
| AP1G2 | pull down | 12505986 | — | — |
| GGA1 | pull down | 12505986 | — | — |
| GGA3 | pull down | 12505986 | — | — |
| GGA2 | pull down | 12505986 | — | — |
| q9vh45_drome | two hybrid | 14605208 | — | — |
| RPS27A | isothermal titration calorimetry | 16499958 | — | — |
| EGFR | anti bait coimmunoprecipitation | 16499958 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Cytoplasm, Early endosome, Recycling endosome, cytosol, nucleolus

**IntAct 查询记录**: IntAct: 80 实验验证互作

**评价**: —


### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅70篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 77.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/RABGEF1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9UJ41)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=RABGEF1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9UJ41)


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
| UniProt | Q9UJ41 |
| SMART | SM00167;SM00259; |
| UniProt Domain [FT] | DOMAIN 232..375; /note="VPS9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00550" |
| InterPro | IPR041545;IPR003123;IPR045046;IPR037191;IPR002653; |
| Pfam | PF18151;PF02204;PF01754; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154710-RABGEF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Intact, Biogrid | true |
| KXD1 | Intact, Biogrid | true |
| RABEP1 | Intact, Biogrid, Opencell | true |
| YWHAB | Intact, Biogrid | true |
| YWHAG | Intact, Biogrid | true |
| YWHAZ | Biogrid, Opencell | true |
| BLOC1S6 | Intact | false |
| CCHCR1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
