---
type: protein-evaluation
gene: "HERPUD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HERPUD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HERPUD2 |
| 蛋白名称 | Homocysteine-responsive endoplasmic reticulum-resident ubiquitin-like domain member 2 protein |
| 蛋白大小 | 406 aa / 45.1 kDa |
| UniProt ID | Q9BSE4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 406 aa / 45.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.6; PDB: 2KDB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039751, IPR000626, IPR029071; Pfam: PF00240 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Potential role of microRNA-7 in the anti-neuroinflammation effects of nicorandil in astrocytes induced by oxygen-glucose deprivation.. *Journal of neuroinflammation*. PMID: 26961366
2. Majority of cerebrospinal fluid-contacting neurons in the spinal cord of C57Bl/6N mice is present in ectopic position unlike in other studied experimental mice strains and mammalian species.. *The Journal of comparative neurology*. PMID: 32212159
3. Ubiquitin-proteasome Pathway-linked Gene Signatures as Prognostic Indicators in Prostate Cancer.. *Anticancer research*. PMID: 40295064
4. Screening of reliable reference genes for the normalization of RT-qPCR in chicken oviduct tract.. *Poultry science*. PMID: 38959666

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.3% |
| 低置信 (pLDDT<50) 占比 | 44.6% |
| 有序区域 (pLDDT>70) 占比 | 39.2% |
| 可用 PDB 条目 | 2KDB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.6），有序残基占 39.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039751, IPR000626, IPR029071; Pfam: PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C7orf26 | 0.516 | 0.000 | — |
| FAM8A1 | 0.504 | 0.000 | — |
| TMUB2 | 0.493 | 0.000 | — |
| OGFOD1 | 0.474 | 0.000 | — |
| OR4F6 | 0.433 | 0.000 | — |
| TMUB1 | 0.406 | 0.000 | — |
| FBXO42 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hmsT | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fabF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rlmG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TMEM60 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC39A9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPTSSA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC7A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| IER3IP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.6 + PDB: 2KDB | pLDDT=60.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HERPUD2 — Homocysteine-responsive endoplasmic reticulum-resident ubiquitin-like domain member 2 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSE4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122557-HERPUD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HERPUD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSE4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000122557-HERPUD2/subcellular

![](https://images.proteinatlas.org/76087/1608_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/76087/1608_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/76087/1610_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/76087/1610_G4_6_red_green.jpg)
![](https://images.proteinatlas.org/76087/1664_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/76087/1664_A3_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSE4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
