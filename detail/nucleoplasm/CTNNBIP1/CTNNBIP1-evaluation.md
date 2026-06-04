---
type: protein-evaluation
gene: "CTNNBIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTNNBIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTNNBIP1 / ICAT |
| 蛋白名称 | Beta-catenin-interacting protein 1 |
| 蛋白大小 | 81 aa / 9.2 kDa |
| UniProt ID | Q9NSA3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | x1 | 5 | 81 aa / 9.2 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=45 篇 (<=60->6) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=79.0; PDB: 1LUJ, 1M1E, 1T08 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR009428, IPR036911; Pfam: PF06384 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- beta-catenin destruction complex (GO:0030877)
- beta-catenin-ICAT complex (GO:1990711)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ICAT |

**关键文献**:
1. Spatial sorting enables comprehensive characterization of liver zonation.. *Nature metabolism*. PMID: 31535084
2. Integrating network pharmacology and pharmacological evaluation for investigating the active ingredient of Chinese herbal formula Zhuhuang Granule in psoriasis.. *Pathology, research and practice*. PMID: 40934693
3. CTNNBIP1 downregulation is associated with tumor grade and viral infections in gastric adenocarcinoma.. *Journal of cellular physiology*. PMID: 30076728
4. The Alteration of CTNNBIP1 in Lung Cancer.. *International journal of molecular sciences*. PMID: 31766223
5. CTNNBIP1-CLSTN1 functions as a housekeeping chimeric RNA and regulates cell proliferation through SERPINE2.. *Cell death discovery*. PMID: 37805599

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 49.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 34.6% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 60.5% |
| 可用 PDB 条目 | 1LUJ, 1M1E, 1T08 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1LUJ, 1M1E, 1T08）+ AlphaFold高质量预测（pLDDT=79.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009428, IPR036911; Pfam: PF06384 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNNB1 | 0.999 | 0.993 | — |
| APC | 0.951 | 0.796 | — |
| AXIN1 | 0.823 | 0.000 | — |
| GSK3B | 0.809 | 0.000 | — |
| CSNK1A1 | 0.782 | 0.000 | — |
| CACYBP | 0.751 | 0.000 | — |
| GSK3A | 0.726 | 0.000 | — |
| SIAH1 | 0.724 | 0.000 | — |
| AXIN2 | 0.699 | 0.000 | — |
| JUP | 0.671 | 0.664 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| LZIC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FSD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MBD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Dctn3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Nedd1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SCLT1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| METTL26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPL35A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 1LUJ, 1M1E, 1T08 | pLDDT=79.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CTNNBIP1 -- Beta-catenin-interacting protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小81 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSA3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178585-CTNNBIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTNNBIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSA3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
