---
type: protein-evaluation
gene: "NQO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation, recovery, re-evaluation]
status: rejected
---

## NQO2 -- REJECTED (研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NQO2 / NMOR2 |
| 蛋白名称 | Ribosyldihydronicotinamide dehydrogenase [quinone] |
| 蛋白大小 | 231 aa / 25.9 kDa |
| UniProt ID | P16083 |
| 数据采集时间 | 2026-06-03 23:53:06 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 231 aa / 25.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=146 篇 (>100 -> REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=98.1; PDB: 1QR2, 1SG0, 1XI2, 1ZX1, 2BZS, 2QMY, |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR003680, IPR029039, IPR051545; Pfam: PF0252 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 247 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NMOR2 |

**关键文献**:
1. NRH:quinone oxidoreductase2 (NQO2).. *Chemico-biological interactions*. PMID: 11154737
2. Polymorphisms and Pharmacogenomics of NQO2: The Past and the Future.. *Genes*. PMID: 38254976
3. Mouse NRH:quinone oxidoreductase (NQO2): cloning of cDNA and gene- and tissue-specific expression.. *Gene*. PMID: 10903442
4. The induction of quinone oxidoreductases NQO1 and NQO2 by clozapine: Potential implications for clozapine-induced agranulocytosis.. *Toxicology letters*. PMID: 40311769
5. The Unusual Cosubstrate Specificity of NQO2: Conservation Throughout the Amniotes and Implications for Cellular Function.. *Frontiers in pharmacology*. PMID: 35517822

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.1 |
| 高置信度残基 (pLDDT>90) 占比 | 98.3% |
| 置信残基 (pLDDT 70-90) 占比 | 0.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 1QR2, 1SG0, 1XI2, 1ZX1, 2BZS, 2QMY, 2QMZ, 2QR2, 2QWX, 2QX4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1QR2, 1SG0, 1XI2, 1ZX1, 2BZS, 2QMY, 2QMZ, 2QR2, 2QWX, 2QX4）+ AlphaFold极高置信度预测（pLDDT=98.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003680, IPR029039, IPR051545; Pfam: PF02525 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRYZ | 0.652 | 0.000 | — |
| CYP19A1 | 0.640 | 0.000 | — |
| TMCO3 | 0.589 | 0.310 | — |
| JMJD7-PLA2G4B | 0.564 | 0.293 | — |
| ABL1 | 0.541 | 0.000 | — |
| IYD | 0.539 | 0.000 | — |
| LRRC7 | 0.536 | 0.536 | — |
| PALB2 | 0.503 | 0.000 | — |
| ARHGEF5 | 0.491 | 0.000 | — |
| B3GAT2 | 0.485 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GORASP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| 38918" | psi-mi:"MI:0405"(competition binding) | pubmed:17721511|imex:IM-19952 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| RHOB | psi-mi:"MI:0018"(two hybrid) | pubmed:19637314|imex:IM-20406 |
| ytfE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| opdA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SPG21 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.1 + PDB: 1QR2, 1SG0, 1XI2, 1ZX1, 2BZS,  | pLDDT=98.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: (REJECTED) (REJECTED)

**核心优势**:
1. NQO2 -- Ribosyldihydronicotinamide dehydrogenase [quinone]，有一定研究基础，但仍存在niche空间。
2. 蛋白大小231 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 146 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16083
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124588-NQO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NQO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16083
- STRING: https://string-db.org/network/9606.NQO2
- Packet data timestamp: 2026-06-03 23:53:06

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000124588-NQO2/subcellular

![](https://images.proteinatlas.org/21332/189_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/21332/189_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/21332/190_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/21332/190_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/21332/191_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/21332/191_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16083-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
