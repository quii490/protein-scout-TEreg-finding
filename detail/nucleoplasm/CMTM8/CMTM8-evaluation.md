---
type: protein-evaluation
gene: "CMTM8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CMTM8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMTM8 |
| 蛋白名称 | CKLF-like MARVEL transmembrane domain-containing protein 8 |
| 蛋白大小 | 173 aa / 19.6 kDa |
| UniProt ID | Q8IZV2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Membrane; Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 173 aa / 19.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=77.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 13 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane; Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 37 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CKLF-like MARVEL transmembrane domain-containing superfamily 8 (CMTM8) promotes Notch signalling to maintain CD8(+) T cell- and NK cell-dependent tumour immune escape.. *Br J Pharmacol*. PMID: 42219547
2. CMTM8 variants influence BNT162b2 COVID-19 vaccination response by regulating granulocytic/polymorphonuclear myeloid-derived suppressor cell activity.. *Front Immunol*. PMID: 41659846
3. Transcriptomic Dysregulation in Animal Models of Attention-Deficit Hyperactivity Disorder and Nicotine Dependence Suggests Shared Neural Mechanisms.. *Brain Behav*. PMID: 40135637
4. Research advances of MAL family members in tumorigenesis and tumor progression (Review).. *Mol Med Rep*. PMID: 38362940
5. Current Opinions on the Relationship Between CMTM Family and Hepatocellular Carcinoma.. *J Hepatocell Carcinoma*. PMID: 37649636

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 38.7% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 71.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.6，有序区 71.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CMTM7 | 0.000 | 0.000 | — |
| CMTM6 | 0.000 | 0.000 | — |
| CKLF | 0.000 | 0.000 | — |
| CMTM3 | 0.000 | 0.000 | — |
| CMTM1 | 0.000 | 0.000 | — |
| CMTM5 | 0.000 | 0.000 | — |
| CMTM2 | 0.000 | 0.000 | — |
| MYADML2 | 0.000 | 0.000 | — |
| FRMD1 | 0.000 | 0.000 | — |
| CCDC155 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8IUG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NUH8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8IZV2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O00124 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O00258 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75146 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75787 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-20591397 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P14859 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P24468 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 30
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 无 | pLDDT=77.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 30 interactions | 数据充分 |

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
1. CMTM8 -- CKLF-like MARVEL transmembrane domain-containing protein 8，非常新颖，仅有少数基础研究。
2. 蛋白大小173 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZV2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170293-CMTM8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMTM8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZV2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZV2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZV2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 36..168; /note="MARVEL"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00581" |
| InterPro | IPR013295;IPR008253;IPR050578; |
| Pfam | PF01284; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170293-CMTM8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Intact | false |
| ICAM2 | Bioplex | false |
| KLRB1 | Bioplex | false |
| KRTAP1-3 | Intact | false |
| LRRC25 | Bioplex | false |
| SLC25A40 | Bioplex | false |
| STX17 | Bioplex | false |
| TMEM14B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
