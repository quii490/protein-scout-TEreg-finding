---
type: protein-evaluation
gene: "POGLUT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POGLUT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POGLUT3 / KDELC2 |
| 蛋白名称 | Protein O-glucosyltransferase 3 |
| 蛋白大小 | 507 aa / 58.6 kDa |
| UniProt ID | Q7Z4H8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 507 aa / 58.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006598, IPR017868, IPR001298, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- endoplasmic reticulum lumen (GO:0005788)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KDELC2 |

**关键文献**:
1. Identification, function, and biological relevance of POGLUT2 and POGLUT3.. *Biochemical Society transactions*. PMID: 35411374
2. POGLUT2 and POGLUT3: Two essential protein O-glucosyltransferases modifying EGF repeats in extracellular matrix proteins.. *Biochimica et biophysica acta. General subjects*. PMID: 41955902
3. POGLUT2 and POGLUT3 O-glucosylate multiple EGF repeats in fibrillin-1, -2, and LTBP1 and promote secretion of fibrillin-1.. *The Journal of biological chemistry*. PMID: 34411563
4. Identifying proteomic risk factors for overall, aggressive, and early onset prostate cancer using Mendelian Randomisation and tumour spatial transcriptomics.. *EBioMedicine*. PMID: 38878676
5. Marfan syndrome variation of the POGLUT2 and POGLUT3 consensus sequence can produce aberrant fibrillin-1 O-glucosylation.. *The Journal of biological chemistry*. PMID: 40107616

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 86.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.9，有序区 92.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006598, IPR017868, IPR001298, IPR013783, IPR014756; Pfam: PF00630, PF05686 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POFUT1 | 0.680 | 0.111 | — |
| C11orf65 | 0.665 | 0.000 | — |
| NPAT | 0.596 | 0.071 | — |
| GXYLT1 | 0.581 | 0.000 | — |
| ELMOD1 | 0.554 | 0.000 | — |
| EOGT | 0.545 | 0.000 | — |
| GXYLT2 | 0.493 | 0.000 | — |
| EXPH5 | 0.487 | 0.000 | — |
| XXYLT1 | 0.479 | 0.000 | — |
| SLC35F2 | 0.461 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| tap | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TUFM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| TCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| FBXO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EBI-25475900 | psi-mi:"MI:0096"(pull down) | imex:IM-28441|pubmed:33060197 |
| C1QTNF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 无 | pLDDT=92.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. POGLUT3 — Protein O-glucosyltransferase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小507 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4H8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178202-POGLUT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POGLUT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4H8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000178202-POGLUT3/subcellular

![](https://images.proteinatlas.org/39817/418_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/39817/418_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/39817/424_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/39817/424_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/39817/429_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/39817/429_C7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z4H8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z4H8 |
| SMART | SM00672;SM00557; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006598;IPR017868;IPR001298;IPR013783;IPR014756;IPR051091; |
| Pfam | PF00630;PF05686; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178202-POGLUT3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXO6 | Biogrid, Bioplex | true |
| CALR3 | Biogrid | false |
| CANX | Opencell | false |
| CBLN4 | Bioplex | false |
| ENPP7 | Bioplex | false |
| FBXO2 | Bioplex | false |
| MFAP4 | Bioplex | false |
| PRG2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
