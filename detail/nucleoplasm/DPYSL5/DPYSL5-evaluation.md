---
type: protein-evaluation
gene: "DPYSL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPYSL5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPYSL5 / CRMP5, ULIP6 |
| 蛋白名称 | Dihydropyrimidinase-related protein 5 |
| 蛋白大小 | 564 aa / 61.4 kDa |
| UniProt ID | Q9BPU6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 564 aa / 61.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=91.0; PDB: 4B90, 4B91, 4B92 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006680, IPR011778, IPR011059, IPR032466, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- glutamatergic synapse (GO:0098978)
- neuronal cell body (GO:0043025)
- protein-containing complex (GO:0032991)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 145 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRMP5, ULIP6 |

**关键文献**:
1. DPYSL5 is highly expressed in treatment-induced neuroendocrine prostate cancer and promotes lineage plasticity via EZH2/PRC2.. *Communications biology*. PMID: 38238517
2. Cross-species analysis of adult hippocampal neurogenesis reveals human-specific gene expression but convergent biological processes.. *Nature neuroscience*. PMID: 40790267
3. Missense variants in DPYSL5 cause a neurodevelopmental disorder with corpus callosum agenesis and cerebellar abnormalities.. *American journal of human genetics*. PMID: 33894126
4. Comparative molecular landscapes of immature neurons in the mammalian dentate gyrus across species reveal special features in humans.. *bioRxiv : the preprint server for biology*. PMID: 40027814
5. Integrative genomic and spatial transcriptomic analysis elucidates the oligodendrocyte-mediated etiology of epileptic cortical thinning.. *Epilepsia open*. PMID: 41885647

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 84.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 88.3% |
| 可用 PDB 条目 | 4B90, 4B91, 4B92 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4B90, 4B91, 4B92）+ AlphaFold高质量预测（pLDDT=91.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006680, IPR011778, IPR011059, IPR032466, IPR050378; Pfam: PF01979 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPYSL2 | 0.990 | 0.873 | — |
| FES | 0.918 | 0.046 | — |
| DPYSL3 | 0.907 | 0.838 | — |
| DPYSL4 | 0.898 | 0.700 | — |
| PNMA2 | 0.892 | 0.000 | — |
| AMPH | 0.888 | 0.000 | — |
| LGI1 | 0.879 | 0.000 | — |
| BIN1 | 0.872 | 0.000 | — |
| SLC6A5 | 0.841 | 0.000 | — |
| CNTNAP2 | 0.825 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| APPL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DARS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TUBA1A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| HSPA8 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| DPYSL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| CFAP161 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LGALS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TGIF2LY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 4B90, 4B91, 4B92 | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DPYSL5 — Dihydropyrimidinase-related protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小564 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPU6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157851-DPYSL5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPYSL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPU6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157851-DPYSL5/subcellular

![](https://images.proteinatlas.org/72387/1437_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/72387/1437_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/72387/1475_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/72387/1475_F9_3_red_green.jpg)
![](https://images.proteinatlas.org/72387/1668_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/72387/1668_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BPU6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
