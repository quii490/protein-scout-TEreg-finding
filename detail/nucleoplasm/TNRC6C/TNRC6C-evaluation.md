---
type: protein-evaluation
gene: "TNRC6C"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TNRC6C 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TNRC6C/IF_images/1127_F5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TNRC6C/IF_images/1127_F5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TNRC6C |
| 蛋白名称 | Trinucleotide repeat-containing gene 6C protein |
| 蛋白大小 | 1936 aa |
| UniProt ID | [Q9HCJ0](https://www.uniprot.org/uniprotkb/Q9HCJ0) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 30 |
| AlphaFold pLDDT | 40.3 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1936 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 30篇 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT: 40.3 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **105/183** |  |
| **归一化总分** |  |  | **57.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TNRC6C 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ghosh DK & Ranjan A (2022). "HYPK coordinates degradation of polyneddylated proteins by autophagy". *Autophagy*. PMID: 34836490
2. Sobti M et al. (2023). "Molecular basis for GIGYF-TNRC6 complex assembly". *RNA*. PMID: 36854607
3. Tong C et al. (2021). "TNRC6C-AS1 Promotes Thyroid Cancer Progression by Upregulating LPAR5 via miR-513c-5p". *Cancer Manag Res*. PMID: 34393509
4. Cai Z et al. (2021). "TNRC6C Functions as a Tumor Suppressor and Is Frequently Downregulated in Papillary Thyroid Cancer". *Int J Endocrinol*. PMID: 33564303
5. Agarwal S et al. (2025). "Mechanistic Insights into Hybridization-Based Off-Target Activity of GalNAc-siRNA Conjugates". *Nucleic Acid Ther*. PMID: 40134378

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
2. **研究新颖性**: PubMed仅30篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 40.3

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TNRC6C)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9HCJ0)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TNRC6C%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9HCJ0)


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
| UniProt | Q9HCJ0 |
| SMART | SM00165; |
| UniProt Domain [FT] | DOMAIN 1140..1185; /note="UBA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00212"; DOMAIN 1811..1878; /note="RRM" |
| InterPro | IPR019486;IPR052068;IPR026805;IPR012677;IPR035979;IPR000504;IPR041917;IPR032226;IPR034927;IPR015940;IPR009060; |
| Pfam | PF10427;PF12938;PF00076;PF16608;PF00627; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000078687-TNRC6C/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGO1 | Intact, Biogrid, Opencell | true |
| AGO2 | Intact, Biogrid, Opencell | true |
| AGO3 | Intact, Biogrid | true |
| AGO4 | Intact, Biogrid | true |
| CNOT1 | Intact, Biogrid | true |
| CNOT10 | Intact, Biogrid | true |
| CNOT2 | Intact, Biogrid | true |
| CNOT3 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
