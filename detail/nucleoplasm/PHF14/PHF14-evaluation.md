---
type: protein-evaluation
gene: "PHF14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF14 / KIAA0783 |
| 蛋白名称 | PHD finger protein 14 |
| 蛋白大小 | 948 aa / 107.0 kDa |
| UniProt ID | O94880 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 948 aa / 107.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034732, IPR050701, IPR019786, IPR011011, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0783 |

**关键文献**:
1. PHF14 enhances DNA methylation of SMAD7 gene to promote TGF-β-driven lung adenocarcinoma metastasis.. *Cell discovery*. PMID: 37072414
2. Epigenetic Regulation and Neurodevelopmental Disorders: From MeCP2 to the TCF20/PHF14 Complex.. *Genes*. PMID: 39766920
3. The high mobility group protein HMG20A cooperates with the histone reader PHF14 to modulate TGFβ and Hippo pathways.. *Nucleic acids research*. PMID: 36124662
4. Depletion of PHF14, a novel histone-binding protein gene, causes neonatal lethality in mice due to respiratory failure.. *Acta biochimica et biophysica Sinica*. PMID: 23688586
5. SP4 Facilitates Esophageal Squamous Cell Carcinoma Progression by Activating PHF14 Transcription and Wnt/Β-Catenin Signaling.. *Molecular cancer research : MCR*. PMID: 37768180

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034732, IPR050701, IPR019786, IPR011011, IPR001965; Pfam: PF00628, PF13831, PF13832 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HMG20A | 0.910 | 0.827 | — |
| H2AZ1 | 0.645 | 0.593 | — |
| BRPF1 | 0.641 | 0.000 | — |
| KAT6A | 0.638 | 0.164 | — |
| BRD1 | 0.614 | 0.000 | — |
| H2AX | 0.608 | 0.599 | — |
| BRPF3 | 0.599 | 0.000 | — |
| KAT7 | 0.596 | 0.000 | — |
| PWWP2A | 0.594 | 0.000 | — |
| CHD4 | 0.583 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| speA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EBI-6927943 | psi-mi:"MI:0018"(two hybrid) | pubmed:24136289|doi:10.1039/C3 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Srp72 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TCF20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HMG20A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DAXX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Vesicles; 额外: Nucleoplasm, Cytosol | 一致 |
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
1. PHF14 — PHD finger protein 14，非常新颖，仅有少数基础研究。
2. 蛋白大小948 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94880
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106443-PHF14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94880
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000106443-PHF14/subcellular

![](https://images.proteinatlas.org/17376/1657_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/17376/1657_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/17376/1786_A5_11_red_green.jpg)
![](https://images.proteinatlas.org/17376/1786_A5_9_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94880-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
