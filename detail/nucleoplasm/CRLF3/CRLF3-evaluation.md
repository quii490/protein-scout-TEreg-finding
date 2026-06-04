---
type: protein-evaluation
gene: "CRLF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRLF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRLF3 / CREME9, CRLM9, CYTOR4, P48 |
| 蛋白名称 | Cytokine receptor-like factor 3 |
| 蛋白大小 | 442 aa / 49.8 kDa |
| UniProt ID | Q8IUI8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 49.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003961, IPR036116, IPR013783 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREME9, CRLM9, CYTOR4, P48 |

**关键文献**:
1. Discovery of a polymorphic gene fusion via bottom-up chimeric RNA prediction.. *Nucleic acids research*. PMID: 38587197
2. Discovery of A Polymorphic Gene Fusion via Bottom-Up Chimeric RNA Prediction.. *bioRxiv : the preprint server for biology*. PMID: 36778239
3. Cytokine Receptor-Like Factor 3 Negatively Regulates Antiviral Immunity by Promoting the Degradation of TBK1 in Teleost Fish.. *Journal of virology*. PMID: 36515543
4. Cytokine Receptor-like Factor 3 (CRLF3) and Its Emerging Roles in Neurobiology, Hematopoiesis and Related Human Diseases.. *International journal of molecular sciences*. PMID: 40331935
5. Protection of insect neurons by erythropoietin/CRLF3-mediated regulation of pro-apoptotic acetylcholinesterase.. *Scientific reports*. PMID: 36329181

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 70.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.7，有序区 93.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR013783 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP6 | 0.802 | 0.000 | — |
| LRRC37B | 0.725 | 0.000 | — |
| ADAP2 | 0.709 | 0.000 | — |
| TEFM | 0.709 | 0.000 | — |
| COPRS | 0.693 | 0.000 | — |
| EVI2B | 0.639 | 0.000 | — |
| EVI2A | 0.635 | 0.000 | — |
| ATAD5 | 0.631 | 0.000 | — |
| RAB11FIP4 | 0.617 | 0.000 | — |
| RNF135 | 0.581 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000318804.6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Wasf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| FAM200C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS25 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| MYOZ3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENPP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDIT4L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LGALS14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZFP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| L3MBTL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 无 | pLDDT=89.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. CRLF3 — Cytokine receptor-like factor 3，非常新颖，仅有少数基础研究。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUI8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176390-CRLF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRLF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUI8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
