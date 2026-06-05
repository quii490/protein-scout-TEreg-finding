---
type: protein-evaluation
gene: "HSF4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HSF4 — REJECTED (研究热度过高 (PubMed strict=159，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSF4 |
| 蛋白名称 | Heat shock factor protein 4 |
| 蛋白大小 | 492 aa / 53.0 kDa |
| UniProt ID | Q9ULV5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 492 aa / 53.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=159 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.6; PDB: 6J6V, 6J6W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000232, IPR036388, IPR036390; Pfam: PF00447 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear speck (GO:0016607)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 159 |
| PubMed broad count | 233 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Extracellular matrix stiffness regulates colorectal cancer progression via HSF4.. *Journal of experimental & clinical cancer research : CR*. PMID: 39881364
2. HSF4 Transcriptionally Activates Autophagy by Regulating ATG9a During Lens Terminal Differentiation.. *Investigative ophthalmology & visual science*. PMID: 37266953
3. The aging mouse lens transcriptome.. *Experimental eye research*. PMID: 34119483
4. Signaling and Gene Regulatory Networks in Mammalian Lens Development.. *Trends in genetics : TIG*. PMID: 28867048
5. Functional diversification of heat shock factors.. *Biologia futura*. PMID: 36402935

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.6 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 34.3% |
| 可用 PDB 条目 | 6J6V, 6J6W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.6），有序残基占 34.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000232, IPR036388, IPR036390; Pfam: PF00447 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NTM | 0.866 | 0.045 | — |
| BFSP2 | 0.847 | 0.053 | — |
| GPA33 | 0.815 | 0.053 | — |
| HSF2 | 0.808 | 0.779 | — |
| VSIG2 | 0.770 | 0.000 | — |
| CRYBB1 | 0.727 | 0.045 | — |
| GJA8 | 0.726 | 0.000 | — |
| LIM2 | 0.723 | 0.000 | — |
| CRYGD | 0.716 | 0.000 | — |
| CRYBB3 | 0.706 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| KRTAP3-1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NHLRC4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| OIP5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PITX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM168B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ALKBH4 | psi-mi:"MI:0018"(two hybrid) | pubmed:23145062|imex:IM-25716 |
| ACTMAP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZMYND12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.6 + PDB: 6J6V, 6J6W | pLDDT=59.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HSF4 — Heat shock factor protein 4，研究基础较多，新颖性有限。
2. 蛋白大小492 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 159 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 159 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULV5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102878-HSF4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSF4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULV5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HSF4/IF_images/804_G4_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HSF4/IF_images/804_G4_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000102878-HSF4/subcellular

![](https://images.proteinatlas.org/48584/712_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/48584/712_G4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/48584/804_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48584/804_G4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULV5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
