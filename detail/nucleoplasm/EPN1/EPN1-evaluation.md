---
type: protein-evaluation
gene: "EPN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPN1 |
| 蛋白名称 | Epsin-1 |
| 蛋白大小 | 576 aa / 60.3 kDa |
| UniProt ID | Q9Y6I3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: Cytoplasm; Cell membrane; Nucleus; Membrane, clathrin-coated |
| 蛋白大小 | 10/10 | ×1 | 10 | 576 aa / 60.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.8; PDB: 1INZ, 1KYD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013809, IPR008942, IPR003903; Pfam: PF01417 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasm; Cell membrane; Nucleus; Membrane, clathrin-coated pit | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin vesicle coat (GO:0030125)
- clathrin-coated pit (GO:0005905)
- cytosol (GO:0005829)
- endosome (GO:0005768)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. UBE2C-induced crosstalk between mono- and polyubiquitination of SNAT2 promotes lymphatic metastasis in bladder cancer.. *The Journal of clinical investigation*. PMID: 38949026
2. Intersectin1 promotes clathrin-mediated endocytosis by organizing and stabilizing endocytic protein interaction networks.. *Cell reports*. PMID: 39580802
3. A single-particle analysis method for detecting membrane remodelling and curvature sensing.. *Journal of cell science*. PMID: 39324332
4. m(6)A Regulator Expression Segregates Meningiomas Into Biologically Distinct Subtypes.. *Frontiers in oncology*. PMID: 35004283
5. Intersectin1 promotes clathrin-mediated endocytosis by organizing and stabilizing endocytic protein interaction networks.. *bioRxiv : the preprint server for biology*. PMID: 38712149

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.8 |
| 高置信度残基 (pLDDT>90) 占比 | 25.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 24.1% |
| 低置信 (pLDDT<50) 占比 | 38.2% |
| 有序区域 (pLDDT>70) 占比 | 37.7% |
| 可用 PDB 条目 | 1INZ, 1KYD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.8），有序残基占 37.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013809, IPR008942, IPR003903; Pfam: PF01417 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS15 | 0.998 | 0.875 | — |
| EPS15L1 | 0.981 | 0.480 | — |
| REPS2 | 0.978 | 0.734 | — |
| EGFR | 0.958 | 0.625 | — |
| AP2A1 | 0.958 | 0.475 | — |
| CLTC | 0.929 | 0.650 | — |
| CLTCL1 | 0.921 | 0.422 | — |
| SNAP91 | 0.908 | 0.095 | — |
| HIP1R | 0.879 | 0.550 | — |
| ITSN1 | 0.872 | 0.108 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED31 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Q81V99 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| FLVCR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PICALM | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.8 + PDB: 1INZ, 1KYD | pLDDT=63.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Nucleus; Membrane, clath / Plasma membrane, Cytosol; 额外: Nucleoplasm, Vesicle | 一致 |
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
1. EPN1 — Epsin-1，非常新颖，仅有少数基础研究。
2. 蛋白大小576 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6I3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000063245-EPN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6I3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000063245-EPN1/subcellular

![](https://images.proteinatlas.org/61136/1118_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61136/1118_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61136/1153_F10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61136/1153_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61136/1192_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61136/1192_F9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6I3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y6I3 |
| SMART | SM00273;SM00726; |
| UniProt Domain [FT] | DOMAIN 12..144; /note="ENTH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00243"; DOMAIN 183..202; /note="UIM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00213"; DOMAIN 208..227; /note="UIM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00213"; DOMAIN 233..252; /note="UIM 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00213" |
| InterPro | IPR013809;IPR008942;IPR003903; |
| Pfam | PF01417; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000063245-EPN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EPS15 | Intact, Biogrid | true |
| PHGDH | Intact, Biogrid, Opencell | true |
| REPS2 | Intact, Biogrid | true |
| AP2A1 | Biogrid | false |
| AP2A2 | Biogrid | false |
| AP2B1 | Biogrid | false |
| CLTA | Biogrid | false |
| CLTC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
