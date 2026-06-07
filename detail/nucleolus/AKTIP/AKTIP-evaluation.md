---
type: protein-evaluation
gene: "AKTIP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## AKTIP 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AKTIP/IF_images/799_E1_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AKTIP/IF_images/799_E1_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | AKTIP |
| 蛋白名称 | AKT-interacting protein |
| 蛋白大小 | 292 aa |
| UniProt ID | [Q9H8T0](https://www.uniprot.org/uniprotkb/Q9H8T0) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 22 |
| AlphaFold pLDDT | 77.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: Cytoplasm; Cell membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 292 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 77.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **119/183** |  |
| **归一化总分** |  |  | **65.0/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 AKTIP 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm; Cell membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Snelleksz M & Dean B (2024). "Higher levels of AKT-interacting protein in the frontal pole from people with schizophrenia are limited to a sub-group who have a marked deficit in cortical muscarinic M1 receptors". *Psychiatry Res*. PMID: 39236366
2. Wang Z et al. (2025). "EZH2 contributes to sepsis-induced acute lung injury through regulating macrophage polarization". *Biochim Biophys Acta Mol Basis Dis*. PMID: 39471914
3. Wang R et al. (2025). "Identification of AKTIP as a biomarker for fibrolamellar carcinoma using WGCNA and machine learning". *3 Biotech*. PMID: 40417661
4. Yuan Y et al. (2024). "Identification of M2 Macrophage-Related Key Genes in Advanced Atherosclerotic Plaques by Network-Based Analysis". *J Cardiovasc Pharmacol*. PMID: 38194604
5. Ng ASN et al. (2022). "AKTIP loss is enriched in ERα-positive breast cancer for tumorigenesis and confers endocrine resistance". *Cell Rep*. PMID: 36516775

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| CTBP2 | two hybrid pooling approach | 16189514 | — | — |
| HOOK2 | two hybrid pooling approach | 16189514 | — | — |
| CEP126 | two hybrid pooling approach | 16169070 | — | — |
| UTP14A | two hybrid pooling approach | 16169070 | — | — |
| RPA1 | two hybrid pooling approach | 16169070 | — | — |
| GTF3C1 | two hybrid pooling approach | 16169070 | — | — |
| IMMT | two hybrid pooling approach | 16169070 | — | — |
| POLA2 | two hybrid pooling approach | 16169070 | — | — |
| ASS1 | two hybrid pooling approach | 16169070 | — | — |
| EXOC7 | two hybrid pooling approach | 16169070 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅22篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 77.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/AKTIP)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9H8T0)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=AKTIP%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9H8T0)


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
| UniProt | Q9H8T0 |
| SMART | SM00212; |
| UniProt Domain [FT] | DOMAIN 74..222; /note="UBC core"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00388" |
| InterPro | IPR050113;IPR000608;IPR016135; |
| Pfam | PF00179; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166971-AKTIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FHIP1A | Intact, Biogrid | true |
| HOOK1 | Intact, Biogrid | true |
| HOOK2 | Intact, Biogrid | true |
| HOOK3 | Intact, Biogrid | true |
| TRIM32 | Intact, Biogrid | true |
| AKT1 | Biogrid | false |
| EGFR | Biogrid | false |
| FHIP1B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
