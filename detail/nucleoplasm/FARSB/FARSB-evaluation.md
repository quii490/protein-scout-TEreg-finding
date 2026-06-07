---
type: protein-evaluation
gene: "FARSB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FARSB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FARSB / FARSLB, FRSB |
| 蛋白名称 | Phenylalanine--tRNA ligase beta subunit |
| 蛋白大小 | 589 aa / 66.1 kDa |
| UniProt ID | Q9NSD9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 589 aa / 66.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.6; PDB: 3L4G |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045864, IPR005146, IPR009061, IPR045060, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- phenylalanine-tRNA ligase complex (GO:0009328)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FARSLB, FRSB |

**关键文献**:
1. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
2. Protein biomarkers for bipolar II disorder are correlated with affective cognitive performance.. *BMC psychiatry*. PMID: 40597064
3. FARSB serves as a novel hypomethylated and immune cell infiltration related prognostic biomarker in hepatocellular carcinoma.. *Aging*. PMID: 37074800
4. Exercise-related immune gene signature for hepatocellular carcinoma: machine learning and multi-omics analysis.. *Frontiers in immunology*. PMID: 40621461
5. Correlation of potential diagnostic biomarkers (circulating miRNA and protein) of bipolar II disorder.. *Journal of psychiatric research*. PMID: 38412788

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.6 |
| 高置信度残基 (pLDDT>90) 占比 | 90.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.6% |
| 可用 PDB 条目 | 3L4G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.6，有序区 99.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045864, IPR005146, IPR009061, IPR045060, IPR004531; Pfam: PF03483, PF03484, PF18262 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FARSA | 0.999 | 0.997 | — |
| FARS2 | 0.997 | 0.574 | — |
| YARS1 | 0.946 | 0.000 | — |
| FDXACB1 | 0.936 | 0.574 | — |
| EEF1B2 | 0.934 | 0.000 | — |
| EPRS1 | 0.925 | 0.126 | — |
| IARS1 | 0.914 | 0.480 | — |
| TMCO1 | 0.884 | 0.000 | — |
| LARS2 | 0.816 | 0.000 | — |
| LARS1 | 0.814 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTB | psi-mi:"MI:0071"(molecular sieving) | pubmed:15047060 |
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| EIF2AK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.6 + PDB: 3L4G | pLDDT=94.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FARSB — Phenylalanine--tRNA ligase beta subunit，非常新颖，仅有少数基础研究。
2. 蛋白大小589 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSD9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116120-FARSB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FARSB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSD9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000116120-FARSB/subcellular

![](https://images.proteinatlas.org/36678/430_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/36678/430_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/36678/432_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/36678/432_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/36678/441_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/36678/441_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NSD9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NSD9 |
| SMART | SM00873;SM00874; |
| UniProt Domain [FT] | DOMAIN 302..379; /note="B5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00816" |
| InterPro | IPR045864;IPR005146;IPR009061;IPR045060;IPR004531;IPR020825;IPR041616;IPR040659;IPR005147; |
| Pfam | PF03483;PF03484;PF18262;PF17759; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116120-FARSB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FARSA | Intact, Biogrid, Bioplex | true |
| ANLN | Biogrid | false |
| ATXN1 | Intact | false |
| HTT | Intact | false |
| IARS1 | Biogrid | false |
| MAD2L2 | Biogrid | false |
| PRKN | Biogrid | false |
| SAR1B | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
