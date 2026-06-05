---
type: protein-evaluation
gene: "CKAP5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CKAP5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CKAP5 |
| 蛋白名称 | Cytoskeleton-associated protein 5 |
| 蛋白大小 | 2032 aa / 225.5 kDa |
| UniProt ID | Q14008 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Centrosome, Basal body; 额外: Nucleoli, Nucleoli rim, Plasma m; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 2/10 | x1 | 2 | 2032 aa / 225.5 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body; 额外: Nucleoli, Nucleoli rim, Plasma membrane, Mitotic spindle, Primary cilium | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, spindle... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 172 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cross-species single-cell transcriptomic analyses reveal evolutionary conservation and diversification of ovarian tissues.. *J Anim Sci Biotechnol*. PMID: 41975518
2. NAT10 and E2F1 Orchestrate CKAP5-Mediated Progression in Esophageal Squamous Cell Carcinoma.. *J Gastroenterol Hepatol*. PMID: 41735227
3. RNAseq-based meta-analyses revealed tumor suppressor-inducer fusion events in liver, oral, and ovarian cancer in the Indian population: a cancer cell surviving mechanism.. *Nucleosides Nucleotides Nucleic Acids*. PMID: 41661231
4. Duplication of the prothrombin gene is associated with a significant increase in thrombin generation.. *Res Pract Thromb Haemost*. PMID: 41769318
5. CKAP5: Unraveling Its Crucial Function in Liver Hepatocellular Carcinoma Progression and Prognosis.. *Dig Dis Sci*. PMID: 41432972

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 42.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 73.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 73.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TACC3 | 0.000 | 0.000 | — |
| SLAIN2 | 0.000 | 0.000 | — |
| NDC80 | 0.000 | 0.000 | — |
| TACC1 | 0.000 | 0.000 | — |
| TACC2 | 0.000 | 0.000 | — |
| AURKA | 0.000 | 0.000 | — |
| MAPRE1 | 0.000 | 0.000 | — |
| MAPRE3 | 0.000 | 0.000 | — |
| NUF2 | 0.000 | 0.000 | — |
| PLK1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q14008 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75410 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:O75410-1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:A2AGT5 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5NHZ0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P62993 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P16333 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P12931 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P06241 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:P27986 | psi-mi:"MI:0081"(peptide array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body; 额外: Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CKAP5 -- Cytoskeleton-associated protein 5，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2032 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14008
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175216-CKAP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CKAP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14008
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14008-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
