---
type: protein-evaluation
gene: "TNIP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNIP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNIP3 / ABIN3, LIND |
| 蛋白名称 | TNFAIP3-interacting protein 3 |
| 蛋白大小 | 325 aa / 38.9 kDa |
| UniProt ID | Q96KP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear bodies, Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 325 aa / 38.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032419; Pfam: PF16516 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear bodies, Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABIN3, LIND |

**关键文献**:
1. Resolving the graft ischemia-reperfusion injury during liver transplantation at the single cell resolution.. *Cell death & disease*. PMID: 34103479
2. TNFAIP3 Interacting Protein 3 Is an Activator of Hippo-YAP Signaling Protecting Against Hepatic Ischemia/Reperfusion Injury.. *Hepatology (Baltimore, Md.)*. PMID: 34133792
3. TNIP3 protects against pathological cardiac hypertrophy by stabilizing STAT1.. *Cell death & disease*. PMID: 38926347
4. Tumour necrosis factor alpha-induced protein 3-interacting protein 3 overexpression protects against arrhythmogenic remodelling in the heart failure mice.. *Europace : European pacing, arrhythmias, and cardiac electrophysiology : journal of the working groups on cardiac pacing, arrhythmias, and cardiac cellular electrophysiology of the European Society of Cardiology*. PMID: 39800969
5. TNFAIP3 Interacting Protein 3 Overexpression Suppresses Nonalcoholic Steatohepatitis by Blocking TAK1 Activation.. *Cell metabolism*. PMID: 32268115

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 68.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 68.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032419; Pfam: PF16516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNFAIP3 | 0.935 | 0.636 | — |
| TNIP2 | 0.764 | 0.000 | — |
| TAX1BP1 | 0.659 | 0.618 | — |
| TNF | 0.497 | 0.299 | — |
| TNIP1 | 0.472 | 0.390 | — |
| NFKB1 | 0.457 | 0.292 | — |
| KRT40 | 0.445 | 0.437 | — |
| TRIM8 | 0.427 | 0.329 | — |
| IRAK3 | 0.413 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KIF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| RNH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| FBXO3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| TBK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CNKSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| GLDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ALDH9A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MCM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PPP6R3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Nuclear bodies, Plasma m | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TNIP3 — TNFAIP3-interacting protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小325 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KP6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050730-TNIP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNIP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000050730-TNIP3/subcellular

![](https://images.proteinatlas.org/43063/2207_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/43063/2207_C9_6_red_green.jpg)
![](https://images.proteinatlas.org/43063/468_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/43063/468_G5_4_red_green.jpg)
![](https://images.proteinatlas.org/43063/470_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/43063/470_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96KP6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96KP6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032419; |
| Pfam | PF16516; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000050730-TNIP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TNFAIP3 | Intact, Biogrid | true |
| TRIM8 | Intact, Biogrid | true |
| CCN3 | Intact | false |
| CRYAA | Intact | false |
| CYSRT1 | Intact | false |
| DAZAP2 | Intact | false |
| FAM161A | Intact | false |
| HTT | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
