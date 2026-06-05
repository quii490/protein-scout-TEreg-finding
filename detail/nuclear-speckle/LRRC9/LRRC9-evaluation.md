---
type: protein-evaluation
gene: "LRRC9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC9 |
| 蛋白名称 | Leucine-rich repeat-containing protein 9 |
| 蛋白大小 | 1453 aa / 166.9 kDa |
| UniProt ID | Q6ZRR7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cell Junctions; 额外: Nucleoplasm, Nuclear bo; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1453 aa / 166.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A novel predicted ADP-ribosyltransferase-like family conserved in eukaryotic evolution.. *PeerJ*. PMID: 33854844
2. Effects of antagonist of retinoid X receptor (UVI3003) on morphology and gene profile of Xenopus tropicalis embryos.. *Environmental toxicology and pharmacology*. PMID: 24950139
3. Tissue-specific gene expression of genome-wide significant loci associated with major depressive disorder subtypes.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 38663672

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.6 |
| 高置信度残基 (pLDDT>90) 占比 | 40.7% |
| 置信残基 (pLDDT 70-90) 占比 | 42.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 82.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.6，有序区 82.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050836; Pfam: PF12799, PF13855, PF14580 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZFP36L2 | 0.683 | 0.299 | — |
| GOLGA8M | 0.621 | 0.000 | — |
| SMIM31 | 0.610 | 0.000 | — |
| SAMD12 | 0.528 | 0.000 | — |
| ADGRL1 | 0.514 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| ADGRL2 | 0.514 | 0.514 | — |
| CDRT4 | 0.479 | 0.000 | — |
| SIX6 | 0.472 | 0.000 | — |
| NME8 | 0.426 | 0.416 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.6 + PDB: 无 | pLDDT=80.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cell Junctions; 额外: Nucleoplasm,  | 一致 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRC9 — Leucine-rich repeat-containing protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1453 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZRR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131951-LRRC9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZRR7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000131951-LRRC9/subcellular

![](https://images.proteinatlas.org/77675/1965_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77675/1965_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77675/1978_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77675/1978_A6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77675/1996_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77675/1996_H1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZRR7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
