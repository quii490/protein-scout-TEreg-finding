---
type: protein-evaluation
gene: "FBXL20"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXL20 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL20 / FBL2 |
| 蛋白名称 | F-box/LRR-repeat protein 20 |
| 蛋白大小 | 436 aa / 48.4 kDa |
| UniProt ID | Q96IG2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 436 aa / 48.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001810, IPR057207, IPR001611, IPR006553, IPR032 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- presynapse (GO:0098793)
- SCF ubiquitin ligase complex (GO:0019005)
- Schaffer collateral - CA1 synapse (GO:0098685)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL2 |

**关键文献**:
1. LUBAC and OTULIN regulate autophagy initiation and maturation by mediating the linear ubiquitination and the stabilization of ATG13.. *Autophagy*. PMID: 32543267
2. FBXL20 promotes synaptic impairment in depression disorder via degrading vesicle-associated proteins.. *Journal of affective disorders*. PMID: 38211741
3. Expression and association of IL-21, FBXL20 and tumour suppressor gene PTEN in laryngeal cancer.. *Saudi journal of biological sciences*. PMID: 31889792
4. Transcriptome-wide association study and Mendelian randomization in pancreatic cancer identifies susceptibility genes and causal relationships with type 2 diabetes and venous thromboembolism.. *EBioMedicine*. PMID: 39002386
5. FBXL20 acts as an invasion inducer and mediates E-cadherin in colorectal adenocarcinoma.. *Oncology letters*. PMID: 24932313

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.9 |
| 高置信度残基 (pLDDT>90) 占比 | 77.1% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.9，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001810, IPR057207, IPR001611, IPR006553, IPR032675; Pfam: PF25372, PF12937, PF13516 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Skp1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12015|pubmed:17803915 |
| Cul1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12015|pubmed:17803915 |
| Rims1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12015|pubmed:17803915 |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12015|pubmed:17803915 |
| Syp | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-12015|pubmed:17803915 |
| YPEL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YPEL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RABGGTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDE6D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 12
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.9 + PDB: 无 | pLDDT=90.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Microtubules | 一致 |
| PPI | STRING + IntAct | 0 + 12 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXL20 — F-box/LRR-repeat protein 20，非常新颖，仅有少数基础研究。
2. 蛋白大小436 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96IG2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108306-FBXL20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IG2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IG2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
