---
type: protein-evaluation
gene: "ANKS6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKS6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKS6 / ANKRD14, PKDR1, SAMD6 |
| 蛋白名称 | Ankyrin repeat and SAM domain-containing protein 6 |
| 蛋白大小 | 871 aa / 92.2 kDa |
| UniProt ID | Q68DC2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Primary cilium; 额外: Cytosol; UniProt: Cell projection, cilium; Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 871 aa / 92.2 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.9; PDB: 4NL9 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051631, IPR002110, IPR036770, IPR001660, IPR013 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Primary cilium; 额外: Cytosol | Approved |
| UniProt | Cell projection, cilium; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- ciliary inversin compartment (GO:0097543)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANKRD14, PKDR1, SAMD6 |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Loss of Anks6 leads to YAP deficiency and liver abnormalities.. *Human molecular genetics*. PMID: 32886109
3. Characterization of the SAM domain of the PKD-related protein ANKS6 and its interaction with ANKS3.. *BMC structural biology*. PMID: 24998259
4. Mitigation of portal fibrosis and cholestatic liver disease in ANKS6-deficient livers by macrophage depletion.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 35032404
5. Certain heterozygous variants in the kinase domain of the serine/threonine kinase NEK8 can cause an autosomal dominant form of polycystic kidney disease.. *Kidney international*. PMID: 37598857

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.9 |
| 高置信度残基 (pLDDT>90) 占比 | 25.0% |
| 置信残基 (pLDDT 70-90) 占比 | 20.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 46.2% |
| 有序区域 (pLDDT>70) 占比 | 45.0% |
| 可用 PDB 条目 | 4NL9 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=59.9），有序残基占 45.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051631, IPR002110, IPR036770, IPR001660, IPR013761; Pfam: PF00023, PF12796, PF00536 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKS3 | 0.994 | 0.970 | — |
| NEK8 | 0.993 | 0.626 | — |
| NEK9 | 0.979 | 0.050 | — |
| NPHP3 | 0.974 | 0.106 | — |
| NEK7 | 0.902 | 0.782 | — |
| INVS | 0.870 | 0.095 | — |
| PENK | 0.769 | 0.000 | — |
| PRKD1 | 0.765 | 0.053 | — |
| NEK6 | 0.731 | 0.461 | — |
| NPHP1 | 0.704 | 0.092 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| PITPNC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| STRIT1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| STX7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| EMD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM120B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BCL2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TIMM9 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.9 + PDB: 4NL9 | pLDDT=59.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm / Nucleoli fibrillar center, Primary cilium; 额外: Cyt | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. ANKS6 — Ankyrin repeat and SAM domain-containing protein 6，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小871 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68DC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165138-ANKS6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKS6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68DC2
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:53:08

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。
