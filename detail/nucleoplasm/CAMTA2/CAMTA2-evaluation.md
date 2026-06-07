---
type: protein-evaluation
gene: "CAMTA2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CAMTA2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAMTA2 / CAMTA2 |
| 蛋白大小 | 1202 aa / ~132.2 kDa |
| UniProt ID | O94983 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO chromatin，calmodulin-binding转录激活因子 |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1202 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=19篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 59.2），42%有序，49%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 6/10 | ×3 | 18 | 4/24调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **140/183** |  |
| **归一化总分** |  |  | **76.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:chromatin; C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm (Approved, A-549) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CAMTA2/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CAMTA2/IF_images/A-549_2.jpg|A-549]]

**结论**: UniProt Nucleus + GO chromatin，calmodulin-binding转录激活因子

#### 3.2 蛋白大小评估
**评价**: 1202 aa

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 19 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 19 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Seluzicki A & Chory J (2025). "Genetic architecture of a light-temperature coincidence detector". *Nat Commun*. PMID: 40858539
2. Hussain S et al. (2024). "Calcium signaling triggers early high humidity responses in Arabidopsis thaliana". *Proc Natl Acad Sci U S A*. PMID: 39661062
3. Schwartz RJ & Schneider MD (2006). "CAMTA in cardiac hypertrophy". *Cell*. PMID: 16678087
4. Monies D et al. (2017). "Identification of a novel genetic locus underlying tremor and dystonia". *Hum Genomics*. PMID: 29110692
5. Luan XF et al. (2021). "The miR-28-5p-CAMTA2 axis regulates colon cancer progression via Wnt/β-catenin signaling". *J Cell Biochem*. PMID: 31709644
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 59.2 |
| 有序区域 (pLDDT>70) 占比 | 41.5% |
| pLDDT>90 占比 | 15.5% |
| pLDDT<50 占比 | 49.1% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold预测置信度偏低（pLDDT 59.2，49%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:nkx25_mouse(display_long)|uniprotkb:Nkx2-5(gene name)|psi-mi:Nkx2-5(display_short)|uniprotkb:Csx(gene name synonym)|uniprotkb:Nkx-2.5(gene name synonym)|uniprotkb:Nkx2e(gene name synonym)|uniprotkb:Homeobox protein NK-2 homolog E(gene name synonym)|uniprotkb:Cardiac-specific homeobox(gene name synonym)|uniprotkb:Homeobox protein CSX(gene name synonym) | psi-mi:"MI:0096"(pull down) | imex:IM-11944|pubmed:16678093 | 待分析 | 是 |
| psi-mi:nkx25_mouse(display_long)|uniprotkb:Nkx2-5(gene name)|psi-mi:Nkx2-5(display_short)|uniprotkb:Csx(gene name synonym)|uniprotkb:Nkx-2.5(gene name synonym)|uniprotkb:Nkx2e(gene name synonym)|uniprotkb:Homeobox protein NK-2 homolog E(gene name synonym)|uniprotkb:Cardiac-specific homeobox(gene name synonym)|uniprotkb:Homeobox protein CSX(gene name synonym) | psi-mi:"MI:0096"(pull down) | imex:IM-11944|pubmed:16678093 | 待分析 | 是 |
| psi-mi:cmta2_human(display_long)|uniprotkb:CAMTA2(gene name)|psi-mi:CAMTA2(display_short)|uniprotkb:KIAA0909(gene name synonym) | psi-mi:"MI:0398"(two hybrid po | imex:IM-13779|pubmed:20711500 | 待分析 | 否 |
| psi-mi:o94983-5(display_long)|uniprotkb:KIAA0909(gene name synonym)|uniprotkb:CAMTA2(gene name)|psi-mi:CAMTA2(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:maga6_human(display_long)|uniprotkb:MAGE-6 antigen(gene name synonym)|uniprotkb:MAGE3B antigen(gene name synonym)|uniprotkb:Cancer/testis antigen 1.6(gene name synonym)|uniprotkb:MAGEA6(gene name)|psi-mi:MAGEA6(display_short)|uniprotkb:MAGE6(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PSME3IP1 | 0.826 | 待分析 | 否 |
| CALM3 | 0.724 | 待分析 | 否 |
| PSME3 | 0.630 | 待分析 | 否 |
| NKX2-5 | 0.629 | 待分析 | 否 |
| CALML3 | 0.628 | 待分析 | 否 |
| CALML5 | 0.628 | 待分析 | 否 |
| CALML4 | 0.627 | 待分析 | 否 |
| CALML6 | 0.627 | 待分析 | 否 |
| HDAC5 | 0.609 | 待分析 | 是 |
| NPPA | 0.605 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:chromatin; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 24 个伙伴
- 调控相关比例: 4/24 (17%)

**评价**: PPI网络有部分调控关联（4/24），40个物理互作，功能关联中等。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 59.2），42%有序，49%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **74.9/100**

**核心优势**:
1. PubMed 19 篇，研究新颖性高
2. 蛋白大小 1202 aa

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94983
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94983
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CAMTA2%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CAMTA2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CAMTA2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CAMTA2/CAMTA2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94983 |
| SMART | SM01076; |
| UniProt Domain [FT] | DOMAIN 537..615; /note="IPT/TIG"; DOMAIN 1049..1078; /note="IQ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116"; DOMAIN 1102..1131; /note="IQ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116" |
| InterPro | IPR036770;IPR005559;IPR013783;IPR014756;IPR002909; |
| Pfam | PF03859;PF01833; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108509-CAMTA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASXL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
