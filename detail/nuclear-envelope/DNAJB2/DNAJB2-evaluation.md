---
type: protein-evaluation
gene: "DNAJB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB2 |
| 蛋白名称 | DnaJ homolog subfamily B member 2 |
| 蛋白大小 | 324 aa / 35.6 kDa |
| UniProt ID | P25686 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear membrane; UniProt: Cytoplasm; Nucleus; Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 324 aa / 35.6 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=44 篇 (<=60->6) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=67.4; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Enhanced |
| UniProt | Cytoplasm; Nucleus; Endoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 61 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Co-Existing Charcot-Marie-Tooth Disease Type II and Parkinson's Disease Linked to a Novel DNAjB2 Pathogenic Variant.. *J Cent Nerv Syst Dis*. PMID: 41799927
2. Broadening the Clinical Spectrum of Axonal Hereditary Neuropathies: A Comparative Case Study on DNAJB2- and HINT1-Related Disease.. *J Peripher Nerv Syst*. PMID: 41549766
3. Unraveling Peripheral Neuropathy in Parkinsonism from Acquired to Genetic Forms: A Review with Diagnostic Framework for Clinicians.. *Mov Disord Clin Pract*. PMID: 41492790
4. Charcot-Marie-Tooth Hereditary Neuropathy Overview.. **. PMID: 20301532
5. DNAJB2 Attenuates Rosacea Skin Inflammation and Angiogenesis by Inhibiting the Endoplasmic Reticulum Stress-mediated TLR2/Myd88/NF-κB pathway.. *Inflammation*. PMID: 40035989

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 24.4% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 48.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.4），有序残基占 48.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| GRPEL1 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSPA9 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| HSPH1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 无 | pLDDT=67.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endoplasmic reticulum membrane / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DNAJB2 -- DnaJ homolog subfamily B member 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小324 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P25686
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135924-DNAJB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P25686
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P25686-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P25686 |
| SMART | SM00271;SM00726; |
| UniProt Domain [FT] | DOMAIN 2..71; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286"; DOMAIN 210..226; /note="UIM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00213"; DOMAIN 250..269; /note="UIM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00213" |
| InterPro | IPR001623;IPR018253;IPR043183;IPR036869;IPR003903; |
| Pfam | PF00226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135924-DNAJB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CFTR | Biogrid | false |
| DNAJC7 | Biogrid | false |
| FKBP8 | Biogrid | false |
| HSPA1A | Biogrid | false |
| HSPA2 | Biogrid | false |
| HSPA4 | Biogrid | false |
| HSPA6 | Biogrid | false |
| HSPA8 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
