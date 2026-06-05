---
type: protein-evaluation
gene: "SINHCAF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SINHCAF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SINHCAF / C12orf14, FAM60A |
| 蛋白名称 | SIN3-HDAC complex-associated factor |
| 蛋白大小 | 221 aa / 24.9 kDa |
| UniProt ID | Q9NP50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 221 aa / 24.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026065; Pfam: PF15396 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- Sin3-type complex (GO:0070822)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf14, FAM60A |

**关键文献**:
1. SINHCAF/FAM60A and SIN3A specifically repress HIF-2α expression.. *The Biochemical journal*. PMID: 29784889
2. A five-gene signature for predicting overall survival of esophagus adenocarcinoma.. *Medicine*. PMID: 33832101
3. BATF2/SINHCAF regulates the quantity and function of macrophages infected with Mycobacterium Tuberculosis via regulation of TTC23 through Wnt/β-catenin pathway.. *International journal of biological macromolecules*. PMID: 39672395
4. SIN3-HDAC complex-associated factor, a chromatin remodelling gene located in the 12p amplicon, is a potential germ cell tumour-specific oncogene.. *The Journal of pathology*. PMID: 36056608

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 40.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 20.8% |
| 低置信 (pLDDT<50) 占比 | 25.3% |
| 有序区域 (pLDDT>70) 占比 | 53.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 53.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026065; Pfam: PF15396 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIN3A | 0.990 | 0.724 | — |
| ING2 | 0.988 | 0.781 | — |
| HDAC2 | 0.976 | 0.713 | — |
| SAP30 | 0.974 | 0.819 | — |
| HDAC1 | 0.967 | 0.778 | — |
| SUDS3 | 0.963 | 0.742 | — |
| BRMS1 | 0.958 | 0.733 | — |
| SAP30L | 0.958 | 0.760 | — |
| BRMS1L | 0.954 | 0.736 | — |
| ING1 | 0.952 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GTPBP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HDAC1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-18733|pubmed:23752268 |
| SELENBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFP41 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TNRC18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIN3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAP30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZMYM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERPINA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. SINHCAF — SIN3-HDAC complex-associated factor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小221 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NP50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139146-SINHCAF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SINHCAF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NP50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SINHCAF/IF_images/SINHCAF_IF_1032_A11_1_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000139146-SINHCAF/subcellular

![](https://images.proteinatlas.org/38167/1032_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/38167/1032_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/38167/428_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/38167/428_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NP50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
