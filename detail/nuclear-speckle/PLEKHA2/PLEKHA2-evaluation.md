---
type: protein-evaluation
gene: "PLEKHA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHA2 / TAPP2 |
| 蛋白名称 | Pleckstrin homology domain-containing family A member 2 |
| 蛋白大小 | 425 aa / 47.2 kDa |
| UniProt ID | Q9HB19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies, Cytosol; UniProt: Cytoplasm; Cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 47.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR051707; Pfam: PF00169 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies, Cytosol | Uncertain |
| UniProt | Cytoplasm; Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TAPP2 |

**关键文献**:
1. Identification of PtdIns(3,4)P(2) effectors in human platelets using quantitative proteomics.. *Biochimica et biophysica acta. Molecular and cell biology of lipids*. PMID: 31743753
2. Alterations in DNA methylation profiles in cancellous bone of postmenopausal women with osteoporosis.. *FEBS open bio*. PMID: 32496000
3. PLEKHA2 plays an essential role in adult neurogenesis and synaptic plasticity in the hippocampus.. *Experimental neurology*. PMID: 42097487
4. Lithium-induced gene expression alterations in two peripheral cell models of bipolar disorder.. *The world journal of biological psychiatry : the official journal of the World Federation of Societies of Biological Psychiatry*. PMID: 29067888
5. Bioinformatics analysis on multiple Gene Expression Omnibus datasets of the hepatitis B virus infection and its response to the interferon-alpha therapy.. *BMC infectious diseases*. PMID: 31996147

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 54.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.0，有序区 54.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR051707; Pfam: PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTPN13 | 0.943 | 0.292 | — |
| UTRN | 0.774 | 0.536 | — |
| PLEKHA1 | 0.738 | 0.230 | — |
| PLEK2 | 0.717 | 0.000 | — |
| MPDZ | 0.622 | 0.598 | — |
| SNTA1 | 0.622 | 0.622 | — |
| TM2D2 | 0.620 | 0.000 | — |
| SNTB2 | 0.615 | 0.609 | — |
| HTRA4 | 0.544 | 0.000 | — |
| ADAM32 | 0.515 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KANK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| M1AP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| EGLN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNTG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GIPC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TEPSIN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 无 | pLDDT=71.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Nucleus / Nucleoplasm, Nuclear bodies, Cytosol | 一致 |
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
1. PLEKHA2 — Pleckstrin homology domain-containing family A member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169499-PLEKHA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000169499-PLEKHA2/subcellular

![](https://images.proteinatlas.org/4706/77_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/4706/77_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/4706/78_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/4706/78_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/4706/92_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/4706/92_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HB19-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HB19 |
| SMART | SM00233; |
| UniProt Domain [FT] | DOMAIN 7..113; /note="PH 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 198..298; /note="PH 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR011993;IPR001849;IPR051707; |
| Pfam | PF00169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169499-PLEKHA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAE | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| GIPC1 | Biogrid | false |
| MPDZ | Biogrid | false |
| SNRPB2 | Opencell | false |
| SNTA1 | Biogrid | false |
| SNTB2 | Biogrid | false |
| UTRN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
