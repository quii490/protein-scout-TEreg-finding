---
type: protein-evaluation
gene: "TCF7L2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TCF7L2 — REJECTED (研究热度过高 (PubMed strict=1197，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF7L2 / TCF4 |
| 蛋白名称 | Transcription factor 7-like 2 |
| 蛋白大小 | 619 aa / 67.9 kDa |
| UniProt ID | Q9NQB0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus, PML body; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 619 aa / 67.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1197 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.0; PDB: 1JDH, 1JPW, 2GL7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus, PML body; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- beta-catenin-TCF7L2 complex (GO:0070369)
- catenin-TCF7L2 complex (GO:0071664)
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- protein-DNA complex (GO:0032993)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1197 |
| PubMed broad count | 2211 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF4 |

**关键文献**:
1. The Role of TCF7L2 in Type 2 Diabetes.. *Diabetes*. PMID: 34016596
2. Identification of core genes in intervertebral disc degeneration using bioinformatics and machine learning algorithms.. *Frontiers in immunology*. PMID: 39050860
3. Targeting the NOTCH2/ADAM10/TCF7L2 Axis-Mediated Transcriptional Regulation of Wnt Pathway Suppresses Tumor Growth and Enhances Chemosensitivity in Colorectal Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39601111
4. Super-Enhancer Reprograming Driven by SOX9 and TCF7L2 Represents Transcription-Targeted Therapeutic Vulnerability for Treating Gallbladder Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39492805
5. The diabetes gene Tcf7l2 organizes gene expression in the liver and regulates amino acid metabolism.. *Molecular metabolism*. PMID: 40675550

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.0 |
| 高置信度残基 (pLDDT>90) 占比 | 9.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 65.1% |
| 有序区域 (pLDDT>70) 占比 | 17.8% |
| 可用 PDB 条目 | 1JDH, 1JPW, 2GL7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.0），有序残基占 17.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024940; Pfam: PF08347, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNNB1 | 0.999 | 0.997 | — |
| NLK | 0.982 | 0.488 | — |
| CTBP1 | 0.977 | 0.510 | — |
| BCL9 | 0.976 | 0.893 | — |
| EP300 | 0.975 | 0.354 | — |
| JUP | 0.972 | 0.658 | — |
| CREBBP | 0.966 | 0.125 | — |
| TCF7L1 | 0.962 | 0.000 | — |
| SMAD4 | 0.948 | 0.100 | — |
| TCF7 | 0.943 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DAXX | psi-mi:"MI:0018"(two hybrid) | imex:IM-14459|pubmed:16569639 |
| CTNNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14459|pubmed:16569639 |
| UBE2I | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| PSMA3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FBLN1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| pgi | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| glnA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| uvrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pagA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.0 + PDB: 1JDH, 1JPW, 2GL7 | pLDDT=53.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, PML body; Nucleus / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TCF7L2 — Transcription factor 7-like 2，研究基础较多，新颖性有限。
2. 蛋白大小619 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1197 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1197 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQB0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148737-TCF7L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF7L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQB0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000148737-TCF7L2/subcellular

![](https://images.proteinatlas.org/38800/2264_E11_235_red_green.jpg)
![](https://images.proteinatlas.org/38800/2264_E11_337_red_green.jpg)
![](https://images.proteinatlas.org/38800/687_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/38800/687_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/38800/776_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/38800/776_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQB0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQB0 |
| SMART | SM01366;SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027397;IPR013558;IPR009071;IPR036910;IPR024940; |
| Pfam | PF08347;PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148737-TCF7L2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTNNB1 | Intact, Biogrid | true |
| DAXX | Intact, Biogrid | true |
| HIC1 | Intact, Biogrid | true |
| XRCC6 | Intact, Biogrid | true |
| AR | Biogrid | false |
| CLTC | Biogrid | false |
| CRX | Biogrid | false |
| CTBP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
