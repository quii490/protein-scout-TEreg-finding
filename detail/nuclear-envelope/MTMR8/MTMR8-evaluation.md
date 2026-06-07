---
type: protein-evaluation
gene: "MTMR8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTMR8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTMR8 |
| 蛋白名称 | Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR8 |
| 蛋白大小 | 704 aa / 78.9 kDa |
| UniProt ID | Q96EF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus envelope |
| 蛋白大小 | 10/10 | ×1 | 10 | 704 aa / 78.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.9; PDB: 4Y7I |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030591, IPR030564, IPR010569, IPR048994, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus envelope | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear envelope (GO:0005635)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and localization of a new human myotubularin-related protein gene, mtmr8, on 8p22-p23.. *Genomics*. PMID: 11472061
2. Human myotubularin-related protein 9 regulates ER-to-Golgi trafficking and modulates WNT3A secretion.. *Experimental cell research*. PMID: 31704058
3. Condition-dependent functional shift of two Drosophila Mtmr lipid phosphatases in autophagy control.. *Autophagy*. PMID: 33779490
4. X-linked MTMR8 diversity and evolutionary history of sub-Saharan populations.. *PloS one*. PMID: 24282552
5. Structure of the catalytic phosphatase domain of MTMR8: implications for dimerization, membrane association and reversible oxidation.. *Acta crystallographica. Section D, Biological crystallography*. PMID: 26143924

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 4Y7I |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=81.9，有序区 75.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030591, IPR030564, IPR010569, IPR048994, IPR011993; Pfam: PF06602, PF21098 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTMR9 | 0.988 | 0.855 | — |
| FIG4 | 0.919 | 0.000 | — |
| PIKFYVE | 0.917 | 0.000 | — |
| INPP4A | 0.905 | 0.000 | — |
| INPP5F | 0.904 | 0.000 | — |
| CDIPT | 0.904 | 0.000 | — |
| INPP4B | 0.903 | 0.000 | — |
| PIP4P2 | 0.900 | 0.000 | — |
| PIP4P1 | 0.900 | 0.000 | — |
| PIK3C3 | 0.806 | 0.075 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MTMR9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPG21 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EMILIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ARL11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTMR7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| MOS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FAM169A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 4Y7I | pLDDT=81.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus envelope / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MTMR8 — Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小704 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102043-MTMR8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTMR8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EF0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96EF0 |
| SMART | SM00404; |
| UniProt Domain [FT] | DOMAIN 126..500; /note="Myotubularin phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00669" |
| InterPro | IPR030591;IPR030564;IPR010569;IPR048994;IPR011993;IPR029021;IPR016130;IPR003595; |
| Pfam | PF06602;PF21098; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102043-MTMR8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MTMR9 | Intact, Biogrid, Bioplex | true |
| STIP1 | Biogrid | false |
| TAB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
