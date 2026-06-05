---
type: protein-evaluation
gene: "BLVRB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BLVRB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLVRB / FLR, SCAN |
| 蛋白名称 | Flavin reductase (NADPH) |
| 蛋白大小 | 206 aa / 22.1 kDa |
| UniProt ID | P30043 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:39:58 |

**IF 图像**:
![](https://images.proteinatlas.org/41698/571_G2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/41698/571_G2_6_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 206 aa / 22.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=44 篇 (41-60->6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=97.7; PDB: 1HDO, 1HE2, ... |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR016040, IPR036291... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **136.5/180** | |
| **归一化总分 (/1.83)** | | | **74.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles, Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 206 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FLR, SCAN |

**关键文献**:
1. Deciphering the cellular and molecular landscape of pulmonary fibrosis through single-cell sequencing and machine learning.. *Journal of translational medicine*. PMID: 39748378
2. Zika virus remodelled ER membranes contain proviral factors involved in redox and methylation pathways.. *Nature communications*. PMID: 38052817
3. Proteomic profiling reveals a higher presence of glycolytic enzymes in human atherosclerotic lesions with unfavourable histological characteristics.. *Cardiovascular research*. PMID: 40354194
4. Evolutionary Adaptations in Biliverdin Reductase B: Insights into Coenzyme Dynamics and Catalytic Efficiency.. *International journal of molecular sciences*. PMID: 39768998
5. Identification of novel gut microbiota-related biomarkers in cerebral hemorrhagic stroke.. *Frontiers in medicine*. PMID: 40933575

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.7 |
| 高置信度残基 (pLDDT>90) 占比 | 98.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.6% |
| 可用 PDB 条目 | 1HDO, 1HE2, 1HE3, 1HE4, 1HE5, 5OOG, 5OOH, 6OPL, 7ER6, 7ER7, 7ER8, 7ER9, 7ERA, 7ERB, 7ERC, 7ERD, 7ERE, 8ELL, 8ELM, 8K4K, 9C16, 9C17, 9C18 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=97.7），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016040, IPR036291, IPR051606; Pfam: PF13460 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BLVRA | 0.993 | 0.000 | -- |
| HMOX1 | 0.952 | 0.000 | -- |
| HMOX2 | 0.951 | 0.000 | -- |
| ACP5 | 0.914 | 0.000 | -- |
| RFK | 0.913 | 0.000 | -- |
| NDUFS3 | 0.876 | 0.571 | -- |
| UQCRFS1 | 0.862 | 0.557 | -- |
| CYC1 | 0.848 | 0.567 | -- |
| NDUFV1 | 0.842 | 0.571 | -- |
| NDUFS8 | 0.840 | 0.571 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORM1 | two hybrid | imex:IM-15364|pubmed:21988832 |
| RPL31 | two hybrid array | imex:IM-15364|pubmed:21988832 |
| VCAM1 | cross-linking study | imex:IM-17358|pubmed:22623428 |
| yscH | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| recN | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| ESR1 | tandem affinity purification | pubmed:31527615|imex:IM-26954 |
| SH3GL3 | anti tag coimmunoprecipitation | pubmed:31980649|imex:IM-26434 |
| GTF2E2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SNRNP27 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| FSD1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.7 + PDB: 1HDO, 1HE2, 1HE3 | pLDDT=97.7, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 74.6/100

**核心优势**:
1. 蛋白大小206 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. AlphaFold高质量预测（pLDDT=97.7），结构可信度高。
3. 已有PDB实验结构：1HDO, 1HE2, 1HE3。
4. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P30043
- Protein Atlas: https://www.proteinatlas.org/search/BLVRB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLVRB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P30043
- STRING: https://string-db.org/network/9606.BLVRB
- Packet data timestamp: 2026-06-03 03:39:58

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P30043-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
