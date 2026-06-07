---
type: protein-evaluation
gene: "TM2D3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TM2D3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TM2D3 / BLP2 |
| 蛋白名称 | TM2 domain-containing protein 3 |
| 蛋白大小 | 247 aa / 27.1 kDa |
| UniProt ID | Q9BRN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 247 aa / 27.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007829, IPR050932; Pfam: PF05154 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BLP2 |

**关键文献**:
1. Bi-allelic variants in TM2D3 cause a severe syndromic neurodevelopmental disorder associated with endoplasmic reticulum and mitochondrial abnormalities.. *American journal of human genetics*. PMID: 40449487
2. Identification of phagocytosis regulators using magnetic genome-wide CRISPR screens.. *Nature genetics*. PMID: 30397336
3. TM2D3, a mammalian homologue of Drosophila neurogenic gene product Almondex, regulates surface presentation of Notch receptors.. *Scientific reports*. PMID: 38016980
4. Functional Studies of Genetic Variants Associated with Human Diseases in Notch Signaling-Related Genes Using Drosophila.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 35674905
5. TM2D genes regulate Notch signaling and neuronal function in Drosophila.. *PLoS genetics*. PMID: 34905536

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 61.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 76.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.7，有序区 76.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007829, IPR050932; Pfam: PF05154 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TARS3 | 0.717 | 0.000 | — |
| NME8 | 0.695 | 0.000 | — |
| LRCH1 | 0.648 | 0.000 | — |
| NHLRC2 | 0.632 | 0.000 | — |
| POLK | 0.624 | 0.000 | — |
| C17orf80 | 0.619 | 0.619 | — |
| OR4F15 | 0.599 | 0.000 | — |
| CALM1 | 0.593 | 0.000 | — |
| TNFAIP6 | 0.588 | 0.000 | — |
| TM2D1 | 0.581 | 0.172 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IL9R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TM2D2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NRG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAV3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPACA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL13RA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC2A12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSPAN17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 无 | pLDDT=79.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TM2D3 — TM2 domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小247 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184277-TM2D3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TM2D3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184277-TM2D3/subcellular

![](https://images.proteinatlas.org/54064/849_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/54064/849_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/54064/869_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/54064/869_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/54064/885_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/54064/885_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BRN9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BRN9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 183..230; /note="TM2"; /evidence="ECO:0000255" |
| InterPro | IPR007829;IPR050932; |
| Pfam | PF05154; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184277-TM2D3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADAM9 | Bioplex | false |
| ARSG | Bioplex | false |
| C1QL4 | Bioplex | false |
| CANX | Opencell | false |
| CERCAM | Bioplex | false |
| CLPTM1 | Bioplex | false |
| CSPG4 | Bioplex | false |
| DCAKD | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
