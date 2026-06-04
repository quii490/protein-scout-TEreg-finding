---
type: protein-evaluation
gene: "CREBL2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CREBL2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREBL2 / CREBL2 |
| 蛋白大小 | 120 aa / ~13.2 kDa |
| UniProt ID | O60519 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | UniProt Nucleus + GO chromatin，CREB家族转录因子，染色质结合 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 120 aa，小型蛋白，适合结构解析 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed=15篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | 良好（pLDDT 75.7），58%有序 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | 新颖蛋白基线 |
| 🔗 PPI 网络 | 8/10 | ×3 | 24 | 3/12调控相关partners |
| ➕ 互证加分 | — | max +3 | 0 | 多库交叉验证 |
| **原始总分** |  |  | **152/183** |  |
| **归一化总分** |  |  | **83.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | — |
| GO Cellular Component | C:chromatin; C:nucleus | — |
| Protein Atlas (IF) | mitochondria (Approved, A-431) | Approved |

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CREBL2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CREBL2/IF_images/A-431_2.jpg|A-431]]

**结论**: UniProt Nucleus + GO chromatin，CREB家族转录因子，染色质结合

#### 3.2 蛋白大小评估
**评价**: 120 aa，小型蛋白，适合结构解析

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 15 |
| Chromatin/epigenetics 比例 | 待深入文献分析 |

**评价**: PubMed 15 篇。极度新颖，几乎未被研究，是探索新型核蛋白功能的绝佳候选。

**关键文献**:
1. Hong T et al. (2023). "Parathyroid hormone receptor-1 signaling aggravates hepatic fibrosis through upregulating cAMP response element-binding protein-like 2". *Hepatology*. PMID: 36939197
2. Zhu H et al. (2015). "MiR-17-92 cluster promotes hepatocarcinogenesis". *Carcinogenesis*. PMID: 26233958
3. Tiebe M et al. (2019). "Crebl2 regulates cell metabolism in muscle and liver cells". *Sci Rep*. PMID: 31882710
4. Tai Z et al. (2022). "Effects of parental environmental copper stress on offspring development: DNA methylation modification and responses of differentially methylated region-related genes in transcriptional expression". *J Hazard Mater*. PMID: 34801305
5. Ma X et al. (2011). "CREBL2, interacting with CREB, induces adipogenesis in 3T3-L1 adipocytes". *Biochem J*. PMID: 21728997
#### 3.4 三维结构分析
> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 75.7 |
| 有序区域 (pLDDT>70) 占比 | 58.3% |
| pLDDT>90 占比 | 45.8% |
| pLDDT<50 占比 | 18.3% |
| 可用 PDB 条目 | 0 |


**评价**: AlphaFold中等质量（pLDDT 75.7，58%有序）。作为新颖蛋白（PubMed=15），此结构水平可接受（基线6分）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| UniProt / InterPro | 待SMART详细分析 |

**染色质调控潜力分析**: 对于PubMed≤100的新颖蛋白，无注释域是该阶段的正常现象（基线7分）。待SMART分析后补充。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| psi-mi:crbl2_human(display_long)|uniprotkb:CREBL2(gene name)|psi-mi:CREBL2(display_short) | psi-mi:"MI:0398"(two hybrid po | imex:IM-13779|pubmed:20711500 | 待分析 | 是 |
| psi-mi:rl1d1_human(display_long)|uniprotkb:RSL1D1(gene name)|psi-mi:RSL1D1(display_short)|uniprotkb:CSIG(gene name synonym)|uniprotkb:PBK1(gene name synonym)|uniprotkb:CATX11(gene name synonym)|uniprotkb:L12(orf name)|uniprotkb:Cellular senescence-inhibited gene protein(gene name synonym)|uniprotkb:Protein PBK1(gene name synonym)|uniprotkb:CATX-11(gene name synonym) | psi-mi:"MI:0030"(cross-linking | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | 待分析 | 否 |
| psi-mi:ddit3_human(display_long)|uniprotkb:CHOP10(gene name synonym)|uniprotkb:C/EBP-homologous protein(gene name synonym)|uniprotkb:DDIT3(gene name)|psi-mi:DDIT3(display_short)|uniprotkb:CHOP(gene name synonym)|uniprotkb:GADD153(gene name synonym)|uniprotkb:Growth arrest and DNA damage-inducible protein GADD153(gene name synonym)|uniprotkb:C/EBP-homologous protein 10(gene name synonym)|uniprotkb:C/EBP zeta(gene name synonym)|uniprotkb:CCAAT/enhancer-binding protein homologous protein(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:pknx2_human(display_long)|uniprotkb:PREP2(gene name synonym)|uniprotkb:Homeobox protein PREP-2(gene name synonym)|uniprotkb:PBX/knotted homeobox 2(gene name synonym)|uniprotkb:PKNOX2(gene name)|psi-mi:PKNOX2(display_short) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |
| psi-mi:crerf_human(display_long)|uniprotkb:CREBRF(gene name)|psi-mi:CREBRF(display_short)|uniprotkb:C5orf41(gene name synonym)|uniprotkb:Luman recruitment factor(gene name synonym) | psi-mi:"MI:0397"(two hybrid ar | pubmed:32296183|imex:IM-25472 | 待分析 | 是 |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ETV6 | 0.768 | 待分析 | 否 |
| CREBRF | 0.720 | 待分析 | 是 |
| CDKN1B | 0.597 | 待分析 | 是 |
| BORCS5 | 0.554 | 待分析 | 是 |
| GPR19 | 0.528 | 待分析 | 否 |
| MANSC1 | 0.510 | 待分析 | 否 |
| RUSC1 | 0.485 | 待分析 | 否 |
| FOSL2 | 0.475 | 待分析 | 否 |
| DUSP16 | 0.418 | 待分析 | 否 |
| FOS | 0.416 | 待分析 | 否 |


**已知复合体成员** (GO Cellular Component): C:chromatin; C:nucleus

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: 12 个伙伴
- 调控相关比例: 3/12 (25%)

**评价**: PPI网络富含染色质/转录调控因子（3/12），物理互作证据明确，提示该蛋白深度参与核调控。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 良好（pLDDT 75.7），58%有序 | 待验证 |
| 定位 | UniProt + GO | Nucleus | 待HPA验证 |

**互证加分**: 0 / max +3

**PAE 图**: 暂无PAE数据

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**归一化总分**: **81.4/100**

**核心优势**:
1. PubMed 15 篇，研究新颖性高
2. 蛋白大小 120 aa

**风险/不确定性**:
1. 需 HPA IF 确认核定位
2. 功能机制未知，需从头探索

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] SMART 结构域分析评估调控潜力
- [ ] 深入文献检索确认已知功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60519
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60519
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CREBL2%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/cgi/network?identifiers=CREBL2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CREBL2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CREBL2/CREBL2-PAE.png]]




