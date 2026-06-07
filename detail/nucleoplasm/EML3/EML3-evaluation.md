---
type: protein-evaluation
gene: "EML3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EML3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EML3 |
| 蛋白名称 | Echinoderm microtubule-associated protein-like 3 |
| 蛋白大小 | 896 aa / 95.2 kDa |
| UniProt ID | Q32P44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton; Cytoplasm; Nucleus; Midbody; Cytopl |
| 蛋白大小 | 8/10 | ×1 | 8 | 896 aa / 95.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055442, IPR055439, IPR005108, IPR011047, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm; Nucleus; Midbody; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- mitotic spindle microtubule (GO:1990498)
- nucleus (GO:0005634)
- spindle (GO:0005819)
- spindle microtubule (GO:0005876)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. EML3 is a nuclear microtubule-binding protein required for the correct alignment of chromosomes in metaphase.. *Journal of cell science*. PMID: 18445686
2. The microtubule-associated protein EML3 regulates mitotic spindle assembly by recruiting the Augmin complex to spindle microtubules.. *The Journal of biological chemistry*. PMID: 30723163
3. FOLFOX treatment response prediction in metastatic or recurrent colorectal cancer patients via machine learning algorithms.. *Cancer medicine*. PMID: 31893575
4. Arabidopsis Histone Reader EMSY-LIKE 1 Binds H3K36 and Suppresses Geminivirus Infection.. *Journal of virology*. PMID: 29875242
5. Identifying cross-tissue molecular targets of lung function by multi-omics integration analysis from DNA methylation and gene expression of diverse human tissues.. *BMC genomics*. PMID: 40128644

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 23.7% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EML3/EML3-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 74.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055442, IPR055439, IPR005108, IPR011047, IPR015943; Pfam: PF23409, PF23414, PF03451 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPSF1 | 0.555 | 0.295 | — |
| NEK6 | 0.549 | 0.480 | — |
| ZNF354A | 0.534 | 0.091 | — |
| REXO1 | 0.530 | 0.045 | — |
| DYNLL1 | 0.513 | 0.324 | — |
| CDK1 | 0.509 | 0.361 | — |
| PAK4 | 0.491 | 0.463 | — |
| KAT2A | 0.479 | 0.275 | — |
| GLI4 | 0.474 | 0.091 | — |
| CCDC124 | 0.469 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| nusA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ORF | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKCB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm; Nucleus; Midbo / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EML3 — Echinoderm microtubule-associated protein-like 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小896 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q32P44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149499-EML3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EML3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q32P44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EML3/EML3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q32P44 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR055442;IPR055439;IPR005108;IPR011047;IPR015943;IPR001680;IPR050630; |
| Pfam | PF23409;PF23414;PF03451; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149499-EML3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| NEK6 | Intact, Biogrid | true |
| NEK7 | Biogrid, Bioplex | true |
| YWHAG | Intact, Biogrid | true |
| YWHAQ | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| CHCHD2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
