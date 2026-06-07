---
type: protein-evaluation
gene: "CRIP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRIP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRIP3 / CRP3 |
| 蛋白名称 | Cysteine-rich protein 3 |
| 蛋白大小 | 217 aa / 24.1 kDa |
| UniProt ID | Q6Q6R5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear speckles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 217 aa / 24.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=13 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=74.4; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 8 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRP3 |

**关键文献**:
1. Spatial transcriptional landscape of human heart failure.. *European heart journal*. PMID: 40335066
2. Transcriptome and microRNAome profiling of human skeletal muscle in pancreatic cancer cachexia.. *medRxiv : the preprint server for health sciences*. PMID: 40950454
3. Rare-variant association analysis reveals known and new age-related hearing loss genes.. *European journal of human genetics : EJHG*. PMID: 36788145
4. Cysteine-rich intestinal protein family: structural overview, functional diversity, and roles in human disease.. *Cell death discovery*. PMID: 40118853
5. Integrated analysis of metabolomic and transcriptomic profiling reveals the effect of Buyang Huanwu decoction on Parkinson's disease in mice.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 36948142

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 22.6% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 58.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.4，有序区 58.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TIRAP | 0.576 | 0.000 | — |
| HOXD8 | 0.538 | 0.000 | — |
| MYD88 | 0.535 | 0.000 | — |
| HOXD3 | 0.521 | 0.000 | — |
| HTRA1 | 0.479 | 0.000 | — |
| SCO1 | 0.467 | 0.000 | — |
| TGFB2 | 0.432 | 0.000 | — |
| COA6 | 0.408 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLOD3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FHL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 2
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 无 | pLDDT=74.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 8 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CRIP3 -- Cysteine-rich protein 3，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6Q6R5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146215-CRIP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRIP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6Q6R5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000146215-CRIP3/subcellular

![](https://images.proteinatlas.org/36198/1145_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/36198/1145_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/36198/403_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/36198/403_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/36198/408_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/36198/408_E10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6Q6R5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6Q6R5 |
| SMART | SM00132; |
| UniProt Domain [FT] | DOMAIN 3..64; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 122..183; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR001781; |
| Pfam | PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146215-CRIP3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
