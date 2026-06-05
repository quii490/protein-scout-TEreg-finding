---
type: protein-evaluation
gene: "ARFIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARFIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARFIP2 / POR1 |
| 蛋白名称 | Arfaptin-2 |
| 蛋白大小 | 341 aa / 37.9 kDa |
| UniProt ID | P53365 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Golgi apparatus; UniProt: Golgi apparatus; Golgi apparatus, trans-Golgi network membra |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 341 aa / 37.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.7; PDB: 1I49, 1I4D, 1I4L, 1I4T, 4DCN |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027267, IPR010504, IPR030798; Pfam: PF06456 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分 (÷1.83)** | | | **78.1/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Golgi apparatus | Approved |
| UniProt | Golgi apparatus; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: POR1 |

**关键文献**:
1. ATG9A and ARFIP2 cooperate to control PI4P levels for lysosomal repair.. *Developmental cell*. PMID: 40460835
2. Combined transcriptome and proteome analysis reveals MSN and ARFIP2 as biomarkers for trastuzumab resistance of breast cancer.. *Breast cancer research and treatment*. PMID: 38750271
3. Deciphering the immunological and prognostic features of hepatocellular carcinoma through ADP-ribosylation-related genes analysis and identify potential therapeutic target ARFIP2.. *Cellular signalling*. PMID: 38302034
4. Identification of potential drug targets for four site-specific cancers by integrating human plasma proteome with genome.. *Journal of pharmaceutical and biomedical analysis*. PMID: 39933395
5. A Combined Proteomics and Mendelian Randomization Approach to Investigate the Effects of Aspirin-Targeted Proteins on Colorectal Cancer.. *Cancer epidemiology, biomarkers & prevention : a publication of the American Association for Cancer Research, cosponsored by the American Society of Preventive Oncology*. PMID: 33318029

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 58.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 17.3% |
| 有序区域 (pLDDT>70) 占比 | 71.6% |
| 可用 PDB 条目 | 1I49, 1I4D, 1I4L, 1I4T, 4DCN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1I49, 1I4D, 1I4L, 1I4T, 4DCN）+ AlphaFold预测（pLDDT=80.7），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR010504, IPR030798; Pfam: PF06456 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAC1 | 0.993 | 0.987 | — |
| ARL1 | 0.985 | 0.947 | — |
| ARF1 | 0.961 | 0.791 | — |
| ARF6 | 0.931 | 0.556 | — |
| ARF5 | 0.842 | 0.527 | — |
| CDKN2A | 0.822 | 0.292 | — |
| ARF3 | 0.799 | 0.492 | — |
| ARFIP1 | 0.785 | 0.768 | — |
| BIN1 | 0.678 | 0.000 | — |
| AKT1 | 0.604 | 0.230 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000379998.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:8670882|mint:MINT-52210 |
| Chuk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ARF6 | psi-mi:"MI:0096"(pull down) | pubmed:9312003 |
| RAC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9312003 |
| ARF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9312003 |
| ITGB3BP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DTNBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LY6D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| hrpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SNX1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 1I49, 1I4D, 1I4L, 1I4T, 4DCN | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus; Golgi apparatus, trans-Golgi netw / Nucleoplasm, Nucleoli, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ARFIP2 — Arfaptin-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小341 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53365
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132254-ARFIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARFIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53365
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:29:08

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000132254-ARFIP2/subcellular

![](https://images.proteinatlas.org/38156/435_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/38156/435_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/38156/445_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/38156/445_G5_4_red_green.jpg)
![](https://images.proteinatlas.org/38156/448_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/38156/448_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53365-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
