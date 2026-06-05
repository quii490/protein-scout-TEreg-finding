---
type: protein-evaluation
gene: "EVA1C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EVA1C — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EVA1C / C21orf63, C21orf64, FAM176C |
| 蛋白名称 | Protein eva-1 homolog C |
| 蛋白大小 | 441 aa / 49.5 kDa |
| UniProt ID | P58658 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 49.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039500, IPR000922, IPR043159; Pfam: PF14851, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf63, C21orf64, FAM176C |

**关键文献**:
1. Unravelling the molecular landscape of endometrial cancer subtypes: insights from multiomics analysis.. *International journal of surgery (London, England)*. PMID: 38775562
2. NAD(+) reverses Alzheimer's neurological deficits via regulating differential alternative RNA splicing of EVA1C.. *Science advances*. PMID: 41202143
3. Systematic Functional Characterization of Human 21st Chromosome Orthologs in Caenorhabditis elegans.. *G3 (Bethesda, Md.)*. PMID: 29367452
4. Genomic Regions Associated with Milk Composition and Fertility Traits in Spring-Calved Dairy Cows in New Zealand.. *Genes*. PMID: 37107618
5. Identifying novel proteins for suicide attempt by integrating proteomes from brain and blood with genome-wide association data.. *Neuropsychopharmacology : official publication of the American College of Neuropsychopharmacology*. PMID: 38317018

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.2% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 55.5% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.2，有序区 55.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039500, IPR000922, IPR043159; Pfam: PF14851, PF02140 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| URB1 | 0.587 | 0.000 | — |
| POFUT2 | 0.587 | 0.000 | — |
| DONSON | 0.581 | 0.000 | — |
| N6AMT1 | 0.575 | 0.000 | — |
| PDXK | 0.488 | 0.000 | — |
| PNPLA6 | 0.475 | 0.471 | — |
| DOP1B | 0.471 | 0.000 | — |
| PAXBP1 | 0.471 | 0.000 | — |
| UNC5D | 0.454 | 0.310 | — |
| BMPR1B | 0.454 | 0.454 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A6ND58 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DBF4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UPK3BL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BMPR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPTLC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSPAN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTDNEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 无 | pLDDT=70.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Cytosol | 一致 |
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
1. EVA1C — Protein eva-1 homolog C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58658
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166979-EVA1C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVA1C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58658
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58658-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
