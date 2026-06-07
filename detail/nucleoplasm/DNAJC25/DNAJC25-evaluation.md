---
type: protein-evaluation
gene: "DNAJC25"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC25 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC25 |
| 蛋白名称 | DnaJ homolog subfamily C member 25 |
| 蛋白大小 | 360 aa / 42.4 kDa |
| UniProt ID | Q9H1X3 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC25/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC25/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 42.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 25 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
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
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Differential expression of lncRNAs and mRNAs in bone marrow-derived mesenchymal stem cells under continuous and intermittent teriparatide treatment.. *Biomed Pharmacother*. PMID: 40609214
2. RNF149 Promotes HCC Progression through Its E3 Ubiquitin Ligase Activity.. *Cancers (Basel)*. PMID: 37958377
3. Impact of the acidic environment on gene expression and functional parameters of tumors in vitro and in vivo.. *J Exp Clin Cancer Res*. PMID: 33407762
4. Transcriptomic analysis of female and male gonads in juvenile snakeskin gourami (Trichopodus pectoralis).. *Sci Rep*. PMID: 32251302
5. A genome-wide association study of heat stress-associated SNPs in catfish.. *Anim Genet*. PMID: 27476875

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 26.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 79.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC25/DNAJC25-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=82.8，有序区 79.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA4 | 0.000 | 0.000 | — |
| BRCC3 | 0.000 | 0.000 | — |
| DNAJC9 | 0.000 | 0.000 | — |
| BABAM2 | 0.000 | 0.000 | — |
| BABAM1 | 0.000 | 0.000 | — |
| DNAJC27 | 0.000 | 0.000 | — |
| DNAJC8 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSPA12B | 0.000 | 0.000 | — |
| DNAJC12 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H1X3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P46736 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P51451 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15018 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IUH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NWV8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NXR7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y2T7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 12
- 调控相关比例: 7 / 20 = 35%

**评价**: STRING 25 个预测互作，IntAct 12 个实验互作。调控相关配体占比 35%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 无 | pLDDT=82.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 12 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC25 — DnaJ homolog subfamily C member 25，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H1X3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000059769-DNAJC25/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H1X3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC25/DNAJC25-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H1X3 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 49..124; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR001623;IPR044632;IPR036869; |
| Pfam | PF00226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000059769-DNAJC25/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC47 | Biogrid | false |
| EMD | Biogrid | false |
| ESYT2 | Biogrid | false |
| FKBP8 | Biogrid | false |
| LSG1 | Biogrid | false |
| MTDH | Biogrid | false |
| PGRMC1 | Biogrid | false |
| POR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
