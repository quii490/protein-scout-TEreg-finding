---
type: protein-evaluation
gene: "PITPNC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PITPNC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PITPNC1 |
| 蛋白名称 | Cytoplasmic phosphatidylinositol transfer protein 1 |
| 蛋白大小 | 332 aa / 38.4 kDa |
| UniProt ID | Q9UKF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 332 aa / 38.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001666, IPR055261, IPR023393; Pfam: PF02121 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PITPNC1 Suppress CD8(+) T cell immune function and promote radioresistance in rectal cancer by modulating FASN/CD155.. *Journal of translational medicine*. PMID: 38291470
2. Golgi signalling proteins GOLPH3, MYO18A, PITPNC1 and RAB1B: implications in prognosis and survival outcomes of AML patients.. *Biomarkers : biochemical indicators of exposure, response, and susceptibility to chemicals*. PMID: 36919644
3. Phosphatidylinositol transfer protein, cytoplasmic 1 (PITPNC1) binds and transfers phosphatidic acid.. *The Journal of biological chemistry*. PMID: 22822086
4. Expanding functions of the phosphatidylinositol/phosphatidate lipid transporter, PITPNC1 in physiology and in pathology.. *Advances in biological regulation*. PMID: 39406587
5. PITPNC1 promotes the thermogenesis of brown adipose tissue under acute cold exposure.. *Science China. Life sciences*. PMID: 36166181

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.0 |
| 高置信度残基 (pLDDT>90) 占比 | 64.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 20.5% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.0，有序区 75.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001666, IPR055261, IPR023393; Pfam: PF02121 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PITPNM3 | 0.915 | 0.000 | — |
| RAB1B | 0.913 | 0.309 | — |
| AGTRAP | 0.838 | 0.612 | — |
| HELZ | 0.546 | 0.000 | — |
| MERTK | 0.478 | 0.053 | — |
| IGFBP2 | 0.468 | 0.000 | — |
| PRKACB | 0.459 | 0.071 | — |
| PRKACA | 0.455 | 0.071 | — |
| PRKACG | 0.454 | 0.071 | — |
| MYO18A | 0.447 | 0.057 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AGTRAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ANKS6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TNFRSF10D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HTATIP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GSG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CACFD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REEP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DGAT2L6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMPD2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.0 + PDB: 无 | pLDDT=82.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PITPNC1 — Cytoplasmic phosphatidylinositol transfer protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小332 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154217-PITPNC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PITPNC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKF7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKF7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001666;IPR055261;IPR023393; |
| Pfam | PF02121; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154217-PITPNC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTRAP | Intact | false |
| CMTM5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
