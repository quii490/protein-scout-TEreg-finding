---
type: protein-evaluation
gene: "SKAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKAP1 / SCAP1, SKAP55 |
| 蛋白名称 | Src kinase-associated phosphoprotein 1 |
| 蛋白大小 | 359 aa / 41.4 kDa |
| UniProt ID | Q86WV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 41.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.6; PDB: 1U5D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR036028, IPR001452, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell-cell junction (GO:0005911)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- immunological synapse (GO:0001772)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- plasma membrane raft (GO:0044853)
- T cell receptor complex (GO:0042101)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 106 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCAP1, SKAP55 |

**关键文献**:
1. SKAP1 Expression in Cancer Cells Enhances Colon Tumor Growth and Impairs Cytotoxic Immunity by Promoting Neutrophil Extracellular Trap Formation via the NFATc1/CXCL8 Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39269257
2. Multi-functional adaptor SKAP1: regulator of integrin activation, the stop-signal, and the proliferation of T cells.. *Frontiers in immunology*. PMID: 37325633
3. The Multiple Roles of the Cytosolic Adapter Proteins ADAP, SKAP1 and SKAP2 for TCR/CD3 -Mediated Signaling Events.. *Frontiers in immunology*. PMID: 34295339
4. Integrative Analysis of TLS-Associated Gene Signatures, Immune Infiltration and Drug Sensitivity in Pancreatic Cancer.. *IET systems biology*. PMID: 41016829
5. Role of two modules controlling the interaction between SKAP1 and SRC kinases comparison with SKAP2 architecture and consequences for evolution.. *PloS one*. PMID: 38483858

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 27.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 30.4% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 1U5D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.6），有序残基占 59.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR036028, IPR001452, IPR035765; Pfam: PF00169, PF14604 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FYB1 | 0.998 | 0.803 | — |
| LCP2 | 0.987 | 0.074 | — |
| APBB1IP | 0.981 | 0.000 | — |
| FYN | 0.972 | 0.735 | — |
| LCK | 0.935 | 0.510 | — |
| RAP1A | 0.925 | 0.000 | — |
| RAP1B | 0.911 | 0.000 | — |
| GRB2 | 0.850 | 0.292 | — |
| ZAP70 | 0.845 | 0.000 | — |
| RASSF5 | 0.831 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FYB1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |
| Lcp2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-25620|pubmed:24584089 |
| PRAM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EEIG1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BLCAP | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SH2D4A | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| MYO9A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIK3R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCP110 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.6 + PDB: 1U5D | pLDDT=69.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nucleoplasm, Plasma membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SKAP1 — Src kinase-associated phosphoprotein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141293-SKAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000141293-SKAP1/subcellular

![](https://images.proteinatlas.org/2969/1787_H4_24_cr5968c4f252599_blue_red_green.jpg)
![](https://images.proteinatlas.org/2969/1787_H4_7_cr5968c4f251dc0_blue_red_green.jpg)
![](https://images.proteinatlas.org/2969/77_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2969/77_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2969/92_D4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2969/92_D4_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86WV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
