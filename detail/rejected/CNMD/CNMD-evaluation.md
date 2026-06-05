---
type: protein-evaluation
gene: "CNMD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNMD — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNMD / CHMI, LECT1, MYETS1 |
| 蛋白名称 | Leukocyte cell-derived chemotaxin 1 |
| 蛋白大小 | 334 aa / 37.1 kDa |
| UniProt ID | O75829 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted, extracellular space, extracellular matrix; Endomem |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 37.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007084, IPR043405; Pfam: PF04089 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted, extracellular space, extracellular matrix; Endomembrane system | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endomembrane system (GO:0012505)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 129 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHMI, LECT1, MYETS1 |

**关键文献**:
1. Chondromodulin is necessary for cartilage callus distraction in mice.. *PloS one*. PMID: 36795722
2. RNA sequencing uncovers key players of cartilage calcification: potential implications for osteoarthritis pathogenesis.. *Rheumatology (Oxford, England)*. PMID: 39432678
3. Chondromodulin-1 in health, osteoarthritis, cancer, and heart disease.. *Cellular and molecular life sciences : CMLS*. PMID: 31317206
4. Characterization of Rabbit Mesenchymal Stem/Stromal Cells after Cryopreservation.. *Biology*. PMID: 37887022
5. Identification of marker genes to monitor residual iPSCs in iPSC-derived products.. *Cytotherapy*. PMID: 36319564

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.8% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 21.6% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.7，有序区 55.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007084, IPR043405; Pfam: PF04089 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LECT2 | 0.910 | 0.000 | — |
| COL2A1 | 0.615 | 0.045 | — |
| COL18A1 | 0.609 | 0.000 | — |
| CHMP5 | 0.590 | 0.000 | — |
| SPARC | 0.587 | 0.000 | — |
| CHMP1A | 0.564 | 0.000 | — |
| VPS4A | 0.555 | 0.000 | — |
| VPS4B | 0.553 | 0.000 | — |
| PTHLH | 0.550 | 0.000 | — |
| TGFB2 | 0.534 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| APOA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| TTMP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HLA-DPA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SOCS4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| HSH2D | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| APPL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 无 | pLDDT=70.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted, extracellular space, extracellular matri / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNMD — Leukocyte cell-derived chemotaxin 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75829
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136110-CNMD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNMD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75829
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75829-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
