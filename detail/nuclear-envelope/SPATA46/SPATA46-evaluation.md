---
type: protein-evaluation
gene: "SPATA46"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA46 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA46 / C1orf111 |
| 蛋白名称 | Spermatogenesis-associated protein 46 |
| 蛋白大小 | 261 aa / 29.1 kDa |
| UniProt ID | Q5T0L3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 29.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040879; Pfam: PF17734 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf111 |

**关键文献**:
1. Nuclear envelope dynamics during mammalian spermatogenesis: new insights on male fertility.. *Biological reviews of the Cambridge Philosophical Society*. PMID: 30701647
2. Deficiency of SPATA46, a Novel Nuclear Membrane Protein, Causes Subfertility in Male Mice.. *Biology of reproduction*. PMID: 27488028
3. Loss of perinuclear theca ACTRT1 causes acrosome detachment and severe male subfertility in mice.. *Development (Cambridge, England)*. PMID: 35616329
4. Comprehensive Analysis of the Transcriptome-Wide m(6)A Methylome in Shaziling Pig Testicular Development.. *International journal of molecular sciences*. PMID: 37833923
5. Transcriptomic profiling of long non-coding RNAs in non-virus associated hepatocellular carcinoma.. *Cell biochemistry and biophysics*. PMID: 32405957

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 16.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 60.2% |
| 有序区域 (pLDDT>70) 占比 | 31.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 31.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040879; Pfam: PF17734 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSNK1A1 | 0.726 | 0.726 | — |
| MDM4 | 0.721 | 0.721 | — |
| GAPVD1 | 0.711 | 0.711 | — |
| SSMEM1 | 0.694 | 0.000 | — |
| SNX24 | 0.692 | 0.692 | — |
| SPACA1 | 0.666 | 0.000 | — |
| SPATA16 | 0.640 | 0.000 | — |
| HLCS | 0.634 | 0.634 | — |
| DPY19L2 | 0.590 | 0.000 | — |
| SNX22 | 0.589 | 0.589 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLX3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HLCS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TYW5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MDM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSNK1A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GAPVD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MGLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPATA46 — Spermatogenesis-associated protein 46，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T0L3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171722-SPATA46/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T0L3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T0L3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T0L3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040879; |
| Pfam | PF17734; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171722-SPATA46/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HLCS | Intact, Biogrid, Bioplex | true |
| CEP95 | Bioplex | false |
| CRYAA | Intact | false |
| CTPS2 | Bioplex | false |
| CYSRT1 | Intact | false |
| DYNC1H1 | Intact | false |
| ENKD1 | Intact | false |
| KLK6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
