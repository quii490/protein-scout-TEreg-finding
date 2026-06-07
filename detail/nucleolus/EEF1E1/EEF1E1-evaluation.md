---
type: protein-evaluation
gene: "EEF1E1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EEF1E1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF1E1 / AIMP3, P18 |
| 蛋白名称 | Eukaryotic translation elongation factor 1 epsilon-1 |
| 蛋白大小 | 174 aa / 19.8 kDa |
| UniProt ID | O43324 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 174 aa / 19.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.4; PDB: 2UZ8, 4BL7, 4BVX, 4BVY, 5BMU, 5Y6L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR053837, IPR053836, IPR042450, IPR010987, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aminoacyl-tRNA synthetase multienzyme complex (GO:0017101)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AIMP3, P18 |

**关键文献**:
1. High-Intensity Interval Training Mitigates Sarcopenia and Suppresses the Myoblast Senescence Regulator EEF1E1.. *Journal of cachexia, sarcopenia and muscle*. PMID: 39276001
2. Phase separation of EEF1E1 promotes tumor stemness via PTEN/AKT-mediated DNA repair in hepatocellular carcinoma.. *Cancer letters*. PMID: 39884379
3. AIMP3 maintains cardiac homeostasis by regulating the editing activity of methionyl-tRNA synthetase.. *Nature cardiovascular research*. PMID: 40562875
4. CT Radiomics Combined with Metabolic-Biomarkers Enables Early Recurrence Prediction in Hepatocellular Carcinoma.. *Journal of hepatocellular carcinoma*. PMID: 41049156
5. Screening of underlying genetic biomarkers for ankylosing spondylitis.. *Molecular medicine reports*. PMID: 31059041

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 80.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |
| 可用 PDB 条目 | 2UZ8, 4BL7, 4BVX, 4BVY, 5BMU, 5Y6L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2UZ8, 4BL7, 4BVX, 4BVY, 5BMU, 5Y6L）+ AlphaFold极高置信度预测（pLDDT=92.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053837, IPR053836, IPR042450, IPR010987, IPR036282; Pfam: PF21972 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DARS1 | 0.999 | 0.977 | — |
| MARS1 | 0.999 | 0.982 | — |
| AIMP2 | 0.999 | 0.980 | — |
| EPRS1 | 0.999 | 0.972 | — |
| AIMP1 | 0.999 | 0.875 | — |
| LARS1 | 0.997 | 0.834 | — |
| KARS1 | 0.997 | 0.875 | — |
| QARS1 | 0.996 | 0.870 | — |
| IARS1 | 0.996 | 0.835 | — |
| RARS1 | 0.996 | 0.875 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| gag | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| VDAC1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| HSD17B10 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| PDHA1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SOAT1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 2UZ8, 4BL7, 4BVX, 4BVY, 5BMU,  | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Nucleus / Nucleoplasm, Cytosol | 一致 |
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
1. EEF1E1 — Eukaryotic translation elongation factor 1 epsilon-1，非常新颖，仅有少数基础研究。
2. 蛋白大小174 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43324
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124802-EEF1E1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF1E1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43324
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000124802-EEF1E1/subcellular

![](https://images.proteinatlas.org/27901/270_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27901/270_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/27901/271_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27901/271_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/27901/272_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27901/272_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43324-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43324 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 50..173; /note="GST C-terminal" |
| InterPro | IPR053837;IPR053836;IPR042450;IPR010987;IPR036282; |
| Pfam | PF21972; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124802-EEF1E1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IARS1 | Biogrid, Bioplex | true |
| LARS1 | Biogrid, Bioplex | true |
| QARS1 | Biogrid, Bioplex | true |
| AIMP1 | Biogrid | false |
| AIMP2 | Biogrid | false |
| CALCOCO2 | Intact | false |
| CAPZB | Opencell | false |
| DARS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
