---
type: protein-evaluation
gene: "HPF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HPF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HPF1 / C4orf27 |
| 蛋白名称 | Histone PARylation factor 1 |
| 蛋白大小 | 346 aa / 39.4 kDa |
| UniProt ID | Q9NWY4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Microtubules, Cytokinetic bridge; UniProt: Chromosome; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 346 aa / 39.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.9; PDB: 6M3G, 6M3I, 6TX2, 6TX3, 6X0L, 6X0M, 6X0N |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019361; Pfam: PF10228 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Microtubules, Cytokinetic bridge | Approved |
| UniProt | Chromosome; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C4orf27 |

**关键文献**:
1. PARP enzyme de novo synthesis of protein-free poly(ADP-ribose).. *Molecular cell*. PMID: 39536748
2. Reversal of tyrosine-linked ADP-ribosylation by ARH3 and PARG.. *The Journal of biological chemistry*. PMID: 39342999
3. HPF1 and nucleosomes mediate a dramatic switch in activity of PARP1 from polymerase to hydrolase.. *eLife*. PMID: 33683197
4. Dual function of HPF1 in the modulation of PARP1 and PARP2 activities.. *Communications biology*. PMID: 34732825
5. HPF1/C4orf27 Is a PARP-1-Interacting Protein that Regulates PARP-1 ADP-Ribosylation Activity.. *Molecular cell*. PMID: 27067600

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.9 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 6M3G, 6M3I, 6TX2, 6TX3, 6X0L, 6X0M, 6X0N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6M3G, 6M3I, 6TX2, 6TX3, 6X0L, 6X0M, 6X0N）+ AlphaFold极高置信度预测（pLDDT=90.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019361; Pfam: PF10228 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARP2 | 0.999 | 0.983 | — |
| PARP1 | 0.979 | 0.955 | — |
| H2AC6 | 0.945 | 0.941 | — |
| H2BC11 | 0.942 | 0.941 | — |
| H2BC12 | 0.765 | 0.765 | — |
| H2BS1 | 0.765 | 0.765 | — |
| LOC102724334 | 0.765 | 0.765 | — |
| ADPRHL2 | 0.721 | 0.000 | — |
| PARG | 0.706 | 0.000 | — |
| PARP3 | 0.680 | 0.175 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF83 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| RBM11 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| ITGB3BP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EMW1 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| MKLN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.9 + PDB: 6M3G, 6M3I, 6TX2, 6TX3, 6X0L,  | pLDDT=90.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome; Nucleus / Cytosol; 额外: Microtubules, Cytokinetic bridge | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HPF1 — Histone PARylation factor 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小346 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWY4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000056050-HPF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HPF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWY4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000056050-HPF1/subcellular

![](https://images.proteinatlas.org/43467/474_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43467/474_D6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/43467/480_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43467/480_D6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/43467/510_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43467/510_D6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWY4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NWY4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019361; |
| Pfam | PF10228; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000056050-HPF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| H1-5 | Biogrid | false |
| H2AC20 | Biogrid | false |
| H3-4 | Biogrid | false |
| MACROH2A1 | Biogrid | false |
| MKLN1 | Intact | false |
| PARP1 | Biogrid | false |
| PARP2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
