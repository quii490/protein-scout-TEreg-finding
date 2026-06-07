---
type: protein-evaluation
gene: "SPRY3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPRY3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPRY3 |
| 蛋白名称 | Protein sprouty homolog 3 |
| 蛋白大小 | 288 aa / 31.2 kDa |
| UniProt ID | O43610 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 288 aa / 31.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007875, IPR051192; Pfam: PF05210 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MicroRNA-143-3p promotes human cardiac fibrosis via targeting sprouty3 after myocardial infarction.. *Journal of molecular and cellular cardiology*. PMID: 30878395
2. Regulation of SPRY3 by X chromosome and PAR2-linked promoters in an autism susceptibility region.. *Human molecular genetics*. PMID: 26089202
3. Opposite Expression Patterns of Spry3 and p75NTR in Cerebellar Vermis Suggest a Male-Specific Mechanism of Autism Pathogenesis.. *Frontiers in psychiatry*. PMID: 31275178
4. Maintenance of X- and Y-inactivation of the pseudoautosomal (PAR2) gene SPRY3 is independent from DNA methylation and associated to multiple layers of epigenetic modifications.. *Human molecular genetics*. PMID: 16500999
5. Identification of two SPRY isoforms SPRY1 and SPRY3 by atomic force microscopy at the single-molecule level.. *The Analyst*. PMID: 36350085

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 15.3% |
| 低置信 (pLDDT<50) 占比 | 43.8% |
| 有序区域 (pLDDT>70) 占比 | 40.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 40.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007875, IPR051192; Pfam: PF05210 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAMP7 | 0.783 | 0.000 | — |
| IL9R | 0.758 | 0.000 | — |
| FGF8 | 0.648 | 0.000 | — |
| SPARC | 0.648 | 0.000 | — |
| FGF6 | 0.626 | 0.000 | — |
| PLCXD1 | 0.579 | 0.000 | — |
| DHRSX | 0.542 | 0.000 | — |
| ASMTL | 0.541 | 0.000 | — |
| TMLHE | 0.539 | 0.000 | — |
| FGF18 | 0.535 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAPKBP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| R3HDM2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LCE3E | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KPRP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CATSPER1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HOXA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LCE1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HR | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPRY3 — Protein sprouty homolog 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小288 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43610
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168939-SPRY3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPRY3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43610
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000168939-SPRY3/subcellular

![](https://images.proteinatlas.org/13505/625_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13505/625_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13505/629_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13505/629_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13505/631_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13505/631_E4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43610-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43610 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 154..260; /note="SPR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00572" |
| InterPro | IPR007875;IPR051192; |
| Pfam | PF05210; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168939-SPRY3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AQP1 | Intact | false |
| BEX2 | Intact | false |
| CATSPER1 | Intact | false |
| CHRD | Intact | false |
| GPSM3 | Intact | false |
| HR | Intact | false |
| KPRP | Intact | false |
| KRT34 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
