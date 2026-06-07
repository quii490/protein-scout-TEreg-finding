---
type: protein-evaluation
gene: "EXOC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC1 / SEC3, SEC3L1 |
| 蛋白名称 | Exocyst complex component 1 |
| 蛋白大小 | 894 aa / 102.0 kDa |
| UniProt ID | Q9NV70 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Microtubules; 额外: Cytosol; UniProt: Midbody, Midbody ring; Cytoplasm; Cytoplasm, perinuclear reg |
| 蛋白大小 | 8/10 | ×1 | 8 | 894 aa / 102.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028258, IPR048628, IPR019160; Pfam: PF15277, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Microtubules; 额外: Cytosol | Uncertain |
| UniProt | Midbody, Midbody ring; Cytoplasm; Cytoplasm, perinuclear region; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- exocyst (GO:0000145)
- Flemming body (GO:0090543)
- membrane (GO:0016020)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEC3, SEC3L1 |

**关键文献**:
1. Single Nucleotide Polymorphisms of EXOC1, BCL2, CCAT2, and CARD8 Genes and Susceptibility to Cervical Cancer in the Northern Chinese Han Population.. *Frontiers in oncology*. PMID: 35814404
2. Exocyst complex component 1 (Exoc1) loss in dormant oocyte disrupts c-KIT and growth differentiation factor (GDF9) subcellular localization and causes female infertility in mice.. *Cell death discovery*. PMID: 39833146
3. The TRIM9/TRIM67 neuronal interactome reveals novel activators of morphogenesis.. *Molecular biology of the cell*. PMID: 33378226
4. Deletion of Exoc7, but not Exoc3, in male germ cells causes severe spermatogenesis failure with spermatocyte aggregation in mice.. *Experimental animals*. PMID: 38325858
5. The role of the exocyst in renal ciliogenesis, cystogenesis, tubulogenesis, and development.. *Kidney research and clinical practice*. PMID: 31284362

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 38.3% |
| 置信残基 (pLDDT 70-90) 占比 | 41.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 13.0% |
| 有序区域 (pLDDT>70) 占比 | 79.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EXOC1/EXOC1-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=79.8，有序区 79.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028258, IPR048628, IPR019160; Pfam: PF15277, PF20654, PF09763 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC7 | 0.999 | 0.979 | — |
| EXOC6 | 0.999 | 0.920 | — |
| EXOC2 | 0.999 | 0.993 | — |
| EXOC4 | 0.999 | 0.993 | — |
| EXOC3 | 0.999 | 0.977 | — |
| EXOC5 | 0.999 | 0.972 | — |
| EXOC8 | 0.999 | 0.978 | — |
| CDC42 | 0.992 | 0.260 | — |
| EXOC6B | 0.991 | 0.953 | — |
| EXOC3L1 | 0.968 | 0.903 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| COLEC12 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| DST | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| RESF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| GOLGA4 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| CCSER2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| CEP295 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MACF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 无 | pLDDT=79.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Midbody, Midbody ring; Cytoplasm; Cytoplasm, perin / Plasma membrane, Microtubules; 额外: Cytosol | 一致 |
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
1. EXOC1 — Exocyst complex component 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小894 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NV70
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090989-EXOC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NV70
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EXOC1/EXOC1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NV70 |
| SMART | SM01313; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028258;IPR048628;IPR019160; |
| Pfam | PF15277;PF20654;PF09763; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000090989-EXOC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EIPR1 | Intact, Biogrid | true |
| EXOC2 | Intact, Biogrid | true |
| EXOC3 | Intact, Biogrid | true |
| EXOC4 | Intact, Biogrid | true |
| EXOC5 | Intact, Biogrid | true |
| EXOC6 | Intact, Biogrid | true |
| EXOC6B | Intact, Biogrid | true |
| EXOC7 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
