---
type: protein-evaluation
gene: "ONECUT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ONECUT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ONECUT3 |
| 蛋白名称 | One cut domain family member 3 |
| 蛋白大小 | 494 aa / 50.0 kDa |
| UniProt ID | O60422 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 494 aa / 50.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003350, IPR051649, IPR001356, IPR009057, IPR010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Concerted transcriptional regulation of the morphogenesis of hypothalamic neurons by ONECUT3.. *Nature communications*. PMID: 39366958
2. Targeting ONECUT3 blocks glycolytic metabolism and potentiates anti-PD-1 therapy in pancreatic cancer.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 37606818
3. Identification of microRNA-mRNA-TF regulatory networks in periodontitis by bioinformatics analysis.. *BMC oral health*. PMID: 35397550
4. Molecular interrogation of hypothalamic organization reveals distinct dopamine neuronal subtypes.. *Nature neuroscience*. PMID: 27991900
5. Construction of a prognostic model for lung squamous cell carcinoma based on immune-related genes.. *Carcinogenesis*. PMID: 36455238

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 61.5% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003350, IPR051649, IPR001356, IPR009057, IPR010982; Pfam: PF02376, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ONECUT1 | 0.770 | 0.000 | — |
| FOXA2 | 0.648 | 0.000 | — |
| TCF15 | 0.597 | 0.000 | — |
| TTR | 0.560 | 0.000 | — |
| DNAJB7 | 0.556 | 0.052 | — |
| ORC3 | 0.538 | 0.514 | — |
| MAU2 | 0.428 | 0.000 | — |
| CIB1 | 0.426 | 0.426 | — |
| CTCFL | 0.413 | 0.092 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A8MZM7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZMYND12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NCK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CIB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CACNA1C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 6
- 调控相关比例: 1 / 9 = 11%

**评价**: STRING 9 个预测互作，IntAct 6 个实验互作。调控相关配体占比 11%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 无 | pLDDT=56.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 9 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ONECUT3 — One cut domain family member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小494 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60422
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205922-ONECUT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ONECUT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60422
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000205922-ONECUT3/subcellular

![](https://images.proteinatlas.org/59936/1018_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/59936/1018_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/59936/1218_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/59936/1218_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/59936/1242_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/59936/1242_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60422-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
