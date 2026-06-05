---
type: protein-evaluation
gene: "FBXO9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO9 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO9 / FBX9, VCIA1 |
| 蛋白名称 | F-box only protein 9 |
| 蛋白大小 | 447 aa / 52.3 kDa |
| UniProt ID | Q9UK97 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 447 aa / 52.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR045464, IPR036181; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX9, VCIA1 |

**关键文献**:
1. Ubiquitin ligase subunit FBXO9 inhibits V-ATPase assembly and impedes lung cancer metastasis.. *Experimental hematology & oncology*. PMID: 38486234
2. F-box only protein 9 and its role in cancer.. *Molecular biology reports*. PMID: 35025031
3. F-box only protein 9 is an E3 ubiquitin ligase of PPARγ.. *Experimental & molecular medicine*. PMID: 27197753
4. F-box only protein 9 is required for adipocyte differentiation.. *Biochemical and biophysical research communications*. PMID: 23643813
5. FBXO9 mediated the ubiquitination and degradation of YAP in a GSK-3β-dependent manner.. *The Journal of biological chemistry*. PMID: 40902979

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 43.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.4，有序区 73.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR045464, IPR036181; Pfam: PF12937, PF19270 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.994 | 0.952 | — |
| CUL1 | 0.973 | 0.763 | — |
| E5RI56_HUMAN | 0.819 | 0.792 | — |
| TTI1 | 0.691 | 0.292 | — |
| FBXO4 | 0.673 | 0.126 | — |
| RBX1 | 0.624 | 0.247 | — |
| NEDD8 | 0.605 | 0.092 | — |
| TELO2 | 0.595 | 0.292 | — |
| FBXO11 | 0.583 | 0.000 | — |
| CAND1 | 0.569 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| pckA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| hmsH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22632967|imex:IM-17368 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| GFOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EEF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 无 | pLDDT=77.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXO9 — F-box only protein 9，非常新颖，仅有少数基础研究。
2. 蛋白大小447 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK97
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112146-FBXO9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK97
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000112146-FBXO9/subcellular

![](https://images.proteinatlas.org/64246/1152_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/64246/1152_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/64246/1156_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/64246/1156_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/64246/1169_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/64246/1169_D12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
