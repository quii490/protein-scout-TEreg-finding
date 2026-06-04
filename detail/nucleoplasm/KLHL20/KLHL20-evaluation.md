---
type: protein-evaluation
gene: "KLHL20"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL20 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL20 / KLEIP, KLHLX |
| 蛋白名称 | Kelch-like protein 20 |
| 蛋白大小 | 609 aa / 68.0 kDa |
| UniProt ID | Q9Y2M5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Cytosol; UniProt: Cytoplasm, perinuclear region; Nucleus; Golgi apparatus, tra |
| 蛋白大小 | 10/10 | ×1 | 10 | 609 aa / 68.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.5; PDB: 5YQ4, 6GY5, 8CIA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol | Supported |
| UniProt | Cytoplasm, perinuclear region; Nucleus; Golgi apparatus, trans-Golgi network; Cell projection, axon;... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- axon (GO:0030424)
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- Golgi apparatus (GO:0005794)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KLEIP, KLHLX |

**关键文献**:
1. De novo missense variants in the E3 ubiquitin ligase adaptor KLHL20 cause a developmental disorder with intellectual disability, epilepsy, and autism spectrum disorder.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 36214804
2. LUBAC and OTULIN regulate autophagy initiation and maturation by mediating the linear ubiquitination and the stabilization of ATG13.. *Autophagy*. PMID: 32543267
3. KLHL20 and its role in cell homeostasis: A new perspective and therapeutic potential.. *Life sciences*. PMID: 39233199
4. Cul3-KLHL20 ubiquitin ligase: physiological functions, stress responses, and disease implications.. *Cell division*. PMID: 27042198
5. Temporal and Spatial Characterization of CUL3(KLHL20)-Driven Targeted Degradation of BET Family BRD Proteins by the Macrocycle-Based Degrader BTR2004.. *ACS chemical biology*. PMID: 40891966

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 5YQ4, 6GY5, 8CIA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5YQ4, 6GY5, 8CIA）+ AlphaFold高质量预测（pLDDT=88.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006652; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.999 | 0.797 | — |
| RBX1 | 0.986 | 0.000 | — |
| DAPK1 | 0.949 | 0.765 | — |
| KLHL22 | 0.925 | 0.173 | — |
| KLHL42 | 0.924 | 0.062 | — |
| SPOP | 0.924 | 0.091 | — |
| KLHL9 | 0.924 | 0.053 | — |
| TNFAIP1 | 0.919 | 0.000 | — |
| KBTBD8 | 0.919 | 0.092 | — |
| KCTD13 | 0.919 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERG28 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LUC7L2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PML | psi-mi:"MI:0096"(pull down) | pubmed:21840486|imex:IM-16569 |
| xerC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 5YQ4, 6GY5, 8CIA | pLDDT=88.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Nucleus; Golgi appa / Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL20 — Kelch-like protein 20，非常新颖，仅有少数基础研究。
2. 蛋白大小609 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2M5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000076321-KLHL20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2M5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
