---
type: protein-evaluation
gene: "HTATSF1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## HTATSF1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Enhanced)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HTATSF1/IF_images/54_C5_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HTATSF1/IF_images/54_C5_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HTATSF1 |
| 蛋白名称 | 17S U2 SnRNP complex component HTATSF1 |
| 蛋白大小 | 755 aa |
| UniProt ID | [O43719](https://www.uniprot.org/uniprotkb/O43719) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Enhanced |
| PubMed 总数 | 7 |
| AlphaFold pLDDT | 59.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoplasm (Enhanced); UniProt: Nucleus; Chromosome |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 755 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 7篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT: 59.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 HTATSF1 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Enhanced
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Nucleus; Chromosome
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Zhao J et al. (2022). "A PARylation-phosphorylation cascade promotes TOPBP1 loading and RPA-RAD51 exchange in homologous recombination". *Mol Cell*. PMID: 35597237
2. Guo Q et al. (2024). "CK2-HTATSF1-TOPBP1 signaling axis modulates tumor chemotherapy response". *J Biol Chem*. PMID: 38762174
3. Miles TK et al. (2025). "Ablation of Leptin Receptor Signaling Alters Somatotrope Transcriptome Maturation in Female Mice". *Endocrinology*. PMID: 39964842
4. Corsini NS et al. (2018). "Coordinated Control of mRNA and rRNA Processing Controls Embryonic Stem Cell Pluripotency and Differentiation". *Cell Stem Cell*. PMID: 29625069
5. Putker K et al. (2025). "Identification of suitable qPCR reference genes for the normalization of gene expression in the BL10-mdx and D2-mdx mouse models of Duchenne muscular dystrophy". *PLoS One*. PMID: 39999085

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
2. **研究新颖性**: PubMed仅7篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 59.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/HTATSF1)
- [UniProt](https://www.uniprot.org/uniprotkb/O43719)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=HTATSF1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/O43719)


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
| UniProt | O43719 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 133..218; /note="RRM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 264..349; /note="RRM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR012677;IPR035979;IPR000504;IPR034393;IPR034392; |
| Pfam | PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102241-HTATSF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SF3A2 | Intact, Biogrid, Opencell | true |
| SNRPB | Intact, Biogrid, Opencell | true |
| SNRPB2 | Biogrid, Opencell, Bioplex | true |
| SNRPD2 | Biogrid, Opencell | true |
| SNRPF | Biogrid, Opencell, Bioplex | true |
| AP3D1 | Biogrid | false |
| BRD4 | Biogrid | false |
| HDAC6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
