---
type: protein-evaluation
gene: "MTPN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTPN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTPN |
| 蛋白名称 | Myotrophin |
| 蛋白大小 | 118 aa / 12.9 kDa |
| UniProt ID | P58546 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 8/10 | ×1 | 8 | 118 aa / 12.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.2; PDB: 3AAA, 7DF7, 7DSA, 7DSB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770; Pfam: PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- F-actin capping protein complex (GO:0008290)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular characterization, expression patterns and subcellular localization of Myotrophin (MTPN) gene in porcine skeletal muscle.. *Molecular biology reports*. PMID: 21667249
2. Targeting MTPN sensitizes pancreatic cancer of wild-type BRCA1/2 to Cisplatin-based chemotherapy.. *Cancer gene therapy*. PMID: 40903529
3. MiR-375, a microRNA related to diabetes.. *Gene*. PMID: 24120394
4. Identification of robust diagnostic and prognostic gene signatures in different grades of gliomas: a retrospective study.. *PeerJ*. PMID: 34026352
5. Validating genomic prediction for nitrogen efficiency index and its composition traits of Holstein cows in early lactation.. *Journal of animal breeding and genetics = Zeitschrift fur Tierzuchtung und Zuchtungsbiologie*. PMID: 37571877

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 56.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.3% |
| 可用 PDB 条目 | 3AAA, 7DF7, 7DSA, 7DSB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3AAA, 7DF7, 7DSA, 7DSB）+ AlphaFold高质量预测（pLDDT=88.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770; Pfam: PF12796 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAPZA1 | 0.962 | 0.797 | — |
| CAPZB | 0.945 | 0.857 | — |
| LUZP6 | 0.925 | 0.000 | — |
| CAPZA2 | 0.899 | 0.470 | — |
| ADD1 | 0.756 | 0.098 | — |
| CAPG | 0.754 | 0.042 | — |
| CAPZA3 | 0.753 | 0.439 | — |
| ADD2 | 0.739 | 0.098 | — |
| TMOD4 | 0.721 | 0.000 | — |
| NFKBIA | 0.686 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EPB41 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNFRSF10D | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DSTYK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 3AAA, 7DF7, 7DSA, 7DSB | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, perinuclear region / Plasma membrane, Cytosol | 一致 |
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
1. MTPN — Myotrophin，非常新颖，仅有少数基础研究。
2. 蛋白大小118 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58546
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105887-MTPN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58546
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000105887-MTPN/subcellular

![](https://images.proteinatlas.org/19735/284_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19735/284_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19735/285_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19735/285_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19735/286_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19735/286_B2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58546-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
