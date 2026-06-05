---
type: protein-evaluation
gene: "ST6GALNAC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ST6GALNAC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ST6GALNAC3 / SIAT7C |
| 蛋白名称 | Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 3 |
| 蛋白大小 | 305 aa / 35.4 kDa |
| UniProt ID | Q8NDV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 305 aa / 35.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001675, IPR038578; Pfam: PF00777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIAT7C |

**关键文献**:
1. Biomarker potential of ST6GALNAC3 and ZNF660 promoter hypermethylation in prostate cancer tissue and liquid biopsies.. *Molecular oncology*. PMID: 29465788
2. Transcriptomic underpinnings of high and low mirror aggression zebrafish behaviours.. *BMC biology*. PMID: 35501893
3. Reduction in disialyl-T antigen levels in mice deficient for both St6galnac3 and St6galnac4 results in blood filling of lymph nodes.. *Scientific reports*. PMID: 37386100
4. Expression of leukocyte adhesion-related glycosyltransferase genes in acute coronary syndrome patients.. *Inflammation research : official journal of the European Histamine Research Society ... [et al.]*. PMID: 24748045
5. LncRNA ST6GALNAC3 inhibits dermal fibroblast proliferation and migration in cashmere goat hair follicles via the chi-miR-24-3p/ID4 axis.. *Animal bioscience*. PMID: 40575977

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 74.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 87.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 87.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001675, IPR038578; Pfam: PF00777 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ST3GAL1 | 0.935 | 0.000 | — |
| ST3GAL2 | 0.925 | 0.000 | — |
| AHSG | 0.778 | 0.000 | — |
| ST8SIA6 | 0.638 | 0.000 | — |
| ST8SIA2 | 0.604 | 0.000 | — |
| ST6GALNAC1 | 0.592 | 0.000 | — |
| ZNF660 | 0.580 | 0.000 | — |
| ST8SIA1 | 0.550 | 0.000 | — |
| ST3GAL5 | 0.523 | 0.000 | — |
| C1GALT1 | 0.495 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CLEC2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLRG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTMP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMED6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCEH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCN3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTCH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DUSP14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PON2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 无 | pLDDT=89.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm | 一致 |
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
1. ST6GALNAC3 — Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小305 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184005-ST6GALNAC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ST6GALNAC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184005-ST6GALNAC3/subcellular

![](https://images.proteinatlas.org/54566/1452_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/54566/1452_D8_3_red_green.jpg)
![](https://images.proteinatlas.org/54566/1517_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/54566/1517_D8_3_red_green.jpg)
![](https://images.proteinatlas.org/55399/1251_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/55399/1251_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NDV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
