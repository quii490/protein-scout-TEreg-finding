---
type: protein-evaluation
gene: "TNRC6A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TNRC6A 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TNRC6A/IF_images/125_D12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TNRC6A/IF_images/125_D12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TNRC6A |
| 蛋白名称 | Trinucleotide repeat-containing gene 6A protein |
| 蛋白大小 | 1962 aa |
| UniProt ID | [Q8NDV7](https://www.uniprot.org/uniprotkb/Q8NDV7) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 65 |
| AlphaFold pLDDT | 37.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm, P-body |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1962 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 65篇 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT: 37.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **85/183** |  |
| **归一化总分** |  |  | **46.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TNRC6A 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, P-body
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Hafner M et al. (2010). "Transcriptome-wide identification of RNA-binding protein and microRNA target sites by PAR-CLIP". *Cell*. PMID: 20371350
2. Shah KM et al. (2025). "C-terminal tagging impairs AGO2 function". *RNA Biol*. PMID: 40698645
3. Ishiura H et al. (2018). "Expansions of intronic TTTCA and TTTTA repeats in benign adult familial myoclonic epilepsy". *Nat Genet*. PMID: 29507423
4. Corbett MA et al. (2023). "Genetics of familial adult myoclonus epilepsy: From linkage studies to noncoding repeat expansions". *Epilepsia*. PMID: 37021642
5. Chen W et al. (2023). "MiR-652-3p promotes malignancy and metastasis of cancer cells via inhibiting TNRC6A in hepatocellular carcinoma". *Biochem Biophys Res Commun*. PMID: 36495604

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
2. **研究新颖性**: PubMed仅65篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 37.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TNRC6A)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8NDV7)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TNRC6A%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8NDV7)


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
| UniProt | Q8NDV7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1781..1853; /note="RRM" |
| InterPro | IPR019486;IPR052068;IPR012677;IPR035979;IPR032226;IPR034924; |
| Pfam | PF10427;PF16608; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000090905-TNRC6A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGO1 | Intact, Biogrid, Opencell | true |
| AGO2 | Intact, Biogrid, Opencell | true |
| AGO3 | Intact, Biogrid | true |
| AGO4 | Intact, Biogrid | true |
| CNOT1 | Intact, Biogrid | true |
| PABPC1 | Intact, Biogrid | true |
| PAN3 | Intact, Biogrid | true |
| ANAPC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
