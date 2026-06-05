---
type: protein-evaluation
gene: "DSEL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DSEL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSEL / C18orf4, NCAG1 |
| 蛋白名称 | Dermatan-sulfate epimerase-like protein |
| 蛋白大小 | 1212 aa / 139.2 kDa |
| UniProt ID | Q8IZU8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1212 aa / 139.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008929, IPR052447, IPR027417, IPR000863; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf4, NCAG1 |

**关键文献**:
1. M6A-mediated molecular patterns and tumor microenvironment infiltration characterization in nasopharyngeal carcinoma.. *Cancer biology & therapy*. PMID: 38532632
2. A maternally inherited chromosome 18q22.1 deletion in a male with late-presenting diaphragmatic hernia and microphthalmia-evaluation of DSEL as a candidate gene for the diaphragmatic defect.. *American journal of medical genetics. Part A*. PMID: 20358601
3. Gene expression of the two developmentally regulated dermatan sulfate epimerases in the Xenopus embryo.. *PloS one*. PMID: 29370293
4. The PTH/PTHrP receptor can delay chondrocyte hypertrophy in vivo without activating phospholipase C.. *Developmental cell*. PMID: 12194850
5. The circular RNA expression profile of human auricle cartilage and the role of circCOL1A2 in isolated microtia.. *Cellular signalling*. PMID: 38123043

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.9 |
| 高置信度残基 (pLDDT>90) 占比 | 67.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 9.3% |
| 有序区域 (pLDDT>70) 占比 | 84.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.9，有序区 84.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008929, IPR052447, IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHST15 | 0.587 | 0.000 | — |
| TMX3 | 0.555 | 0.000 | — |
| CHST14 | 0.552 | 0.000 | — |
| CHST3 | 0.551 | 0.000 | — |
| CHST13 | 0.539 | 0.000 | — |
| DCN | 0.519 | 0.000 | — |
| CSGALNACT2 | 0.495 | 0.000 | — |
| BGN | 0.492 | 0.000 | — |
| FAM240B | 0.479 | 0.000 | — |
| CSPG5 | 0.457 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=85.9 + PDB: 无 | pLDDT=85.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DSEL — Dermatan-sulfate epimerase-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1212 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZU8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171451-DSEL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSEL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZU8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000171451-DSEL/subcellular

![](https://images.proteinatlas.org/60942/1138_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/60942/1138_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60942/1149_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/60942/1149_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60942/1527_E4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/60942/1527_E4_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZU8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
