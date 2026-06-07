---
type: protein-evaluation
gene: "FBXL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL3 / FBL3A, FBXL3A |
| 蛋白名称 | F-box/LRR-repeat protein 3 |
| 蛋白大小 | 428 aa / 48.7 kDa |
| UniProt ID | Q9UKT7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FBXL3/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FBXL3/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 428 aa / 48.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.3; PDB: 4I6J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 89 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL3A, FBXL3A |

**关键文献**:
1. Phosphorylation regulates cullin-based ubiquitination in tumorigenesis.. *Acta pharmaceutica Sinica. B*. PMID: 33643814
2. Fbxl3 deletion mitigates myopathy in mdx mice through upregulation of myogenin.. *Biochemical and biophysical research communications*. PMID: 40554051
3. FBXL3 serves as a suppressor of regenerative myogenesis.. *Frontiers in immunology*. PMID: 40755783
4. Circadian mutant Overtime reveals F-box protein FBXL3 regulation of cryptochrome and period gene expression.. *Cell*. PMID: 17462724
5. The circadian E3 ligase complex SCF(FBXL3+CRY) targets TLK2.. *Scientific reports*. PMID: 30655559

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 80.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 4I6J |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FBXL3/FBXL3-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=90.3，有序区 91.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR032675; Pfam: PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY2 | 0.999 | 0.967 | — |
| CRY1 | 0.999 | 0.875 | — |
| SKP1 | 0.999 | 0.995 | — |
| CUL1 | 0.973 | 0.836 | — |
| CLOCK | 0.931 | 0.000 | — |
| ARNTL | 0.921 | 0.000 | — |
| PER2 | 0.917 | 0.154 | — |
| CSNK1E | 0.876 | 0.053 | — |
| CSNK1D | 0.813 | 0.053 | — |
| NPAS2 | 0.798 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cry1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11930|pubmed:17462724 |
| Cry2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11930|pubmed:17462724 |
| mviM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL1 | psi-mi:"MI:0809"(bimolecular fluorescence compleme | pubmed:23452855|imex:IM-20967 |
| SKP1 | psi-mi:"MI:0809"(bimolecular fluorescence compleme | pubmed:23452855|imex:IM-20967 |
| Per2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23452855|imex:IM-20967 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| MSRA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CEP57 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RFX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 4I6J | pLDDT=90.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXL3 — F-box/LRR-repeat protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小428 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKT7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005812-FBXL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKT7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/FBXL3/FBXL3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKT7 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 34..81; /note="F-box" |
| InterPro | IPR036047;IPR001810;IPR032675; |
| Pfam | PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005812-FBXL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CRY1 | Biogrid, Bioplex | true |
| SKP1 | Biogrid, Bioplex | true |
| CRY2 | Biogrid | false |
| CUL1 | Biogrid | false |
| MSRA | Intact | false |
| PICK1 | Intact | false |
| RFX1 | Bioplex | false |
| SLC25A31 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
