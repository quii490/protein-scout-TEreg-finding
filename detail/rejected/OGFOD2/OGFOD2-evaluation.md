---
type: protein-evaluation
gene: "OGFOD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## OGFOD2 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OGFOD2 |
| 蛋白名称 | 2-oxoglutarate and iron-dependent oxygenase domain-containing protein 2 |
| 蛋白大小 | 350 aa / 39.0 kDa |
| UniProt ID | Q6N063 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 39.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005123, IPR006620; Pfam: PF25238 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Association of Redox Regulatory Drug Target Genes with Psychiatric Disorders: A Mendelian Randomization Study.. *Antioxidants (Basel, Switzerland)*. PMID: 38671846
2. Identification of a functional SNP rs7304782 at schizophrenia risk locus 12q24.31 and validation of its association with schiz ophrenia in Chinese populations.. *Psychiatry research*. PMID: 33070109
3. Integrated Analysis of Summary Statistics to Identify Pleiotropic Genes and Pathways for the Comorbidity of Schizophrenia and Cardiometabolic Disease.. *Frontiers in psychiatry*. PMID: 32425817

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 90.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 3.1% |
| 有序区域 (pLDDT>70) 占比 | 93.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.7，有序区 93.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005123, IPR006620; Pfam: PF25238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRMT2A | 0.805 | 0.000 | — |
| JMJD4 | 0.685 | 0.000 | — |
| ABCB9 | 0.637 | 0.000 | — |
| ARL6IP4 | 0.576 | 0.000 | — |
| WBP1 | 0.573 | 0.000 | — |
| OGFOD1 | 0.561 | 0.000 | — |
| WDR83 | 0.548 | 0.000 | — |
| TMEM218 | 0.542 | 0.000 | — |
| PITPNM2 | 0.510 | 0.000 | — |
| LRRC14 | 0.483 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TRIM55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| PRPF40A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| COQ8A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RAN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| LAMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CASP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 无 | pLDDT=93.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. OGFOD2 — 2-oxoglutarate and iron-dependent oxygenase domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6N063
- Protein Atlas: https://www.proteinatlas.org/search/OGFOD2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OGFOD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6N063
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000111325-OGFOD2/subcellular

![](https://images.proteinatlas.org/40306/417_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/40306/417_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/40306/420_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/40306/420_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/40306/990_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/40306/990_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6N063-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
