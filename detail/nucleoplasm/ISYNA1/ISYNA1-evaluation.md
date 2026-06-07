---
type: protein-evaluation
gene: "ISYNA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ISYNA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ISYNA1 / INO1 |
| 蛋白名称 | Inositol-3-phosphate synthase 1 |
| 蛋白大小 | 558 aa / 61.1 kDa |
| UniProt ID | Q9NPH2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 61.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002587, IPR013021, IPR036291; Pfam: PF01658, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: INO1 |

**关键文献**:
1. ISYNA1 is overexpressed in bladder carcinoma and regulates cell proliferation and apoptosis.. *Biochemical and biophysical research communications*. PMID: 31495492
2. The myo-inositol biosynthesis rate-limiting enzyme ISYNA1 suppresses the stemness of ovarian cancer via Notch1 pathway.. *Cellular signalling*. PMID: 37105506
3. Musashi2 promotes the progression of pancreatic cancer through a novel ISYNA1-p21/ZEB-1 pathway.. *Journal of cellular and molecular medicine*. PMID: 32779876
4. The Association Between Breast Cancer and Blood-Based Methylation of CD160, ISYNA1 and RAD51B in the Chinese Population.. *Frontiers in genetics*. PMID: 35812748
5. The paradoxical role of inositol in cancer: a consequence of the metabolic state of a tumor.. *Cancer metastasis reviews*. PMID: 35462605

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 87.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 90.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 90.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002587, IPR013021, IPR036291; Pfam: PF01658, PF07994 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IMPA1 | 0.994 | 0.000 | — |
| IMPA2 | 0.992 | 0.000 | — |
| INPP4A | 0.912 | 0.000 | — |
| INPP4B | 0.902 | 0.000 | — |
| INPP1 | 0.856 | 0.000 | — |
| CDIPT | 0.816 | 0.000 | — |
| BPNT1 | 0.782 | 0.000 | — |
| IMPAD1 | 0.761 | 0.000 | — |
| GTF2B | 0.707 | 0.000 | — |
| MIOX | 0.701 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2CA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NME2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DUSP14 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| V | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| Kcnma1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-9475|pubmed:19423573 |
| ptsA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPA8 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ISYNA1 — Inositol-3-phosphate synthase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPH2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105655-ISYNA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ISYNA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPH2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000105655-ISYNA1/subcellular

![](https://images.proteinatlas.org/7931/113_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/7931/113_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/7931/1272_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/7931/1272_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/7931/161_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/7931/161_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPH2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NPH2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002587;IPR013021;IPR036291; |
| Pfam | PF01658;PF07994; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000105655-ISYNA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNF | Biogrid | false |
| CYSRT1 | Intact | false |
| EZR | Biogrid | false |
| POT1 | Intact | false |
| PRNP | Biogrid | false |
| TRAF4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
