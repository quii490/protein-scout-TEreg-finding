---
type: protein-evaluation
gene: "GPR156"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR156 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR156 / GABABL, PGR28 |
| 蛋白名称 | Probable G-protein coupled receptor 156 |
| 蛋白大小 | 814 aa / 89.1 kDa |
| UniProt ID | Q8NFN8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; UniProt: Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 814 aa / 89.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.5; PDB: 8IEB, 8IED, 8IEI, 8IEP, 8IEQ, 8YJP, 8YK0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002455, IPR017978, IPR041946; Pfam: PF00003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- G protein-coupled receptor heterodimeric complex (GO:0038039)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GABABL, PGR28 |

**关键文献**:
1. Genetic association analysis of 77,539 genomes reveals rare disease etiologies.. *Nature medicine*. PMID: 36928819
2. Molecular insights into the activation mechanism of GPR156 in maintaining auditory function.. *Nature communications*. PMID: 39638804
3. In vitro profiling of orphan G protein coupled receptor (GPCR) constitutive activity.. *British journal of pharmacology*. PMID: 33784795
4. Age-associated changes in gene expression in the anterior pituitary glands of female Japanese black cattle.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 35838775
5. Hear the sounds: the role of G protein-coupled receptors in the cochlea.. *American journal of physiology. Cell physiology*. PMID: 35938679

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 11.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 55.4% |
| 有序区域 (pLDDT>70) 占比 | 33.1% |
| 可用 PDB 条目 | 8IEB, 8IED, 8IEI, 8IEP, 8IEQ, 8YJP, 8YK0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.5），有序残基占 33.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002455, IPR017978, IPR041946; Pfam: PF00003 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABBR1 | 0.934 | 0.000 | — |
| GABBR2 | 0.933 | 0.000 | — |
| GPR158 | 0.676 | 0.000 | — |
| GRM1 | 0.665 | 0.091 | — |
| RAMP3 | 0.649 | 0.000 | — |
| GPRC5A | 0.580 | 0.000 | — |
| CALCRL | 0.551 | 0.000 | — |
| CALCR | 0.551 | 0.000 | — |
| RAMP1 | 0.540 | 0.000 | — |
| RAMP2 | 0.540 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC4A7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZZEF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THAP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOS1AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OBSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRNP200 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FARP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5 + PDB: 8IEB, 8IED, 8IEI, 8IEP, 8IEQ,  | pLDDT=55.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR156 — Probable G-protein coupled receptor 156，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小814 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175697-GPR156/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR156
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000175697-GPR156/subcellular

![](https://images.proteinatlas.org/28644/2242_F6_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/28644/2242_F6_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/28644/2243_A2_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/28644/2243_A2_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/28644/2244_C6_72_blue_red_green.jpg)
![](https://images.proteinatlas.org/28644/2244_C6_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFN8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
