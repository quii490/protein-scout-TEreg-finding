---
type: protein-evaluation
gene: "EEF1AKMT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EEF1AKMT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF1AKMT3 / FAM119B, HCA557A, METTL21B |
| 蛋白名称 | EEF1A lysine methyltransferase 3 |
| 蛋白大小 | 226 aa / 24.9 kDa |
| UniProt ID | Q96AZ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing c |
| 蛋白大小 | 10/10 | ×1 | 10 | 226 aa / 24.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.0; PDB: 4QPN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019410, IPR029063; Pfam: PF10294 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Nucleoplasm, Mitotic chromosome | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM119B, HCA557A, METTL21B |

**关键文献**:
1. Endothelial RIPK1 protects artery bypass graft against arteriosclerosis by regulating SMC growth.. *Science advances*. PMID: 37647392
2. SETD2 regulates the methylation of translation elongation factor eEF1A1 in clear cell renal cell carcinoma.. *Kidney cancer journal : official journal of the Kidney Cancer Association*. PMID: 36684483
3. Early response to heat stress in Chinese tongue sole (Cynoglossus semilaevis): performance of different sexes, candidate genes and networks.. *BMC genomics*. PMID: 33109079
4. METTL21B Is a Novel Human Lysine Methyltransferase of Translation Elongation Factor 1A: Discovery by CRISPR/Cas9 Knockout.. *Molecular & cellular proteomics : MCP*. PMID: 28663172
5. The EEF1AKMT3/MAP2K7/TP53 axis suppresses tumor invasiveness and metastasis in gastric cancer.. *Cancer letters*. PMID: 35753528

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 88.1% |
| 可用 PDB 条目 | 4QPN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.0，有序区 88.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019410, IPR029063; Pfam: PF10294 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSFM | 0.738 | 0.000 | — |
| EEF1AKMT1 | 0.685 | 0.000 | — |
| METTL1 | 0.663 | 0.000 | — |
| EEF1AKMT2 | 0.663 | 0.000 | — |
| ETFBKMT | 0.646 | 0.065 | — |
| METTL18 | 0.600 | 0.000 | — |
| HSP90AB1 | 0.566 | 0.292 | — |
| HSP90AA1 | 0.562 | 0.292 | — |
| CSKMT | 0.538 | 0.000 | — |
| KIN | 0.520 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEB4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| VAC14 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MSRB3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZIC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ALS2CL | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMCHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZSWIM8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ESPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RTCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PIK3C2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 4QPN | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, microtubule or / Centrosome; 额外: Nucleoplasm, Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EEF1AKMT3 — EEF1A lysine methyltransferase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小226 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AZ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123427-EEF1AKMT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF1AKMT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AZ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000123427-EEF1AKMT3/subcellular

![](https://images.proteinatlas.org/45492/1806_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45492/1806_A5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45492/1846_D6_26_cr5abb6eb75d307_blue_red_green.jpg)
![](https://images.proteinatlas.org/45492/1846_D6_7_cr5abb6eb75d0d4_blue_red_green.jpg)
![](https://images.proteinatlas.org/45492/1870_E2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/45492/1870_E2_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AZ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
