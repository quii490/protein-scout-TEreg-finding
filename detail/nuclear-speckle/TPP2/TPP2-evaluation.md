---
type: protein-evaluation
gene: "TPP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TPP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPP2 |
| 蛋白名称 | Tripeptidyl-peptidase 2 |
| 蛋白大小 | 1249 aa / 138.3 kDa |
| UniProt ID | P29144 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1249 aa / 138.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000209, IPR036852, IPR022398, IPR023828, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Primary Immune Regulatory Disorders With an Autoimmune Lymphoproliferative Syndrome-Like Phenotype: Immunologic Evaluation, Early Diagnosis and Management.. *Frontiers in immunology*. PMID: 34447369
2. Tripeptidyl peptidase II coordinates the homeostasis of calcium and lipids in the central nervous system and its depletion causes presenile dementia in female mice through calcium/lipid dyshomeostasis-induced autophagic degradation of CYP19A1.. *Theranostics*. PMID: 38389851
3. Identification of multiple organ metastasis-associated hub mRNA/miRNA signatures in non-small cell lung cancer.. *Cell death & disease*. PMID: 38057344
4. Hippocampal proteomic changes of susceptibility and resilience to depression or anxiety in a rat model of chronic mild stress.. *Translational psychiatry*. PMID: 31624233
5. Tripeptidyl peptidase II in human oral squamous cell carcinoma.. *Journal of cancer research and clinical oncology*. PMID: 22986808

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.9 |
| 高置信度残基 (pLDDT>90) 占比 | 80.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.9，有序区 96.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000209, IPR036852, IPR022398, IPR023828, IPR050131; Pfam: PF00082, PF12580, PF12583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERAP2 | 0.905 | 0.000 | — |
| ERAP1 | 0.868 | 0.000 | — |
| POLB | 0.743 | 0.740 | — |
| NRDC | 0.696 | 0.000 | — |
| LNPEP | 0.653 | 0.000 | — |
| THOP1 | 0.639 | 0.000 | — |
| BLMH | 0.634 | 0.000 | — |
| CHIA | 0.627 | 0.387 | — |
| DOK3 | 0.601 | 0.421 | — |
| CARNMT1 | 0.598 | 0.314 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| SMARCB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| RIPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| PTPN1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PTPRA | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.9 + PDB: 无 | pLDDT=91.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TPP2 — Tripeptidyl-peptidase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小1249 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29144
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134900-TPP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29144
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000134900-TPP2/subcellular

![](https://images.proteinatlas.org/49630/1177_A8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/49630/1177_A8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/49630/783_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49630/783_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49630/987_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49630/987_C4_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P29144-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
