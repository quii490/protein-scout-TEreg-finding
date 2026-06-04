---
type: protein-evaluation
gene: "MTUS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTUS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTUS1 / ATBP, ATIP, GK1, KIAA1288, MTSG1 |
| 蛋白名称 | Microtubule-associated tumor suppressor 1 |
| 蛋白大小 | 1270 aa / 141.4 kDa |
| UniProt ID | Q9ULD2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Microtubules; UniProt: Mitochondrion; Golgi apparatus; Cell membrane; Nucleus; Cyto |
| 蛋白大小 | 5/10 | ×1 | 5 | 1270 aa / 141.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051293 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Microtubules | Enhanced |
| UniProt | Mitochondrion; Golgi apparatus; Cell membrane; Nucleus; Cytoplasm, cytoskeleton, microtubule organiz... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 125 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATBP, ATIP, GK1, KIAA1288, MTSG1 |

**关键文献**:
1. Mitochondrial Tumor Suppressor 1A Attenuates Myocardial Infarction Injury by Maintaining the Coupling Between Mitochondria and Endoplasmic Reticulum.. *Circulation*. PMID: 40583767
2. Mitochondrial outer membrane protein MTUS1/ATIP1 exerts antitumor effects through ROS-induced mitochondrial pyroptosis in head and neck squamous cell carcinoma.. *International journal of biological sciences*. PMID: 38725862
3. Integrative eQTL and Mendelian randomization analysis reveals key genetic markers in mesothelioma.. *Respiratory research*. PMID: 40223054
4. MTUS1, a gene encoding angiotensin-II type 2 (AT2) receptor-interacting proteins, in health and disease, with special emphasis on its role in carcinogenesis.. *Gene*. PMID: 28499941
5. Low MTUS1 Protein Expression Is Associated with Poor Survival in Patients with Colorectal Adenocarcinoma.. *Diagnostics (Basel, Switzerland)*. PMID: 36980447

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.7 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 71.3% |
| 有序区域 (pLDDT>70) 占比 | 25.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=51.7），有序残基占 25.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051293 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTLA4 | 0.925 | 0.000 | — |
| CD274 | 0.909 | 0.000 | — |
| PDCD1 | 0.908 | 0.000 | — |
| AGTR2 | 0.871 | 0.292 | — |
| HAVCR2 | 0.817 | 0.000 | — |
| CD4 | 0.802 | 0.000 | — |
| TIGIT | 0.783 | 0.000 | — |
| AURKB | 0.780 | 0.000 | — |
| CD8A | 0.780 | 0.000 | — |
| KIF2C | 0.735 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORC4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| A0A0F7R803 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| UBE3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| GLS | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PB2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MAP3K14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| STX7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.7 + PDB: 无 | pLDDT=51.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion; Golgi apparatus; Cell membrane; Nuc / Nucleoli, Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MTUS1 — Microtubule-associated tumor suppressor 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1270 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULD2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129422-MTUS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTUS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULD2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
