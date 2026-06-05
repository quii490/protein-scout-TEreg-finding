---
type: protein-evaluation
gene: "HECTD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HECTD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HECTD1 / KIAA1131 |
| 蛋白名称 | E3 ubiquitin-protein ligase HECTD1 |
| 蛋白大小 | 2610 aa / 289.4 kDa |
| UniProt ID | Q9ULT8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2610 aa / 289.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 2DK3, 2LC3, 3DKM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR011989, IPR016024, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1131 |

**关键文献**:
1. α-Klotho prevents diabetic retinopathy by reversing the senescence of macrophages.. *Cell communication and signaling : CCS*. PMID: 39327553
2. HectD1 controls hematopoietic stem cell regeneration by coordinating ribosome assembly and protein synthesis.. *Cell stem cell*. PMID: 33711283
3. Sequence variants in HECTD1 result in a variable neurodevelopmental disorder.. *American journal of human genetics*. PMID: 39879987
4. HECTD1-Mediated Ubiquitination and Degradation of Rubicon Regulates Autophagy and Osteoarthritis Pathogenesis.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 36121967
5. HECTD1 regulates the expression of SNAIL: Implications for epithelial‑mesenchymal transition.. *International journal of oncology*. PMID: 32319576

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.7% |
| 置信残基 (pLDDT 70-90) 占比 | 49.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 26.6% |
| 有序区域 (pLDDT>70) 占比 | 64.3% |
| 可用 PDB 条目 | 2DK3, 2LC3, 3DKM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 64.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR011989, IPR016024, IPR041200; Pfam: PF12796, PF18410, PF00632 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZRANB1 | 0.745 | 0.688 | — |
| BIRC6 | 0.676 | 0.510 | — |
| UBR3 | 0.673 | 0.000 | — |
| TRIP12 | 0.641 | 0.000 | — |
| USP9X | 0.610 | 0.292 | — |
| ANKRD17 | 0.604 | 0.000 | — |
| ZNF622 | 0.587 | 0.549 | — |
| UBE2D3 | 0.556 | 0.510 | — |
| COPA | 0.554 | 0.510 | — |
| UBR4 | 0.541 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IGSF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| DDX56 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ZRANB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| UVRAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TFCP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| RIOK2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 2DK3, 2LC3, 3DKM | pLDDT=68.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HECTD1 — E3 ubiquitin-protein ligase HECTD1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2610 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULT8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092148-HECTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HECTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULT8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000092148-HECTD1/subcellular

![](https://images.proteinatlas.org/2929/103_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/2929/103_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/2929/104_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/2929/104_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/2929/1404_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/2929/1404_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULT8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
