---
type: protein-evaluation
gene: "SRRM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SRRM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRRM1 / SRM160 |
| 蛋白名称 | Serine/arginine repetitive matrix protein 1 |
| 蛋白大小 | 904 aa / 102.3 kDa |
| UniProt ID | Q8IYB3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus matrix; Nucleus speckle |
| 蛋白大小 | 8/10 | ×1 | 8 | 904 aa / 102.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.6; PDB: 1MP1, 6FF4, 6FF7, 7ABG, 7ABH, 7ABI, 7DVQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002483, IPR036483, IPR052225; Pfam: PF01480 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Enhanced |
| UniProt | Nucleus matrix; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- cytosol (GO:0005829)
- nuclear matrix (GO:0016363)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SRM160 |

**关键文献**:
1. Identification of a lactylation-related gene signature to characterize subtypes of hepatocellular carcinoma using bulk sequencing data.. *Journal of gastrointestinal oncology*. PMID: 39279958
2. A Prion-Like Domain in EBV EBNA1 Promotes Phase Separation and Enables SRRM1 Splicing.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40729735
3. A multi-scale map of cell structure fusing protein images and interactions.. *Nature*. PMID: 34819669
4. Single-cell RNA sequencing reveals the critical role of alternative splicing in cattle testicular spermatagonia.. *Biology direct*. PMID: 39726007
5. Dysregulation of the splicing machinery is directly associated to aggressiveness of prostate cancer.. *EBioMedicine*. PMID: 31902674

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.6 |
| 高置信度残基 (pLDDT>90) 占比 | 3.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.8% |
| 低置信 (pLDDT<50) 占比 | 66.7% |
| 有序区域 (pLDDT>70) 占比 | 18.5% |
| 可用 PDB 条目 | 1MP1, 6FF4, 6FF7, 7ABG, 7ABH, 7ABI, 7DVQ, 8I0P, 8I0R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.6），有序残基占 18.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002483, IPR036483, IPR052225; Pfam: PF01480 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRRM2 | 0.999 | 0.935 | — |
| RNPS1 | 0.999 | 0.222 | — |
| UPF3A | 0.999 | 0.994 | — |
| RBM25 | 0.999 | 0.687 | — |
| UPF2 | 0.998 | 0.994 | — |
| NXF1 | 0.997 | 0.994 | — |
| UPF1 | 0.997 | 0.994 | — |
| ALYREF | 0.993 | 0.638 | — |
| TCERG1 | 0.984 | 0.800 | — |
| SRSF11 | 0.984 | 0.339 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG10324 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ABI1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SPOP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| CG18546 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3918 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG6843 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.6 + PDB: 1MP1, 6FF4, 6FF7, 7ABG, 7ABH,  | pLDDT=51.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix; Nucleus speckle / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SRRM1 — Serine/arginine repetitive matrix protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小904 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYB3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133226-SRRM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRRM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYB3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000133226-SRRM1/subcellular

![](https://images.proteinatlas.org/49941/694_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/49941/694_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/49941/736_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/49941/736_F9_3_red_green.jpg)
![](https://images.proteinatlas.org/49941/805_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/49941/805_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYB3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IYB3 |
| SMART | SM00311; |
| UniProt Domain [FT] | DOMAIN 27..126; /note="PWI"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00627" |
| InterPro | IPR002483;IPR036483;IPR052225; |
| Pfam | PF01480; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133226-SRRM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLK2 | Intact, Biogrid | true |
| RBM39 | Biogrid, Opencell | true |
| RNPS1 | Intact, Biogrid | true |
| SF3B1 | Biogrid, Opencell | true |
| SNRPA | Biogrid, Opencell | true |
| SNRPB | Biogrid, Opencell | true |
| SNRPB2 | Biogrid, Opencell | true |
| SNRPC | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
