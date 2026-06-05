---
type: protein-evaluation
gene: "MNS1"
date: 2026-06-03
tags: [protein-scout, nuclear-speckle, re-evaluation, recovery]
status: scored
category: nuclear-speckle
normalized_score: 66.7
raw_score: 122.0
nuclear_score: 7
---

## MNS1 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MNS1 |
| 蛋白名称 | Meiosis-specific nuclear structural protein 1 |
| 蛋白大小 | 495 aa / 60.6 kDa |
| UniProt ID | Q8NEH6 |
| PubMed (strict) | 43 |
| PubMed (broad) | 80 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles, Primary cilium, End piece; Ba; UniProt: Nucleus; Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 495 aa / 60.6 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (41-60→6) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.9，PDB: 7UNG, 8J07 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026504, IPR043597; Pfam: PF13868 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/183** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles, Primary cilium, End piece; Basal body, Cytosol, Perinuclear theca, Flagellar centriole | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, flage... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**HPA IF 图像**:
![IF 1](https://images.proteinatlas.org/39975/2238_D9_10_blue_red_green.jpg)
![IF 2](https://images.proteinatlas.org/39975/2238_D9_39_blue_red_green.jpg)

**GO Cellular Component**:
- axonemal A tubule inner sheath (GO:0160111)
- axonemal microtubule (GO:0005879)
- axoneme (GO:0005930)
- centriole (GO:0005814)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- intermediate filament (GO:0005882)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 80 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Expanding MNS1 Heterotaxy Phenotype.. *American journal of medical genetics. Part A*. PMID: 39233552
2. Heterologous expression and biochemical characterization of an alpha1,2-mannosidase encoded by the Candida albicans MNS1 gene.. *Memorias do Instituto Oswaldo Cruz*. PMID: 19057825
3. MNS1 is essential for spermiogenesis and motile ciliary functions in mice.. *PLoS genetics*. PMID: 22396656
4. Integrated gene expression proﬁling analysis reveals SERPINA3, FCN3, FREM1, MNS1 as candidate biomarkers in heart failure and their correlation with immune inﬁltration.. *Journal of thoracic disease*. PMID: 35572891
5. SGAM1 orchestrates salt tolerance by balancing mitochondrial translation and ROS homeostasis in Arabidopsis.. *The Plant journal : for cell and molecular biology*. PMID: 40633123

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 35.8% |
| 置信残基 (pLDDT 70-90) 占比 | 44.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 80.4% |
| 可用 PDB 条目 | 7UNG, 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7UNG, 8J07）+ AlphaFold高质量预测（pLDDT=81.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026504, IPR043597; Pfam: PF13868 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFAP53 | 0.902 | 0.821 | — |
| C9orf116 | 0.874 | 0.818 | — |
| CFAP161 | 0.873 | 0.811 | — |
| RIBC2 | 0.871 | 0.821 | — |
| TEKT1 | 0.866 | 0.817 | — |
| EFHC2 | 0.863 | 0.819 | — |
| EFHC1 | 0.861 | 0.819 | — |
| EFHB | 0.857 | 0.825 | — |
| FAM166B | 0.855 | 0.800 | — |
| PACRG | 0.849 | 0.821 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000260453.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SOG2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| MET30 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SURF6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MTDH | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KRT34 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**已知复合体成员** (GO Cellular Component):
- axonemal A tubule inner sheath (GO:0160111)
- axonemal microtubule (GO:0005879)
- axoneme (GO:0005930)
- centriole (GO:0005814)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- intermediate filament (GO:0005882)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 7UNG, 8J07 | pLDDT=81.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, cilium axoneme;  / Nucleoplasm, Nuclear speckles, Primary cilium, End | 一致 |
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
1. MNS1 — Meiosis-specific nuclear structural protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小495 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEH6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138587-MNS1
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000138587-MNS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MNS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEH6
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MNS1
- Packet data timestamp: 2026-06-03 21:47:49

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:47:49），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEH6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
