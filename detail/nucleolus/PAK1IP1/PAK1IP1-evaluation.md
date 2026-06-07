---
type: protein-evaluation
gene: "PAK1IP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAK1IP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAK1IP1 / PIP1, WDR84 |
| 蛋白名称 | p21-activated protein kinase-interacting protein 1 |
| 蛋白大小 | 392 aa / 44.0 kDa |
| UniProt ID | Q9NWT1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 392 aa / 44.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051959, IPR015943, IPR020472, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.5/180** | |
| **归一化总分** | | | **79.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PIP1, WDR84 |

**关键文献**:
1. Endothelial TBK1 Deficiency Inhibits Endothelial-to-Mesenchymal Transition and Atherogenesis Through Suppressing PAK1/ERK1/2 Signaling.. *Circulation research*. PMID: 41685426
2. PAK1IP1, a ribosomal stress-induced nucleolar protein, regulates cell proliferation via the p53-MDM2 loop.. *Nucleic acids research*. PMID: 21097889
3. A mutation in mouse Pak1ip1 causes orofacial clefting while human PAK1IP1 maps to 6p24 translocation breaking points associated with orofacial clefting.. *PloS one*. PMID: 23935987
4. Identification of qPCR reference genes suitable for normalising gene expression in the developing mouse embryo.. *Wellcome open research*. PMID: 35509373
5. Identification of suitable qPCR reference genes for the normalization of gene expression in the BL10-mdx and D2-mdx mouse models of Duchenne muscular dystrophy.. *PloS one*. PMID: 39999085

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 68.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 18.1% |
| 有序区域 (pLDDT>70) 占比 | 76.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 76.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051959, IPR015943, IPR020472, IPR019775, IPR036322; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSL24D1 | 0.975 | 0.422 | — |
| RPF2 | 0.973 | 0.154 | — |
| NIP7 | 0.923 | 0.098 | — |
| EBNA1BP2 | 0.915 | 0.095 | — |
| MRTO4 | 0.898 | 0.095 | — |
| BRIX1 | 0.898 | 0.095 | — |
| GNL2 | 0.895 | 0.000 | — |
| RRP15 | 0.890 | 0.399 | — |
| GTPBP4 | 0.885 | 0.099 | — |
| MAK16 | 0.884 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PPAN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| H1-4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL37A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PAK1IP1 — p21-activated protein kinase-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小392 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWT1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111845-PAK1IP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAK1IP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWT1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000111845-PAK1IP1/subcellular

![](https://images.proteinatlas.org/30111/1684_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30111/1684_B1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWT1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NWT1 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051959;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111845-PAK1IP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPL10 | Biogrid, Bioplex | true |
| RPS6 | Biogrid, Bioplex | true |
| ABT1 | Bioplex | false |
| FGFBP1 | Bioplex | false |
| H1-1 | Bioplex | false |
| H1-4 | Bioplex | false |
| HMGN4 | Bioplex | false |
| LIN28A | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
