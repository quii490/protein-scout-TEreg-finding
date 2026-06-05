---
type: protein-evaluation
gene: "TSSK6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSSK6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSSK6 / SSTK |
| 蛋白名称 | Testis-specific serine/threonine-protein kinase 6 |
| 蛋白大小 | 273 aa / 30.3 kDa |
| UniProt ID | Q9BXA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Cytoplasm, cytoskeleton, flagellum axoneme; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 30.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axonemal microtubule doublet inner sheath (GO:0160110)
- nucleus (GO:0005634)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SSTK |

**关键文献**:
1. Integrative genomic and single-cell framework identifies druggable targets for colorectal cancer precision therapy.. *Frontiers in immunology*. PMID: 40496862
2. Identification of Potential Drug Targets for Myopia Through Mendelian Randomization.. *Investigative ophthalmology & visual science*. PMID: 39110588
3. TSSK6 is required for γH2AX formation and the histone-to-protamine transition during spermiogenesis.. *Journal of cell science*. PMID: 28389581
4. Tssk6 is essential for the regulation of male zebrafish fertility.. *Theriogenology*. PMID: 40570569
5. Doublet microtubule-associated tektins and enzymes differentially regulate sperm flagellar integrity and motility.. *Nature communications*. PMID: 41764189

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.5，有序区 98.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR042710; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90AB1 | 0.863 | 0.634 | — |
| TNP1 | 0.818 | 0.000 | — |
| HSP90AA1 | 0.760 | 0.613 | — |
| TSKS | 0.725 | 0.000 | — |
| IZUMO1 | 0.666 | 0.000 | — |
| SPEM1 | 0.629 | 0.000 | — |
| HSPA4 | 0.621 | 0.303 | — |
| SPACA6 | 0.621 | 0.052 | — |
| OAZ3 | 0.615 | 0.000 | — |
| HSPA8 | 0.612 | 0.314 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15870294 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15870294 |
| HSPA1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15870294 |
| B2R9F8 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:15870294 |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| FKBP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 无 | pLDDT=93.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, flagellum axoneme; Nucleu / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSSK6 — Testis-specific serine/threonine-protein kinase 6，非常新颖，仅有少数基础研究。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178093-TSSK6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSSK6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (uncertain)。来源: https://www.proteinatlas.org/ENSG00000178093-TSSK6/subcellular

![](https://images.proteinatlas.org/65281/1445_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/65281/1445_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/65281/1450_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/65281/1450_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/65281/1520_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/65281/1520_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXA6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
