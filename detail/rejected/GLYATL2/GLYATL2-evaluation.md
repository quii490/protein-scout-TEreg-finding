---
type: protein-evaluation
gene: "GLYATL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLYATL2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLYATL2 |
| 蛋白名称 | Glycine N-acyltransferase-like protein 2 |
| 蛋白大小 | 294 aa / 34.3 kDa |
| UniProt ID | Q8WU03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 34.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR010313, IPR013652, IPR015938; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A Circadian Rhythm-related Signature to Predict Prognosis, Immune Infiltration, and Drug Response in Breast Cancer.. *Current medicinal chemistry*. PMID: 39279697
2. The critical roles of lnc-GLYATL2-2/PD-L1 axis in immune microenvironment and the clinical value of intracranial chordomas.. *American journal of cancer research*. PMID: 38187065
3. A novel gene signature related to fatty acid metabolism predicts prognosis, immune landscape, and drug sensitivity in early-stage lung squamous cell carcinoma.. *Translational cancer research*. PMID: 38482436
4. Deciphering the Transcriptomic Complexity of Yak Skin Across Different Ages and Body Sites.. *International journal of molecular sciences*. PMID: 40429746
5. Identification of glycine N-acyltransferase-like 2 (GLYATL2) as a transferase that produces N-acyl glycines in humans.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 20305126

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.8 |
| 高置信度残基 (pLDDT>90) 占比 | 77.2% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.8，有序区 89.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR010313, IPR013652, IPR015938; Pfam: PF08444, PF06021 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MUCL1 | 0.537 | 0.000 | — |
| CDK1 | 0.451 | 0.301 | — |
| CCNB1 | 0.422 | 0.279 | — |
| CDK15 | 0.422 | 0.301 | — |
| CDK17 | 0.421 | 0.301 | — |
| CDK16 | 0.421 | 0.301 | — |
| CLDN25 | 0.421 | 0.301 | — |
| CDK3 | 0.421 | 0.301 | — |
| CDK6 | 0.421 | 0.301 | — |
| CDK4 | 0.421 | 0.301 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.8 + PDB: 无 | pLDDT=89.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLYATL2 — Glycine N-acyltransferase-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WU03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156689-GLYATL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLYATL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WU03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000156689-GLYATL2/subcellular

![](https://images.proteinatlas.org/65454/1543_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65454/1543_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65454/1544_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65454/1544_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65454/1559_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65454/1559_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WU03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
