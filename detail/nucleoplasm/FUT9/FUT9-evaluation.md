---
type: protein-evaluation
gene: "FUT9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FUT9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FUT9 |
| 蛋白名称 | 4-galactosyl-N-acetylglucosaminide 3-alpha-L-fucosyltransferase 9 |
| 蛋白大小 | 359 aa / 42.1 kDa |
| UniProt ID | Q9Y231 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, Cytosol; UniProt: Golgi apparatus, trans-Golgi network membrane; Golgi apparat |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 42.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.5; PDB: 8D0O, 8D0P, 8D0Q, 8D0R, 8D0S, 8D0U, 8D0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR055270, IPR031481, IPR001503, IPR038577; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, Cytosol | Approved |
| UniProt | Golgi apparatus, trans-Golgi network membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- trans-Golgi network (GO:0005802)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 77 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FUT4 and FUT9 genes are expressed early in human embryogenesis.. *Glycobiology*. PMID: 10929005
2. Mice lacking α1,3-fucosyltransferase 9 exhibit modulation of in vivo immune responses against pathogens.. *Pathology international*. PMID: 24888773
3. Polymorphisms of FUT9 and its relationship with susceptibility towards DHAV-3 in Pekin duck.. *Gene*. PMID: 40090531
4. Transcriptional activation of fucosyltransferase (FUT) genes using the CRISPR-dCas9-VPR technology reveals potent N-glycome alterations in colorectal cancer cells.. *Glycobiology*. PMID: 30476078
5. ELF4 contributes to esophageal squamous cell carcinoma growth and metastasis by augmenting cancer stemness via FUT9.. *Acta biochimica et biophysica Sinica*. PMID: 37674363

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 82.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 8D0O, 8D0P, 8D0Q, 8D0R, 8D0S, 8D0U, 8D0W, 8D0X |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8D0O, 8D0P, 8D0Q, 8D0R, 8D0S, 8D0U, 8D0W, 8D0X）+ AlphaFold极高置信度预测（pLDDT=90.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055270, IPR031481, IPR001503, IPR038577; Pfam: PF17039, PF00852 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FUT1 | 0.971 | 0.000 | — |
| FUT2 | 0.960 | 0.000 | — |
| ST3GAL6 | 0.942 | 0.000 | — |
| B4GALT1 | 0.940 | 0.000 | — |
| B4GALT2 | 0.936 | 0.000 | — |
| B3GNT2 | 0.936 | 0.000 | — |
| B4GALT4 | 0.935 | 0.000 | — |
| B3GNT3 | 0.930 | 0.000 | — |
| B4GALT3 | 0.926 | 0.000 | — |
| B3GNT4 | 0.923 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSSK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GOLM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CLRN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CANX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FKBP14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSF2BP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| PRR11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 8D0O, 8D0P, 8D0Q, 8D0R, 8D0S,  | pLDDT=90.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network membrane; Gol / Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FUT9 — 4-galactosyl-N-acetylglucosaminide 3-alpha-L-fucosyltransferase 9，非常新颖，仅有少数基础研究。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y231
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172461-FUT9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FUT9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y231
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
