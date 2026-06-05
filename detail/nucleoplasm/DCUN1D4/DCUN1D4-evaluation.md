---
type: protein-evaluation
gene: "DCUN1D4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCUN1D4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCUN1D4 / KIAA0276 |
| 蛋白名称 | DCN1-like protein 4 |
| 蛋白大小 | 292 aa / 34.1 kDa |
| UniProt ID | Q92564 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 34.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.7; PDB: 5V89 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR014764, IPR042460, IPR005176; Pfam: PF03556 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0276 |

**关键文献**:
1. Whole transcriptome analysis of platelet concentrates during storage.. *Blood transfusion = Trasfusione del sangue*. PMID: 35175191
2. Identification of Serum Exosomal MicroRNA Expression Profiling in Menopausal Females with Osteoporosis by High-throughput Sequencing.. *Current medical science*. PMID: 33428145
3. circDCUN1D4 suppresses tumor metastasis and glycolysis in lung adenocarcinoma by stabilizing TXNIP expression.. *Molecular therapy. Nucleic acids*. PMID: 33425493
4. Resequencing Composite Kazakh Whiteheaded Cattle: Insights into Ancestral Breed Contributions, Selection Signatures, and Candidate Genetic Variants.. *Animals : an open access journal from MDPI*. PMID: 39943155

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 64.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 18.8% |
| 有序区域 (pLDDT>70) 占比 | 70.6% |
| 可用 PDB 条目 | 5V89 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.7，有序区 70.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014764, IPR042460, IPR005176; Pfam: PF03556 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.906 | 0.647 | — |
| UBE2M | 0.896 | 0.712 | — |
| CUL1 | 0.848 | 0.805 | — |
| CUL2 | 0.845 | 0.625 | — |
| CAND1 | 0.766 | 0.292 | — |
| UBE2F | 0.743 | 0.266 | — |
| CUL4B | 0.715 | 0.292 | — |
| RBX1 | 0.713 | 0.347 | — |
| DCUN1D1 | 0.704 | 0.073 | — |
| CUL4A | 0.703 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| ARL4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MSRB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000334625.5 | psi-mi:"MI:1204"(split firefly luciferase compleme | imex:IM-21138|pubmed:21911577 |
| AFP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITIH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PCK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DDX21 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| ENST00000334635 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 5V89 | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCUN1D4 — DCN1-like protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92564
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109184-DCUN1D4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCUN1D4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92564
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000109184-DCUN1D4/subcellular

![](https://images.proteinatlas.org/36483/1743_C7_27_cr57ff82eca4454_blue_red_green.jpg)
![](https://images.proteinatlas.org/36483/1743_C7_3_cr57ff82e2d3d85_blue_red_green.jpg)
![](https://images.proteinatlas.org/36483/544_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36483/544_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36484/403_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36484/403_D11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92564-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
