---
type: protein-evaluation
gene: "DYRK1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYRK1A — REJECTED (研究热度过高 (PubMed strict=716，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYRK1A / DYRK, MNB, MNBH |
| 蛋白名称 | Dual specificity tyrosine-phosphorylation-regulated kinase 1A |
| 蛋白大小 | 763 aa / 85.6 kDa |
| UniProt ID | Q13627 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Nucleoplasm, Centrosome, Cytosol; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 763 aa / 85.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=716 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.4; PDB: 2VX3, 2WO6, 3ANQ, 3ANR, 4AZE, 4MQ1, 4MQ2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR044131, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm, Centrosome, Cytosol | Supported |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 716 |
| PubMed broad count | 1121 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DYRK, MNB, MNBH |

**关键文献**:
1. Multiplex targeted sequencing identifies recurrently mutated genes in autism spectrum disorders.. *Science (New York, N.Y.)*. PMID: 23160955
2. Modulation of the Wnt pathway through inhibition of CLK2 and DYRK1A by lorecivivint as a novel, potentially disease-modifying approach for knee osteoarthritis treatment.. *Osteoarthritis and cartilage*. PMID: 31132406
3. DYRK1A signalling synchronizes the mitochondrial import pathways for metabolic rewiring.. *Nature communications*. PMID: 38902238
4. DYRK1A and cognition: A lifelong relationship.. *Pharmacology & therapeutics*. PMID: 30268771
5. DYRK1A Overexpression Drives Muscle Wasting by Impeding Myogenesis via a USP7-Axin1-β-Catenin Regulatory Axis in Mice.. *IUBMB life*. PMID: 40970570

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.4 |
| 高置信度残基 (pLDDT>90) 占比 | 43.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 47.2% |
| 有序区域 (pLDDT>70) 占比 | 49.3% |
| 可用 PDB 条目 | 2VX3, 2WO6, 3ANQ, 3ANR, 4AZE, 4MQ1, 4MQ2, 4NCT, 4YLJ, 4YLK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.4），有序残基占 49.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR044131, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF7 | 0.997 | 0.953 | — |
| RNF169 | 0.932 | 0.827 | — |
| RAD54L2 | 0.925 | 0.790 | — |
| LIN52 | 0.903 | 0.625 | — |
| FAM53C | 0.900 | 0.873 | — |
| FAM117B | 0.882 | 0.841 | — |
| RCAN1 | 0.881 | 0.097 | — |
| WDR26 | 0.842 | 0.292 | — |
| MED13L | 0.820 | 0.000 | — |
| NFATC1 | 0.819 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mnb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSMUSP00000113660.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9070862 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38918" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| SMAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| PRKACA | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| PRKACB | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.4 + PDB: 2VX3, 2WO6, 3ANQ, 3ANR, 4AZE,  | pLDDT=66.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nuclear speckles; 额外: Nucleoplasm, Centrosome, Cyt | 一致 |
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
1. DYRK1A — Dual specificity tyrosine-phosphorylation-regulated kinase 1A，研究基础较多，新颖性有限。
2. 蛋白大小763 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 716 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 716 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13627
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157540-DYRK1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYRK1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13627
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000157540-DYRK1A/subcellular

![](https://images.proteinatlas.org/15813/2006_A9_4_red_green.jpg)
![](https://images.proteinatlas.org/15813/2006_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/15813/2104_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/15813/2104_F7_4_red_green.jpg)
![](https://images.proteinatlas.org/15813/2207_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/15813/2207_G3_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13627-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
