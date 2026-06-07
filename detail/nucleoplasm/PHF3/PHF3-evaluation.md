---
type: protein-evaluation
gene: "PHF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF3 / KIAA0244 |
| 蛋白名称 | PHD finger protein 3 |
| 蛋白大小 | 2039 aa / 229.5 kDa |
| UniProt ID | Q92576 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2039 aa / 229.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.0; PDB: 2DME, 6IC8, 6IC9, 6Q2V, 6Q5Y |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012921, IPR003618, IPR036575, IPR019786, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0244 |

**关键文献**:
1. The SPOC proteins DIDO3 and PHF3 co-regulate gene expression and neuronal differentiation.. *Nature communications*. PMID: 38036524
2. Loss of circIGF1R Suppresses Cardiomyocytes Proliferation by Sponging miR-362-5p.. *DNA and cell biology*. PMID: 37347924
3. Genomic analysis of 116 autism families strengthens known risk genes and highlights promising candidates.. *NPJ genomic medicine*. PMID: 38519481
4. PhCHS5 and PhF3'5'H Genes Over-Expression in Petunia (Petunia hybrida) and Phalaenopsis (Phalaenopsis aphrodite) Regulate Flower Color and Branch Number.. *Plants (Basel, Switzerland)*. PMID: 37299183
5. PHF3 regulates neuronal gene expression through the Pol II CTD reader domain SPOC.. *Nature communications*. PMID: 34667177

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.0 |
| 高置信度残基 (pLDDT>90) 占比 | 7.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 80.3% |
| 有序区域 (pLDDT>70) 占比 | 17.6% |
| 可用 PDB 条目 | 2DME, 6IC8, 6IC9, 6Q2V, 6Q5Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.0），有序残基占 17.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012921, IPR003618, IPR036575, IPR019786, IPR011011; Pfam: PF00628, PF07744, PF07500 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NIPBL | 0.976 | 0.000 | — |
| POLR2A | 0.877 | 0.839 | — |
| PTP4A1 | 0.801 | 0.000 | — |
| POLR2E | 0.799 | 0.797 | — |
| HELZ | 0.787 | 0.000 | — |
| CEP350 | 0.784 | 0.000 | — |
| SETD2 | 0.766 | 0.000 | — |
| SETX | 0.722 | 0.000 | — |
| BPTF | 0.680 | 0.000 | — |
| TRIP12 | 0.661 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| NR3C1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| MAPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBA52 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.0 + PDB: 2DME, 6IC8, 6IC9, 6Q2V, 6Q5Y | pLDDT=43.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PHF3 — PHD finger protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小2039 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=43.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92576
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118482-PHF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92576
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000118482-PHF3/subcellular

![](https://images.proteinatlas.org/25763/583_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/25763/583_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/25763/598_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/25763/598_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/25763/602_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/25763/602_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92576-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92576 |
| SMART | SM00249;SM00510; |
| UniProt Domain [FT] | DOMAIN 927..1046; /note="TFIIS central"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00651" |
| InterPro | IPR012921;IPR003618;IPR036575;IPR019786;IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF00628;PF07744;PF07500; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118482-PHF3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SUPT5H | Biogrid, Opencell | true |
| CPSF6 | Opencell | false |
| MAPK3 | Biogrid | false |
| MYC | Biogrid | false |
| SNRPA | Opencell | false |
| SNRPB | Opencell | false |
| SNRPC | Opencell | false |
| SNRPF | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
