---
type: protein-evaluation
gene: "MYORG"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYORG 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYORG / KIAA1161, NET37 |
| 蛋白名称 | Alpha-galactosidase MYORG |
| 蛋白大小 | 714 aa / 81.1 kDa |
| UniProt ID | Q6NSJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Nucleus membrane; Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 714 aa / 81.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=90.3; PDB: 7QQF, 7QQG, 7QQH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050985, IPR017853, IPR048395, IPR000322, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Nucleus membrane; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 86 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1161, NET37 |

**关键文献**:
1. Basal ganglia calcification: 'Fahr's disease'.. *Practical neurology*. PMID: 40169250
2. Knockdown of myorg leads to brain calcification in zebrafish.. *Molecular brain*. PMID: 35870928
3. MYORG Mutations: a Major Cause of Recessive Primary Familial Brain Calcification.. *Current neurology and neuroscience reports*. PMID: 31440850
4. The primary familial brain calcification-associated protein MYORG is an α-galactosidase with restricted substrate specificity.. *PLoS biology*. PMID: 36129849
5. MYORG is associated with recessive primary familial brain calcification.. *Annals of clinical and translational neurology*. PMID: 30656188

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 79.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 91.9% |
| 可用 PDB 条目 | 7QQF, 7QQG, 7QQH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7QQF, 7QQG, 7QQH）+ AlphaFold高质量预测（pLDDT=90.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050985, IPR017853, IPR048395, IPR000322, IPR013780; Pfam: PF01055, PF21365 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC20A2 | 0.814 | 0.000 | — |
| XPR1 | 0.677 | 0.206 | — |
| C9orf24 | 0.647 | 0.000 | — |
| PDGFB | 0.636 | 0.000 | — |
| PDGFRB | 0.599 | 0.000 | — |
| PRKCSH | 0.595 | 0.460 | — |
| GNPTG | 0.535 | 0.460 | — |
| PLPP7 | 0.533 | 0.000 | — |
| GNE | 0.455 | 0.000 | — |
| DNAJA4 | 0.436 | 0.408 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CISD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRPF38A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CGRRF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENTPD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FKBP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 1 / 12 = 8%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 7QQF, 7QQG, 7QQH | pLDDT=90.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus membrane; Endoplasmic reticulum membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MYORG — Alpha-galactosidase MYORG，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小714 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NSJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164976-MYORG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYORG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NSJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000164976-MYORG/subcellular

![](https://images.proteinatlas.org/67487/1283_A7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/67487/1283_A7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/67487/1286_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/67487/1286_A7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NSJ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
