---
type: protein-evaluation
gene: "WDFY4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## WDFY4 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDFY4/IF_images/1752_D4_3_cr5804df8a8cea7_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDFY4/IF_images/1752_D4_8_cr5804df940fa7f_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | WDFY4 |
| 蛋白名称 | WD repeat- and FYVE domain-containing protein 4 |
| 蛋白大小 | 3184 aa |
| UniProt ID | [Q6ZS81](https://www.uniprot.org/uniprotkb/Q6ZS81) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 42 |
| AlphaFold pLDDT | 78.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Early endosome; Endoplasmic reticulum |
| 📏 蛋白大小 | 0/10 | ×1 | 0 | 3184 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 78.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **99/183** |  |
| **归一化总分** |  |  | **54.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 WDFY4 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Early endosome; Endoplasmic reticulum
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Theisen DJ et al. (2018). "WDFY4 is required for cross-presentation in response to viral and tumor antigens". *Science*. PMID: 30409884
2. Lyu X et al. (2024). "The clinical relevance of WDFY4 in autoimmune diseases in diverse ancestral populations". *Rheumatology (Oxford)*. PMID: 38507703
3. Jo S et al. (2025). "Shared pathway of WDFY4-dependent cross-presentation of immune complexes by cDC1 and cDC2". *J Exp Med*. PMID: 39918736
4. Zhong N et al. (2025). "WDFY4 Promotes the Progression of Atherosclerosis by Regulating Ferroptosis Mediated by the LAPTM5/CDC42/mTOR/4EBP1/SLC7A11 Pathway". *J Cell Mol Med*. PMID: 40755163
5. Postoak JL et al. (2025). "WDFY4-dependent cross-presentation proceeds via a vacuolar antigen-processing route". *Proc Natl Acad Sci U S A*. PMID: 41364771

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
2. **研究新颖性**: PubMed仅42篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 78.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/WDFY4)
- [UniProt](https://www.uniprot.org/uniprotkb/Q6ZS81)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=WDFY4%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q6ZS81)


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
| UniProt | Q6ZS81 |
| SMART | SM01026;SM00320; |
| UniProt Domain [FT] | DOMAIN 2385..2510; /note="BEACH-type PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01119"; DOMAIN 2527..2821; /note="BEACH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00026" |
| InterPro | IPR011989;IPR016024;IPR000409;IPR036372;IPR051944;IPR023362;IPR011993;IPR015943;IPR019775;IPR036322;IPR001680; |
| Pfam | PF02138;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128815-WDFY4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
