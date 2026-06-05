---
type: protein-evaluation
gene: "TMCO6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMCO6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMCO6 |
| 蛋白名称 | Transmembrane and coiled-coil domain-containing protein 6 |
| 蛋白大小 | 493 aa / 54.4 kDa |
| UniProt ID | Q96DC7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 493 aa / 54.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR000225, IPR002652 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Epigenetic findings in periodontitis in UK twins: a cross-sectional study.. *Clinical epigenetics*. PMID: 30760334
2. Loss-of-function variant in the ovine TMCO6 gene in North Country Cheviot sheep with motor neuron disease.. *Genomics*. PMID: 37488055
3. Promoter hypomethylation of CDH7: a novel epigenetic marker associated with cerebral small vessel disease.. *Frontiers in genetics*. PMID: 41890232
4. Transcriptome analyses indicate that heat stress-induced inflammation in white adipose tissue and oxidative stress in skeletal muscle is partially moderated by zilpaterol supplementation in beef cattle.. *Journal of animal science*. PMID: 35079800
5. Comparative transcriptomic analysis reveals the gonadal development-related gene response to environmental temperature in Mauremys mutica.. *Comparative biochemistry and physiology. Part D, Genomics & proteomics*. PMID: 34689019

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 75.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.3，有序区 85.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR002652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF511 | 0.787 | 0.786 | — |
| LSM5 | 0.637 | 0.627 | — |
| PHYHIPL | 0.609 | 0.538 | — |
| CSE1L | 0.602 | 0.503 | — |
| KPNB1 | 0.596 | 0.506 | — |
| MISP3 | 0.581 | 0.000 | — |
| LSM4 | 0.563 | 0.551 | — |
| NUP153 | 0.536 | 0.449 | — |
| EXOSC10 | 0.513 | 0.504 | — |
| PDZD9 | 0.513 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF511 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LSM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHYHIPL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LSM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LSM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PSME4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LSM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.3 + PDB: 无 | pLDDT=87.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TMCO6 — Transmembrane and coiled-coil domain-containing protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小493 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DC7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113119-TMCO6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMCO6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DC7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000113119-TMCO6/subcellular

![](https://images.proteinatlas.org/37474/517_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37474/517_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37474/520_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37474/520_B5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37474/523_B5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37474/523_B5_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DC7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
