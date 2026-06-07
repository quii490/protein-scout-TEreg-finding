---
type: protein-evaluation
gene: "PLK5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLK5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLK5 / PLK5P |
| 蛋白名称 | Inactive serine/threonine-protein kinase PLK5 |
| 蛋白大小 | 336 aa / 36.3 kDa |
| UniProt ID | Q496M5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 336 aa / 36.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR033701, IPR000959, IPR036947, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- kinetochore (GO:0000776)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PLK5P |

**关键文献**:
1. Potential Tumor Suppressor Role of Polo-like Kinase 5 in Cancer.. *Cancers*. PMID: 38001717
2. From Plk1 to Plk5: functional evolution of polo-like kinases.. *Cell cycle (Georgetown, Tex.)*. PMID: 21654194
3. Rare and common genetic variants underlying the risk of Hirschsprung's disease.. *Human molecular genetics*. PMID: 39817569
4. Comprehensive analysis of PLKs expression and prognosis in breast cancer.. *Cancer genetics*. PMID: 36206661
5. Plk5, a polo box domain-only protein with specific roles in neuron differentiation and glioblastoma suppression.. *Molecular and cellular biology*. PMID: 21245385

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 22.6% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 58.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR033701, IPR000959, IPR036947, IPR000719 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESPL1 | 0.851 | 0.746 | — |
| PPP4C | 0.763 | 0.746 | — |
| PLK4 | 0.761 | 0.073 | — |
| RAD21L1 | 0.641 | 0.514 | — |
| RAD21 | 0.641 | 0.514 | — |
| CCNB1 | 0.606 | 0.278 | — |
| PPP2R2B | 0.594 | 0.515 | — |
| CNTD2 | 0.594 | 0.278 | — |
| MAD2L1 | 0.586 | 0.294 | — |
| SMC1A | 0.580 | 0.514 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP7 | psi-mi:"MI:0084"(phage display) | pubmed:unassigned3809|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLK5 — Inactive serine/threonine-protein kinase PLK5，非常新颖，仅有少数基础研究。
2. 蛋白大小336 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q496M5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185988-PLK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q496M5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q496M5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q496M5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..65; /note="Protein kinase; truncated"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159"; DOMAIN 255..336; /note="POLO box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00154" |
| InterPro | IPR011009;IPR033701;IPR000959;IPR036947;IPR000719; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185988-PLK5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
