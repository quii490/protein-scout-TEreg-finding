---
type: protein-evaluation
gene: "NOS1AP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation, recovery, re-evaluation]
status: rejected
---

## NOS1AP -- REJECTED (研究热度过高 (PubMed strict=156，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOS1AP / CAPON, KIAA0464 |
| 蛋白名称 | Carboxyl-terminal PDZ ligand of neuronal nitric oxide synthase protein |
| 蛋白大小 | 506 aa / 56.1 kDa |
| UniProt ID | O75052 |
| 数据采集时间 | 2026-06-03 23:51:45 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Cell projection, filopodium; Cell projection, podo |
| 蛋白大小 | 10/10 | x1 | 10 | 506 aa / 56.1 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=156 篇 (>100 -> REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR051133, IPR011993, IPR006020; Pfam: PF0064 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cell projection, filopodium; Cell projection, podosome | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- caveola (GO:0005901)
- cytosol (GO:0005829)
- filopodium (GO:0030175)
- glutamatergic synapse (GO:0098978)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 156 |
| PubMed broad count | 258 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAPON, KIAA0464 |

**关键文献**:
1. Functional Insights in PLS3-Mediated Osteogenic Regulation.. *Cells*. PMID: 39273077
2. Research progress in NOS1AP in neurological and psychiatric diseases.. *Brain research bulletin*. PMID: 27237129
3. Recessive variants in the intergenic NOS1AP-C1orf226 locus cause monogenic kidney disease responsive to anti-proteinuric treatment.. *Nature communications*. PMID: 41309577
4. NOS1AP Gene Variants and Their Role in Metabolic Syndrome: A Study of Patients with Schizophrenia.. *Biomedicines*. PMID: 38540239
5. Mechanisms of NOS1AP action on NMDA receptor-nNOS signaling.. *Frontiers in cellular neuroscience*. PMID: 25221472

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 45.8% |
| 有序区域 (pLDDT>70) 占比 | 43.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 43.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051133, IPR011993, IPR006020; Pfam: PF00640 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOS1 | 0.999 | 0.411 | — |
| RASD1 | 0.996 | 0.292 | — |
| C1orf226 | 0.943 | 0.000 | — |
| F8W6W0_HUMAN | 0.899 | 0.000 | — |
| DLG4 | 0.867 | 0.000 | — |
| SCRIB | 0.857 | 0.129 | — |
| SYN2 | 0.839 | 0.310 | — |
| SYN1 | 0.812 | 0.310 | — |
| KCNH2 | 0.752 | 0.000 | — |
| SNTA1 | 0.723 | 0.114 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTPRN | psi-mi:"MI:0096"(pull down) | pubmed:11043403 |
| Snta1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11043403 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FAM133A | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| ZCCHC17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NKAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP2M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AKAP17A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, filopodium; Cell projection, podo / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: (REJECTED) (REJECTED)

**核心优势**:
1. NOS1AP -- Carboxyl-terminal PDZ ligand of neuronal nitric oxide synthase protein，有一定研究基础，但仍存在niche空间。
2. 蛋白大小506 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 156 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 156 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75052
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198929-NOS1AP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOS1AP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75052
- STRING: https://string-db.org/network/9606.NOS1AP
- Packet data timestamp: 2026-06-03 23:51:45

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198929-NOS1AP/subcellular

![](https://images.proteinatlas.org/30066/1002_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/30066/1002_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/30066/1004_E7_3_red_green.jpg)
![](https://images.proteinatlas.org/30066/1004_E7_6_red_green.jpg)
![](https://images.proteinatlas.org/30066/1182_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/30066/1182_H8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75052-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
