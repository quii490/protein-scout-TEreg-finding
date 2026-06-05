---
type: protein-evaluation
gene: "DGAT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DGAT1 — REJECTED (研究热度过高 (PubMed strict=845，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGAT1 / AGRP1, DGAT |
| 蛋白名称 | Diacylglycerol O-acyltransferase 1 |
| 蛋白大小 | 488 aa / 55.3 kDa |
| UniProt ID | O75907 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Endoplasmic reticulum; 额外: Nucleoli, Nucleoli rim; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 488 aa / 55.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=845 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.3; PDB: 6VP0, 6VYI, 6VZ1, 8ESM, 8ETM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027251, IPR004299, IPR014371; Pfam: PF03062 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoli, Nucleoli rim | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- specific granule membrane (GO:0035579)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 845 |
| PubMed broad count | 1483 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AGRP1, DGAT |

**关键文献**:
1. Identification of an alternative triglyceride biosynthesis pathway.. *Nature*. PMID: 37648867
2. Glycerol Kinase Drives Hepatic de novo Lipogenesis and Triglyceride Synthesis in Nonalcoholic Fatty Liver by Activating SREBP-1c Transcription, Upregulating DGAT1/2 Expression, and Promoting Glycerol Metabolism.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39418169
3. Inhibition of diacylglycerol O-acyltransferase 1 provides neuroprotection by inhibiting ferroptosis in ischemic stroke.. *Molecular medicine (Cambridge, Mass.)*. PMID: 40375180
4. Strong evidence for association between K232A polymorphism of the DGAT1 gene and milk fat and protein contents: A meta-analysis.. *Journal of dairy science*. PMID: 36870848
5. Diacylglycerol O-acyltransferase isoforms play a role in peridroplet mitochondrial fatty acid metabolism in bovine liver.. *Journal of dairy science*. PMID: 38851581

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 50.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 78.9% |
| 可用 PDB 条目 | 6VP0, 6VYI, 6VZ1, 8ESM, 8ETM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6VP0, 6VYI, 6VZ1, 8ESM, 8ETM）+ AlphaFold极高置信度预测（pLDDT=80.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027251, IPR004299, IPR014371; Pfam: PF03062 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DGAT2 | 0.999 | 0.215 | — |
| MOGAT1 | 0.996 | 0.215 | — |
| MOGAT2 | 0.993 | 0.215 | — |
| MOGAT3 | 0.989 | 0.215 | — |
| PLPP2 | 0.978 | 0.060 | — |
| PLPP3 | 0.962 | 0.060 | — |
| PLPP4 | 0.956 | 0.067 | — |
| AWAT2 | 0.952 | 0.215 | — |
| PLPP5 | 0.952 | 0.067 | — |
| RPE65 | 0.931 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABRA4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CD1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NAC089 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| SLC7A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C3AR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POMK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 6VP0, 6VYI, 6VZ1, 8ESM, 8ETM | pLDDT=80.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum; 额外: Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DGAT1 — Diacylglycerol O-acyltransferase 1，研究基础较多，新颖性有限。
2. 蛋白大小488 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 845 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 845 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75907
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185000-DGAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75907
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000185000-DGAT1/subcellular

![](https://images.proteinatlas.org/32853/924_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/32853/924_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/32853/932_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/32853/932_F9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/32853/971_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/32853/971_F9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75907-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
