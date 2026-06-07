---
type: protein-evaluation
gene: "GPRC5A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPRC5A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRC5A / GPCR5A, RAI3, RAIG1 |
| 蛋白名称 | Retinoic acid-induced protein 3 |
| 蛋白大小 | 357 aa / 40.3 kDa |
| UniProt ID | Q8NFJ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Plasma membrane, Primary cilium, Primary ciliu; UniProt: Cell membrane; Cytoplasmic vesicle membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 357 aa / 40.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR051753; Pfam: PF00003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Plasma membrane, Primary cilium, Primary cilium tip | Supported |
| UniProt | Cell membrane; Cytoplasmic vesicle membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle membrane (GO:0030659)
- extracellular exosome (GO:0070062)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)
- vesicle (GO:0031982)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 38.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 14.6% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 68.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR051753; Pfam: PF00003 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRM2 | 0.831 | 0.000 | — |
| GPR156 | 0.580 | 0.000 | — |
| EIF4A1 | 0.513 | 0.219 | — |
| HSPA9 | 0.496 | 0.209 | — |
| GPR158 | 0.490 | 0.000 | — |
| APOLD1 | 0.447 | 0.000 | — |
| ACTR2 | 0.422 | 0.422 | — |
| KRTCAP3 | 0.416 | 0.000 | — |
| VSIG8 | 0.407 | 0.000 | — |
| TSPEAR | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| Trim69 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| GAPDH | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| Myh10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Actb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAB5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Fam83d | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAB7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasmic vesicle membrane / Vesicles; 额外: Plasma membrane, Primary cilium, Pri | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPRC5A — Retinoic acid-induced protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小357 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFJ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013588-GPRC5A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRC5A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFJ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000013588-GPRC5A/subcellular

![](https://images.proteinatlas.org/46526/2242_F7_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/46526/2242_F7_71_blue_red_green.jpg)
![](https://images.proteinatlas.org/46526/2243_C6_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/46526/2243_C6_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/46526/2244_E8_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/46526/2244_E8_41_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFJ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFJ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017978;IPR051753; |
| Pfam | PF00003; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013588-GPRC5A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANLN | Biogrid | false |
| CFTR | Biogrid | false |
| KRAS | Biogrid | false |
| LAMTOR1 | Bioplex | false |
| RHOB | Biogrid | false |
| TRIM25 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
