---
type: protein-evaluation
gene: "HEPACAM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEPACAM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEPACAM2 / MIKI |
| 蛋白名称 | HEPACAM family member 2 |
| 蛋白大小 | 462 aa / 51.4 kDa |
| UniProt ID | A8MVW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Mitotic spindle; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane; Cytoplasm, cytoskeleton, spindle;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 462 aa / 51.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052280, IPR007110, IPR036179, IPR013783, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Mitotic spindle; 额外: Nucleoplasm | Supported |
| UniProt | Golgi apparatus membrane; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, microtubule org... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- midbody (GO:0030496)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MIKI |

**关键文献**:
1. Identification of HEPACAM2 as a novel and specific marker of small cell carcinoma.. *Cancer*. PMID: 39301750
2. Constructing a molecular subtype model of colon cancer using machine learning.. *Frontiers in pharmacology*. PMID: 36188575
3. Gene expression analysis of conjunctival epithelium of patients with Stevens-Johnson syndrome in the chronic stage.. *BMJ open ophthalmology*. PMID: 31276031
4. Analysis of potential genes and pathways associated with the colorectal normal mucosa-adenoma-carcinoma sequence.. *Cancer medicine*. PMID: 29659199
5. Effects of smoking cessation on gene expression in human leukocytes of chronic smoker.. *Psychiatry investigation*. PMID: 25110502

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 54.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.6，有序区 70.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052280, IPR007110, IPR036179, IPR013783, IPR003599; Pfam: PF13927 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SAMD9L | 0.696 | 0.000 | — |
| VPS50 | 0.670 | 0.000 | — |
| SAMD9 | 0.651 | 0.000 | — |
| FGFR1 | 0.616 | 0.321 | — |
| C21orf58 | 0.601 | 0.000 | — |
| KCNQ1 | 0.599 | 0.053 | — |
| UGCG | 0.557 | 0.547 | — |
| TNFRSF10B | 0.548 | 0.548 | — |
| TNKS | 0.496 | 0.000 | — |
| HEMGN | 0.485 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF10B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP4K4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGFR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACVR2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BMPR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MFAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACVR2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 无 | pLDDT=78.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Cytoplasm, cytoskeleton, / Vesicles, Mitotic spindle; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HEPACAM2 — HEPACAM family member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小462 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MVW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188175-HEPACAM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEPACAM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MVW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000188175-HEPACAM2/subcellular

![](https://images.proteinatlas.org/12381/102_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12381/102_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12381/1877_D2_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/12381/1877_D2_32_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MVW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
