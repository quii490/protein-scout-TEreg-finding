---
type: protein-evaluation
gene: "OPLAH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OPLAH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OPLAH |
| 蛋白名称 | 5-oxoprolinase |
| 蛋白大小 | 1288 aa / 137.5 kDa |
| UniProt ID | O14841 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 5/10 | ×1 | 5 | 1288 aa / 137.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR049517, IPR008040, IPR002821, IPR003692, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Is 5-Oxoprolinase Deficiency More than Just a Benign Condition?. *Molecular syndromology*. PMID: 39129838
2. Heart failure and the glutathione cycle: an integrated view.. *The Biochemical journal*. PMID: 32886767
3. OPLAH Protein Expression Stratifies the Prognosis of Patients With Squamous Cell Carcinoma of the Esophagus.. *Cancer genomics & proteomics*. PMID: 37400143
4. 5-Oxoprolinuria in Heterozygous Patients for 5-Oxoprolinase (OPLAH) Missense Changes.. *JIMD reports*. PMID: 23430506
5. Accumulation of 5-oxoproline in myocardial dysfunction and the protective effects of OPLAH.. *Science translational medicine*. PMID: 29118264

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 57.6% |
| 置信残基 (pLDDT 70-90) 占比 | 36.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.9，有序区 93.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049517, IPR008040, IPR002821, IPR003692, IPR045079; Pfam: PF19278, PF05378, PF01968 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GGCT | 0.966 | 0.000 | — |
| GCLC | 0.959 | 0.000 | — |
| GGT5 | 0.948 | 0.000 | — |
| GGT1 | 0.936 | 0.000 | — |
| GCLM | 0.935 | 0.000 | — |
| GGT7 | 0.935 | 0.000 | — |
| CHAC1 | 0.933 | 0.000 | — |
| CHAC2 | 0.925 | 0.000 | — |
| GGT6 | 0.922 | 0.000 | — |
| GLUD1 | 0.870 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000480476.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GK | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TPK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM63 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |
| TRIM55 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |
| Cav3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 无 | pLDDT=87.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

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
1. OPLAH — 5-oxoprolinase，非常新颖，仅有少数基础研究。
2. 蛋白大小1288 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14841
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178814-OPLAH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OPLAH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14841
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
