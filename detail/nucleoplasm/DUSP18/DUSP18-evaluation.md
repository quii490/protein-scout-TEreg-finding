---
type: protein-evaluation
gene: "DUSP18"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP18 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP18 / LMWDSP20 |
| 蛋白名称 | Dual specificity protein phosphatase 18 |
| 蛋白大小 | 188 aa / 21.1 kDa |
| UniProt ID | Q8NEJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Mitochondrion inner membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 21.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.8; PDB: 2ESB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020420, IPR000340, IPR029021, IPR016130, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial inner membrane (GO:0005743)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LMWDSP20 |

**关键文献**:
1. Inhibition of DUSP18 impairs cholesterol biosynthesis and promotes anti-tumor immunity in colorectal cancer.. *Nature communications*. PMID: 38992029
2. Kisspeptin-10 binding to Gpr54 in osteoclasts prevents bone loss by activating Dusp18-mediated dephosphorylation of Src.. *Nature communications*. PMID: 38346942
3. Dual-specificity phosphatase 18 modulates the SUMOylation and aggregation of Ataxin-1.. *Biochemical and biophysical research communications*. PMID: 29852174
4. Expression of dual-specificity phosphatases in TGFß1-induced EMT in SKOV3 cells.. *Turkish journal of medical sciences*. PMID: 37476896
5. Hypoxia-induced HIF1A activates DUSP18-mediated MAPK14 dephosphorylation to promote hepatocellular carcinoma cell migration and invasion.. *Pathology, research and practice*. PMID: 35841693

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.8 |
| 高置信度残基 (pLDDT>90) 占比 | 86.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 2ESB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.8，有序区 91.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020420, IPR000340, IPR029021, IPR016130, IPR000387; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.530 | 0.114 | — |
| MAPK3 | 0.508 | 0.175 | — |
| MAPK14 | 0.502 | 0.175 | — |
| HDHD5 | 0.456 | 0.000 | — |
| PTPN21 | 0.449 | 0.071 | — |
| DUSP11 | 0.432 | 0.046 | — |
| PUDP | 0.406 | 0.071 | — |
| PPM1M | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 8，IntAct interactions: 0
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.8 + PDB: 2ESB | pLDDT=92.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion inner membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUSP18 — Dual specificity protein phosphatase 18，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167065-DUSP18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000167065-DUSP18/subcellular

![](https://images.proteinatlas.org/51349/792_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/51349/792_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/51349/795_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/51349/795_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/51349/799_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/51349/799_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEJ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEJ0 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 19..160; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR020420;IPR000340;IPR029021;IPR016130;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167065-DUSP18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| INSR | Intact, Biogrid | true |
| ATXN1 | Biogrid | false |
| JPH3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
