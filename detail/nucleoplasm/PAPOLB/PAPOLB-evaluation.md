---
type: protein-evaluation
gene: "PAPOLB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAPOLB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAPOLB / PAPT |
| 蛋白名称 | Poly(A) polymerase beta |
| 蛋白大小 | 637 aa / 71.8 kDa |
| UniProt ID | Q9NRJ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 637 aa / 71.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043519, IPR011068, IPR007012, IPR048840, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAPT |

**关键文献**:
1. The poly(A) polymerase beta gene may not be associated with azoospermia caused by Sertoli-cell-only syndrome in Japanese patients by comparing patients and normal controls.. *Journal of obstetrics and gynaecology : the journal of the Institute of Obstetrics and Gynaecology*. PMID: 30744435
2. MiR-125b-2 Knockout in Testis Is Associated with Targeting to the PAP Gene, Mitochondrial Copy Number, and Impaired Sperm Quality.. *International journal of molecular sciences*. PMID: 30609807
3. BNC1 Promotes Spermatogenesis by Regulating Transcription of Ybx2 and Papolb via Direct Binding to Their Promotor Elements.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 33211273
4. Use of Genome-Scale Integrated Analysis to Identify Key Genes and Potential Molecular Mechanisms in Recurrence of Lower-Grade Brain Glioma.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 31104065

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 23.7% |
| 有序区域 (pLDDT>70) 占比 | 73.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.4，有序区 73.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043519, IPR011068, IPR007012, IPR048840, IPR007010; Pfam: PF04928, PF20750, PF04926 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTREX | 0.995 | 0.135 | — |
| ZCCHC7 | 0.994 | 0.000 | — |
| SYMPK | 0.994 | 0.785 | — |
| SNRNP70 | 0.988 | 0.235 | — |
| CPSF3 | 0.964 | 0.783 | — |
| CPSF1 | 0.959 | 0.785 | — |
| FIP1L1 | 0.957 | 0.789 | — |
| CSTF3 | 0.949 | 0.841 | — |
| CSTF2 | 0.941 | 0.719 | — |
| WDR33 | 0.935 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tcf3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 无 | pLDDT=79.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. PAPOLB — Poly(A) polymerase beta，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小637 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRJ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000218823-PAPOLB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAPOLB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRJ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000218823-PAPOLB/subcellular

![](https://images.proteinatlas.org/47285/1944_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/47285/1944_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/47285/2013_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/47285/2013_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRJ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRJ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043519;IPR011068;IPR007012;IPR048840;IPR007010;IPR014492; |
| Pfam | PF04928;PF20750;PF04926; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000218823-PAPOLB/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
