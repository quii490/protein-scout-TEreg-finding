---
type: protein-evaluation
gene: "CCDC82"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC82 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC82 / CCDC82 |
| 蛋白大小 | 544 aa / ~59.8 kDa |
| UniProt ID | Q8N4S0 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | GO nucleus，UniProt无亚细胞注释，核定位较弱 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 544 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=4篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 64.3），42%有序，46%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | 0/1调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **125/183** |  |
| **归一化总分** |  |  | **68.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | 无UniProt注释 | — |
| GO Cellular Component | C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm+cytosol (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC82/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC82/IF_images/A-431_2.jpg|A-431]]

**结论**: GO nucleus，UniProt无亚细胞注释，核定位较弱

#### 3.2 蛋白大小评估
**评价**: 544 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 4 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Yahia A et al. (2022). "Genetic diagnosis in Sudanese and Tunisian families with syndromic intellectual disability through exome sequencing". *Ann Hum Genet*. PMID: 35118659
2. Komiya T et al. (2025). "Novel MAML2 Fusions in Human Malignancy". *Cancers (Basel)*. PMID: 41097675
3. Li X et al. (2023). "Establishment of a primary renal lymphoma model and its clinical relevance". *Front Oncol*. PMID: 37700827
4. Kozlov SV et al. (2016). "Reactive Oxygen Species (ROS)-Activated ATM-Dependent Phosphorylation of Cytoplasmic Substrates Identified by Large-Scale Phosphoproteomics Screen". *Mol Cell Proteomics*. PMID: 26699800
5. Bauer G et al. (2022). "CCDC82 frameshift mutation associated with intellectual disability, spastic paraparesis, and dysmorphic features". *Clin Genet*. PMID: 35373332
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 64.3 |
| 有序区域 (pLDDT>70) 占比 | 41.5% |
| pLDDT>90 占比 | 31.8% |
| pLDDT<50 占比 | 46.3% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold预测置信度偏低（pLDDT 64.3，46%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:ccd82_human(display_long)|uniprotkb:CCDC82(gene name)|psi-mi:CCDC82(display_short)|uniprotkb:HT025(orf name) | psi-mi:"MI:0006"(anti bait coi | pubmed:17353931 | 待分析 | 是 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component): C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 0 个伙伴
- 调控相关比例: 0/1 (0%)

**评价**: PPI网络稀薄，调控关联极少（0/1），可能为独立功能蛋白。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 64.3），42%有序，46%无序 | 待验证 |
| 定位 | UniProt + GO | 无UniProt注释 | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **66.7/100**

**核心优势**:
1. PubMed 4 篇，研究新颖性高
2. 蛋白大小 544 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4S0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4S0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CCDC82%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CCDC82&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CCDC82


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC82/CCDC82-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N4S0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025244;IPR025451; |
| Pfam | PF13846;PF13926; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149231-CCDC82/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Opencell | false |
| CSNK2A2 | Opencell | false |
| CSNK2B | Opencell | false |
| RALBP1 | Opencell | false |
| SSRP1 | Opencell | false |
| SUPT16H | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
