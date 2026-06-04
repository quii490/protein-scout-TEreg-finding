---
type: protein-evaluation
gene: "CCDC86"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC86 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC86 / CCDC86 |
| 蛋白大小 | 360 aa / ~39.6 kDa |
| UniProt ID | Q9H6F5 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | UniProt Nucleus+Nucleolus+Chromosome，GO chromosome/nucleolus，强核定位 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 360 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=13篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 61.5），29%有序，36%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 2/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome; Nucleus, nucleolus | — |
| GO Cellular Component | C:chromosome; C:nucleolus; C:nucleoplasm; C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC86/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC86/IF_images/A-431_2.jpg|A-431]]

**结论**: UniProt Nucleus+Nucleolus+Chromosome，GO chromosome/nucleolus，强核定位

#### 3.2 蛋白大小评估
**评价**: 360 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 13 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 13 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Replogle JM et al. (2022). "Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq". *Cell*. PMID: 35688146
2. Liu J et al. (2025). "CCDC86-BHLHE40-ATF3 axis promotes aerobic glycolysis and tumor development in glioma". *Genes Dis*. PMID: 40837407
3. Gao P et al. (2025). "Multi-omics identification of RNASE6 as an immune regulatory RNA-binding protein associated with melanoma metastasis". *Autoimmunity*. PMID: 41055424
4. Chen X et al. (2025). "Role of Coiled-Coil Domain-Containing Protein 86 in Tumorigenesis of Nasopharyngeal Carcinoma". *Bull Exp Biol Med*. PMID: 41196480
5. Stamatiou K et al. (2023). "CCDC86 is a novel Ki-67-interacting protein important for cell division". *J Cell Sci*. PMID: 36695333
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 61.5 |
| 有序区域 (pLDDT>70) 占比 | 28.6% |
| pLDDT>90 占比 | 13.3% |
| pLDDT<50 占比 | 36.1% |
| 可用 PDB 条目 | 10 |


**评价**: AlphaFold预测置信度偏低（pLDDT 61.5，36%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:odo2_human(display_long)|uniprotkb:DLST(gene name)|psi-mi:DLST(display_short)|uniprotkb:DLTS(gene name synonym)|uniprotkb:Dihydrolipoamide succinyltransferase component of 2-oxoglutarate dehydrogenase complex(gene name synonym)|uniprotkb:E2K(gene name synonym)|uniprotkb:2-oxoglutarate dehydrogenase complex component E2(gene name synonym) | psi-mi:"MI:0398"(two hybrid po | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | 待分析 | 否 |
| psi-mi:ccd86_human(display_long)|uniprotkb:Cytokine-induced protein with coiled-coil domain(gene name synonym)|uniprotkb:CYCLON(gene name synonym)|uniprotkb:CCDC86(gene name)|psi-mi:CCDC86(display_short) | psi-mi:"MI:0030"(cross-linking | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | 待分析 | 是 |
| psi-mi:ccd86_human(display_long)|uniprotkb:Cytokine-induced protein with coiled-coil domain(gene name synonym)|uniprotkb:CYCLON(gene name synonym)|uniprotkb:CCDC86(gene name)|psi-mi:CCDC86(display_short) | psi-mi:"MI:0030"(cross-linking | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | 待分析 | 是 |
| psi-mi:hsa-mir-92a-3p(display_short)|psi-mi:EBI-21019856(display_long) | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030|doi:10.1016/j.cell.2013.03.043 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MRTO4 | 0.777 | 待分析 | 否 |
| NSA2 | 0.769 | 待分析 | 否 |
| NIP7 | 0.655 | 待分析 | 否 |
| RRP9 | 0.626 | 待分析 | 否 |
| NHP2 | 0.594 | 待分析 | 否 |
| LYAR | 0.590 | 待分析 | 否 |
| ZCRB1 | 0.581 | 待分析 | 是 |
| BYSL | 0.564 | 待分析 | 否 |
| IL3 | 0.545 | 待分析 | 否 |
| H4C6 | 0.519 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:chromosome; C:nucleolus; C:nucleoplasm; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 2/30 (7%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作4个，调控关联2个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 61.5），29%有序，36%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus; Chromosome; Nucleus, nucleolus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**归一化总分**: **76.5/100**

**核心优势**:
1. PubMed 13 篇，研究新颖性高
2. 蛋白大小 360 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6F5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6F5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CCDC86%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CCDC86&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CCDC86


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCDC86/CCDC86-PAE.png]]




