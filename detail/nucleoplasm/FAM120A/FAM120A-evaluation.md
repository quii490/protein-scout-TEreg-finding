---
type: protein-evaluation
gene: "FAM120A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM120A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM120A / C9orf10, KIAA0183, OSSA |
| 蛋白名称 | Constitutive coactivator of PPAR-gamma-like protein 1 |
| 蛋白大小 | 1118 aa / 121.9 kDa |
| UniProt ID | Q9NZB2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM120A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM120A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: Cytoplasm; Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1118 aa / 121.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026784, IPR029060 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf10, KIAA0183, OSSA |

**关键文献**:
1. FAM120A couples SREBP-dependent transcription and splicing of lipogenesis enzymes downstream of mTORC1.. *Molecular cell*. PMID: 37595559
2. Loss of Lamin A leads to the nuclear translocation of AGO2 and compromised RNA interference.. *Nucleic acids research*. PMID: 38994560
3. Sequestration of microRNA-mediated target repression by the Ago2-associated RNA-binding protein FAM120A.. *RNA (New York, N.Y.)*. PMID: 31289130
4. Associations between Gene-Gene Interaction and Overweight/Obesity of 12-Month-Old Chinese Infants.. *BioMed research international*. PMID: 35295960
5. Thermal Proteome Profiling Reveals Meltome Upon NLRP3 Inflammasome Activation.. *Molecular & cellular proteomics : MCP*. PMID: 40250624

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 40.9% |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM120A/FAM120A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 55.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026784, IPR029060 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| DYSF | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| BECN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Ybx1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| lutA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000277165.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-6096764 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |
| EBI-6095751 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 无 | pLDDT=67.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM120A — Constitutive coactivator of PPAR-gamma-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1118 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZB2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000048828-FAM120A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM120A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZB2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM120A/FAM120A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZB2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026784;IPR029060; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000048828-FAM120A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX6 | Biogrid, Opencell | true |
| DHX9 | Biogrid, Opencell | true |
| G3BP2 | Biogrid, Opencell | true |
| HNRNPC | Biogrid, Opencell | true |
| HNRNPD | Biogrid, Opencell | true |
| HNRNPL | Biogrid, Opencell | true |
| IGF2BP1 | Biogrid, Opencell | true |
| ILF3 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
