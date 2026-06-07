---
type: protein-evaluation
gene: "CPNE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPNE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPNE2 |
| 蛋白名称 | Copine-2 |
| 蛋白大小 | 548 aa / 61.2 kDa |
| UniProt ID | Q96FN4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Mitochondria, Cytosol; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 548 aa / 61.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.1; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CPNE2 might serve as a new negative prognostic biomarker in gastric cancer.. *3 Biotech*. PMID: 40893153
2. Micro RNA 181c-5p: A promising target for post-stroke recovery in socially isolated mice.. *Neuroscience letters*. PMID: 31722236
3. Antineoplastic Nature of WWOX in Glioblastoma Is Mainly a Consequence of Reduced Cell Viability and Invasion.. *Biology*. PMID: 36979157
4. Identification of Key Genes Associated with Risk and Prognosis of Neuroblastoma.. *Journal of molecular neuroscience : MN*. PMID: 36443552

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.1 |
| 高置信度残基 (pLDDT>90) 占比 | 81.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.1，有序区 94.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010734; Pfam: PF00168, PF07002 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSME3IP1 | 0.544 | 0.000 | — |
| PRKRIP1 | 0.521 | 0.000 | — |
| CMTR2 | 0.482 | 0.000 | — |
| COG4 | 0.472 | 0.000 | — |
| RAD1 | 0.470 | 0.000 | — |
| POLR2D | 0.468 | 0.468 | — |
| CHCHD1 | 0.420 | 0.000 | — |
| UBA3 | 0.416 | 0.401 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| Grb2 | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| SORBS3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KATNBL1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| THAP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GBP7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 1 / 8 = 12%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.1 + PDB: 无 | pLDDT=91.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nucleoplasm, Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CPNE2 -- Copine-2，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小548 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FN4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140848-CPNE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPNE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FN4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000140848-CPNE2/subcellular

![](https://images.proteinatlas.org/41132/1319_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/41132/1319_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/41132/403_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/41132/403_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/41132/408_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/41132/408_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96FN4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96FN4 |
| SMART | SM00239;SM00327; |
| UniProt Domain [FT] | DOMAIN 5..131; /note="C2 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 138..263; /note="C2 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 305..507; /note="VWFA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00219" |
| InterPro | IPR000008;IPR035892;IPR037768;IPR045052;IPR010734;IPR002035;IPR036465; |
| Pfam | PF00168;PF07002; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140848-CPNE2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| THAP4 | Intact, Biogrid, Bioplex | true |
| ANAPC13 | Bioplex | false |
| ANLN | Biogrid | false |
| BVES | Bioplex | false |
| CT55 | Intact | false |
| DMAP1 | Bioplex | false |
| EFHC2 | Intact | false |
| EWSR1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
