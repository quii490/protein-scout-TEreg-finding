---
type: protein-evaluation
gene: "NMRK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NMRK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NMRK2 / ITGB1BP3, NRK2 |
| 蛋白名称 | Nicotinamide riboside kinase 2 |
| 蛋白大小 | 230 aa / 26.0 kDa |
| UniProt ID | Q9NPI5 |
| 数据采集时间 | 2026-06-03 23:49:41 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 230 aa / 26.0 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (21-40 -> 8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR027417; Pfam: PF13238 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ITGB1BP3, NRK2 |

**关键文献**:
1. Nicotinamide Riboside Preserves Cardiac Function in a Mouse Model of Dilated Cardiomyopathy.. *Circulation*. PMID: 29217642
2. NMRK2-YAP-NADK axis preserves redox protection against myocardial ischemia/reperfusion injury.. *Redox biology*. PMID: 41762891
3. Aged Nicotinamide Riboside Kinase 2 Deficient Mice Present an Altered Response to Endurance Exercise Training.. *Frontiers in physiology*. PMID: 30283350
4. NMRK2 Gene Is Upregulated in Dilated Cardiomyopathy and Required for Cardiac Function and NAD Levels during Aging.. *International journal of molecular sciences*. PMID: 33805532
5. NMRK2 is an efficient diagnostic indicator for Xp11.2 translocation renal cell carcinoma.. *The Journal of pathology*. PMID: 39092712

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 73.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 83.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417; Pfam: PF13238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAPRT | 0.965 | 0.116 | — |
| NMNAT1 | 0.963 | 0.000 | — |
| QPRT | 0.952 | 0.000 | — |
| NMNAT2 | 0.951 | 0.000 | — |
| NAMPT | 0.947 | 0.000 | — |
| PNP | 0.942 | 0.115 | — |
| NMRK1 | 0.910 | 0.000 | — |
| NUDT12 | 0.901 | 0.053 | — |
| ENPP1 | 0.901 | 0.000 | — |
| ENPP3 | 0.901 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRP12 | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| CDKN1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SAT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NMRK2 -- Nicotinamide riboside kinase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPI5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000077009-NMRK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NMRK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPI5
- STRING: https://string-db.org/network/9606.NMRK2
- Packet data timestamp: 2026-06-03 23:49:41

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000077009-NMRK2/subcellular

![](https://images.proteinatlas.org/49909/1361_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/49909/1361_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/49909/1520_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/49909/1520_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/54792/1452_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/54792/1452_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPI5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
