---
type: protein-evaluation
gene: "U2SURP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## U2SURP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | U2SURP / KIAA0332, SR140 |
| 蛋白名称 | U2 snRNP-associated SURP motif-containing protein |
| 蛋白大小 | 1029 aa / 118.3 kDa |
| UniProt ID | O15042 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1029 aa / 118.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006569, IPR008942, IPR013170, IPR012677, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- U2 snRNP (GO:0005686)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0332, SR140 |

**关键文献**:
1. RBM17 Interacts with U2SURP and CHERP to Regulate Expression and Splicing of RNA-Processing Proteins.. *Cell reports*. PMID: 30332651
2. Bioinformatics analysis of the mechanisms of traumatic brain injury-associated dementia based on the competing endogenous RNA.. *Psychopharmacology*. PMID: 39317770
3. MYC-driven U2SURP regulates alternative splicing of SAT1 to promote triple-negative breast cancer progression.. *Cancer letters*. PMID: 36907504
4. Comprehensive systems biology analysis reveals splicing factor contributions to cutaneous melanoma progression.. *Scientific reports*. PMID: 40108329
5. LncRNA RP11-10E18.7 cooperates with lncRNA RP11-481C4.2 to affect the overall survival of breast cancer patients: a TCGA-based retrospective study.. *Translational cancer research*. PMID: 38130297

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 26.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 45.2% |
| 有序区域 (pLDDT>70) 占比 | 46.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 46.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006569, IPR008942, IPR013170, IPR012677, IPR035979; Pfam: PF04818, PF08312, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHERP | 0.995 | 0.792 | — |
| RBM17 | 0.995 | 0.865 | — |
| SF3A2 | 0.963 | 0.815 | — |
| DHX15 | 0.950 | 0.376 | — |
| SNRPA1 | 0.934 | 0.591 | — |
| PRPF40A | 0.927 | 0.488 | — |
| DDX46 | 0.918 | 0.000 | — |
| SF3B1 | 0.908 | 0.481 | — |
| PUF60 | 0.886 | 0.114 | — |
| SNRPB2 | 0.884 | 0.166 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| TBC1D4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| Sf3a1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ESR1 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13780|pubmed:21182205 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 无 | pLDDT=64.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. U2SURP — U2 snRNP-associated SURP motif-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1029 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15042
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163714-U2SURP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=U2SURP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15042
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163714-U2SURP/subcellular

![](https://images.proteinatlas.org/37545/430_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/37545/430_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/37545/432_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/37545/432_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/37545/441_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/37545/441_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15042-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
