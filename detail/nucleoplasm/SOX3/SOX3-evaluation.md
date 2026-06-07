---
type: protein-evaluation
gene: "SOX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOX3 — REJECTED (研究热度过高 (PubMed strict=354，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOX3 |
| 蛋白名称 | Transcription factor SOX-3 |
| 蛋白大小 | 446 aa / 45.2 kDa |
| UniProt ID | P41225 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 45.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=354 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR022097, IPR050140; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 354 |
| PubMed broad count | 563 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Hypoparathyroidism and Pseudohypoparathyroidism.. **. PMID: 25905388
2. The epigenetic landscape of T cell exhaustion.. *Science (New York, N.Y.)*. PMID: 27789799
3. ZBTB16/PLZF regulates juvenile spermatogonial stem cell development through an extensive transcription factor poising network.. *Nature structural & molecular biology*. PMID: 40033150
4. Human Pituitary Organoids: Transcriptional Landscape Deciphered by scRNA-Seq and Stereo-Seq, with Insights into SOX3's Role in Pituitary Development.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39951008
5. Diagnosis and management of non-CAH 46,XX disorders/differences in sex development.. *Frontiers in endocrinology*. PMID: 38812815

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 28.7% |
| 低置信 (pLDDT<50) 占比 | 51.8% |
| 有序区域 (pLDDT>70) 占比 | 19.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 19.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR022097, IPR050140; Pfam: PF00505, PF12336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DMRT1 | 0.888 | 0.065 | — |
| ATP11C | 0.798 | 0.046 | — |
| OTX2 | 0.796 | 0.091 | — |
| HESX1 | 0.770 | 0.000 | — |
| NEUROG2 | 0.761 | 0.051 | — |
| LHX4 | 0.736 | 0.066 | — |
| ESX1 | 0.735 | 0.057 | — |
| SHOX | 0.692 | 0.000 | — |
| POU1F1 | 0.677 | 0.113 | — |
| CTNNB1 | 0.675 | 0.047 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATXN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CRX | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMARCA4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| SMAD4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| TP53 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| AKT1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| FBXW7 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| PTPN11 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| PTEN | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 无 | pLDDT=56.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SOX3 — Transcription factor SOX-3，研究基础较多，新颖性有限。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 354 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 354 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41225
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134595-SOX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41225
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000134595-SOX3/subcellular

![](https://images.proteinatlas.org/54720/1504_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/54720/1504_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/54720/1512_B2_3_red_green.jpg)
![](https://images.proteinatlas.org/54720/1512_B2_4_red_green.jpg)
![](https://images.proteinatlas.org/54720/1593_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/54720/1593_F8_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P41225-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P41225 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR022097;IPR050140; |
| Pfam | PF00505;PF12336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134595-SOX3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact | false |
| CRX | Intact | false |
| TRAF2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
