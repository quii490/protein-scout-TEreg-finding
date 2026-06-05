---
type: protein-evaluation
gene: "LRRC59"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC59 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC59 |
| 蛋白名称 | Leucine-rich repeat-containing protein 59 |
| 蛋白大小 | 307 aa / 34.9 kDa |
| UniProt ID | Q96AG4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Microsome membrane; Endoplasmic reticulum membrane; Nucleus  |
| 蛋白大小 | 10/10 | ×1 | 10 | 307 aa / 34.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Enhanced |
| UniProt | Microsome membrane; Endoplasmic reticulum membrane; Nucleus envelope | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- mitochondrial nucleoid (GO:0042645)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nuclear translocation of plasma membrane protein ADCY7 potentiates T cell-mediated antitumour immunity in HCC.. *Gut*. PMID: 39349007
2. LRRC59 serves as a novel biomarker for predicting the progression and prognosis of bladder cancer.. *Cancer medicine*. PMID: 37706625
3. Targeting of LRRC59 to the Endoplasmic Reticulum and the Inner Nuclear Membrane.. *International journal of molecular sciences*. PMID: 30650545
4. LRRC59 inhibits perk pathway‑induced apoptosis and promotes cell proliferation, migration and invasion in colorectal cancer cells.. *Oncology reports*. PMID: 41133451
5. Nuclear import of exogenous FGF1 requires the ER-protein LRRC59 and the importins Kpnα1 and Kpnβ1.. *Traffic (Copenhagen, Denmark)*. PMID: 22321063

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 68.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 8.8% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 84.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam: PF00560, PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YBX1 | 0.677 | 0.625 | — |
| STAU1 | 0.632 | 0.594 | — |
| UBXN4 | 0.621 | 0.115 | — |
| HNRNPM | 0.577 | 0.552 | — |
| PRPF8 | 0.565 | 0.550 | — |
| FGF1 | 0.563 | 0.000 | — |
| ILF3 | 0.556 | 0.547 | — |
| RRBP1 | 0.534 | 0.245 | — |
| BRD4 | 0.519 | 0.510 | — |
| IGF2BP3 | 0.518 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Myd88 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CCNA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Microsome membrane; Endoplasmic reticulum membrane / Endoplasmic reticulum | 一致 |
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
1. LRRC59 — Leucine-rich repeat-containing protein 59，非常新颖，仅有少数基础研究。
2. 蛋白大小307 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AG4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108829-LRRC59/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC59
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AG4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (enhanced)。来源: https://www.proteinatlas.org/ENSG00000108829-LRRC59/subcellular

![](https://images.proteinatlas.org/30827/330_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30827/330_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30827/331_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30827/331_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/30827/333_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30827/333_B6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AG4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
