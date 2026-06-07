---
type: protein-evaluation
gene: "DEDD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEDD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEDD2 / FLAME3 |
| 蛋白名称 | DNA-binding death effector domain-containing protein 2 |
| 蛋白大小 | 326 aa / 36.2 kDa |
| UniProt ID | Q8WXF8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 326 aa / 36.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011029, IPR001875, IPR038856, IPR049341; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FLAME3 |

**关键文献**:
1. Identification and characterization of DEDD2, a death effector domain-containing protein.. *The Journal of biological chemistry*. PMID: 11741985
2. DEDD and DEDD2 associate with caspase-8/10 and signal cell death.. *Oncogene*. PMID: 12527898
3. Macrophage Cell and Diagnostic Biomarkers in BLCA: Integrating Machine Learning With Single-Cell Analysis.. *Clinical genitourinary cancer*. PMID: 41139554
4. Construction and Multi-dimensional Validation of a Lactylation-Related Signature for Glioblastoma Multiforme Prognostic and Therapeutic Purposes.. *Molecular biotechnology*. PMID: 40407859
5. DEDD regulates degradation of intermediate filaments during apoptosis.. *The Journal of cell biology*. PMID: 12235123

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 43.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.5，有序区 63.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011029, IPR001875, IPR038856, IPR049341; Pfam: PF01335, PF20694 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFLAR | 0.789 | 0.510 | — |
| GTF3C3 | 0.692 | 0.292 | — |
| KRT18 | 0.669 | 0.000 | — |
| KRT8 | 0.668 | 0.000 | — |
| CASP8 | 0.629 | 0.510 | — |
| FADD | 0.592 | 0.000 | — |
| DEDD | 0.585 | 0.510 | — |
| ATG16L1 | 0.529 | 0.510 | — |
| CCAR1 | 0.511 | 0.000 | — |
| PRR19 | 0.476 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| HNRNPAB | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NR2E3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| RHOXF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| RBFOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000336034 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 无 | pLDDT=72.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. DEDD2 — DNA-binding death effector domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小326 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXF8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160570-DEDD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEDD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000160570-DEDD2/subcellular

![](https://images.proteinatlas.org/43419/1874_C7_41_cr5b83c7a98bacd_red_green.jpg)
![](https://images.proteinatlas.org/43419/1874_C7_62_red_green.jpg)
![](https://images.proteinatlas.org/43419/542_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/43419/542_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/43419/544_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/43419/544_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WXF8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXF8 |
| SMART | SM00031; |
| UniProt Domain [FT] | DOMAIN 25..104; /note="DED"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00065" |
| InterPro | IPR011029;IPR001875;IPR038856;IPR049341; |
| Pfam | PF01335;PF20694; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160570-DEDD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATG16L1 | Biogrid | false |
| CASP8 | Biogrid | false |
| CFLAR | Biogrid | false |
| DEDD | Biogrid | false |
| FBXO38 | Biogrid | false |
| GTF3C3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
