---
type: protein-evaluation
gene: "UBXN7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN7 / KIAA0794, UBXD7 |
| 蛋白名称 | UBX domain-containing protein 7 |
| 蛋白大小 | 489 aa / 54.9 kDa |
| UniProt ID | O94888 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 489 aa / 54.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.9; PDB: 1WJ4, 2DAL, 2DLX, 5X3P, 5X4L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036249, IPR006577, IPR009060, IPR054109, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- VCP-NPL4-UFD1 AAA ATPase complex (GO:0034098)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0794, UBXD7 |

**关键文献**:
1. Cooperative assembly of p97 complexes involved in replication termination.. *Nature communications*. PMID: 36329031
2. Multiple UBX proteins reduce the ubiquitin threshold of the mammalian p97-UFD1-NPL4 unfoldase.. *eLife*. PMID: 35920641
3. UBXN7 cofactor of CRL3(KEAP1) and CRL2(VHL) ubiquitin ligase complexes mediates reciprocal regulation of NRF2 and HIF-1α proteins.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 33444648
4. UBXN7 facilitates SARS-CoV-2 replication via inhibiting the K48-linked ubiquitination of viral N protein.. *PLoS pathogens*. PMID: 41086194
5. Weighted gene co-expression network analysis reveals the hub genes associated with pulmonary hypertension.. *Experimental biology and medicine (Maywood, N.J.)*. PMID: 36740764

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.9% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 58.1% |
| 可用 PDB 条目 | 1WJ4, 2DAL, 2DLX, 5X3P, 5X4L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1WJ4, 2DAL, 2DLX, 5X3P, 5X4L）+ AlphaFold极高置信度预测（pLDDT=72.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036249, IPR006577, IPR009060, IPR054109, IPR029071; Pfam: PF13899, PF22566, PF00789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NPLOC4 | 0.999 | 0.998 | — |
| UFD1 | 0.999 | 0.997 | — |
| FAF2 | 0.999 | 0.994 | — |
| FAF1 | 0.999 | 0.994 | — |
| UBXN1 | 0.999 | 0.994 | — |
| VCP | 0.999 | 0.999 | — |
| ASPSCR1 | 0.997 | 0.994 | — |
| NSFL1C | 0.997 | 0.994 | — |
| VCPIP1 | 0.996 | 0.994 | — |
| KCTD10 | 0.995 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vcp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| PLAA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| NPLOC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| HIF1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| CUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| DDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| BRWD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 1WJ4, 2DAL, 2DLX, 5X3P, 5X4L | pLDDT=72.9, v6 | 预测+实验 |
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
1. UBXN7 — UBX domain-containing protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小489 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94888
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163960-UBXN7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94888
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000163960-UBXN7/subcellular

![](https://images.proteinatlas.org/48441/755_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/48441/755_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/48441/759_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/48441/759_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/48441/814_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/48441/814_B9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94888-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94888 |
| SMART | SM00594;SM00166; |
| UniProt Domain [FT] | DOMAIN 2..54; /note="UBA"; DOMAIN 285..304; /note="UIM"; DOMAIN 408..485; /note="UBX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00215" |
| InterPro | IPR036249;IPR006577;IPR009060;IPR054109;IPR029071;IPR017346;IPR001012;IPR050730; |
| Pfam | PF13899;PF22566;PF00789; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163960-UBXN7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL1 | Intact, Biogrid | true |
| CUL2 | Intact, Biogrid | true |
| CUL3 | Intact, Biogrid | true |
| CUL4A | Intact, Biogrid | true |
| CUL4B | Intact, Biogrid | true |
| HIF1A | Intact, Biogrid | true |
| NEDD8 | Intact, Biogrid | true |
| NPLOC4 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
