---
type: protein-evaluation
gene: "PCGF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCGF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCGF1 / NSPC1, RNF68 |
| 蛋白名称 | Polycomb group RING finger protein 1 |
| 蛋白大小 | 259 aa / 30.3 kDa |
| UniProt ID | Q9BSM1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 30.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.8; PDB: 4HPL, 4HPM, 5JH5, 8HCU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR032443, IPR001841, IPR013083, IPR017907; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)
- PRC1 complex (GO:0035102)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NSPC1, RNF68 |

**关键文献**:
1. Epigenetic regulation of noncanonical menin targets modulates menin inhibitor response in acute myeloid leukemia.. *Blood*. PMID: 39158067
2. Microglial PCGF1 alleviates neuroinflammation associated depressive behavior in adolescent mice.. *Molecular psychiatry*. PMID: 39215186
3. Targeting Menin disrupts the KMT2A/B and polycomb balance to paradoxically activate bivalent genes.. *Nature cell biology*. PMID: 36635503
4. SKP1A bound to Polycomb-silenced genes mediates degradation of PRC2 and preconditions their activation.. *Molecular cell*. PMID: 40858113
5. Functional redundancy among Polycomb complexes in maintaining the pluripotent state of embryonic stem cells.. *Stem cell reports*. PMID: 35364009

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 56.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 14.3% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 4HPL, 4HPM, 5JH5, 8HCU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4HPL, 4HPM, 5JH5, 8HCU）+ AlphaFold高质量预测（pLDDT=81.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032443, IPR001841, IPR013083, IPR017907; Pfam: PF16207, PF13923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAF2 | 0.999 | 0.833 | — |
| RNF2 | 0.999 | 0.941 | — |
| RING1 | 0.999 | 0.901 | — |
| BCOR | 0.999 | 0.989 | — |
| RYBP | 0.999 | 0.866 | — |
| KDM2B | 0.999 | 0.989 | — |
| SKP1 | 0.998 | 0.965 | — |
| BCORL1 | 0.996 | 0.984 | — |
| CBX2 | 0.994 | 0.422 | — |
| CBX8 | 0.993 | 0.831 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| Rnf2 | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| RING1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| PCGF5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| RNF125 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM55 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| Rybp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17309|pubmed:22325148 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 4HPL, 4HPM, 5JH5, 8HCU | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. PCGF1 — Polycomb group RING finger protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115289-PCGF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCGF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSM1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000115289-PCGF1/subcellular

![](https://images.proteinatlas.org/11356/94_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/11356/94_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/11356/95_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/11356/95_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/11356/96_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/11356/96_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSM1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BSM1 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032443;IPR001841;IPR013083;IPR017907; |
| Pfam | PF16207;PF13923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115289-PCGF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCOR | Intact, Biogrid | true |
| CBX6 | Intact, Biogrid | true |
| CBX7 | Intact, Biogrid | true |
| CBX8 | Intact, Biogrid | true |
| RING1 | Intact, Biogrid, Bioplex | true |
| RNF2 | Intact, Biogrid, Bioplex | true |
| YAF2 | Biogrid, Bioplex | true |
| BCORL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
