---
type: protein-evaluation
gene: "TTF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TTF1 — REJECTED (研究热度过高 (PubMed strict=1130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTF1 |
| 蛋白名称 | Transcription termination factor 1 |
| 蛋白大小 | 905 aa / 103.1 kDa |
| UniProt ID | Q15361 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli fibrillar center; UniProt: Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 905 aa / 103.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1130 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001005, IPR053078; Pfam: PF13921 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- fibrillar center (GO:0001650)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1130 |
| PubMed broad count | 3273 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeted next-generation sequencing of thirteen causative genes in Chinese patients with congenital hypothyroidism.. *Endocrine journal*. PMID: 30022773
2. Thyroid transcription factor-1.. *The international journal of biochemistry & cell biology*. PMID: 9570141
3. Replication and Meta-Analysis of Common Gene Mutations in TTF1 and TTF2 with Papillary Thyroid Cancer.. *Medicine*. PMID: 26356687
4. TP53, NOTCH2, and STK11 Mutations in a Rare Tumor of non-Small Cell Lung Carcinoma with Diffuse Coexpression of TTF1 and p40 in the Same Tumor Cells.. *International journal of surgical pathology*. PMID: 36253711
5. Regulation of surfactant protein gene transcription.. *Biochimica et biophysica acta*. PMID: 9813380

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 20.6% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 57.8% |
| 有序区域 (pLDDT>70) 占比 | 38.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 38.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001005, IPR053078; Pfam: PF13921 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAZ2A | 0.977 | 0.292 | — |
| CCDC59 | 0.905 | 0.000 | — |
| PRKCB | 0.900 | 0.000 | — |
| PRKACB | 0.900 | 0.000 | — |
| PRKACA | 0.900 | 0.000 | — |
| PRKCG | 0.900 | 0.000 | — |
| PRKACG | 0.900 | 0.000 | — |
| PRKCA | 0.900 | 0.000 | — |
| SMARCA5 | 0.826 | 0.074 | — |
| SFTPC | 0.781 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NKX2-1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| Pax8 | psi-mi:"MI:0096"(pull down) | pubmed:12441357 |
| Wwtr1 | psi-mi:"MI:0096"(pull down) | pubmed:14970209 |
| FOXA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-26468|pubmed:18003659 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HSPD1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| RPS14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 无 | pLDDT=57.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TTF1 — Transcription termination factor 1，研究基础较多，新颖性有限。
2. 蛋白大小905 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1130 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15361
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125482-TTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15361
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (supported)。来源: https://www.proteinatlas.org/ENSG00000125482-TTF1/subcellular

![](https://images.proteinatlas.org/51105/713_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51105/713_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51105/714_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51105/714_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51105/876_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51105/876_E8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15361-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
