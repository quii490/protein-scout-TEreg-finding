---
type: protein-evaluation
gene: "SYN2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## SYN2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SYN2/IF_images/1729_G2_2_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SYN2/IF_images/1729_G2_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SYN2 |
| 蛋白名称 | Synapsin-2 |
| 蛋白大小 | 582 aa |
| UniProt ID | [Q86VA8](https://www.uniprot.org/uniprotkb/Q86VA8) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 99 |
| AlphaFold pLDDT | N/A |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Synapse |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 582 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 99篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: N/A |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **86/183** |  |
| **归一化总分** |  |  | **47.0/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 SYN2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Synapse
- **结构域**: None identified
- **关键词**: ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Wang W et al. (2024). "Identification of early Alzheimer's disease subclass and signature genes based on PANoptosis genes". *Front Immunol*. PMID: 39650656
2. Oike A et al. (2025). "Syncytin-1 Is Responsible for the Fusion Between Human Trophoblasts and Endometrial Stromal Cells". *Dev Growth Differ*. PMID: 40509769
3. Sugimoto J et al. (2013). "A novel human endogenous retroviral protein inhibits cell-cell fusion". *Sci Rep*. PMID: 23492904
4. Haerian BS et al. (2011). "Lack of association between synapsin II (SYN2) gene polymorphism and susceptibility epilepsy: a case-control study and meta-analysis". *Synapse*. PMID: 21465568
5. Taylor PN et al. (2015). "Whole-genome sequence-based analysis of thyroid function". *Nat Commun*. PMID: 25743335

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
2. **研究新颖性**: PubMed仅99篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = N/A

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/SYN2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q86VA8)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=SYN2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q86VA8)


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
| UniProt | Q92777 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013815;IPR016185;IPR001359;IPR020898;IPR019735;IPR019736;IPR020897; |
| Pfam | PF02078;PF02750;PF10581; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157152-SYN2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Opencell | false |
| PDCD6IP | Opencell | false |
| SYN1 | Biogrid | false |
| SYN3 | Intact, Biogrid | false |
| YWHAB | Opencell | false |
| YWHAG | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
