---
type: protein-evaluation
gene: "LGALS13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGALS13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALS13 / PLAC8 |
| 蛋白名称 | Galactoside-binding soluble lectin 13 |
| 蛋白大小 | 139 aa / 16.1 kDa |
| UniProt ID | Q9UHV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus matrix; Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 139 aa / 16.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.5; PDB: 5XG7, 5XG8, 5Y03, 6A62, 6A63, 6A64, 6A65 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus matrix; Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular region (GO:0005576)
- nuclear body (GO:0016604)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PLAC8 |

**关键文献**:
1. Overexpression of Galectin10 Predicts a Better Prognosis in Human Ovarian Cancer.. *Journal of Cancer*. PMID: 33854625
2. Intronic variants of LGALS13 gene encoding placental protein (PP13) are linked with increased risk of infection-associated spontaneous preterm birth.. *American journal of reproductive immunology (New York, N.Y. : 1989)*. PMID: 37641375
3. Placental protein 13: An important biological protein in preeclampsia.. *Journal of circulating biomarkers*. PMID: 30023011
4. Predicting the Risk to Develop Preeclampsia in the First Trimester Combining Promoter Variant -98A/C of LGALS13 (Placental Protein 13), Black Ethnicity, Previous Preeclampsia, Obesity, and Maternal Age.. *Fetal diagnosis and therapy*. PMID: 28728156
5. The choriocarcinoma cell line BeWo: syncytial fusion and expression of syncytium-specific proteins.. *Reproduction (Cambridge, England)*. PMID: 20696850

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.5 |
| 高置信度残基 (pLDDT>90) 占比 | 97.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 5XG7, 5XG8, 5Y03, 6A62, 6A63, 6A64, 6A65, 6A66, 6KJW, 6KJX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5XG7, 5XG8, 5Y03, 6A62, 6A63, 6A64, 6A65, 6A66, 6KJW, 6KJX）+ AlphaFold极高置信度预测（pLDDT=97.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAPPA | 0.877 | 0.000 | — |
| PGF | 0.723 | 0.000 | — |
| ENDOU | 0.710 | 0.000 | — |
| ACTG1 | 0.697 | 0.000 | — |
| GAL | 0.684 | 0.000 | — |
| ADAM12 | 0.668 | 0.000 | — |
| LGALS12 | 0.665 | 0.000 | — |
| HEBP2 | 0.601 | 0.000 | — |
| LGALS2 | 0.599 | 0.000 | — |
| NUTF2 | 0.584 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| PHLDA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OTX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PWP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CENPV | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTBD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNPEP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CREB5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.5 + PDB: 5XG7, 5XG8, 5Y03, 6A62, 6A63,  | pLDDT=97.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus matrix; Secreted / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. LGALS13 — Galactoside-binding soluble lectin 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小139 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105198-LGALS13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALS13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
