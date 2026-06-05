---
type: protein-evaluation
gene: "BORA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BORA — REJECTED (研究热度过高 (PubMed strict=115，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BORA / C13orf34 |
| 蛋白名称 | Protein aurora borealis |
| 蛋白大小 | 559 aa / 61.2 kDa |
| UniProt ID | Q6PGQ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 559 aa / 61.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=115 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023252; Pfam: PF15280 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- meiotic spindle (GO:0072687)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 115 |
| PubMed broad count | 5976 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf34 |

**关键文献**:
1. Predictive gene expression signature diagnoses neonatal sepsis before clinical presentation.. *EBioMedicine*. PMID: 39472236
2. The cAMP-PKA signaling initiates mitosis by phosphorylating Bora.. *Nature communications*. PMID: 40849432
3. Molecular basis for the activation of Aurora A and Plk1 kinases during mitotic entry.. *The EMBO journal*. PMID: 41606196
4. Decoding the language of PLK1 docking motifs and activation mechanisms.. *Trends in cell biology*. PMID: 40783322
5. Plk1- and beta-TrCP-dependent degradation of Bora controls mitotic progression.. *The Journal of cell biology*. PMID: 18378770

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.9 |
| 高置信度残基 (pLDDT>90) 占比 | 2.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 64.9% |
| 有序区域 (pLDDT>70) 占比 | 14.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.9），有序残基占 14.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023252; Pfam: PF15280 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLK1 | 0.997 | 0.837 | — |
| AURKA | 0.976 | 0.328 | — |
| CDK1 | 0.911 | 0.000 | — |
| AJUBA | 0.828 | 0.000 | — |
| CCNB1 | 0.803 | 0.000 | — |
| PLK4 | 0.761 | 0.000 | — |
| BTRC | 0.754 | 0.420 | — |
| ECT2 | 0.737 | 0.000 | — |
| RACGAP1 | 0.735 | 0.000 | — |
| HAUS6 | 0.730 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FGFR3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FEZ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ctp | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| AAF59068 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cdlc2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "NEST:bs17h08" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| RABGGTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.9 + PDB: 无 | pLDDT=50.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli fibrillar center; 额外: Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BORA — Protein aurora borealis，研究基础较多，新颖性有限。
2. 蛋白大小559 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 115 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 115 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PGQ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136122-BORA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BORA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PGQ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000136122-BORA/subcellular

![](https://images.proteinatlas.org/40866/474_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/40866/474_G7_5_red_green.jpg)
![](https://images.proteinatlas.org/40866/480_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/40866/480_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/40866/510_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/40866/510_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PGQ7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
