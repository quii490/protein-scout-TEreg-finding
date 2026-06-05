---
type: protein-evaluation
gene: "SHOC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHOC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHOC1 / C9orf84, ZIP2 |
| 蛋白名称 | Protein shortage in chiasmata 1 ortholog |
| 蛋白大小 | 1444 aa / 165.2 kDa |
| UniProt ID | Q5VXU9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1444 aa / 165.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039991; Pfam: PF17825 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- condensed nuclear chromosome (GO:0000794)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf84, ZIP2 |

**关键文献**:
1. Genotype-specific differences in infertile men due to loss-of-function variants in M1AP or ZZS genes.. *EMBO molecular medicine*. PMID: 40374915
2. A comprehensive study of common and rare genetic variants in spermatogenesis-related loci identifies new risk factors for idiopathic severe spermatogenic failure.. *Human reproduction open*. PMID: 39678461
3. SHOC1, an XPF endonuclease-related protein, is essential for the formation of class I meiotic crossovers.. *Current biology : CB*. PMID: 18812090
4. SHOC1 is a ERCC4-(HhH)2-like protein, integral to the formation of crossover recombination intermediates during mammalian meiosis.. *PLoS genetics*. PMID: 29742103
5. Pathogenic bi-allelic variants of meiotic ZMM complex gene SPO16 in premature ovarian insufficiency.. *Clinical genetics*. PMID: 37270785

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 29.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 62.2% |
| 有序区域 (pLDDT>70) 占比 | 30.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.1），有序残基占 30.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039991; Pfam: PF17825 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEX11 | 0.833 | 0.253 | — |
| MSH4 | 0.760 | 0.000 | — |
| HFM1 | 0.740 | 0.000 | — |
| RNF212 | 0.713 | 0.000 | — |
| C1orf146 | 0.666 | 0.000 | — |
| SYCP1 | 0.598 | 0.000 | — |
| MSH5 | 0.584 | 0.000 | — |
| ADAD2 | 0.583 | 0.000 | — |
| STAG3 | 0.580 | 0.000 | — |
| REC8 | 0.574 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| maP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.1 + PDB: 无 | pLDDT=49.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. SHOC1 — Protein shortage in chiasmata 1 ortholog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1444 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VXU9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165181-SHOC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHOC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VXU9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165181-SHOC1/subcellular

![](https://images.proteinatlas.org/52214/1208_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/52214/1208_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/52214/893_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/52214/893_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/52214/895_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/52214/895_H10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VXU9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
