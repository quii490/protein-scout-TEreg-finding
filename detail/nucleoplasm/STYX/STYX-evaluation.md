---
type: protein-evaluation
gene: "STYX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STYX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STYX |
| 蛋白名称 | Serine/threonine/tyrosine-interacting protein |
| 蛋白大小 | 223 aa / 25.5 kDa |
| UniProt ID | Q8WUJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 223 aa / 25.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 2R0B |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000340, IPR029021, IPR052449, IPR000387, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 127 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. STYX: a versatile pseudophosphatase.. *Biochemical Society transactions*. PMID: 28408485
2. Understanding Pseudophosphatase Function Through Biochemical Interactions.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 38147206
3. Evolutionary genomic relationships and coupling in MK-STYX and STYX pseudophosphatases.. *Scientific reports*. PMID: 35264672
4. The DUSP domain of pseudophosphatase MK-STYX interacts with G3BP1 to decrease stress granules.. *Archives of biochemistry and biophysics*. PMID: 37516290
5. Pseudophosphatase STYX promotes tumor growth and metastasis by inhibiting FBXW7 function in colorectal cancer.. *Cancer letters*. PMID: 30981757

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 74.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 2R0B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 84.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR029021, IPR052449, IPR000387, IPR020422; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBXW7 | 0.798 | 0.692 | — |
| MAPK1 | 0.683 | 0.441 | — |
| GNPNAT1 | 0.611 | 0.053 | — |
| TXNDC16 | 0.586 | 0.000 | — |
| MAPK3 | 0.568 | 0.243 | — |
| SKP1 | 0.560 | 0.223 | — |
| FBXO38 | 0.557 | 0.525 | — |
| GPR137C | 0.550 | 0.000 | — |
| CUL1 | 0.533 | 0.105 | — |
| DDHD1 | 0.511 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRMU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GARIN1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POLR2J | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LAMTOR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 2R0B | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. STYX — Serine/threonine/tyrosine-interacting protein，非常新颖，仅有少数基础研究。
2. 蛋白大小223 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198252-STYX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STYX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198252-STYX/subcellular

![](https://images.proteinatlas.org/40290/1129_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/40290/1129_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/40290/487_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/40290/487_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/40290/491_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/40290/491_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUJ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WUJ0 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 28..176; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR029021;IPR052449;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198252-STYX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXW7 | Intact, Biogrid | true |
| CAP1 | Biogrid | false |
| FAM172A | Biogrid | false |
| FBXL12 | Biogrid | false |
| FBXO38 | Biogrid | false |
| KPNA1 | Biogrid | false |
| MAPK1 | Biogrid | false |
| MYH8 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
