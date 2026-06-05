---
type: protein-evaluation
gene: "HMBOX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMBOX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMBOX1 / HOT1, TAH1 |
| 蛋白名称 | Homeobox-containing protein 1 |
| 蛋白大小 | 420 aa / 47.3 kDa |
| UniProt ID | Q6NT76 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus; Cytoplasm; Chromosome, telomere; Nucleus, Cajal bod |
| 蛋白大小 | 10/10 | ×1 | 10 | 420 aa / 47.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 2CUF, 4J19 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001387, IPR001356, IPR040363, IPR006899, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Chromosome, telomere; Nucleus, Cajal body; Nucleus, PML body; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- centrosome (GO:0005813)
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HOT1, TAH1 |

**关键文献**:
1. HMBOX1 reverses autophagy mediated 5-fluorouracil resistance through promoting HACE1-induced ubiquitination and degradation of ATG5 in colorectal cancer.. *Autophagy*. PMID: 40126194
2. Identification of new telomere- and telomerase-associated autoantigens in systemic sclerosis.. *Journal of autoimmunity*. PMID: 36634459
3. HMBOX1, a member of the homeobox family: current research progress.. *Central-European journal of immunology*. PMID: 37206587
4. Homeobox‑containing protein 1 loss is associated with clinicopathological performance in glioma.. *Molecular medicine reports*. PMID: 28731165
5. Isolation and functional analysis of human HMBOX1, a homeobox containing protein with transcriptional repressor activity.. *Cytogenetic and genome research*. PMID: 16825764

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 40.0% |
| 有序区域 (pLDDT>70) 占比 | 51.7% |
| 可用 PDB 条目 | 2CUF, 4J19 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 51.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001387, IPR001356, IPR040363, IPR006899, IPR044869; Pfam: PF04814, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEMO1 | 0.591 | 0.591 | — |
| MT2A | 0.576 | 0.000 | — |
| CTC1 | 0.537 | 0.000 | — |
| NHP2 | 0.519 | 0.301 | — |
| HIPK1 | 0.508 | 0.000 | — |
| RUVBL2 | 0.481 | 0.000 | — |
| RUVBL1 | 0.480 | 0.000 | — |
| ASB7 | 0.466 | 0.421 | — |
| NR2E1 | 0.463 | 0.046 | — |
| ZBTB48 | 0.459 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D3DSU0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENTPD2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| MEMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMNA | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| DYNLL2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MGC50722 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZFYVE26 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDK18 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 2CUF, 4J19 | pLDDT=68.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome, telomere; Nucleus, / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
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
1. HMBOX1 — Homeobox-containing protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小420 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NT76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147421-HMBOX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMBOX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NT76
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000147421-HMBOX1/subcellular

![](https://images.proteinatlas.org/55855/874_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/55855/874_G11_6_red_green.jpg)
![](https://images.proteinatlas.org/55855/879_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/55855/879_B10_5_red_green.jpg)
![](https://images.proteinatlas.org/55855/881_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/55855/881_G11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NT76-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
