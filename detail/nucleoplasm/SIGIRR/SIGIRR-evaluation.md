---
type: protein-evaluation
gene: "SIGIRR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SIGIRR — REJECTED (研究热度过高 (PubMed strict=116，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIGIRR |
| 蛋白名称 | Single Ig IL-1-related receptor |
| 蛋白大小 | 410 aa / 45.7 kDa |
| UniProt ID | Q6IA17 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 410 aa / 45.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=116 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR015621, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.5/180** | |
| **归一化总分** | | | **39.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 116 |
| PubMed broad count | 250 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. SIGIRR Mutation in Human Necrotizing Enterocolitis (NEC) Disrupts STAT3-Dependent microRNA Expression in Neonatal Gut.. *Cellular and molecular gastroenterology and hepatology*. PMID: 34563711
2. Dominant-Negative Form of SIGIRR: SIGIRR(ΔE8) Promotes Tumor Growth Through Regulation of Metabolic Pathways.. *Journal of interferon & cytokine research : the official journal of the International Society for Interferon and Cytokine Research*. PMID: 35900274
3. SIGIRR gene variants in term newborns with congenital heart defects and necrotizing enterocolitis.. *Annals of pediatric cardiology*. PMID: 38766461
4. SIGIRR suppresses hepatitis B virus X protein-induced chronic inflammation in hepatocytes.. *Gene*. PMID: 39013482
5. SIGIRR deficiency contributes to CD4 T cell abnormalities by facilitating the IL1/C/EBPβ/TNF-α signaling axis in rheumatoid arthritis.. *Molecular medicine (Cambridge, Mass.)*. PMID: 36401167

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.3% |
| 置信残基 (pLDDT 70-90) 占比 | 39.8% |
| 中等置信 (pLDDT 50-70) 占比 | 16.3% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 67.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 67.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR015621, IPR000157; Pfam: PF01582 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRAK1 | 0.970 | 0.333 | — |
| IL37 | 0.943 | 0.000 | — |
| MYD88 | 0.928 | 0.126 | — |
| TLR4 | 0.923 | 0.326 | — |
| IL18R1 | 0.919 | 0.000 | — |
| TRAF6 | 0.870 | 0.292 | — |
| IRAK3 | 0.853 | 0.097 | — |
| TLR5 | 0.846 | 0.088 | — |
| IL33 | 0.827 | 0.000 | — |
| TIRAP | 0.775 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENSP00000519686.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| LGALS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LGALS8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000397632 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli fibrillar center, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SIGIRR — Single Ig IL-1-related receptor，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 116 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 116 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IA17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185187-SIGIRR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIGIRR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IA17
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
