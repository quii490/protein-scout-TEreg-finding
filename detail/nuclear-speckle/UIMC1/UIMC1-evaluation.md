---
type: protein-evaluation
gene: "UIMC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UIMC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UIMC1 / RAP80, RXRIP110 |
| 蛋白名称 | BRCA1-A complex subunit RAP80 |
| 蛋白大小 | 719 aa / 79.7 kDa |
| UniProt ID | Q96RL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 719 aa / 79.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.4; PDB: 2MKF, 2MKG, 2N9E, 2RR9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006642, IPR038868, IPR040714, IPR003903; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BRCA1-A complex (GO:0070531)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 116 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAP80, RXRIP110 |

**关键文献**:
1. Large-scale targeted sequencing identifies risk genes for neurodevelopmental disorders.. *Nature communications*. PMID: 33004838
2. AlphaFold2 SLiM screen for LC3-LIR interactions in autophagy.. *Autophagy*. PMID: 40320752
3. USP28 promotes PARP inhibitor resistance by enhancing SOX9-mediated DNA damage repair in ovarian cancer.. *Cell death & disease*. PMID: 40240356
4. Comprehensive analysis reveals COPB2 and RYK associated with tumor stages of larynx squamous cell carcinoma.. *BMC cancer*. PMID: 35715770
5. Identification of potential diagnostic gene biomarkers in patients with osteoarthritis.. *Scientific reports*. PMID: 32788627

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.4 |
| 高置信度残基 (pLDDT>90) 占比 | 12.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 19.2% |
| 低置信 (pLDDT<50) 占比 | 57.3% |
| 有序区域 (pLDDT>70) 占比 | 23.5% |
| 可用 PDB 条目 | 2MKF, 2MKG, 2N9E, 2RR9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.4），有序残基占 23.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006642, IPR038868, IPR040714, IPR003903; Pfam: PF18282 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BARD1 | 0.999 | 0.477 | — |
| BRCC3 | 0.999 | 0.994 | — |
| BABAM2 | 0.999 | 0.994 | — |
| BRCA1 | 0.999 | 0.994 | — |
| BABAM1 | 0.999 | 0.994 | — |
| ABRAXAS1 | 0.999 | 0.994 | — |
| MDC1 | 0.997 | 0.778 | — |
| UBC | 0.996 | 0.991 | — |
| SUMO2 | 0.995 | 0.978 | — |
| TP53BP1 | 0.985 | 0.455 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| INO80B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| H2AX | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-11889|pubmed:18001824 |
| BRCA1 | psi-mi:"MI:0096"(pull down) | pubmed:17525340|imex:IM-19729 |
| ABRAXAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17525340|imex:IM-19729 |
| RAD51 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:17525340|imex:IM-19729 |
| RBBP8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525340|imex:IM-19729 |
| BRCC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| AMOT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| BABAM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| G3BP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.4 + PDB: 2MKF, 2MKG, 2N9E, 2RR9 | pLDDT=55.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. UIMC1 — BRCA1-A complex subunit RAP80，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小719 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087206-UIMC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UIMC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000087206-UIMC1/subcellular

![](https://images.proteinatlas.org/37504/403_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/37504/403_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/37504/406_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/37504/406_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/37504/408_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/37504/408_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RL1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
