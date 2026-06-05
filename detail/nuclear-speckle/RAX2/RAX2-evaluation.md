---
type: protein-evaluation
gene: "RAX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RAX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAX2 / QRX, RAXL1 |
| 蛋白名称 | Retina and anterior neural fold homeobox protein 2 |
| 蛋白大小 | 184 aa / 20.1 kDa |
| UniProt ID | Q96IS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 20.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR043562; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: QRX, RAXL1 |

**关键文献**:
1. PABPC1-induced stabilization of BDNF-AS inhibits malignant progression of glioblastoma cells through STAU1-mediated decay.. *Cell death & disease*. PMID: 32015336
2. Evolution of the Rax family of developmental transcription factors in vertebrates.. *Mechanisms of development*. PMID: 27838261
3. Biallelic sequence and structural variants in RAX2 are a novel cause for autosomal recessive inherited retinal disease.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 30377383
4. Function of rax2p in the polarized growth of fission yeast.. *Molecules and cells*. PMID: 17085965
5. Multigenerational cortical inheritance of the Rax2 protein in orienting polarity and division in yeast.. *Science (New York, N.Y.)*. PMID: 11110666

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 58.7% |
| 低置信 (pLDDT<50) 占比 | 7.6% |
| 有序区域 (pLDDT>70) 占比 | 33.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 33.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR043562; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PITPNM3 | 0.814 | 0.000 | — |
| GUCY2D | 0.774 | 0.000 | — |
| ABCA4 | 0.768 | 0.045 | — |
| AIPL1 | 0.751 | 0.000 | — |
| CDHR1 | 0.737 | 0.000 | — |
| RPGRIP1 | 0.726 | 0.065 | — |
| UNC119 | 0.713 | 0.000 | — |
| SEMA4A | 0.692 | 0.000 | — |
| RIMS1 | 0.674 | 0.000 | — |
| USP49 | 0.660 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RIX7 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| LTE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14660704 |
| COP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18397371|imex:IM-19023 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| NAP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:25416945|imex:IM-23842 |
| EBI-46417783 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37965720|imex:IM-28211 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 无 | pLDDT=69.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RAX2 — Retina and anterior neural fold homeobox protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96IS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173976-RAX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000173976-RAX2/subcellular

![](https://images.proteinatlas.org/52533/1952_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/52533/1952_D5_3_red_green.jpg)
![](https://images.proteinatlas.org/52533/1977_G2_59_cr5e58c8649bfee_red_green.jpg)
![](https://images.proteinatlas.org/52533/1977_G2_61_red_green.jpg)
![](https://images.proteinatlas.org/52533/2070_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/52533/2070_F4_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IS3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
