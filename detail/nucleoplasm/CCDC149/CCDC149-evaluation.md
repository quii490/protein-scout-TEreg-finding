---
type: protein-evaluation
gene: "CCDC149"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC149 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC149 |
| 蛋白名称 | Coiled-coil domain-containing protein 149 |
| 蛋白大小 | 474 aa / 52.8 kDa |
| UniProt ID | Q6ZUS6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 474 aa / 52.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019179; Pfam: PF09789 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
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
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cryptorchidism: Novel genetic insights into CCDC149 mutations.. *Andrology*. PMID: 40459248
2. A Higher Dysregulation Burden of Brain DNA Methylation in Female Patients Implicated in the Sex Bias of Schizophrenia.. *Research square*. PMID: 36778507
3. Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport.. *PLoS genetics*. PMID: 27930654
4. Case Report of CCDC149-ALK Fusion: A Novel Genetic Alteration and a Clinically Relevant Target in Metastatic Papillary Thyroid Carcinoma.. *Thyroid : official journal of the American Thyroid Association*. PMID: 36150036
5. A higher dysregulation burden of brain DNA methylation in female patients implicated in the sex bias of Schizophrenia.. *Molecular psychiatry*. PMID: 37696874

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 33.8% |
| 有序区域 (pLDDT>70) 占比 | 49.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 49.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019179; Pfam: PF09789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RMDN2 | 0.600 | 0.000 | — |
| SRGAP2 | 0.540 | 0.000 | — |
| DLGAP1 | 0.539 | 0.000 | — |
| IQCA1 | 0.531 | 0.000 | — |
| ADGB | 0.520 | 0.000 | — |
| MYO10 | 0.516 | 0.000 | — |
| SRGAP3 | 0.515 | 0.000 | — |
| PPP2R5C | 0.514 | 0.000 | — |
| LGI2 | 0.487 | 0.000 | — |
| PPP1R21 | 0.478 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRNP | psi-mi:"MI:0089"(protein array) | pubmed:18482256|imex:IM-19010 |
| MFHAS1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| DAPK1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| MKNK1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 无 | pLDDT=68.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC149 — Coiled-coil domain-containing protein 149，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小474 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUS6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181982-CCDC149/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC149
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUS6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000181982-CCDC149/subcellular

![](https://images.proteinatlas.org/44158/565_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44158/565_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44158/570_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44158/570_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44158/584_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44158/584_H3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZUS6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZUS6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019179; |
| Pfam | PF09789; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181982-CCDC149/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
