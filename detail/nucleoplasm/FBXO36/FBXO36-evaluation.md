---
type: protein-evaluation
gene: "FBXO36"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO36 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO36 / FBX36 |
| 蛋白名称 | F-box only protein 36 |
| 蛋白大小 | 188 aa / 22.1 kDa |
| UniProt ID | Q8NEA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 22.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR052301; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX36 |

**关键文献**:
1. The influence of rare variants in circulating metabolic biomarkers.. *PLoS genetics*. PMID: 32150548
2. Transcriptomic analysis of female and male gonads in juvenile snakeskin gourami (Trichopodus pectoralis).. *Scientific reports*. PMID: 32251302
3. A special prognostic indicator: tumor mutation burden combined with immune infiltrates in lung adenocarcinoma with TP53 mutation.. *Translational cancer research*. PMID: 35116695
4. Identification of candidate gene networks affecting the number of somatic cells count and milk production in Iranian Holstein cows using Genome-wide association study.. *Scientific reports*. PMID: 40890164
5. Simultaneous VENTANA IHC and RT-PCR testing of ALK status in Chinese non-small cell lung cancer patients and response to crizotinib.. *Journal of translational medicine*. PMID: 29642919

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 63.8% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 93.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.7，有序区 93.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR052301; Pfam: PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.818 | 0.558 | — |
| TEKT3 | 0.728 | 0.000 | — |
| AK7 | 0.625 | 0.000 | — |
| EFCAB6 | 0.615 | 0.000 | — |
| TSNAXIP1 | 0.614 | 0.000 | — |
| DRC3 | 0.613 | 0.000 | — |
| CUL1 | 0.612 | 0.045 | — |
| DNAH10 | 0.611 | 0.000 | — |
| DNAI1 | 0.604 | 0.000 | — |
| VWA3B | 0.603 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 无 | pLDDT=89.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO36 — F-box only protein 36，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153832-FBXO36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000153832-FBXO36/subcellular

![](https://images.proteinatlas.org/53865/1353_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/53865/1353_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/53865/1363_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/53865/1363_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/53865/1430_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/53865/1430_A10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEA4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEA4 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 91..137; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR052301; |
| Pfam | PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153832-FBXO36/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
