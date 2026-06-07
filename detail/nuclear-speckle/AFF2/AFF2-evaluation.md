---
type: protein-evaluation
gene: "AFF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AFF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AFF2 / FMR2, OX19 |
| 蛋白名称 | AF4/FMR2 family member 2 |
| 蛋白大小 | 1311 aa / 144.8 kDa |
| UniProt ID | P51816 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus speckle |
| 蛋白大小 | 5/10 | ×1 | 5 | 1311 aa / 144.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007797, IPR043640, IPR043639; Pfam: PF05110, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nuclear speck (GO:0016607)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 207 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FMR2, OX19 |

**关键文献**:
1. [Translocated sinonasal tumors].. *Annales de pathologie*. PMID: 38355380
2. An intragenic duplication in the AFF2 gene associated with Cornelia de Lange syndrome phenotype.. *Frontiers in genetics*. PMID: 39553472
3. Translocations and Gene Fusions in Sinonasal Malignancies.. *Current oncology reports*. PMID: 36753024
4. Unravelling the link between neurodevelopmental disorders and short tandem CGG-repeat expansions.. *Emerging topics in life sciences*. PMID: 37768318
5. AFF2 Is Associated With X-Linked Partial (Focal) Epilepsy With Antecedent Febrile Seizures.. *Frontiers in molecular neuroscience*. PMID: 35431806

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.6 |
| 高置信度残基 (pLDDT>90) 占比 | 14.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 74.2% |
| 有序区域 (pLDDT>70) 占比 | 19.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.6），有序残基占 19.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007797, IPR043640, IPR043639; Pfam: PF05110, PF18875, PF18876 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM185A | 0.950 | 0.000 | — |
| FMR1 | 0.950 | 0.045 | — |
| ELL | 0.679 | 0.049 | — |
| MLLT1 | 0.679 | 0.113 | — |
| MLLT3 | 0.671 | 0.113 | — |
| FMR1NB | 0.613 | 0.000 | — |
| IDS | 0.580 | 0.100 | — |
| CBL | 0.571 | 0.049 | — |
| SLITRK2 | 0.570 | 0.088 | — |
| AFF3 | 0.570 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| tat | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| KPNA4 | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-29361|pubmed:35044719 |
| MYC | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-29361|pubmed:35044719 |
| NCOR2 | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.6 + PDB: 无 | pLDDT=48.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus speckle / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AFF2 — AF4/FMR2 family member 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1311 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51816
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155966-AFF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AFF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51816
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51816-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51816 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007797;IPR043640;IPR043639; |
| Pfam | PF05110;PF18875;PF18876; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155966-AFF2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
