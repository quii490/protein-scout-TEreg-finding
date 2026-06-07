---
type: protein-evaluation
gene: "FAM178A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM178A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM178A / C10orf6, FAM178A |
| 蛋白名称 | SMC5-SMC6 complex localization factor protein 2 |
| 蛋白大小 | 1173 aa / 131.9 kDa |
| UniProt ID | Q8IX21 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM178A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM178A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Nucleus, PML body |
| 蛋白大小 | 8/10 | ×1 | 8 | 1173 aa / 131.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 7T5P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044276, IPR026161; Pfam: PF14816 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.5/180** | |
| **归一化总分** | | | **79.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- site of double-strand break (GO:0035861)
- Smc5-Smc6 complex (GO:0030915)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf6, FAM178A |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 8.7% |
| 置信残基 (pLDDT 70-90) 占比 | 27.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 55.8% |
| 有序区域 (pLDDT>70) 占比 | 36.4% |
| 可用 PDB 条目 | 7T5P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM178A/FAM178A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 36.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044276, IPR026161; Pfam: PF14816 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLF1 | 0.999 | 0.826 | — |
| SMC5 | 0.967 | 0.695 | — |
| SMC6 | 0.955 | 0.779 | — |
| NSMCE1 | 0.927 | 0.743 | — |
| RAD18 | 0.924 | 0.624 | — |
| NSMCE3 | 0.904 | 0.610 | — |
| NSMCE2 | 0.883 | 0.610 | — |
| NSMCE4A | 0.866 | 0.589 | — |
| TWNK | 0.764 | 0.000 | — |
| CYP17A1 | 0.582 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RIN3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PSMA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SFMBT2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM14 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAD18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| NSMCE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 6 / 15 = 40%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 40%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 7T5P | pLDDT=55.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM178A — SMC5-SMC6 complex localization factor protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1173 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IX21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119906-SLF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM178A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IX21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM178A/FAM178A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IX21 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR044276;IPR026161; |
| Pfam | PF14816; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119906-SLF2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
