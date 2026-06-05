---
type: protein-evaluation
gene: "BICDL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BICDL1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BICDL1 / BICDR1, CCDC64 |
| 蛋白名称 | BICD family-like cargo adapter 1 |
| 蛋白大小 | 573 aa / 64.8 kDa |
| UniProt ID | Q6ZP65 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubul |
| 蛋白大小 | 10/10 | ×1 | 10 | 573 aa / 64.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051149 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BICDR1, CCDC64 |

**关键文献**:
1. BICDL1 Predicts Poor Prognosis and is Correlated with Methylation and Immune Infiltration in Colorectal Cancer.. *Pharmacogenomics and personalized medicine*. PMID: 38149287
2. BICDL1 Mediates Pyroptosis to Promote Breast Cancer Cell Proliferation, Inhibition, and Migration.. *Rejuvenation research*. PMID: 40944522

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 50.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 67.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.1，有序区 67.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051149 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTR1A | 0.942 | 0.910 | — |
| DYNC1LI2 | 0.942 | 0.900 | — |
| DCTN5 | 0.939 | 0.925 | — |
| CAPZB | 0.935 | 0.900 | — |
| DYNC1H1 | 0.934 | 0.900 | — |
| DYNC1I2 | 0.921 | 0.900 | — |
| DCTN4 | 0.912 | 0.892 | — |
| RAB6A | 0.894 | 0.100 | — |
| ACTR10 | 0.889 | 0.831 | — |
| DCTN6 | 0.880 | 0.831 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| CSNK2B | psi-mi:"MI:0030"(cross-linking study) | pubmed:36876296|imex:IM-30472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 无 | pLDDT=75.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BICDL1 — BICD family-like cargo adapter 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小573 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZP65
- Protein Atlas: https://www.proteinatlas.org/search/BICDL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BICDL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZP65
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135127-BICDL1/subcellular

![](https://images.proteinatlas.org/61116/1082_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/61116/1082_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/61116/1136_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/61116/1136_D3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZP65-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
