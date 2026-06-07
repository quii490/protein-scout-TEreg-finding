---
type: protein-evaluation
gene: "NABP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NABP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NABP2 / OBFC2B, SSB1 |
| 蛋白名称 | SOSS complex subunit B1 |
| 蛋白大小 | 211 aa / 22.3 kDa |
| UniProt ID | Q9BQ15 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 211 aa / 22.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.8; PDB: 4OWT, 4OWW, 4OWX, 5D8E, 5D8F, 8RBZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012340, IPR048970, IPR051231; Pfam: PF21473 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)
- SOSS complex (GO:0070876)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OBFC2B, SSB1 |

**关键文献**:
1. NABP2 as an oncogenic biomarker promotes hepatocellular carcinoma progression and metastasis.. *American journal of translational research*. PMID: 37434816
2. C-termini are essential and distinct for nucleic acid binding of human NABP1 and NABP2.. *Biochimica et biophysica acta*. PMID: 26550690
3. hSSB1 (NABP2/OBFC2B) modulates the DNA damage and androgen-induced transcriptional response in prostate cancer.. *The Prostate*. PMID: 36811381
4. Decoding the role of nucleic acid binding protein 2 in lipid dysregulation and hepatocellular carcinoma progression through LKB1-mediated mitochondrial dysfunction.. *Cellular signalling*. PMID: 40250697
5. Comprehensive Analysis of NABP2 as a Prognostic Biomarker and Its Correlation with Immune Infiltration in Hepatocellular Carcinoma.. *Journal of inflammation research*. PMID: 37113629

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 50.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 30.3% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 4OWT, 4OWW, 4OWX, 5D8E, 5D8F, 8RBZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4OWT, 4OWW, 4OWX, 5D8E, 5D8F, 8RBZ）+ AlphaFold极高置信度预测（pLDDT=76.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012340, IPR048970, IPR051231; Pfam: PF21473 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| INTS3 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| DBT | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| INIP | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| HNRNPH1 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| PRDX1 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| ENSP00000369545.2 | psi-mi:"MI:0413"(electrophoretic mobility shift as | imex:IM-25484|pubmed:19683501 |
| PPP2R1A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| LUC7L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BUD13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 4OWT, 4OWW, 4OWX, 5D8E, 5D8F,  | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NABP2 — SOSS complex subunit B1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小211 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ15
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139579-NABP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NABP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ15
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000139579-NABP2/subcellular

![](https://images.proteinatlas.org/44615/518_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44615/518_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/44615/530_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44615/530_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/44615/558_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/44615/558_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ15-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ15 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012340;IPR048970;IPR051231; |
| Pfam | PF21473; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139579-NABP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| INTS3 | Intact, Biogrid | true |
| ATM | Intact | false |
| BLM | Intact | false |
| CDKN1A | Intact | false |
| EP300 | Biogrid | false |
| FBXL5 | Biogrid | false |
| INIP | Biogrid | false |
| INTS5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
