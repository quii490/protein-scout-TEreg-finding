---
type: protein-evaluation
gene: "MAMDC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAMDC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAMDC4 / AEGP |
| 蛋白名称 | Apical endosomal glycoprotein |
| 蛋白大小 | 1216 aa / 131.5 kDa |
| UniProt ID | Q6UXC1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1216 aa / 131.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013320, IPR036055, IPR023415, IPR002172, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AEGP |

**关键文献**:
1. Regulation of YAP and Wnt signaling by the endosomal protein MAMDC4.. *PloS one*. PMID: 38787854
2. Postnatal regulation of MAMDC4 in the porcine intestinal epithelium is influenced by bacterial colonization.. *Physiological reports*. PMID: 27821716
3. Differential effects of Mediterranean vs. Western diets on coronary atherosclerosis and peripheral artery transcriptomics.. *Frontiers in nutrition*. PMID: 40709334
4. [Differential expression of LLGL2 in prostate ductal adenocarcinoma and acinar adenocarcinoma and its significance].. *Zhonghua bing li xue za zhi = Chinese journal of pathology*. PMID: 37805392
5. Private rare deletions in SEC16A and MAMDC4 may represent novel pathogenic variants in familial axial spondyloarthritis.. *Annals of the rheumatic diseases*. PMID: 25956157

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 28.2% |
| 置信残基 (pLDDT 70-90) 占比 | 51.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 79.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 79.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR036055, IPR023415, IPR002172, IPR000998; Pfam: PF00057, PF00629 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC183 | 0.591 | 0.000 | — |
| LCN12 | 0.559 | 0.000 | — |
| TMEM141 | 0.556 | 0.000 | — |
| NPDC1 | 0.507 | 0.000 | — |
| ANKDD1B | 0.477 | 0.093 | — |
| ETDB | 0.471 | 0.000 | — |
| VWCE | 0.463 | 0.000 | — |
| ABCA2 | 0.461 | 0.000 | — |
| ETDA | 0.447 | 0.000 | — |
| TMEM121 | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 14，IntAct interactions: 0
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 0 interactions | 数据有限 |

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
1. MAMDC4 — Apical endosomal glycoprotein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1216 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UXC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177943-MAMDC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAMDC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXC1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177943-MAMDC4/subcellular

![](https://images.proteinatlas.org/26377/625_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/26377/625_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/26377/629_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/26377/629_G2_3_red_green.jpg)
![](https://images.proteinatlas.org/26377/631_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/26377/631_G2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UXC1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UXC1 |
| SMART | SM00192;SM00137; |
| UniProt Domain [FT] | DOMAIN 26..53; /note="LDL-receptor class A 1; truncated"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 64..222; /note="MAM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128"; DOMAIN 228..266; /note="LDL-receptor class A 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 269..425; /note="MAM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128"; DOMAIN 456..491; /note="LDL-receptor class A 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 491..644; /note="MAM 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128"; DOMAIN 654..809; /note="MAM 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128"; DOMAIN 811..969; /note="MAM 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128"; DOMAIN 971..1138; /note="MAM 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00128" |
| InterPro | IPR013320;IPR036055;IPR023415;IPR002172;IPR000998;IPR051560; |
| Pfam | PF00057;PF00629; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177943-MAMDC4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
