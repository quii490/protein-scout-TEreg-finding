---
type: protein-evaluation
gene: "EEF1D"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EEF1D 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF1D / EF1D |
| 蛋白名称 | Elongation factor 1-delta |
| 蛋白大小 | 281 aa / 31.1 kDa |
| UniProt ID | P29692 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 281 aa / 31.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.0; PDB: 2MVM, 2MVN, 2N51, 5JPO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036219, IPR018940, IPR049720, IPR014038, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- eukaryotic translation elongation factor 1 complex (GO:0005853)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EF1D |

**关键文献**:
1. Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders.. *JAMA psychiatry*. PMID: 28097321
2. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
3. LGALS9B stabilizes EEF1D protein and activates the PI3K/AKT signaling pathway to promote gastric cancer occurrence and metastasis.. *Oncogene*. PMID: 39639171
4. EEF1D Promotes Glioma Proliferation, Migration, and Invasion through EMT and PI3K/Akt Pathway.. *BioMed research international*. PMID: 33029523
5. Regulation of translation factor EEF1D gene function by alternative splicing.. *International journal of molecular sciences*. PMID: 25686034

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 40.6% |
| 中等置信 (pLDDT 50-70) 占比 | 22.8% |
| 低置信 (pLDDT<50) 占比 | 16.4% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 2MVM, 2MVN, 2N51, 5JPO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MVM, 2MVN, 2N51, 5JPO）+ AlphaFold高质量预测（pLDDT=73.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036219, IPR018940, IPR049720, IPR014038, IPR014717; Pfam: PF10587, PF00736 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF1G | 0.999 | 0.999 | — |
| EEF1B2 | 0.999 | 0.845 | — |
| EEF1A1 | 0.997 | 0.870 | — |
| VARS1 | 0.978 | 0.900 | — |
| KTN1 | 0.969 | 0.630 | — |
| EEF1A2 | 0.960 | 0.724 | — |
| RPS19 | 0.952 | 0.178 | — |
| RPS11 | 0.951 | 0.130 | — |
| TPT1 | 0.950 | 0.290 | — |
| RPL23 | 0.950 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000487680.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ASCC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FRA10AC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HEXD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CD48 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 2MVM, 2MVN, 2N51, 5JPO | pLDDT=73.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EEF1D — Elongation factor 1-delta，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小281 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29692
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104529-EEF1D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF1D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29692
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000104529-EEF1D/subcellular

![](https://images.proteinatlas.org/51002/700_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/51002/700_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/51002/722_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/51002/722_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/51002/726_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/51002/726_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P29692-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P29692 |
| SMART | SM01182;SM00888; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036219;IPR018940;IPR049720;IPR014038;IPR014717;IPR001326; |
| Pfam | PF10587;PF00736; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104529-EEF1D/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABTB1 | Intact, Biogrid | true |
| EEF1A2 | Intact, Biogrid | true |
| EEF1G | Intact, Biogrid | true |
| ERP27 | Intact, Biogrid | true |
| SIAH1 | Intact, Biogrid | true |
| ACE2 | Biogrid | false |
| ANLN | Biogrid | false |
| ARHGAP21 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
