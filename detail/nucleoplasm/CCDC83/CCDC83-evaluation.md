---
type: protein-evaluation
gene: "CCDC83"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC83 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC83 |
| 蛋白名称 | Coiled-coil domain-containing protein 83 |
| 蛋白大小 | 413 aa / 48.9 kDa |
| UniProt ID | Q8IWF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 48.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026702 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 9 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cancer Testis Antigen, NOL4, Is an Immunogenic Antigen Specifically Expressed in Small-Cell Lung Cancer.. *Current oncology (Toronto, Ont.)*. PMID: 34065612
2. Integrated Analysis of Long Non-Coding RNA and mRNA Expression Profiles in Testes of Calves and Sexually Mature Wandong Bulls (Bos taurus).. *Animals : an open access journal from MDPI*. PMID: 34359134
3. KP-CoT-23 (CCDC83) is a novel immunogenic cancer/testis antigen in colon cancer.. *International journal of oncology*. PMID: 22923163

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 25.7% |
| 有序区域 (pLDDT>70) 占比 | 58.6% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.0，有序区 58.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026702 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC65 | 0.683 | 0.000 | — |
| IQCF1 | 0.628 | 0.000 | — |
| CDADC1 | 0.583 | 0.000 | — |
| IQCG | 0.572 | 0.000 | — |
| SPAG9 | 0.539 | 0.000 | — |
| FMR1NB | 0.529 | 0.000 | — |
| RPH3AL | 0.510 | 0.000 | — |
| KLHL10 | 0.470 | 0.000 | — |
| DMRTC2 | 0.466 | 0.000 | — |
| EIF4ENIF1 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM161B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CHMP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPID | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTC33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC50 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9
- 调控相关比例: 1 / 14 = 7%

**评价**: STRING 14 个预测互作，IntAct 9 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 无 | pLDDT=73.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC83 — Coiled-coil domain-containing protein 83，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150676-CCDC83/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:40:52

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150676-CCDC83/subcellular

![](https://images.proteinatlas.org/39882/2163_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/2163_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/39882/534_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/534_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/39882/539_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/539_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IWF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IWF9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026702; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000150676-CCDC83/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM161B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
