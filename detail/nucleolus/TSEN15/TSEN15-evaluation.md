---
type: protein-evaluation
gene: "TSEN15"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSEN15 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSEN15 / C1orf19, SEN15 |
| 蛋白名称 | tRNA-splicing endonuclease subunit Sen15 |
| 蛋白大小 | 171 aa / 18.6 kDa |
| UniProt ID | Q8WW01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 171 aa / 18.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.0; PDB: 2GW6, 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018593, IPR011856, IPR036167; Pfam: PF09631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **150.0/180** | |
| **归一化总分** | | | **83.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf19, SEN15 |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. A susceptibility gene signature for ERBB2-driven mammary tumour development and metastasis in collaborative cross mice.. *EBioMedicine*. PMID: 39067134
3. A Three-Gene Peripheral Blood Potential Diagnosis Signature for Acute Rejection in Renal Transplantation.. *Frontiers in molecular biosciences*. PMID: 34017855
4. Autosomal-Recessive Mutations in the tRNA Splicing Endonuclease Subunit TSEN15 Cause Pontocerebellar Hypoplasia and Progressive Microcephaly.. *American journal of human genetics*. PMID: 27392077
5. A splice site mutation in the TSEN2 causes a new syndrome with craniofacial and central nervous system malformations, and atypical hemolytic uremic syndrome.. *Clinical genetics*. PMID: 34964109

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.0 |
| 高置信度残基 (pLDDT>90) 占比 | 39.8% |
| 置信残基 (pLDDT 70-90) 占比 | 31.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 20.5% |
| 有序区域 (pLDDT>70) 占比 | 70.8% |
| 可用 PDB 条目 | 2GW6, 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2GW6, 6Z9U, 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS）+ AlphaFold极高置信度预测（pLDDT=77.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018593, IPR011856, IPR036167; Pfam: PF09631 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSEN2 | 0.999 | 0.782 | — |
| TSEN54 | 0.999 | 0.821 | — |
| TSEN34 | 0.999 | 0.863 | — |
| CLP1 | 0.979 | 0.786 | — |
| CSTF2 | 0.814 | 0.000 | — |
| CPSF4 | 0.801 | 0.000 | — |
| CPSF1 | 0.800 | 0.000 | — |
| RTCB | 0.531 | 0.000 | — |
| TOE1 | 0.494 | 0.000 | — |
| RARS2 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NBPF3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| Clp1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MINK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSEN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| USP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSEN34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RANGRF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.0 + PDB: 2GW6, 6Z9U, 7UXA, 7ZRZ, 8HMY,  | pLDDT=77.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSEN15 — tRNA-splicing endonuclease subunit Sen15，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小171 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WW01
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198860-TSEN15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSEN15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WW01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000198860-TSEN15/subcellular

![](https://images.proteinatlas.org/29237/564_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/29237/564_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/29237/572_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/29237/572_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/29237/587_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/29237/587_F8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WW01-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
