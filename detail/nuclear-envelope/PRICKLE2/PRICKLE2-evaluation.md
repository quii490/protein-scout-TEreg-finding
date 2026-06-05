---
type: protein-evaluation
gene: "PRICKLE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRICKLE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRICKLE2 |
| 蛋白名称 | Prickle-like protein 2 |
| 蛋白大小 | 844 aa / 95.6 kDa |
| UniProt ID | Q7Z3G6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Vesicles; UniProt: Postsynaptic density; Cell projection, axon; Cell projection |
| 蛋白大小 | 8/10 | ×1 | 8 | 844 aa / 95.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033725, IPR033726, IPR033727, IPR010442, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Vesicles | Approved |
| UniProt | Postsynaptic density; Cell projection, axon; Cell projection, dendrite; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- axon initial segment (GO:0043194)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- nuclear membrane (GO:0031965)
- nucleus (GO:0005634)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 96 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Evolving Insights into Prickle2 in Neurodevelopment and Neurological Disorders.. *Molecular neurobiology*. PMID: 40009262
2. Decoding Epilepsy: Prickle2 and Multifaceted Molecular Pathway Connections.. *Current pharmaceutical design*. PMID: 39754765
3. The core PCP protein Prickle2 regulates axon number and AIS maturation by binding to AnkG and modulating microtubule bundling.. *Science advances*. PMID: 36083912
4. Role of Prickle1 and Prickle2 in neurite outgrowth in murine neuroblastoma cells.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 22218901
5. Modulation of Prickle2 Expression to Facilitate Dentine Formation: A Laboratory Investigation.. *International endodontic journal*. PMID: 40916368

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 60.7% |
| 有序区域 (pLDDT>70) 占比 | 33.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 33.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033725, IPR033726, IPR033727, IPR010442, IPR033723; Pfam: PF00412, PF06297 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VANGL2 | 0.997 | 0.301 | — |
| VANGL1 | 0.994 | 0.301 | — |
| DVL1 | 0.993 | 0.238 | — |
| DVL2 | 0.971 | 0.238 | — |
| DVL3 | 0.962 | 0.238 | — |
| ANKRD6 | 0.854 | 0.106 | — |
| CELSR1 | 0.782 | 0.081 | — |
| DLG4 | 0.712 | 0.047 | — |
| INVS | 0.686 | 0.096 | — |
| FZD6 | 0.682 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Smurf2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12177|pubmed:19379695 |
| SYNGAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| RIMS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynaptic density; Cell projection, axon; Cell  / Golgi apparatus; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. PRICKLE2 — Prickle-like protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小844 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3G6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163637-PRICKLE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRICKLE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3G6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000163637-PRICKLE2/subcellular

![](https://images.proteinatlas.org/35493/381_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35493/381_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35493/389_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35493/389_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35493/398_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35493/398_G8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z3G6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
