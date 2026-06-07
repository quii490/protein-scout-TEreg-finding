---
type: protein-evaluation
gene: "DDIT4L"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## DDIT4L 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DDIT4L/IF_images/DDIT4L_BJ_3.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DDIT4L/IF_images/DDIT4L_BJ_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DDIT4L |
| 蛋白名称 | DNA damage-inducible transcript 4-like protein |
| 蛋白大小 | 193 aa |
| UniProt ID | [Q96D03](https://www.uniprot.org/uniprotkb/Q96D03) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 39 |
| AlphaFold pLDDT | 76.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 193 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 39篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 76.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DDIT4L 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm
- **结构域**: None identified
- **关键词**: ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Michalski C et al. (2024). "DDIT4L regulates mitochondrial and innate immune activities in early life". *JCI Insight*. PMID: 38319716
2. Wu E et al. (2024). "Exploration of potential shared gene signatures between periodontitis and multiple sclerosis". *BMC Oral Health*. PMID: 38218802
3. Yamada Y et al. (2025). "Nrf2-and p53-inducible REDD2/DDiT4L/Rtp801L confers pancreatic β-cell dysfunction, leading to glucose intolerance in high-fat diet-fed mice". *J Biol Chem*. PMID: 40409543
4. Pachera E et al. (2020). "Long noncoding RNA H19X is a key mediator of TGF-β-driven fibrosis". *J Clin Invest*. PMID: 32603313
5. Andersson B et al. (2023). "Development of a machine learning framework for radiation biomarker discovery and absorbed dose prediction". *Front Oncol*. PMID: 37256187

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
2. **研究新颖性**: PubMed仅39篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 76.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DDIT4L)
- [UniProt](https://www.uniprot.org/uniprotkb/Q96D03)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DDIT4L%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q96D03)


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
| UniProt | Q96D03 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012918;IPR038281; |
| Pfam | PF07809; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000145358-DDIT4L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PRKAB2 | Intact, Biogrid | true |
| ABCB11 | Intact | false |
| ACY3 | Intact | false |
| AFMID | Intact | false |
| AIDA | Intact | false |
| AKT1 | Intact | false |
| ARHGEF3 | Intact | false |
| ARPIN | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
