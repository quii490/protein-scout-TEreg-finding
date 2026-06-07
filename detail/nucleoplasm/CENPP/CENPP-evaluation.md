---
type: protein-evaluation
gene: "CENPP"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPP / CENPP |
| 蛋白大小 | 288 aa / ~31.7 kDa |
| UniProt ID | Q6IPU0 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | UniProt Nucleus+Centromere + GO kinetochore/nucleoplasm，着丝粒蛋白 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 288 aa，200-800 aa最优区间，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=16篇 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | 高质量（pLDDT 85.0），84%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 | 0/30调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **155/183** |  |
| **归一化总分** |  |  | **84.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus; Chromosome, centromere | — |
| GO Cellular Component | C:cytosol; C:inner kinetochore; C:nucleolus; C:nucleoplasm; C:nucleus | — |
| Protein Atlas (IF) | nucleoplasm+nucleoli (Approved, Rh30) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPP/IF_images/Rh30_1.jpg|Rh30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPP/IF_images/Rh30_2.jpg|Rh30]]

**结论**: UniProt Nucleus+Centromere + GO kinetochore/nucleoplasm，着丝粒蛋白

#### 3.2 蛋白大小评估
**评价**: 288 aa，200-800 aa最优区间，适合生化实验和结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 16 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 16 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Su XT et al. (2024). "Enriched Single-Nucleus RNA-Sequencing Reveals Unique Attributes of Distal Convoluted Tubule Cells". *J Am Soc Nephrol*. PMID: 38238903
2. Kitaba NT et al. (2023). "Fathers' preconception smoking and offspring DNA methylation". *Clin Epigenetics*. PMID: 37649101
3. Hu W et al. (2024). "Immunomodulatory effect of Atractylodis macrocephala Koidz. polysaccharides in vitro". *Poult Sci*. PMID: 37925772
4. Zhang Z et al. (2022). "Exploring a four-gene risk model based on doxorubicin resistance-associated lncRNAs in hepatocellular carcinoma". *Front Pharmacol*. PMID: 36457707
5. Chen H et al. (2021). "A nomogram based on CENPP expression for survival prediction in breast cancer". *Gland Surg*. PMID: 34268072
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 85.0 |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| pLDDT>90 占比 | 58.3% |
| pLDDT<50 占比 | 10.1% |
| 可用 PDB 条目 | 9 |


**评价**: PDB实验结构+AlphaFold高质量预测（pLDDT 85.0，84%有序），结构可信度极高。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:k1328_human(display_long)|uniprotkb:KIAA1328(gene name)|psi-mi:KIAA1328(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:cenpo_human(display_long)|uniprotkb:Interphase centromere complex protein 36(gene name synonym)|uniprotkb:CENPO(gene name)|psi-mi:CENPO(display_short)|uniprotkb:MCM21R(gene name synonym)|uniprotkb:ICEN36(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:cenpp_human(display_long)|uniprotkb:CENPP(gene name)|psi-mi:CENPP(display_short) | psi-mi:"MI:1112"(two hybrid pr | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:"ccsb orf id: 8359"(display_short)|psi-mi:EBI-16439879(display_long) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |
| psi-mi:cenpp_human(display_long)|uniprotkb:CENPP(gene name)|psi-mi:CENPP(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 否 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CENPU | 0.999 | 待分析 | 否 |
| CENPQ | 0.999 | 待分析 | 否 |
| ITGB3BP | 0.999 | 待分析 | 否 |
| CENPH | 0.999 | 待分析 | 否 |
| CENPO | 0.999 | 待分析 | 否 |
| CENPN | 0.999 | 待分析 | 否 |
| CENPI | 0.999 | 待分析 | 否 |
| CENPK | 0.998 | 待分析 | 否 |
| CENPM | 0.998 | 待分析 | 否 |
| CENPL | 0.998 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:cytosol; C:inner kinetochore; C:nucleolus; C:nucleoplasm; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 30 个伙伴
- 调控相关比例: 0/30 (0%)

**评价**: PPI网络以功能关联为主（30个STRING伙伴），物理互作104个，调控关联0个。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 高质量（pLDDT 85.0），84%有序 | 待验证 |
| 定位 | UniProt + GO | Nucleus; Chromosome, centromere | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**归一化总分**: **83.1/100**

**核心优势**:
1. PubMed 16 篇，研究新颖性高
2. 蛋白大小 288 aa，适合生化实验

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IPU0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IPU0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CENPP%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CENPP&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CENPP


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPP/CENPP-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6IPU0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027801; |
| Pfam | PF13096; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188312-CENPP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENPO | Intact, Biogrid, Bioplex | true |
| CENPQ | Biogrid, Bioplex | true |
| CENPU | Biogrid, Bioplex | true |
| ATP6V0D2 | Intact | false |
| BACH2 | Intact | false |
| C2orf88 | Intact | false |
| CCDC85B | Intact | false |
| CENPH | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
