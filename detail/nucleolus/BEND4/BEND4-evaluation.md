---
type: protein-evaluation
gene: "BEND4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEND4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEND4 / CCDC4 |
| 蛋白名称 | BEN domain-containing protein 4 |
| 蛋白大小 | 534 aa / 58.4 kDa |
| UniProt ID | Q6ZU67 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:34:16 |

**IF 图像**:
![](https://images.proteinatlas.org/36850/1182_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36850/1182_H7_3_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoli fibrillar center |
| 蛋白大小 | 10/10 | x1 | 10 | 534 aa / 58.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=9 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=59.1 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR018379, IPR038950 |
| PPI 网络 | 4/10 | x3 | 12 | STRING 13 partners; IntAct 1 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **138.0/180** | |
| **归一化总分 (/1.83)** | | | **75.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm, Nucleoli fibrillar center, Cytosol | Approved |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 534 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC4 |

**关键文献**:
1. Epigenetic silencing of BEND4, a novel DNA damage repair gene, is a synthetic lethal marker for ATM inhibitor in pancreatic cancer.. *Frontiers of medicine*. PMID: 38926248
2. BEND4: a novel prognostic biomarker in diffuse large B-cell lymphoma.. *Discover oncology*. PMID: 40327257
3. BEND4 as a Candidate Gene for an Infection-Induced Acute Encephalopathy Characterized by a Cyst and Calcification of the Pons and Cerebellar Atrophy.. *Molecular syndromology*. PMID: 35221871
4. Bend family proteins mark chromatin boundaries and synergistically promote early germ cell differentiation.. *Protein & cell*. PMID: 34731408
5. Genome-Wide Association Study to Identify QTL for Carcass Traits in Korean Hanwoo Cattle.. *Animals : an open access journal from MDPI*. PMID: 37685003

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 19.1% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 52.6% |
| 有序区域 (pLDDT>70) 占比 | 36.9% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=59.1），大部分区域无序。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018379, IPR038950; Pfam: PF10523 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZCCHC7 | 0.418 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M1 | tandem affinity purification | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 1

**评价**: 互作网络中等：STRING 13 预测 + IntAct 1 实验互作。PPI 评分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=59.1 | 单一来源 |
| 定位 | HPA | Nucleoplasm, Nucleoli fibrillar center | 单一来源 |
| PPI | STRING + IntAct | 13 + 1 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 75.4/100

**核心优势**:
1. BEND4 -- BEN domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小534 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 3 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. AlphaFold pLDDT 较低（59.1），存在显著无序区
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q6ZU67
- Protein Atlas: https://www.proteinatlas.org/search/BEND4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEND4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZU67
- STRING: https://string-db.org/network/9606.BEND4
- Packet data timestamp: 2026-06-03 03:34:16

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZU67-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZU67 |
| SMART | SM01025; |
| UniProt Domain [FT] | DOMAIN 390..498; /note="BEN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00784" |
| InterPro | IPR018379;IPR038950; |
| Pfam | PF10523; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188848-BEND4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
