---
type: protein-evaluation
gene: "CSRNP1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSRNP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSRNP1 / CSRNP1 |
| 蛋白大小 | 589 aa / ~64.8 kDa |
| UniProt ID | Q96S65 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO chromatin/nucleus，CSRNP家族核蛋白 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 589 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed=37篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | 中等（pLDDT 58.3），35%有序，55%无序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 1/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:chromatin; C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP1/IF_images/A-431_2.jpg|A-431]]

**结论**: UniProt Nucleus + GO chromatin/nucleus，CSRNP家族核蛋白

#### 3.2 蛋白大小评估
**评价**: 589 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 37 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 37 篇。非常新颖，研究空间充足。

**关键文献**:
1. Wang Z et al. (2024). "Inhibition of cysteine-serine-rich nuclear protein 1 ameliorates ischemia-reperfusion injury during liver transplantation in an MAPK-dependent manner". *Mol Biomed*. PMID: 38902590
2. Pang J et al. (2022). "Integrating Single-cell RNA-seq to construct a Neutrophil prognostic model for predicting immune responses in non-small cell lung cancer". *J Transl Med*. PMID: 36401283
3. Maissan P & Carlberg C (2025). "Circadian Regulation of Vitamin D Target Genes Reveals a Network Shaped by Individual Responsiveness". *Nutrients*. PMID: 40218962
4. Zhu J et al. (2024). "Silencing of cysteine and serine rich nuclear protein 1 inhibits apoptosis, senescence and collagen degradation in human-derived vaginal fibroblasts in response to oxidative stress or DNA damage". *Exp Cell Res*. PMID: 38908423
5. Geng X et al. (2022). "Whole transcriptome sequencing reveals neutrophils' transcriptional landscape associated with active tuberculosis". *Front Immunol*. PMID: 36059536
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 58.3 |
| 有序区域 (pLDDT>70) 占比 | 35.3% |
| pLDDT>90 占比 | 22.6% |
| pLDDT<50 占比 | 55.3% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold预测置信度偏低（pLDDT 58.3，55%无序）。作为新颖蛋白，正常现象，不扣分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:csrn1_human(display_long)|uniprotkb:CSRNP1(gene name)|psi-mi:CSRNP1(display_short)|uniprotkb:AXUD1(gene name synonym)|uniprotkb:TAIP3(gene name synonym)|uniprotkb:Axin-1 up-regulated gene 1 protein(gene name synonym)|uniprotkb:Protein URAX1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 3(gene name synonym) | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 | 待分析 | 否 |
| psi-mi:p36873-2(display_long)|uniprotkb:Protein phosphatase 1C catalytic subunit(gene name synonym)|uniprotkb:PPP1CC(gene name)|psi-mi:PPP1CC(display_short)|uniprotkb:Gamma-2(isoform synonym)|uniprotkb:PPPCC2(isoform synonym) | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 | 待分析 | 否 |
| psi-mi:csrn1_human(display_long)|uniprotkb:CSRNP1(gene name)|psi-mi:CSRNP1(display_short)|uniprotkb:AXUD1(gene name synonym)|uniprotkb:TAIP3(gene name synonym)|uniprotkb:Axin-1 up-regulated gene 1 protein(gene name synonym)|uniprotkb:Protein URAX1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 3(gene name synonym) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:pp1b_human(display_long)|uniprotkb:PPP1CB(gene name)|psi-mi:PPP1CB(display_short) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:csrn1_human(display_long)|uniprotkb:CSRNP1(gene name)|psi-mi:CSRNP1(display_short)|uniprotkb:AXUD1(gene name synonym)|uniprotkb:TAIP3(gene name synonym)|uniprotkb:Axin-1 up-regulated gene 1 protein(gene name synonym)|uniprotkb:Protein URAX1(gene name synonym)|uniprotkb:TGF-beta-induced apoptosis protein 3(gene name synonym) | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| GADD45B | 0.858 | 待分析 | 否 |
| MSX1 | 0.845 | 待分析 | 否 |
| PAX7 | 0.690 | 待分析 | 否 |
| PPP1R15A | 0.684 | 待分析 | 否 |
| FOSB | 0.678 | 待分析 | 否 |
| AXIN1 | 0.675 | 待分析 | 否 |
| PPP1CA | 0.666 | 待分析 | 否 |
| JUNB | 0.660 | 待分析 | 否 |
| ZFP36 | 0.659 | 待分析 | 否 |
| PPP1CB | 0.599 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:chromatin; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 1/30 (3%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作35个，调控关联1个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 中等（pLDDT 58.3），35%有序，55%无序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**归一化总分**: **68.9/100**

**核心优势**:
1. PubMed 37 篇，研究新颖性高
2. 蛋白大小 589 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96S65
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96S65
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CSRNP1%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CSRNP1&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CSRNP1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRNP1/CSRNP1-PAE.png]]




