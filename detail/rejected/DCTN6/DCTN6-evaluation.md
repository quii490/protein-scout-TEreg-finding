---
type: protein-evaluation
gene: "DCTN6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCTN6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTN6 / WS3 |
| 蛋白名称 | Dynactin subunit 6 |
| 蛋白大小 | 190 aa / 20.7 kDa |
| UniProt ID | O00399 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytoskeleton; Chromosome, centromere, kinetochore |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 20.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.0; PDB: 3TV0, 9B7J, 9B85 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027777, IPR011004 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- dynactin complex (GO:0005869)
- kinetochore (GO:0000776)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WS3 |

**关键文献**:
1. Prognostic Value of Dynactin mRNA Expression in Cutaneous Melanoma.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 29864111
2. Dynactin 6 deficiency enhances aging-associated dystrophic neurite formation in mouse brains.. *Neurobiology of aging*. PMID: 34371284
3. Study on the Prognostic Values of Dynactin Genes in Low-Grade Glioma.. *Technology in cancer research & treatment*. PMID: 33896271
4. Dynactin pathway-related gene expression is altered by aging, but not by vitrification.. *Reproductive toxicology (Elmsford, N.Y.)*. PMID: 31260804
5. Dynactin 2 acts as an oncogene in hepatocellular carcinoma through promoting cell cycle progression.. *Liver research (Beijing, China)*. PMID: 39958200

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 5.8% |
| 置信残基 (pLDDT 70-90) 占比 | 56.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.6% |
| 低置信 (pLDDT<50) 占比 | 25.3% |
| 有序区域 (pLDDT>70) 占比 | 62.1% |
| 可用 PDB 条目 | 3TV0, 9B7J, 9B85 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3TV0, 9B7J, 9B85）+ AlphaFold高质量预测（pLDDT=71.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027777, IPR011004 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCTN5-p25 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| DCTN6-p27 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RPSA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Dmel\CG17107 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Capza1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Actr1a | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dctn1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| UQCRH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 3TV0, 9B7J, 9B85 | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Chromosome, centromere, k / Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DCTN6 — Dynactin subunit 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00399
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104671-DCTN6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTN6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00399
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000104671-DCTN6/subcellular

![](https://images.proteinatlas.org/24558/195_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24558/195_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24558/196_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24558/196_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24558/197_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24558/197_D8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00399-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
