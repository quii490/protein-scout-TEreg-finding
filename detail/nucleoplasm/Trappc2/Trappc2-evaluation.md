---
type: protein-evaluation
gene: "Trappc2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Trappc2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Trappc2 / SEDL |
| 蛋白名称 | Trafficking protein particle complex subunit 2 |
| 蛋白大小 | 140 aa / 16.4 kDa |
| UniProt ID | P0DI81 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Vesicles; 额外: Nucleoplasm; UniProt: Cytoplasm, perinuclear region; Endoplasmic reticulum-Golgi i |
| 蛋白大小 | 8/10 | ×1 | 8 | 140 aa / 16.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011012, IPR006722; Pfam: PF04628 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, perinuclear region; Endoplasmic reticulum-Golgi intermediate compartment; Nucleus; Cytopl... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- TRAPP complex (GO:0030008)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEDL |

**关键文献**:
1. X-Linked Spondyloepiphyseal Dysplasia Tarda.. **. PMID: 20301324
2. Role of trafficking protein particle complex 2 in medaka development.. *Traffic (Copenhagen, Denmark)*. PMID: 37963679
3. A Humanized Yeast Model for Studying TRAPP Complex Mutations; Proof-of-Concept Using Variants from an Individual with a TRAPPC1-Associated Neurodevelopmental Syndrome.. *Cells*. PMID: 39273027
4. Functional consequences of copy number variants in miscarriage.. *Molecular cytogenetics*. PMID: 25674159
5. The adaptor function of TRAPPC2 in mammalian TRAPPs explains TRAPPC2-associated SEDT and TRAPPC9-associated congenital intellectual disability.. *PloS one*. PMID: 21858081

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 82.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 93.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 93.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011012, IPR006722; Pfam: PF04628 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAPPC10 | 0.999 | 0.915 | — |
| TRAPPC5 | 0.999 | 0.972 | — |
| TRAPPC4 | 0.999 | 0.958 | — |
| TRAPPC1 | 0.999 | 0.962 | — |
| TRAPPC3 | 0.999 | 0.957 | — |
| TRAPPC2L | 0.999 | 0.959 | — |
| TRAPPC9 | 0.999 | 0.961 | — |
| TRAPPC8 | 0.999 | 0.963 | — |
| TRAPPC6A | 0.999 | 0.940 | — |
| TRAPPC6B | 0.998 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBED1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Trappc3 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-12005|pubmed:17110339 |
| ENSMUSP00000112195.2 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-12005|pubmed:17110339 |
| REPS1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ABRA | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| EIF3C | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ENO1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ENO3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| HLA-E | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| PYGM | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Endoplasmic reticul / Endoplasmic reticulum, Vesicles; 额外: Nucleoplasm | 一致 |
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
1. Trappc2 — Trafficking protein particle complex subunit 2，非常新颖，仅有少数基础研究。
2. 蛋白大小140 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0DI81
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196459-TRAPPC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Trappc2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0DI81
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000196459-TRAPPC2/subcellular

![](https://images.proteinatlas.org/63308/1186_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/63308/1186_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/63308/1200_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/63308/1200_G12_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0DI81-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
