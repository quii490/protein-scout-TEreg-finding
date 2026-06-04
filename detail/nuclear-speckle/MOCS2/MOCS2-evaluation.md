---
type: protein-evaluation
gene: "MOCS2"
date: 2026-06-03
tags: [protein-scout, nuclear-speckle, re-evaluation, recovery]
status: scored
category: nuclear-speckle
normalized_score: 62.3
raw_score: 114.0
nuclear_score: 7
---

## MOCS2 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOCS2 / MOCO1 |
| 蛋白名称 | Molybdopterin synthase sulfur carrier subunit |
| 蛋白大小 | 88 aa / 9.8 kDa |
| UniProt ID | O96033 |
| PubMed (strict) | 42 |
| PubMed (broad) | 59 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; Nucleoplasm, Nuclear speckles; UniProt: Cytoplasm, cytosol; Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 88 aa / 9.8 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (41-60→6) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8，PDB: 5MPO |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012675, IPR044672, IPR028887, IPR016155, IPR003 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/183** | |
| **归一化总分** | | | **62.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**HPA IF 图像**:
![IF 1](https://images.proteinatlas.org/37680/441_D4_1_blue_red_green.jpg)
![IF 2](https://images.proteinatlas.org/37680/441_D4_2_blue_red_green.jpg)
![IF 3](https://images.proteinatlas.org/37680/430_D4_1_blue_red_green.jpg)

**GO Cellular Component**:
- cytosol (GO:0005829)
- molybdopterin synthase complex (GO:1990140)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MOCO1 |

**关键文献**:
1. Molybdenum Cofactor Deficiency.. **. PMID: 34870926
2. Mutations in the molybdenum cofactor biosynthetic genes MOCS1, MOCS2, and GEPH.. *Human mutation*. PMID: 12754701
3. Metabolic reprogramming signature predicts prognosis and immune landscape in small cell lung cancer: MOCS2 validation and implications for personalized therapy.. *Frontiers in molecular biosciences*. PMID: 40452920
4. Molybdenum cofactor deficiency: Mutations in GPHN, MOCS1, and MOCS2.. *Human mutation*. PMID: 21031595
5. The Clinical and Molecular Characteristics of Molybdenum Cofactor Deficiency Due to MOCS2 Mutations.. *Pediatric neurology*. PMID: 31201073

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 95.5% |
| 可用 PDB 条目 | 5MPO |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 95.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012675, IPR044672, IPR028887, IPR016155, IPR003749; Pfam: PF02597 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MOCS3 | 0.999 | 0.099 | — |
| MOCS1 | 0.999 | 0.000 | — |
| GPHN | 0.998 | 0.000 | — |
| SUOX | 0.969 | 0.000 | — |
| SGF29 | 0.957 | 0.954 | — |
| AOX1 | 0.945 | 0.000 | — |
| TST | 0.939 | 0.000 | — |
| MARC2 | 0.918 | 0.000 | — |
| MPST | 0.871 | 0.000 | — |
| TSTD1 | 0.870 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-4462876 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| Mocs3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mocs2B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RPL9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ABCF3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Atac2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 |
| Chrac-14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 |
| Ada2a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 |
| D12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 |
| Jra | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 |

**已知复合体成员** (GO Cellular Component):
- cytosol (GO:0005829)
- molybdopterin synthase complex (GO:1990140)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 5MPO | pLDDT=91.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Cytosol; Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MOCS2 — Molybdopterin synthase sulfur carrier subunit，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小88 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O96033
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164172-MOCS2
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000164172-MOCS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOCS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O96033
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MOCS2
- Packet data timestamp: 2026-06-03 21:51:04

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:51:04），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*
