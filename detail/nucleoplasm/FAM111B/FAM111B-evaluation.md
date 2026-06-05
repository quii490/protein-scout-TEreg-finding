---
type: protein-evaluation
gene: "FAM111B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM111B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM111B / CANP |
| 蛋白名称 | Serine protease FAM111B |
| 蛋白大小 | 734 aa / 84.7 kDa |
| UniProt ID | Q6SJ93 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 734 aa / 84.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009003, IPR043504; Pfam: PF13365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear lamina (GO:0005652)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CANP |

**关键文献**:
1. FAM111B enhances glycolysis and promotes metastasis of prostate cancer by upregulating LDHA.. *Neoplasia (New York, N.Y.)*. PMID: 40975977
2. Targeting FAM111B attenuates mitophagy and increases the sensitivity to lenvatinib treatment by increasing MFN2 stability in hepatocellular carcinoma.. *Cell death & disease*. PMID: 40855067
3. Proposed Cellular Function of the Human FAM111B Protein and Dysregulation in Fibrosis and Cancer.. *Frontiers in oncology*. PMID: 35860584
4. Unveiling FAM111B: A Pan-Cancer Biomarker for DNA Repair and Immune Infiltration.. *International journal of molecular sciences*. PMID: 40243892
5. FAM111B Overexpression and Immune Cell Infiltration: Implications for Ovarian Cancer Immunotherapy.. *Biomedicines*. PMID: 40564014

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.5 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 36.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 25.7% |
| 有序区域 (pLDDT>70) 占比 | 61.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.5），有序残基占 61.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009003, IPR043504; Pfam: PF13365 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SET | 0.653 | 0.615 | — |
| ESCO2 | 0.508 | 0.000 | — |
| C2orf16 | 0.483 | 0.000 | — |
| ELSPBP1 | 0.459 | 0.000 | — |
| ZNF367 | 0.457 | 0.000 | — |
| SCLT1 | 0.454 | 0.000 | — |
| CCDC73 | 0.450 | 0.000 | — |
| CDCP2 | 0.450 | 0.000 | — |
| TMEM185B | 0.447 | 0.000 | — |
| ZDBF2 | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| SET | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Vps41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Spcs2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Itgb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Kctd5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TACC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BAG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EXOSC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.5 + PDB: 无 | pLDDT=69.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM111B — Serine protease FAM111B，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小734 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6SJ93
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189057-FAM111B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM111B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6SJ93
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000189057-FAM111B/subcellular

![](https://images.proteinatlas.org/38637/431_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/38637/431_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/38637/437_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/38637/437_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/38637/443_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/38637/443_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6SJ93-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
