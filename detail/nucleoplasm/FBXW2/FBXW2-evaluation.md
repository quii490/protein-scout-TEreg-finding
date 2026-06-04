---
type: protein-evaluation
gene: "FBXW2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXW2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXW2 / FBW2, FWD2 |
| 蛋白名称 | F-box/WD repeat-containing protein 2 |
| 蛋白大小 | 454 aa / 51.5 kDa |
| UniProt ID | Q9UKT8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 51.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR042627, IPR015943, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBW2, FWD2 |

**关键文献**:
1. Ubiquitination of NF-κB p65 by FBXW2 suppresses breast cancer stemness, tumorigenesis, and paclitaxel resistance.. *Cell death and differentiation*. PMID: 34465889
2. FBXW2 suppresses migration and invasion of lung cancer cells via promoting β-catenin ubiquitylation and degradation.. *Nature communications*. PMID: 30918250
3. FBXW2 inhibits prostate cancer proliferation and metastasis via promoting EGFR ubiquitylation and degradation.. *Cellular and molecular life sciences : CMLS*. PMID: 35499593
4. FBXW2 suppresses breast tumorigenesis by targeting AKT-Moesin-SKP2 axis.. *Cell death & disease*. PMID: 37736741
5. Elastic Fibers and F-Box and WD-40 Domain-Containing Protein 2 in Bovine Periosteum and Blood Vessels.. *Biomimetics (Basel, Switzerland)*. PMID: 36648793

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 64.3% |
| 置信残基 (pLDDT 70-90) 占比 | 30.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 94.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 94.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR042627, IPR015943, IPR020472; Pfam: PF12937, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.988 | 0.917 | — |
| CUL1 | 0.979 | 0.878 | — |
| RBX1 | 0.898 | 0.777 | — |
| SPANXN3 | 0.813 | 0.813 | — |
| DCTN5 | 0.779 | 0.000 | — |
| FBXW4 | 0.759 | 0.000 | — |
| BTRC | 0.736 | 0.599 | — |
| FBXW7 | 0.735 | 0.519 | — |
| FBXO17 | 0.729 | 0.610 | — |
| GCM1 | 0.729 | 0.524 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15070733|imex:IM-19870 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| CDC37 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| TRIM54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31391242|imex:IM-25805| |
| CLVS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FBXO17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXW7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARIH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 无 | pLDDT=89.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXW2 — F-box/WD repeat-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKT8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119402-FBXW2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXW2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKT8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
