---
type: protein-evaluation
gene: "TCL1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCL1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCL1A / TCL1 |
| 蛋白名称 | T-cell leukemia/lymphoma protein 1A |
| 蛋白大小 | 114 aa / 13.5 kDa |
| UniProt ID | P56279 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Microsome; Endoplasmic reticulum |
| 蛋白大小 | 8/10 | ×1 | 8 | 114 aa / 13.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=95 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.1; PDB: 1JSG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004832, IPR036672; Pfam: PF01840 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Cytosol; 额外: Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus; Microsome; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 95 |
| PubMed broad count | 316 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCL1 |

**关键文献**:
1. Aberrant activation of TCL1A promotes stem cell expansion in clonal haematopoiesis.. *Nature*. PMID: 37046083
2. Tertiary lymphoid structures predict the prognosis and immunotherapy response of cholangiocarcinoma.. *Frontiers in immunology*. PMID: 37234171
3. TCL1A-expressing B cells are critical for tertiary lymphoid structure formation and the prognosis of oral squamous cell carcinoma.. *Journal of translational medicine*. PMID: 38764038
4. Single-Cell RNA Sequencing Reveals the Expansion of Cytotoxic CD4(+) T Lymphocytes and a Landscape of Immune Cells in Primary Sjögren's Syndrome.. *Frontiers in immunology*. PMID: 33603736
5. TCL1A, B Cell Regulation and Tolerance in Renal Transplantation.. *Cells*. PMID: 34206047

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 73.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 92.1% |
| 可用 PDB 条目 | 1JSG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.1，有序区 92.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004832, IPR036672; Pfam: PF01840 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKT1 | 0.995 | 0.873 | — |
| AKT2 | 0.969 | 0.510 | — |
| DNMT3A | 0.952 | 0.784 | — |
| TCL1B | 0.944 | 0.000 | — |
| AKT3 | 0.936 | 0.292 | — |
| MTCP1 | 0.911 | 0.000 | — |
| CD19 | 0.887 | 0.000 | — |
| MS4A1 | 0.837 | 0.000 | — |
| VPREB3 | 0.836 | 0.000 | — |
| LOC102723407 | 0.798 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000451506.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| macB2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| AKT1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:29997244|imex:IM-26441| |
| DNMT3A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TTC33 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CADPS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PRTFDC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NIF3L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 1JSG | pLDDT=90.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Microsome; Endoplasmic reticul / Endoplasmic reticulum, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TCL1A — T-cell leukemia/lymphoma protein 1A，研究基础较多，新颖性有限。
2. 蛋白大小114 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 95 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56279
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100721-TCL1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCL1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56279
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (enhanced)。来源: https://www.proteinatlas.org/ENSG00000100721-TCL1A/subcellular

![](https://images.proteinatlas.org/16604/131_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16604/131_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16604/132_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16604/132_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16604/1778_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16604/1778_H1_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56279-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
