---
type: protein-evaluation
gene: "FAM161A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM161A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM161A |
| 蛋白名称 | Protein FAM161A |
| 蛋白大小 | 660 aa / 76.8 kDa |
| UniProt ID | Q3B820 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM161A/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM161A/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome, Basal body, Flagellar centriole; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cell projection, |
| 蛋白大小 | 10/10 | ×1 | 10 | 660 aa / 76.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051655, IPR019579; Pfam: PF10595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body, Flagellar centriole; 额外: Nucleoplasm, Golgi apparatus, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, cilium basal body; Cell projection, cilium; Cytoplasm, cytoskeleton, microt... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- astral microtubule (GO:0000235)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- mitotic spindle (GO:0072686)
- mitotic spindle pole (GO:0097431)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. Gene augmentation in FAM161A ciliopathy: Toward functional vision rescue.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 37729904
3. FAM161A, a novel centrosomal-ciliary protein implicated in autosomal recessive retinitis pigmentosa.. *Advances in experimental medicine and biology*. PMID: 24664697
4. Fine-tuning FAM161A gene augmentation therapy to restore retinal function.. *EMBO molecular medicine*. PMID: 38504136
5. Gene augmentation therapy attenuates retinal degeneration in a knockout mouse model of Fam161a retinitis pigmentosa.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 37580905

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.4% |
| 置信残基 (pLDDT 70-90) 占比 | 27.6% |
| 中等置信 (pLDDT 50-70) 占比 | 26.4% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 44.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM161A/FAM161A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=66.4），有序残基占 44.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051655, IPR019579; Pfam: PF10595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCT2 | 0.979 | 0.751 | — |
| CCT5 | 0.972 | 0.765 | — |
| POC1B | 0.952 | 0.297 | — |
| POC5 | 0.940 | 0.330 | — |
| PEX19 | 0.852 | 0.840 | — |
| CCT7 | 0.841 | 0.417 | — |
| LCA5 | 0.815 | 0.292 | — |
| CRX | 0.797 | 0.000 | — |
| HSPE1 | 0.797 | 0.470 | — |
| PDE6B | 0.788 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000385893.3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PPM1F | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRKDC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| POC5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| PPFIA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| CARD9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| DHX32 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM54 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PNMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.4 + PDB: 无 | pLDDT=66.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium basal body; Cell p / Centrosome, Basal body, Flagellar centriole; 额外: N | 一致 |
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
1. FAM161A — Protein FAM161A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小660 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3B820
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170264-FAM161A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM161A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3B820
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM161A/FAM161A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3B820 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051655;IPR019579; |
| Pfam | PF10595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170264-FAM161A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PNMA2 | Intact, Biogrid | true |
| POC5 | Intact, Biogrid | true |
| PPFIA1 | Intact, Biogrid | true |
| AQP1 | Intact | false |
| AXIN2 | Intact | false |
| BACH2 | Intact | false |
| BEGAIN | Intact | false |
| BEND3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
