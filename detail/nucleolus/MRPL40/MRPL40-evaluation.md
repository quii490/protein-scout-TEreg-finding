---
type: protein-evaluation
gene: "MRPL40"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## MRPL40 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MRPL40/IF_images/5_D5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MRPL40/IF_images/5_D5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MRPL40 |
| 蛋白名称 | Large ribosomal subunit protein mL40 |
| 蛋白大小 | 206 aa |
| UniProt ID | [Q9NQ50](https://www.uniprot.org/uniprotkb/Q9NQ50) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Supported |
| PubMed 总数 | 10 |
| AlphaFold pLDDT | 78.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Supported); UniProt: Mitochondrion |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 206 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 10篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 MRPL40 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Mitochondrion
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; 

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/MRPL40/MRPL40-PAE.png]]

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Campbell PD et al. (2023). "Mitochondrial proteins encoded by the 22q11.2 neurodevelopmental locus regulate neural stem and progenitor cell proliferation". *Mol Psychiatry*. PMID: 37794116
2. Cheong A et al. (2020). "Expression analysis of mammalian mitochondrial ribosomal protein genes". *Gene Expr Patterns*. PMID: 32987154
3. Campbell PD et al. (2023). "Mitochondrial genes in the 22q11.2 deleted region regulate neural stem and progenitor cell proliferation". *bioRxiv*. PMID: 36711666
4. Li J et al. (2019). "Mitochondrial deficits in human iPSC-derived neurons from patients with 22q11.2 deletion syndrome and schizophrenia". *Transl Psychiatry*. PMID: 31740674
5. Liu Y et al. (2023). "Insufficiency of Mrpl40 disrupts testicular structure and semen parameters in a murine model". *Asian J Androl*. PMID: 36891938

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Bap60 | two hybrid | 14605208 | — | — |
| HLAB | anti bait coimmunoprecipitation | 17353931 | — | — |
| ATG17 | two hybrid | 18719252 | — | — |
| SIF2 | two hybrid | 18719252 | — | — |
| HLH4C | two hybrid | 14605208 | — | — |
| mRpL46 | two hybrid | 14605208 | — | — |
| HSPB1 | reverse ras recruitment system | 25277244 | — | — |
| NOTCH2NLC | two hybrid array | 32296183 | — | — |
| CYSRT1 | validated two hybrid | 32296183 | — | — |
| kra31_human | validated two hybrid | 32296183 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Mitochondrion

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅10篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/MRPL40)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9NQ50)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=MRPL40%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9NQ50)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MRPL40-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/MRPL40/MRPL40-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQ50 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019192;IPR039145; |
| Pfam | PF09812; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185608-MRPL40/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MRPL2 | Biogrid, Bioplex | true |
| MRPL37 | Biogrid, Bioplex | true |
| MRPL42 | Biogrid, Bioplex | true |
| MRPL46 | Biogrid, Bioplex | true |
| MRPL50 | Biogrid, Bioplex | true |
| MRPL51 | Biogrid, Bioplex | true |
| MRPL52 | Biogrid, Bioplex | true |
| CS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
