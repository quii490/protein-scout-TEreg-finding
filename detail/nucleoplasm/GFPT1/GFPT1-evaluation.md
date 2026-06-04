---
type: protein-evaluation
gene: "GFPT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GFPT1 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GFPT1 / GFAT, GFPT |
| 蛋白名称 | Glutamine--fructose-6-phosphate aminotransferase [isomerizing] 1 |
| 蛋白大小 | 699 aa / 78.8 kDa |
| UniProt ID | Q06210 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 699 aa / 78.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.9; PDB: 2V4M, 2ZJ3, 2ZJ4, 6R4E, 6R4F, 6R4G, 6R4H |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017932, IPR005855, IPR047084, IPR035466, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 198 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GFAT, GFPT |

**关键文献**:
1. The Hexosamine Biosynthesis Pathway: Regulation and Function.. *Genes*. PMID: 37107691
2. Congenital Myasthenic Syndromes Overview.. **. PMID: 20301347
3. The pan-cancer proteome atlas, a mass spectrometry-based landscape for discovering tumor biology, biomarkers, and therapeutic targets.. *Cancer cell*. PMID: 40446800
4. Endogenous glutamate determines ferroptosis sensitivity via ADCY10-dependent YAP suppression in lung adenocarcinoma.. *Theranostics*. PMID: 33897873
5. Clinical and genetic characterisation of a large Indian congenital myasthenic syndrome cohort.. *Brain : a journal of neurology*. PMID: 37721175

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 86.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 94.8% |
| 可用 PDB 条目 | 2V4M, 2ZJ3, 2ZJ4, 6R4E, 6R4F, 6R4G, 6R4H, 6R4I, 6R4J, 6SVM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2V4M, 2ZJ3, 2ZJ4, 6R4E, 6R4F, 6R4G, 6R4H, 6R4I, 6R4J, 6SVM）+ AlphaFold极高置信度预测（pLDDT=92.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017932, IPR005855, IPR047084, IPR035466, IPR035490; Pfam: PF13522, PF01380 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNPNAT1 | 0.994 | 0.071 | — |
| GPI | 0.991 | 0.000 | — |
| AMDHD2-2 | 0.978 | 0.000 | — |
| GFPT2 | 0.973 | 0.741 | — |
| GNPDA1 | 0.969 | 0.000 | — |
| GLUL | 0.965 | 0.000 | — |
| GNPDA2 | 0.962 | 0.000 | — |
| CAD | 0.949 | 0.203 | — |
| MPI | 0.945 | 0.000 | — |
| PPAT | 0.941 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| MAPK8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| PRKAA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| GFPT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 2V4M, 2ZJ3, 2ZJ4, 6R4E, 6R4F,  | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli; 额外: Nucleoli fibrillar cent | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GFPT1 — Glutamine--fructose-6-phosphate aminotransferase [isomerizing] 1，研究基础较多，新颖性有限。
2. 蛋白大小699 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06210
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198380-GFPT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GFPT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06210
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
