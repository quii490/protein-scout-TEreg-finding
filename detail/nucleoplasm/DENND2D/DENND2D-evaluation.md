---
type: protein-evaluation
gene: "DENND2D"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## DENND2D 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DENND2D/IF_images/DENND2D_A_431_2.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DENND2D/IF_images/DENND2D_A_431_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DENND2D |
| 蛋白名称 | DENN domain-containing protein 2D |
| 蛋白大小 | 471 aa |
| UniProt ID | [Q9H6A0](https://www.uniprot.org/uniprotkb/Q9H6A0) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 84.6 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 471 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 84.6 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DENND2D 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Kanda M et al. (2015). "Prognostic impact of expression and methylation status of DENN/MADD domain-containing protein 2D in gastric cancer". *Gastric Cancer*. PMID: 24695972
2. Kanda M et al. (2014). "Downregulation of DENND2D by promoter hypermethylation is associated with early recurrence of hepatocellular carcinoma". *Int J Oncol*. PMID: 24189587
3. Ma WJ et al. (2022). "Stage IV colon cancer patients without DENND2D expression benefit more from neoadjuvant chemotherapy". *Cell Death Dis*. PMID: 35523764
4. Kim J et al. (2016). "Precise and selective sensing of DNA-DNA hybridization by graphene/Si-nanowires diode-type biosensors". *Sci Rep*. PMID: 27534818
5. Kuo HD et al. (2022). "DNA Methylome and Transcriptome Study of Triterpenoid CDDO in TPA-Mediated Skin Carcinogenesis Model". *AAPS J*. PMID: 36324037

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
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 84.6

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DENND2D)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9H6A0)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DENND2D%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9H6A0)


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
| UniProt | Q9H6A0 |
| SMART | SM00801;SM00799;SM00800; |
| UniProt Domain [FT] | DOMAIN 55..204; /note="uDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 226..359; /note="cDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 361..445; /note="dDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304" |
| InterPro | IPR001194;IPR005112;IPR043153;IPR051942;IPR037516;IPR005113; |
| Pfam | PF03455;PF02141;PF03456; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162777-DENND2D/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM9B | Intact | false |
| HSPA9 | Intact, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
