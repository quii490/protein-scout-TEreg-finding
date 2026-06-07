---
type: protein-evaluation
gene: "CSRNP3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSRNP3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSRNP3 / CSRNP3 |
| 蛋白大小 | 585 aa / ~64.3 kDa |
| UniProt ID | Q8WYN3 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO chromatin/nucleus，chromatin-associated nuclear protein |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 585 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=3篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 59.8），36%有序，52%无序 |
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
| Protein Atlas (IF) | nucleoli rim (Approved, SH-SY5Y) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP3/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP3/IF_images/SH-SY5Y_2.jpg|SH-SY5Y]]

**结论**: UniProt Nucleus + GO chromatin/nucleus，chromatin-associated nuclear protein

#### 3.2 蛋白大小评估
**评价**: 585 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 3 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 3 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Huang Y et al. (2024). "Cancer-associated fibroblast-derived colony-stimulating factor 2 confers acquired osimertinib resistance in lung adenocarcinoma via promoting ribosome biosynthesis". *MedComm (2020)*. PMID: 39036343
2. Zhang H et al. (2021). "The CSRNP Gene Family Serves as a Prognostic Biomarker in Clear Cell Renal Cell Carcinoma". *Front Oncol*. PMID: 33869003
3. Campeau S et al. (2023). "Determination of steady-state transcriptome modifications associated with repeated homotypic stress in the rat rostral posterior hypothalamic region". *Front Neurosci*. PMID: 37360161
4. Wang K et al. (2021). "Genomic Analysis Reveals Human-Mediated Introgression From European Commercial Pigs to Henan Indigenous Pigs". *Front Genet*. PMID: 34220966
5. Mulari S et al. (2021). "Ischemic Heart Disease Selectively Modifies the Right Atrial Appendage Transcriptome". *Front Cardiovasc Med*. PMID: 34926599
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 59.8 |
| 有序区域 (pLDDT>70) 占比 | 36.5% |
| pLDDT>90 占比 | 25.6% |
| pLDDT<50 占比 | 51.8% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold预测置信度偏低（pLDDT 59.8，52%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:csrn3_human(display_long)|uniprotkb:CSRNP3(gene name)|psi-mi:CSRNP3(display_short)|uniprotkb:FAM130A2(gene name synonym)|uniprotkb:TAIP2(gene name synonym)|uniprotkb:Protein FAM130A2(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 2(gene name synonym) | psi-mi:"MI:0018"(two hybrid) | pubmed:17924338|imex:IM-27670 | 待分析 | 否 |


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
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 59.8），36%有序，52%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **71.0/100**

**核心优势**:
1. PubMed 3 篇，研究新颖性高
2. 蛋白大小 585 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYN3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CSRNP3%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CSRNP3&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CSRNP3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP3/CSRNP3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WYN3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031972;IPR023260; |
| Pfam | PF16019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178662-CSRNP3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
