---
type: protein-evaluation
gene: "NAV2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAV2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAV2 / HELAD1, KIAA1419, POMFIL2, RAINB1, STEERIN2 |
| 蛋白名称 | Neuron navigator 2 |
| 蛋白大小 | 2488 aa / 268.2 kDa |
| UniProt ID | Q8IVL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytoskeleton; Cell projection, axon; Per |
| 蛋白大小 | 2/10 | ×1 | 2 | 2488 aa / 268.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.0; PDB: 2YRN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR001715, IPR036872, IPR057568, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton; Cell projection, axon; Perikaryon | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- interstitial matrix (GO:0005614)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HELAD1, KIAA1419, POMFIL2, RAINB1, STEERIN2 |

**关键文献**:
1. Comprehensive molecular characterization of human colon and rectal cancer.. *Nature*. PMID: 22810696
2. GP73-dependent regulation of exosome biogenesis promotes colorectal cancer liver metastasis.. *Molecular cancer*. PMID: 40414849
3. Gut bacteria-derived succinate induces enteric nervous system regeneration.. *bioRxiv : the preprint server for biology*. PMID: 39463929
4. Concerted transcriptional regulation of the morphogenesis of hypothalamic neurons by ONECUT3.. *Nature communications*. PMID: 39366958
5. Identification of novel genes including NAV2 associated with isolated tall stature.. *Frontiers in endocrinology*. PMID: 38152138

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.0 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 71.7% |
| 有序区域 (pLDDT>70) 占比 | 24.9% |
| 可用 PDB 条目 | 2YRN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=46.0），有序残基占 24.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR001715, IPR036872, IPR057568, IPR039041; Pfam: PF25408, PF00307, PF23092 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNN1 | 0.725 | 0.127 | — |
| ING5 | 0.688 | 0.644 | — |
| TCF7L1 | 0.685 | 0.048 | — |
| NAV3 | 0.648 | 0.610 | — |
| ABI1 | 0.575 | 0.094 | — |
| CAPN6 | 0.535 | 0.098 | — |
| RBM15 | 0.531 | 0.531 | — |
| PIAS2 | 0.490 | 0.473 | — |
| MGAT5B | 0.464 | 0.098 | — |
| GAS2 | 0.424 | 0.070 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ING5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PIAS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| MKI67 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RBM15B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| RBM15 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PRPF3 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| CFAP58 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.0 + PDB: 2YRN | pLDDT=46.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton; Cell projection, / Nucleoplasm | 一致 |
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
1. NAV2 — Neuron navigator 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2488 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166833-NAV2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAV2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166833-NAV2/subcellular

![](https://images.proteinatlas.org/11755/88_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/11755/88_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/11755/89_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/11755/89_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/11755/90_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/11755/90_E8_20_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IVL1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
