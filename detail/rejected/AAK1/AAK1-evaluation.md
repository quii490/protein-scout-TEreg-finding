---
type: protein-evaluation
gene: "AAK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AAK1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AAK1 / KIAA1048 |
| 蛋白名称 | AP2-associated protein kinase 1 |
| 蛋白大小 | 961 aa / 103.9 kDa |
| UniProt ID | Q2M2I8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Vesicles, Cytosol; UniProt: Cell membrane; Membrane, clathrin-coated pit; Presynapse |
| 蛋白大小 | 8/10 | ×1 | 8 | 961 aa / 103.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 4WSQ, 5L4Q, 5TE0, 8GMC, 8GMD, 9F6S, 9F8T |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051744, IPR011009, IPR000719, IPR008271; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.5/180** | |
| **归一化总分** | | | **33.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Vesicles, Cytosol | Supported |
| UniProt | Cell membrane; Membrane, clathrin-coated pit; Presynapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell leading edge (GO:0031252)
- clathrin-coated pit (GO:0005905)
- clathrin-coated vesicle (GO:0030136)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)
- presynapse (GO:0098793)
- terminal bouton (GO:0043195)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 177 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1048 |

**关键文献**:
1. Investigational Drugs for the Treatment of Postherpetic Neuralgia: Systematic Review of Randomized Controlled Trials.. *International journal of molecular sciences*. PMID: 37629168
2. Development of a novel AAK1 inhibitor via Kinobeads-based screening.. *Scientific reports*. PMID: 38509168
3. AAK1 activation-mediated iron trafficking drives ferroptotic cell death.. *Nature communications*. PMID: 41407700
4. Characterisation of the antinociceptive effect of baricitinib in the collagen antibody-induced arthritis mouse model.. *Annals of the rheumatic diseases*. PMID: 39924372
5. M2 Microglia Extracellular Vesicle miR-124 Regulates Neural Stem Cell Differentiation in Ischemic Stroke via AAK1/NOTCH.. *Stroke*. PMID: 37586072

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 30.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 61.0% |
| 有序区域 (pLDDT>70) 占比 | 35.6% |
| 可用 PDB 条目 | 4WSQ, 5L4Q, 5TE0, 8GMC, 8GMD, 9F6S, 9F8T, 9QB5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 35.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051744, IPR011009, IPR000719, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP2M1 | 0.979 | 0.856 | — |
| REPS1 | 0.971 | 0.831 | — |
| EPS15 | 0.960 | 0.409 | — |
| AP2B1 | 0.958 | 0.811 | — |
| AP2S1 | 0.954 | 0.849 | — |
| SGIP1 | 0.864 | 0.000 | — |
| RALBP1 | 0.844 | 0.843 | — |
| NECAP2 | 0.836 | 0.565 | — |
| SNAP91 | 0.822 | 0.136 | — |
| CLTB | 0.796 | 0.481 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FER | psi-mi:"MI:0018"(two hybrid) | pubmed:31867824|imex:IM-27345 |
| flgK | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| yycF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| EBI-1380999 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| EBI-1380972 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38918" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 4WSQ, 5L4Q, 5TE0, 8GMC, 8GMD,  | pLDDT=58.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Membrane, clathrin-coated pit; Pres / Plasma membrane; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AAK1 — AP2-associated protein kinase 1，研究基础较多，新颖性有限。
2. 蛋白大小961 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2M2I8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115977-AAK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AAK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2M2I8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000115977-AAK1/subcellular

![](https://images.proteinatlas.org/17931/149_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17931/149_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17931/150_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17931/150_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17931/151_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17931/151_G1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2M2I8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
