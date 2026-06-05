---
type: protein-evaluation
gene: "GMPR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GMPR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GMPR2 |
| 蛋白名称 | GMP reductase 2 |
| 蛋白大小 | 348 aa / 37.9 kDa |
| UniProt ID | Q9P2T1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 37.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=96.8; PDB: 2A7R, 2BZN, 2C6Q |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013785, IPR050139, IPR005993, IPR015875, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- GMP reductase complex (GO:1902560)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of prospective aging drug targets via Mendelian randomization analysis.. *Aging cell*. PMID: 38572516
2. Genetic variation perspective reveals potential drug targets for subtypes of endometrial cancer.. *Scientific reports*. PMID: 39548148
3. Lack of expression of the proteins GMPR2 and PPARα are associated with the basal phenotype and patient outcome in breast cancer.. *Breast cancer research and treatment*. PMID: 23208589
4. NopAA and NopD Signaling Association-Related Gene GmNAC27 Promotes Nodulation in Soybean (Glycine max).. *International journal of molecular sciences*. PMID: 38139327
5. Cloning and functional characterization of GMPR2, a novel human guanosine monophosphate reductase, which promotes the monocytic differentiation of HL-60 leukemia cells.. *Journal of cancer research and clinical oncology*. PMID: 12669231

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.8 |
| 高置信度残基 (pLDDT>90) 占比 | 93.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 98.9% |
| 可用 PDB 条目 | 2A7R, 2BZN, 2C6Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2A7R, 2BZN, 2C6Q）+ AlphaFold高质量预测（pLDDT=96.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013785, IPR050139, IPR005993, IPR015875, IPR001093; Pfam: PF00478 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GMPR | 0.900 | 0.672 | — |
| EPHX2 | 0.860 | 0.000 | — |
| GMPS | 0.848 | 0.000 | — |
| ATIC | 0.704 | 0.000 | — |
| GART | 0.622 | 0.000 | — |
| SNX17 | 0.612 | 0.583 | — |
| ADSL | 0.608 | 0.000 | — |
| ADSS2 | 0.597 | 0.000 | — |
| ADSS1 | 0.577 | 0.000 | — |
| FH | 0.577 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GMPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| lepB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| SNX17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ENST00000355299 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.8 + PDB: 2A7R, 2BZN, 2C6Q | pLDDT=96.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GMPR2 — GMP reductase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2T1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100938-GMPR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GMPR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2T1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000100938-GMPR2/subcellular

![](https://images.proteinatlas.org/67884/1354_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/67884/1354_D9_3_red_green.jpg)
![](https://images.proteinatlas.org/67884/1362_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/67884/1362_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/67884/1418_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/67884/1418_D8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2T1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
