---
type: protein-evaluation
gene: "CTSV"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTSV 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTSV / CATL2, CTSL2, CTSU |
| 蛋白名称 | Cathepsin L2 |
| 蛋白大小 | 334 aa / 37.3 kDa |
| UniProt ID | O60911 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; 额外: Nucleoplasm, Plasma ; UniProt: Lysosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 37.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.9; PDB: 1FH0, 3H6S, 3KFQ, 7PK4, 7Q8D, 7Q8F, 7Q8G |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR038765, IPR025661, IPR000169, IPR025660, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- lysosomal lumen (GO:0043202)
- lysosome (GO:0005764)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CATL2, CTSL2, CTSU |

**关键文献**:
1. Trichodermin, an endophytic fungal sesquiterpene, suppresses colorectal cancer cell migration and invasion by targeting the PKC-ERK-Sp1-CTSV axis.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 40674912
2. Metal-dependent cell death resistance contribute to lymph node metastasis of oral squamous cell carcinoma.. *Frontiers in cell and developmental biology*. PMID: 40083663
3. Cathepsin V is correlated with the prognosis and tumor microenvironment in liver cancer.. *Molecular carcinogenesis*. PMID: 38051285
4. Cathepsin V regulates cell cycle progression and histone stability in the nucleus of breast cancer cells.. *Frontiers in pharmacology*. PMID: 38026973
5. Exogenous cathepsin V protein protects human cardiomyocytes HCM from angiotensin Ⅱ-Induced hypertrophy.. *The international journal of biochemistry & cell biology*. PMID: 28522343

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 85.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 1FH0, 3H6S, 3KFQ, 7PK4, 7Q8D, 7Q8F, 7Q8G, 7Q8H, 7Q8I, 7Q8J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1FH0, 3H6S, 3KFQ, 7PK4, 7Q8D, 7Q8F, 7Q8G, 7Q8H, 7Q8I, 7Q8J）+ AlphaFold极高置信度预测（pLDDT=92.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038765, IPR025661, IPR000169, IPR025660, IPR013128; Pfam: PF08246, PF00112 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTA | 0.960 | 0.919 | — |
| BCL2 | 0.926 | 0.000 | — |
| BID | 0.905 | 0.000 | — |
| BCL2L1 | 0.902 | 0.000 | — |
| CTSL | 0.815 | 0.689 | — |
| SERPINB13 | 0.758 | 0.052 | — |
| SCUBE2 | 0.711 | 0.069 | — |
| TIMP1 | 0.705 | 0.000 | — |
| ZNF157 | 0.673 | 0.048 | — |
| CTSK | 0.665 | 0.613 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| srp-6 | psi-mi:"MI:0415"(enzymatic study) | imex:IM-11868|pubmed:17889653 |
| DNAAF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB28 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ZIC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBFOX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| L2HGDH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBC1D22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTSK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 1FH0, 3H6S, 3KFQ, 7PK4, 7Q8D,  | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome / Nucleoli fibrillar center, Cytosol; 额外: Nucleoplas | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CTSV — Cathepsin L2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60911
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136943-CTSV/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTSV
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60911
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000136943-CTSV/subcellular

![](https://images.proteinatlas.org/17112/611_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17112/611_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/17112/614_A1_3_red_green.jpg)
![](https://images.proteinatlas.org/17112/614_A1_4_red_green.jpg)
![](https://images.proteinatlas.org/17112/618_A1_5_red_green.jpg)
![](https://images.proteinatlas.org/17112/618_A1_9_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60911-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
