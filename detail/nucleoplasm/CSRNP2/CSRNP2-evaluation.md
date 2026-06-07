---
type: protein-evaluation
gene: "CSRNP2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CSRNP2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSRNP2 / CSRNP2 |
| 蛋白大小 | 543 aa / ~59.7 kDa |
| UniProt ID | Q9H175 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO chromatin，nuclear protein with chromatin association |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 543 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=4篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 63.2），44%有序，46%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6 | 0/1调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:chromatin; C:nucleus | — |
| Protein Atlas (IF) | nuclear speckles (Approved, AF22) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP2/IF_images/AF22_1.jpg|AF22]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP2/IF_images/AF22_2.jpg|AF22]]

**结论**: UniProt Nucleus + GO chromatin，nuclear protein with chromatin association

#### 3.2 蛋白大小评估
**评价**: 543 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 4 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 4 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**
**关键文献**:
1. Vargas DM et al. (2018). "Alzheimer's disease master regulators analysis: search for potential molecular targets and drug repositioning candidates". *Alzheimers Res Ther*. PMID: 29935546
2. Zhang H et al. (2021). "The CSRNP Gene Family Serves as a Prognostic Biomarker in Clear Cell Renal Cell Carcinoma". *Front Oncol*. PMID: 33869003
3. Chen J et al. (2013). "Identifying candidate genes for Type 2 Diabetes Mellitus and obesity through gene expression profiling in multiple tissues or cells". *J Diabetes Res*. PMID: 24455749
4. Reddy MK et al. (2001). "Cloning and expression of a nuclear encoded plastid specific 33 kDa ribonucleoprotein gene (33RNP) from pea that is light stimulated". *Gene*. PMID: 11223256

**评价**: AlphaFold预测置信度偏低（pLDDT 63.2，46%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:csrn2_human(display_long)|uniprotkb:CSRNP2(gene name)|psi-mi:CSRNP2(display_short)|uniprotkb:C12orf22(gene name synonym)|uniprotkb:FAM130A1(gene name synonym)|uniprotkb:TAIP12(gene name synonym)|uniprotkb:Protein FAM130A1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 12(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:29892012|doi:10.1038/s41588-018-0130-z|imex:IM-27553 | 待分析 | 否 |
| psi-mi:csrn2_human(display_long)|uniprotkb:CSRNP2(gene name)|psi-mi:CSRNP2(display_short)|uniprotkb:C12orf22(gene name synonym)|uniprotkb:FAM130A1(gene name synonym)|uniprotkb:TAIP12(gene name synonym)|uniprotkb:Protein FAM130A1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 12(gene name synonym) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:csrn2_human(display_long)|uniprotkb:CSRNP2(gene name)|psi-mi:CSRNP2(display_short)|uniprotkb:C12orf22(gene name synonym)|uniprotkb:FAM130A1(gene name synonym)|uniprotkb:TAIP12(gene name synonym)|uniprotkb:Protein FAM130A1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 12(gene name synonym) | psi-mi:"MI:0090"(protein compl | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:csrn2_human(display_long)|uniprotkb:CSRNP2(gene name)|psi-mi:CSRNP2(display_short)|uniprotkb:C12orf22(gene name synonym)|uniprotkb:FAM130A1(gene name synonym)|uniprotkb:TAIP12(gene name synonym)|uniprotkb:Protein FAM130A1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 12(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:csrn2_human(display_long)|uniprotkb:CSRNP2(gene name)|psi-mi:CSRNP2(display_short)|uniprotkb:C12orf22(gene name synonym)|uniprotkb:FAM130A1(gene name synonym)|uniprotkb:TAIP12(gene name synonym)|uniprotkb:Protein FAM130A1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 12(gene name synonym) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component): C:chromatin; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 0 个伙伴
- 调控相关比例: 0/1 (0%)

**评价**: PPI网络稀薄，调控关联极少（0/1），可能为独立功能蛋白。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 63.2），44%有序，46%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **71.0/100**

**核心优势**:
1. PubMed 4 篇，研究新颖性高
2. 蛋白大小 543 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H175
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H175
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CSRNP2%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CSRNP2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CSRNP2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP2/CSRNP2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H175 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031972;IPR023260; |
| Pfam | PF16019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110925-CSRNP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP1CA | Intact, Biogrid | true |
| PPP1CC | Intact, Biogrid | true |
| PPP1CB | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
