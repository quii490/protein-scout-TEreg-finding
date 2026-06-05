---
type: protein-evaluation
gene: "SAFB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SAFB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SAFB2 / KIAA0138 |
| 蛋白名称 | Scaffold attachment factor B2 |
| 蛋白大小 | 953 aa / 107.5 kDa |
| UniProt ID | Q14151 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 953 aa / 107.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR000504, IPR051738, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Vesicles | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0138 |

**关键文献**:
1. Scaffold attachment factors SAFB1 and SAFB2: Innocent bystanders or critical players in breast tumorigenesis?. *Journal of cellular biochemistry*. PMID: 14587024
2. Blood transcriptome sequencing identifies biomarkers able to track disease stages in spinocerebellar ataxia type 3.. *Brain : a journal of neurology*. PMID: 37071051
3. SUMOylation substrate encoding genes as prognostic biomarkers in pancreatic ductal adenocarcinoma with functional assessment of SAF-B2.. *Frontiers in pharmacology*. PMID: 40308776
4. SAFB2, a new scaffold attachment factor homolog and estrogen receptor corepressor.. *The Journal of biological chemistry*. PMID: 12660241
5. Low SAFB levels are associated with worse outcome in breast cancer patients.. *Breast cancer research and treatment*. PMID: 19137425

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 66.9% |
| 有序区域 (pLDDT>70) 占比 | 25.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 25.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR000504, IPR051738, IPR034781; Pfam: PF00076, PF02037 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SORBS3 | 0.887 | 0.292 | — |
| ESR1 | 0.872 | 0.292 | — |
| SAFB | 0.754 | 0.622 | — |
| SRPK1 | 0.693 | 0.292 | — |
| NCBP2 | 0.689 | 0.599 | — |
| HNRNPUL1 | 0.686 | 0.622 | — |
| RBMX | 0.629 | 0.477 | — |
| SRCAP | 0.625 | 0.602 | — |
| HNRNPU | 0.618 | 0.000 | — |
| FUS | 0.612 | 0.424 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| CHGB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GIT2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FUS | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FNTA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZSCAN18 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ESR1 | psi-mi:"MI:0096"(pull down) | pubmed:12660241|imex:IM-19378 |
| SORBS3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12660241|imex:IM-19378 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 无 | pLDDT=54.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nuclear bodies, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SAFB2 — Scaffold attachment factor B2，非常新颖，仅有少数基础研究。
2. 蛋白大小953 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14151
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130254-SAFB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAFB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14151
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000130254-SAFB2/subcellular

![](https://images.proteinatlas.org/50894/712_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/50894/712_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/50894/804_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/50894/804_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/50894/964_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/50894/964_G9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14151-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
