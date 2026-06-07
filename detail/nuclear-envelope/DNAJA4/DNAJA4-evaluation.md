---
type: protein-evaluation
gene: "DNAJA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJA4 |
| 蛋白名称 | DnaJ homolog subfamily A member 4 |
| 蛋白大小 | 397 aa / 44.8 kDa |
| UniProt ID | Q8WW22 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/DNAJA4/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/DNAJA4/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nuclear membrane, Primary cili; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 397 aa / 44.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nuclear membrane, Primary cilium, Centriolar satellite, Basal body | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 52 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A Cross-Tissue Transcriptome Association Study Revealed Novel Susceptibility Genes for Chronic Obstructive Pulmonary Disease.. *Int J Chron Obstruct Pulmon Dis*. PMID: 41821648
2. Comprehensive co-expression analysis reveals candidate regulatory genes associated with carcass and meat quality traits in Neijiang and Large White pigs.. *Anim Biosci*. PMID: 40575980
3. Identifying PDAP1 as a Biological Target on Human Longevity: Integration of Mendelian Randomization, Cohort, and Cell Experiments Validation Study.. *Aging Cell*. PMID: 40211681
4. Homeobox protein MSX-1 restricts hepatitis B virus by promoting ubiquitin-independent proteasomal degradation of HBx protein.. *PLoS Pathog*. PMID: 39883729
5. Transcriptome analysis revealed differences in gene expression in sheep muscle tissue at different developmental stages.. *BMC Genom Data*. PMID: 38849746

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 32.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/DNAJA4/DNAJA4-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=84.4，有序区 85.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA1B | 0.000 | 0.000 | — |
| DNAJA1 | 0.000 | 0.000 | — |
| HSPA8 | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| DNAJA2 | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |
| DNAJB1 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8WW22 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q9P0V3 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q7SZ03 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WW22-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6IAW5 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:Q8N9N5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q14249 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q71U36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6NSI4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O60884 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 4 / 20 = 20%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.4 + PDB: 无 | pLDDT=84.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cytosol; 额外: Nuclear membrane, Pr | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DNAJA4 — DnaJ homolog subfamily A member 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小397 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WW22
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140403-DNAJA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WW22
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/DNAJA4/DNAJA4-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WW22 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 4..70; /note="J" |
| InterPro | IPR012724;IPR002939;IPR001623;IPR018253;IPR044713;IPR008971;IPR001305;IPR036410;IPR036869; |
| Pfam | PF00226;PF01556;PF00684; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140403-DNAJA4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DNAJA2 | Intact, Biogrid | true |
| ENDOG | Intact, Biogrid | true |
| DNAJA1 | Biogrid | false |
| GRPEL1 | Biogrid | false |
| HSPA1A | Biogrid | false |
| MLLT11 | Biogrid | false |
| PRPS1 | Biogrid | false |
| RADX | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
