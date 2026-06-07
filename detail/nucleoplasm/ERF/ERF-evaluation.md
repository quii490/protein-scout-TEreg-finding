---
type: protein-evaluation
gene: "ERF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERF — REJECTED (研究热度过高 (PubMed strict=2206，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERF |
| 蛋白名称 | ETS domain-containing transcription factor ERF |
| 蛋白大小 | 548 aa / 58.7 kDa |
| UniProt ID | P50548 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Plasma membrane, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 548 aa / 58.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2206 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 7JSA, 7JSL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2206 |
| PubMed broad count | 4006 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Advances in AP2/ERF super-family transcription factors in plant.. *Critical reviews in biotechnology*. PMID: 32522044
2. Genome-wide analysis of the ERF gene family in Arabidopsis and rice.. *Plant physiology*. PMID: 16407444
3. ERF.D2 negatively controls drought tolerance through synergistic regulation of abscisic acid and jasmonic acid in tomato.. *Plant biotechnology journal*. PMID: 40424069
4. Understanding AP2/ERF Transcription Factor Responses and Tolerance to Various Abiotic Stresses in Plants: A Comprehensive Review.. *International journal of molecular sciences*. PMID: 38255967
5. Identification and Analysis of the AP2/ERF Gene Family in Barley Based on Pan-Genome and Pan-Transcriptome.. *Journal of agricultural and food chemistry*. PMID: 40657825

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 18.8% |
| 低置信 (pLDDT<50) 占比 | 63.7% |
| 有序区域 (pLDDT>70) 占比 | 17.5% |
| 可用 PDB 条目 | 7JSA, 7JSL |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 17.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam: PF00178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCAF1 | 0.999 | 0.000 | — |
| MAPK3 | 0.876 | 0.190 | — |
| MAPK1 | 0.858 | 0.196 | — |
| ETS2 | 0.807 | 0.000 | — |
| REXO1 | 0.768 | 0.000 | — |
| FURIN | 0.549 | 0.000 | — |
| ZNF865 | 0.514 | 0.045 | — |
| PRSS57 | 0.507 | 0.000 | — |
| CCNB1 | 0.504 | 0.000 | — |
| ZNF282 | 0.500 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIPK22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000163491 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000179603 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000148120 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000183354 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000178568 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000183722 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000177694 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| MAPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 7JSA, 7JSL | pLDDT=53.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli, Plasma membrane, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERF — ETS domain-containing transcription factor ERF，研究基础较多，新颖性有限。
2. 蛋白大小548 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2206 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2206 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50548
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105722-ERF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50548
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50548-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50548 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR036388;IPR036390; |
| Pfam | PF00178; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000105722-ERF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ZRANB1 | Intact, Biogrid | true |
| AMZ1 | Bioplex | false |
| CIAO2A | Bioplex | false |
| D2HGDH | Bioplex | false |
| DDX20 | Biogrid | false |
| DNAJB8 | Bioplex | false |
| EEF1AKMT3 | Bioplex | false |
| HSPB8 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
