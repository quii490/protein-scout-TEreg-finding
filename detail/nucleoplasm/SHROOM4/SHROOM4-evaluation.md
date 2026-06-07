---
type: protein-evaluation
gene: "SHROOM4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHROOM4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHROOM4 / KIAA1202, SHAP |
| 蛋白名称 | Protein Shroom4 |
| 蛋白大小 | 1493 aa / 164.9 kDa |
| UniProt ID | Q9ULL8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Focal adhesion sites; 额外: Nucleoplasm, Vesicles; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 5/10 | ×1 | 5 | 1493 aa / 164.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.1; PDB: 2EDP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014799, IPR001478, IPR036034, IPR027685; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Focal adhesion sites; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin filament (GO:0005884)
- adherens junction (GO:0005912)
- apical junction complex (GO:0043296)
- apical plasma membrane (GO:0016324)
- basal plasma membrane (GO:0009925)
- cortical actin cytoskeleton (GO:0030864)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1202, SHAP |

**关键文献**:
1. Shroom4 (Kiaa1202) is an actin-associated protein implicated in cytoskeletal organization.. *Cell motility and the cytoskeleton*. PMID: 17009331
2. X-linked variations in SHROOM4 are implicated in congenital anomalies of the urinary tract and the anorectal, cardiovascular and central nervous systems.. *Journal of medical genetics*. PMID: 36379543
3. SHROOM4 Variants Are Associated With X-Linked Epilepsy With Features of Generalized Seizures or Generalized Discharges.. *Frontiers in molecular neuroscience*. PMID: 35663265
4. Familial Xp11.22 microdeletion including SHROOM4 and CLCN5 is associated with intellectual disability, short stature, microcephaly and Dent disease: a case report.. *BMC medical genomics*. PMID: 30630535
5. Comprehensive Long-Read Sequencing Analysis Discloses the Transcriptome Features of Papillary Thyroid Microcarcinoma.. *The Journal of clinical endocrinology and metabolism*. PMID: 38038628

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 73.5% |
| 有序区域 (pLDDT>70) 占比 | 22.0% |
| 可用 PDB 条目 | 2EDP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.1），有序残基占 22.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014799, IPR001478, IPR036034, IPR027685; Pfam: PF08687, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APEX1 | 0.657 | 0.000 | — |
| PROM2 | 0.545 | 0.000 | — |
| CENPVL1 | 0.507 | 0.000 | — |
| LYG1 | 0.507 | 0.000 | — |
| ZNF106 | 0.488 | 0.088 | — |
| ALMS1 | 0.486 | 0.070 | — |
| EPM2AIP1 | 0.475 | 0.088 | — |
| IQSEC2 | 0.472 | 0.000 | — |
| KDM6A | 0.471 | 0.060 | — |
| IL7R | 0.467 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| ABCC4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ASIC3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| APBA1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| APBA2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| AHNAK | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| CARD11 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| CASK | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ARHGAP21 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ARHGEF11 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.1 + PDB: 2EDP | pLDDT=47.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Focal adhesion sites; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SHROOM4 — Protein Shroom4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1493 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULL8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158352-SHROOM4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHROOM4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULL8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Focal adhesion sites (approved)。来源: https://www.proteinatlas.org/ENSG00000158352-SHROOM4/subcellular

![](https://images.proteinatlas.org/10089/1878_D10_40_cr5b7d732830784_blue_red_green.jpg)
![](https://images.proteinatlas.org/10089/1878_D10_48_cr5b7d732830cd9_blue_red_green.jpg)
![](https://images.proteinatlas.org/10089/1901_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10089/1901_G4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/10089/1919_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10089/1919_B6_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULL8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9ULL8 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 10..92; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 1213..1492; /note="ASD2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00638" |
| InterPro | IPR014799;IPR001478;IPR036034;IPR027685; |
| Pfam | PF08687;PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158352-SHROOM4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
