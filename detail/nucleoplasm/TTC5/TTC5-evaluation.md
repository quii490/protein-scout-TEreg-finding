---
type: protein-evaluation
gene: "TTC5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC5 |
| 蛋白名称 | Tetratricopeptide repeat protein 5 |
| 蛋白大小 | 440 aa / 48.9 kDa |
| UniProt ID | Q8N0Z6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasmic vesicle; Mitochondrion matri |
| 蛋白大小 | 10/10 | ×1 | 10 | 440 aa / 48.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.3; PDB: 2XVS, 6T59, 7QWS, 8BPO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011990, IPR019734, IPR032076, IPR038645; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasmic vesicle; Mitochondrion matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mechanism of ribosome-associated mRNA degradation during tubulin autoregulation.. *Molecular cell*. PMID: 37295431
2. Soluble αβ-tubulins reversibly sequester TTC5 to regulate tubulin mRNA decay.. *Nature communications*. PMID: 39551769
3. TTC5 syndrome: Clinical and molecular spectrum of a severe and recognizable condition.. *American journal of medical genetics. Part A*. PMID: 35670379
4. Regulation of JMY's actin nucleation activity by TTC5/STRAP and LC3 during autophagy.. *Autophagy*. PMID: 30593260
5. Regulation of glucocorticoid receptor activity by a stress responsive transcriptional cofactor.. *Molecular endocrinology (Baltimore, Md.)*. PMID: 21147850

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.3 |
| 高置信度残基 (pLDDT>90) 占比 | 83.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 2.0% |
| 有序区域 (pLDDT>70) 占比 | 96.1% |
| 可用 PDB 条目 | 2XVS, 6T59, 7QWS, 8BPO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XVS, 6T59, 7QWS, 8BPO）+ AlphaFold高质量预测（pLDDT=93.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734, IPR032076, IPR038645; Pfam: PF16669 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.990 | 0.510 | — |
| JMY | 0.929 | 0.292 | — |
| RPLP0 | 0.904 | 0.800 | — |
| TUBB | 0.904 | 0.904 | — |
| RPL9 | 0.901 | 0.850 | — |
| RPL23A | 0.900 | 0.840 | — |
| RPL11 | 0.899 | 0.829 | — |
| RPL13A | 0.890 | 0.819 | — |
| RPL5 | 0.882 | 0.820 | — |
| RPL23 | 0.880 | 0.820 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OFCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDIPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUBA1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| CAMK2D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HDX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TUBB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.3 + PDB: 2XVS, 6T59, 7QWS, 8BPO | pLDDT=93.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasmic vesicle; Mitochond / Nucleoplasm | 一致 |
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
1. TTC5 — Tetratricopeptide repeat protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小440 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N0Z6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136319-TTC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N0Z6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000136319-TTC5/subcellular

![](https://images.proteinatlas.org/54198/867_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/54198/867_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/54198/903_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/54198/903_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/54198/981_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/54198/981_G2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N0Z6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
