---
type: protein-evaluation
gene: "UEVLD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UEVLD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UEVLD / UEV3 |
| 蛋白名称 | Ubiquitin-conjugating enzyme E2 variant 3 |
| 蛋白大小 | 471 aa / 52.3 kDa |
| UniProt ID | Q8IX04 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 52.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.2; PDB: 2I6T, 3DL2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001557, IPR022383, IPR001236, IPR015955, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ESCRT I complex (GO:0000813)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UEV3 |

**关键文献**:
1. Targeted next generation sequencing identifies somatic mutations and gene fusions in papillary thyroid carcinoma.. *Oncotarget*. PMID: 28507274
2. NMR chemical shift assignment of UEV domain of ubiquitin-conjugating enzyme E2 variant 3 lactate dehydrogenase (UEVLD).. *Biomolecular NMR assignments*. PMID: 40571836
3. Transcriptome-wide association study of HIV-1 acquisition identifies HERC1 as a susceptibility gene.. *iScience*. PMID: 36034232
4. mTOR pathway gene knockout results in mTOR-dependent cellular aggregation.. *bioRxiv : the preprint server for biology*. PMID: 41279080

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 87.9% |
| 可用 PDB 条目 | 2I6T, 3DL2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2I6T, 3DL2）+ AlphaFold高质量预测（pLDDT=87.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001557, IPR022383, IPR001236, IPR015955, IPR036291; Pfam: PF02866, PF00056, PF05743 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS28 | 0.948 | 0.833 | — |
| GGH | 0.900 | 0.000 | — |
| CS | 0.825 | 0.274 | — |
| HGS | 0.825 | 0.485 | — |
| MVB12B | 0.816 | 0.439 | — |
| VPS37A | 0.809 | 0.483 | — |
| MVB12A | 0.808 | 0.414 | — |
| VPS37D | 0.805 | 0.483 | — |
| VPS37C | 0.805 | 0.483 | — |
| VPS37B | 0.805 | 0.483 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| LRSAM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| DTX3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| SDF2L1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| GALM | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| RNF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| RNF114 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| TRAF2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| BIRC2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RBCK1 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 2I6T, 3DL2 | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. UEVLD — Ubiquitin-conjugating enzyme E2 variant 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IX04
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151116-UEVLD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UEVLD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IX04
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000151116-UEVLD/subcellular

![](https://images.proteinatlas.org/47134/728_B9_4_red_green.jpg)
![](https://images.proteinatlas.org/47134/728_B9_5_red_green.jpg)
![](https://images.proteinatlas.org/47134/748_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/47134/748_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/47134/896_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/47134/896_B9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IX04-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IX04 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 2..145; /note="UEV"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00652" |
| InterPro | IPR001557;IPR022383;IPR001236;IPR015955;IPR036291;IPR016135;IPR008883; |
| Pfam | PF02866;PF00056;PF05743; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151116-UEVLD/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MORN4 | Intact, Bioplex | false |
| WDR59 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
