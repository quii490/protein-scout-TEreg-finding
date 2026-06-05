---
type: protein-evaluation
gene: "FRG2C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRG2C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRG2C |
| 蛋白名称 | Protein FRG2-like-2 |
| 蛋白大小 | 282 aa / 30.8 kDa |
| UniProt ID | A6NGY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 282 aa / 30.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026245; Pfam: PF15315 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sequence variant of POU5F1 as risk factor for premature ovarian insufficiency by mis-regulating transcription.. *Gene*. PMID: 40744326
2. Alterations in SAMD9, AHSG, FRG2C, and FGFR4 Genes in a Case of Late-Onset Massive Tumoral Calcinosis.. *AACE clinical case reports*. PMID: 37736313
3. Differential Expression Profiles of Long Noncoding RNA and mRNA of Osteogenically Differentiated Mesenchymal Stem Cells in Ankylosing Spondylitis.. *The Journal of rheumatology*. PMID: 27182066
4. Whole Exome Sequencing Reveals Potential Single Nucleotide Polymorphisms and Copy Number Variations in 26 Sporadic Patients with Immature Teratoma.. *International journal of general medicine*. PMID: 42038264

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 10.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 46.5% |
| 低置信 (pLDDT<50) 占比 | 30.5% |
| 有序区域 (pLDDT>70) 占比 | 23.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 23.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026245; Pfam: PF15315 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF354A | 0.700 | 0.000 | — |
| USP50 | 0.665 | 0.000 | — |
| LIN54 | 0.620 | 0.000 | — |
| ZNF717 | 0.611 | 0.000 | — |
| FAM104B | 0.515 | 0.000 | — |
| OR2T27 | 0.507 | 0.000 | — |
| SP6 | 0.475 | 0.000 | — |
| NUTM2G | 0.446 | 0.000 | — |
| KRTAP4-6 | 0.446 | 0.000 | — |
| ANKRD36C | 0.440 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 无 | pLDDT=60.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FRG2C — Protein FRG2-like-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小282 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NGY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172969-FRG2C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRG2C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NGY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NGY1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
