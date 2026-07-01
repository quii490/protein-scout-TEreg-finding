---
type: protein-evaluation
gene: "ERICH5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERICH5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERICH5 / C8orf47 |
| 蛋白名称 | Glutamate-rich protein 5 |
| 蛋白大小 | 374 aa / 39.9 kDa |
| UniProt ID | Q6P6B1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 39.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027856 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf47 |

**关键文献**:
1. Binding Affinity Determines Substrate Specificity and Enables Discovery of Substrates for N-Myristoyltransferases.. *ACS catalysis*. PMID: 34956690
2. Construction of a novel risk model for esophageal squamous cell carcinoma associated with purinergic signaling pathways and chemoradiotherapy sensitivity genes.. *Frontiers in medicine*. PMID: 41924732

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 38.8% |
| 低置信 (pLDDT<50) 占比 | 60.2% |
| 有序区域 (pLDDT>70) 占比 | 1.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.9），有序残基占 1.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027856 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRC45 | 0.555 | 0.000 | — |
| WDR37 | 0.551 | 0.105 | — |
| ARMC8 | 0.460 | 0.000 | — |
| LRRC57 | 0.455 | 0.088 | — |
| FAM193B | 0.448 | 0.000 | — |
| MANBAL | 0.427 | 0.000 | — |
| GRTP1 | 0.411 | 0.111 | — |
| ODF3L2 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 8，IntAct interactions: 0
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.9 + PDB: 无 | pLDDT=48.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 8 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ERICH5 — Glutamate-rich protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SLC25A41 | BioGRID | 0 |
| HOXB5 | BioGRID | 0 |
| FYTTD1 | BioGRID | 0 |
| TMEM185A | BioGRID | 0 |
| TMEM17 | BioGRID | 0 |
| FADS3 | BioGRID | 0 |
| GJB7 | BioGRID | 0 |
| KIFAP3 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

ERICH5（Glutamate-rich protein 5, 374 aa, UniProt Q6P6B1）。定位于Golgi apparatus（HPA Approved），但额外检出Nucleoplasm和Cytosol信号。InterPro注释仅IPR027856（DUF4542，功能未知结构域），Pfam未检出。AlphaFold pLDDT=48.9（有序区仅1.1%），提示该蛋白几乎完全处于内在无序状态。

从结构生物学角度，pLDDT=48.9且0%残基>90置信度，表明AlphaFold无法为该蛋白预测可靠三级结构。高比例无序区域（约99%）是IDP（内在无序蛋白）的典型特征。IDP在转录调控和染色质组织中扮演重要角色——它们通过多价弱相互作用参与液-液相分离（LLPS），是核凝聚体（如转录凝聚体、核仁）的常见组分。ERICH5富含谷氨酸（如其名称所示），酸性残基富集是转录激活域和LLPS支架蛋白的特征序列偏好。

PPI网络极其稀疏：STRING仅8个伙伴（最高score LRRC45=0.555），IntAct为0。但HPA interaction页面上CFTR（IntAct）、KEAP1（IntAct）等有实验互作记录。KEAP1是Nrf2氧化应激通路的核心调控因子，若ERICH5与KEAP1确实存在互作，可能参与氧化还原信号传导。BioGRID鉴定的伙伴包括HOXB5（homeobox转录因子）、FYTTD1（转录延伸因子），进一步支持其核功能潜力。

从TE调控角度，ERICH5作为IDP在nucleoplasm中的存在提示可能通过LLPS参与核体形成。目前PubMed仅2篇文献（PMID:34956690、41924732），功能完全未知。综合评分65.0/100。建议：（1）测定ERICH5是否在细胞核内形成凝聚体；（2）通过APEX2邻近标记鉴定其核内互作组；（3）评估过表达/敲低对TE表达的影响。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P6B1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177459-ERICH5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERICH5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P6B1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000177459-ERICH5/subcellular

![](https://images.proteinatlas.org/25293/1042_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25293/1042_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25293/1423_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25293/1423_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/25293/214_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/25293/214_H7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P6B1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P6B1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027856; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177459-ERICH5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CFTR | Intact | false |
| FADS3 | Bioplex | false |
| KEAP1 | Intact | false |
| ZDHHC23 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
