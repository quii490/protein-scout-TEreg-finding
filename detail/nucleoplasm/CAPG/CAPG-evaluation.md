---
type: protein-evaluation
gene: "CAPG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAPG — REJECTED (研究热度过高 (PubMed strict=214，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAPG / AFCP, MCP |
| 蛋白名称 | Macrophage-capping protein |
| 蛋白大小 | 348 aa / 38.5 kDa |
| UniProt ID | P40121 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic chromosome; UniProt: Nucleus; Cytoplasm; Melanosome; Cell projection, lamellipodi |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 38.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=214 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.4; PDB: 1J72, 1JHW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029006, IPR007123, IPR007122; Pfam: PF00626 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome | Supported |
| UniProt | Nucleus; Cytoplasm; Melanosome; Cell projection, lamellipodium; Cell projection, ruffle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- centriole (GO:0005814)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- F-actin capping protein complex (GO:0008290)
- Flemming body (GO:0090543)
- lamellipodium (GO:0030027)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 214 |
| PubMed broad count | 303 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AFCP, MCP |

**关键文献**:
1. A novel polypeptide CAPG-171aa encoded by circCAPG plays a critical role in triple-negative breast cancer.. *Molecular cancer*. PMID: 37408008
2. Increased CAPG inhibits ferroptosis to drive tumor proliferation and sorafenib resistance in hepatocellular carcinoma via the WDR74-p53-SLC7A11 pathway.. *International journal of biological sciences*. PMID: 40959275
3. CAPG and GIPC1: Breast Cancer Biomarkers for Bone Metastasis Development and Treatment.. *Journal of the National Cancer Institute*. PMID: 26757732
4. Super-enhancer-associated gene CAPG promotes AML progression.. *Communications biology*. PMID: 37296281
5. Differential Intracellular Protein Distribution in Cancer and Normal Cells-Beta-Catenin and CapG in Gynecologic Malignancies.. *Cancers*. PMID: 36230711

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.4 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 37.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 1J72, 1JHW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1J72, 1JHW）+ AlphaFold高质量预测（pLDDT=86.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029006, IPR007123, IPR007122; Pfam: PF00626 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTPN | 0.754 | 0.042 | — |
| ADD2 | 0.744 | 0.000 | — |
| ADD1 | 0.741 | 0.000 | — |
| CAPZB | 0.690 | 0.000 | — |
| CFL1 | 0.640 | 0.180 | — |
| CAPZA2 | 0.599 | 0.000 | — |
| CRIP1 | 0.598 | 0.469 | — |
| CAPZA1 | 0.572 | 0.000 | — |
| CAPZA3 | 0.560 | 0.000 | — |
| CFL2 | 0.527 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YCG1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| NCAPG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| TAM41 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Kcnma1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-9475|pubmed:19423573 |
| SMC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10811823|imex:IM-19494 |
| SMC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10811823|imex:IM-19494 |
| RLF2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.4 + PDB: 1J72, 1JHW | pLDDT=86.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Melanosome; Cell projection, l / Nucleoplasm; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CAPG — Macrophage-capping protein，研究基础较多，新颖性有限。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 214 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 214 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40121
- Protein Atlas: https://www.proteinatlas.org/ENSG00000042493-CAPG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAPG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40121
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000042493-CAPG/subcellular

![](https://images.proteinatlas.org/19080/2120_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/19080/2120_F8_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/19080/2132_E5_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/19080/2132_E5_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/19080/2171_A3_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/19080/2171_A3_76_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P40121-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P40121 |
| SMART | SM00262; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029006;IPR007123;IPR007122; |
| Pfam | PF00626; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000042493-CAPG/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SIAH1 | Intact | false |
| SPRED1 | Intact | false |
| STK38 | Biogrid | false |
| TRUB1 | Intact, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
