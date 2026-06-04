---
type: protein-evaluation
gene: "NKTR"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## NKTR 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Supported)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NKTR/IF_images/237_D2_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NKTR/IF_images/237_D2_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NKTR |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase |
| 蛋白大小 | 104 aa |
| UniProt ID | [C9JMM5](https://www.uniprot.org/uniprotkb/C9JMM5) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Supported |
| PubMed 总数 | 100 |
| AlphaFold pLDDT | 89.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Supported); UniProt: N/A |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 104 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 100篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 89.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **90/183** |  |
| **归一化总分** |  |  | **49.2/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 NKTR 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Supported
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Unknown (2006). "Naloxegol". **. PMID: 31260226
2. Dixit N et al. (2021). "NKTR-358: A novel regulatory T-cell stimulator that selectively stimulates expansion and suppressive function of regulatory T cells for the treatment of autoimmune and inflammatory diseases". *J Transl Autoimmun*. PMID: 34041473
3. Srinagesh H et al. (2024). "A phase 1 clinical trial of NKTR-255 with CD19-22 CAR T-cell therapy for refractory B-cell acute lymphoblastic leukemia". *Blood*. PMID: 38968138
4. Luo W et al. (2024). "Circumventing resistance within the Ewing sarcoma microenvironment by combinatorial innate immunotherapy". *J Immunother Cancer*. PMID: 39266215
5. Hirayama AV et al. (2023). "A novel polymer-conjugated human IL-15 improves efficacy of CD19-targeted CAR T-cell immunotherapy". *Blood Adv*. PMID: 36332004

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
2. **研究新颖性**: PubMed仅100篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 89.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/NKTR)
- [UniProt](https://www.uniprot.org/uniprotkb/C9JMM5)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=NKTR%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/C9JMM5)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




