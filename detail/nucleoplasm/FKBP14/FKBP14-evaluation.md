---
type: protein-evaluation
gene: "FKBP14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKBP14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKBP14 / FKBP22 |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase FKBP14 |
| 蛋白大小 | 211 aa / 24.2 kDa |
| UniProt ID | Q9NWM8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Golgi apparatus; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 211 aa / 24.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.4; PDB: 4DIP, 4MSP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR018247, IPR002048, IPR046357, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKBP22 |

**关键文献**:
1. FKBP14 Kyphoscoliotic Ehlers-Danlos Syndrome.. **. PMID: 31132235
2. FKBP14 is an essential gene that regulates Presenilin protein levels and Notch signaling in Drosophila.. *Development (Cambridge, England)*. PMID: 23318643
3. Further delineation of FKBP14-related Ehlers-Danlos syndrome: A patient with early vascular complications and non-progressive kyphoscoliosis, and literature review.. *American journal of medical genetics. Part A*. PMID: 27149304
4. FKBP14 overexpression contributes to osteosarcoma carcinogenesis and indicates poor survival outcome.. *Oncotarget*. PMID: 27223089
5. Ehlers-Danlos syndrome related to FKBP14 mutations: detailed cutaneous phenotype.. *Clinical and experimental dermatology*. PMID: 27905128

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 66.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 4DIP, 4MSP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4DIP, 4MSP）+ AlphaFold高质量预测（pLDDT=88.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR046357, IPR052273; Pfam: PF00254 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XBP1 | 0.771 | 0.000 | — |
| PLOD1 | 0.692 | 0.000 | — |
| CHST14 | 0.665 | 0.000 | — |
| SLC39A13 | 0.645 | 0.000 | — |
| B4GALT7 | 0.625 | 0.000 | — |
| ZNF469 | 0.617 | 0.070 | — |
| COL3A1 | 0.616 | 0.067 | — |
| FKBP6 | 0.607 | 0.000 | — |
| B3GALT6 | 0.605 | 0.000 | — |
| PRDM5 | 0.574 | 0.070 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG5890 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| H4C16 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12102|pubmed:19862764 |
| SERPINA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM237 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LYZL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| S1PR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSHB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POMGNT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 4DIP, 4MSP | pLDDT=88.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / Cytosol; 额外: Nucleoplasm, Golgi apparatus | 一致 |
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
1. FKBP14 — Peptidyl-prolyl cis-trans isomerase FKBP14，非常新颖，仅有少数基础研究。
2. 蛋白大小211 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWM8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106080-FKBP14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKBP14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWM8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
