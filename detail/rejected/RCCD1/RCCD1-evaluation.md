---
type: protein-evaluation
gene: "RCCD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RCCD1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RCCD1 |
| 蛋白名称 | RCC1 domain-containing protein 1 |
| 蛋白大小 | 376 aa / 40.1 kDa |
| UniProt ID | A6NED2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 376 aa / 40.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.1; PDB: 6F4R, 6F4S, 6F4T |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009091, IPR052830, IPR000408; Pfam: PF00415 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Enhanced |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and Validation of RPL7 and RCCD1 as Potential Biomarkers Associated with Immune Infiltration in Patients with Thin Endometrium.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 40457017
2. Polymorphic variants involved in methylation regulation: a strategy to discover risk loci for pancreatic ductal adenocarcinoma.. *Journal of medical genetics*. PMID: 37130759
3. RCCD1 promotes breast carcinogenesis through regulating hypoxia-associated mitochondrial homeostasis.. *Oncogene*. PMID: 37903896
4. Gene Expression-Based Colorectal Cancer Prediction Using Machine Learning and SHAP Analysis.. *Genes*. PMID: 41595533
5. A novel lactylation-related gene signature to predict prognosis and treatment response in lung adenocarcinoma.. *Frontiers in oncology*. PMID: 40161374

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 71.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| 可用 PDB 条目 | 6F4R, 6F4S, 6F4T |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6F4R, 6F4S, 6F4T）+ AlphaFold高质量预测（pLDDT=87.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009091, IPR052830, IPR000408; Pfam: PF00415 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KDM8 | 0.906 | 0.730 | — |
| INPP5A | 0.501 | 0.438 | — |
| WDFY4 | 0.494 | 0.068 | — |
| LRRC25 | 0.466 | 0.045 | — |
| MT-ND4 | 0.462 | 0.417 | — |
| ANKLE1 | 0.449 | 0.050 | — |
| CZIB | 0.446 | 0.000 | — |
| TYW5 | 0.437 | 0.091 | — |
| TMEM220 | 0.433 | 0.000 | — |
| ZNF433 | 0.425 | 0.049 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF219 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YJU2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INPP5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALDH3A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC27A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF609 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPAG9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLI3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 1 / 13 = 8%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 6F4R, 6F4S, 6F4T | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. RCCD1 — RCC1 domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小376 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NED2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166965-RCCD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RCCD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NED2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
