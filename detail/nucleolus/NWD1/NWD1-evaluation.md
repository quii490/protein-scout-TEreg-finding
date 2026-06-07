---
type: protein-evaluation
gene: "NWD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## NWD1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NWD1/IF_images/1938_E4_29_cr5d248b943a769_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NWD1/IF_images/1954_B2_40_cr5dfb7ba912e7f_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NWD1 |
| 蛋白名称 | NACHT domain- and WD repeat-containing protein 1 |
| 蛋白大小 | 1564 aa |
| UniProt ID | [Q149M9](https://www.uniprot.org/uniprotkb/Q149M9) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 12 |
| AlphaFold pLDDT | 80.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: Cytoplasm, cytosol |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1564 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 12篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 80.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NWD1 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytosol
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Yamada S et al. (2022). "Identification and expression profile of novel STAND gene Nwd2 in the mouse central nervous system". *Gene Expr Patterns*. PMID: 36341976
2. Wu Y et al. (2022). "NWD1 facilitates synaptic transmission and contributes to neuropathic pain". *Neuropharmacology*. PMID: 34902349
3. Bao T et al. (2024). "NWD1 influences the extension of neuronal axons by regulating microtubule stability". *Biochem Biophys Res Commun*. PMID: 39383832
4. Li W et al. (2020). "Vitamin D and the nutritional environment in functions of intestinal stem cells: Implications for tumorigenesis and prevention". *J Steroid Biochem Mol Biol*. PMID: 31783155
5. Yamada S et al. (2024). "Purinosomes and Purine Metabolism in Mammalian Neural Development: A Review". *Acta Histochem Cytochem*. PMID: 38988694

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| b4dyc6_human | luminescence based mammalian interactome mapping | 25036637 | — | — |
| NUDC | luminescence based mammalian interactome mapping | 25036637 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- GO: Cytoplasm, cytosol

**IntAct 查询记录**: IntAct: 2 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅12篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 80.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NWD1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q149M9)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NWD1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q149M9)


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
| UniProt | Q149M9 |
| SMART | SM00320; |
| UniProt Domain [FT] | DOMAIN 335..661; /note="NACHT" |
| InterPro | IPR024977;IPR007111;IPR043365;IPR057588;IPR027417;IPR011047;IPR015943;IPR019775;IPR001680; |
| Pfam | PF12894;PF05729;PF00400;PF25469; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188039-NWD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
