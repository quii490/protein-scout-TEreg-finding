---
type: protein-evaluation
gene: "DDAH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DDAH1 — REJECTED (研究热度过高 (PubMed strict=215，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDAH1 / DDAH |
| 蛋白名称 | N(G),N(G)-dimethylarginine dimethylaminohydrolase 1 |
| 蛋白大小 | 285 aa / 31.1 kDa |
| UniProt ID | O94760 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 285 aa / 31.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=215 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.6; PDB: 2JAI, 2JAJ, 3I2E, 3I4A, 3P8E, 3P8P, 6DGE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033199; Pfam: PF19420 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoli | Approved |
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
| PubMed strict count | 215 |
| PubMed broad count | 390 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDAH |

**关键文献**:
1. DDAH1 promotes neurogenesis and neural repair in cerebral ischemia.. *Acta pharmaceutica Sinica. B*. PMID: 38799640
2. Cancer-cell-secreted DDAH1 induces TGF-β1/Smad3 signaling pathway to promote fibrosis and aging in lung.. *Nature aging*. PMID: 41444413
3. Hepatic DDAH1 mitigates hepatic steatosis and insulin resistance in obese mice: Involvement of reduced S100A11 expression.. *Acta pharmaceutica Sinica. B*. PMID: 37655336
4. Integrated machine learning reveals the role of tryptophan metabolism in clear cell renal cell carcinoma and its association with patient prognosis.. *Biology direct*. PMID: 39707545
5. AK4 promotes nasopharyngeal carcinoma metastasis and chemoresistance by activating NLRP3 inflammatory complex.. *Cell death & disease*. PMID: 40593461

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 93.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 2JAI, 2JAJ, 3I2E, 3I4A, 3P8E, 3P8P, 6DGE, 6SZP, 6SZQ, 7ULU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2JAI, 2JAJ, 3I2E, 3I4A, 3P8E, 3P8P, 6DGE, 6SZP, 6SZQ, 7ULU）+ AlphaFold极高置信度预测（pLDDT=95.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033199; Pfam: PF19420 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOS3 | 0.865 | 0.000 | — |
| AGXT2 | 0.852 | 0.000 | — |
| PRMT1 | 0.692 | 0.000 | — |
| DDAH2 | 0.660 | 0.628 | — |
| NOS1 | 0.606 | 0.000 | — |
| ARG2 | 0.547 | 0.000 | — |
| OAT | 0.525 | 0.000 | — |
| NF1 | 0.506 | 0.000 | — |
| BCL10 | 0.499 | 0.000 | — |
| ZNF225 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Kcnma1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-9475|pubmed:19423573 |
| der | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PSMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26336|pubmed:24338975 |
| APOOL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| SDHAF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ATP5F1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| BOLA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| LYRM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 2JAI, 2JAJ, 3I2E, 3I4A, 3P8E,  | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cytosol; 额外: Nucleoli | 一致 |
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
1. DDAH1 — N(G),N(G)-dimethylarginine dimethylaminohydrolase 1，研究基础较多，新颖性有限。
2. 蛋白大小285 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 215 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 215 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94760
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153904-DDAH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDAH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94760
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
