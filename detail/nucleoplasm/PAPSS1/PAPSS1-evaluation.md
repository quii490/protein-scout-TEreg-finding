---
type: protein-evaluation
gene: "PAPSS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAPSS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAPSS1 / ATPSK1, PAPSS |
| 蛋白名称 | Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 1 |
| 蛋白大小 | 624 aa / 70.8 kDa |
| UniProt ID | O43252 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim, Mitotic chromosome; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 624 aa / 70.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.5; PDB: 1X6V, 1XJQ, 1XNJ, 2OFW, 2OFX, 2PEY, 2PEZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002891, IPR059117, IPR025980, IPR027417, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim, Mitotic chromosome; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATPSK1, PAPSS |

**关键文献**:
1. Human 3'-phosphoadenosine 5'-phosphosulfate synthetase 1 (PAPSS1) and PAPSS2: gene cloning, characterization and chromosomal localization.. *Biochemical and biophysical research communications*. PMID: 10679223
2. The PAPSS1 gene is a modulator of response to cisplatin by regulating estrogen receptor alpha signaling activity in ovarian cancer cells.. *Journal of ovarian research*. PMID: 37684671
3. Pharmacogenetics of human 3'-phosphoadenosine 5'-phosphosulfate synthetase 1 (PAPSS1): gene resequencing, sequence variation, and functional genomics.. *Biochemical pharmacology*. PMID: 12781330
4. Molecular mechanisms of recombinant proteins PTTG1IP, ADAM12, PAPSS1, and MYO1B and their effects on wound repair induced by tendon exposure: Analysis of key genes.. *International journal of biological macromolecules*. PMID: 39978508
5. Human DHEA sulfation requires direct interaction between PAPS synthase 2 and DHEA sulfotransferase SULT2A1.. *The Journal of biological chemistry*. PMID: 29743239

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 87.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 1X6V, 1XJQ, 1XNJ, 2OFW, 2OFX, 2PEY, 2PEZ, 2QJF, 8I1M |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1X6V, 1XJQ, 1XNJ, 2OFW, 2OFX, 2PEY, 2PEZ, 2QJF, 8I1M）+ AlphaFold极高置信度预测（pLDDT=93.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002891, IPR059117, IPR025980, IPR027417, IPR015947; Pfam: PF01583, PF01747, PF14306 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLAD1 | 0.990 | 0.602 | — |
| SUOX | 0.976 | 0.000 | — |
| IMPAD1 | 0.974 | 0.000 | — |
| BPNT1 | 0.972 | 0.000 | — |
| PAPSS2 | 0.951 | 0.448 | — |
| SLC26A2 | 0.925 | 0.000 | — |
| EEF1A1 | 0.921 | 0.074 | — |
| EEF1A2 | 0.919 | 0.000 | — |
| HBS1L | 0.909 | 0.000 | — |
| GSPT1 | 0.901 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q3U647 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1R16A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENSP00000265174.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SOCS3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PRKCE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| INPP5D | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| STAT5A | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 1X6V, 1XJQ, 1XNJ, 2OFW, 2OFX,  | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli rim, Mitotic chromosome; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PAPSS1 — Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小624 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43252
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138801-PAPSS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAPSS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43252
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (approved)。来源: https://www.proteinatlas.org/ENSG00000138801-PAPSS1/subcellular

![](https://images.proteinatlas.org/49781/1888_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/49781/1888_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/49781/721_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/49781/721_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/49781/733_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/49781/733_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43252-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
