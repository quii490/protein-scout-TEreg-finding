---
type: protein-evaluation
gene: "PCYT2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## PCYT2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCYT2/IF_images/222_D11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCYT2/IF_images/222_D11_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCYT2 |
| 蛋白名称 | Ethanolamine-phosphate cytidylyltransferase |
| 蛋白大小 | 389 aa |
| UniProt ID | [Q99447](https://www.uniprot.org/uniprotkb/Q99447) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 48 |
| AlphaFold pLDDT | 86.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 389 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 48篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 86.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **112/183** |  |
| **归一化总分** |  |  | **61.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 PCYT2 定位：
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
1. Fu G et al. (2021). "Metabolic control of T(FH) cells and humoral immunity by phosphatidylethanolamine". *Nature*. PMID: 34234346
2. Cikes D et al. (2023). "PCYT2-regulated lipid biosynthesis is critical to muscle health and ageing". *Nat Metab*. PMID: 36941451
3. Zhou L et al. (2024). "PCYT2 inhibits epithelial-mesenchymal transition in colorectal cancer by elevating YAP1 phosphorylation". *JCI Insight*. PMID: 39531326
4. Wen Y et al. (2024). "Chaiqin chengqi decoction treatment mitigates hypertriglyceridemia-associated acute pancreatitis by modulating liver-mediated glycerophospholipid metabolism". *Phytomedicine*. PMID: 39217651
5. Grapentine S et al. (2023). "Skeletal Muscle Consequences of Phosphatidylethanolamine Synthesis Deficiency". *Function (Oxf)*. PMID: 37342414

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
2. **研究新颖性**: PubMed仅48篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 86.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/PCYT2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q99447)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=PCYT2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q99447)


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
| UniProt | Q99447 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR041723;IPR004821;IPR044608;IPR014729; |
| Pfam | PF01467; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185813-PCYT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASP6 | Intact | false |
| CLVS2 | Intact | false |
| INCA1 | Intact | false |
| INPPL1 | Intact, Bioplex | false |
| PSMA1 | Intact | false |
| RIPPLY1 | Bioplex | false |
| SLC35G2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
