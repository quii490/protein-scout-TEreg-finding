---
type: protein-evaluation
gene: "FOXC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXC1 — REJECTED (研究热度过高 (PubMed strict=585，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXC1 / FKHL7, FREAC3 |
| 蛋白名称 | Forkhead box protein C1 |
| 蛋白大小 | 553 aa / 56.8 kDa |
| UniProt ID | Q12948 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 553 aa / 56.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=585 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001766, IPR050211, IPR047391, IPR018122, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- heterochromatin (GO:0000792)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 585 |
| PubMed broad count | 993 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHL7, FREAC3 |

**关键文献**:
1. Axenfeld-Rieger syndrome: more than meets the eye.. *Journal of medical genetics*. PMID: 35882526
2. FOXC1.. *Archives of pathology & laboratory medicine*. PMID: 34784418
3. Molecular Subtyping of Triple-Negative Breast Cancers by Immunohistochemistry: Molecular Basis and Clinical Relevance.. *The oncologist*. PMID: 32406563
4. Potential diagnostic markers and therapeutic targets for periodontitis and Alzheimer's disease based on bioinformatics analysis.. *Journal of periodontal research*. PMID: 38189472
5. DEK::NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.. *Leukemia*. PMID: 40204893

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.3 |
| 高置信度残基 (pLDDT>90) 占比 | 13.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 25.0% |
| 低置信 (pLDDT<50) 占比 | 58.6% |
| 有序区域 (pLDDT>70) 占比 | 16.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.3），有序残基占 16.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001766, IPR050211, IPR047391, IPR018122, IPR030456; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PITX2 | 0.991 | 0.306 | — |
| GMDS | 0.886 | 0.000 | — |
| CYP1B1 | 0.856 | 0.046 | — |
| PBX1 | 0.828 | 0.399 | — |
| SOX2 | 0.769 | 0.438 | — |
| PAX6 | 0.767 | 0.065 | — |
| PPP2R2A | 0.743 | 0.739 | — |
| GLI2 | 0.717 | 0.096 | — |
| BMP4 | 0.684 | 0.000 | — |
| SIX1 | 0.655 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pitx2 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:16449236|imex:IM-19694 |
| ORF | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| BCOR | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-25601|pubmed:27505670 |
| PPP2R2A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2D | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| HSPBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| METTL6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TFAP2C | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25303530|imex:IM-23610 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.3 + PDB: 无 | pLDDT=54.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXC1 — Forkhead box protein C1，研究基础较多，新颖性有限。
2. 蛋白大小553 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 585 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 585 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12948
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054598-FOXC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12948
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000054598-FOXC1/subcellular

![](https://images.proteinatlas.org/40670/411_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/40670/411_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/40670/415_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/40670/415_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/40670/416_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/40670/416_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12948-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12948 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR050211;IPR047391;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000054598-FOXC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP2R1A | Biogrid, Bioplex | true |
| APEX1 | Biogrid | false |
| C1QBP | Intact | false |
| CBFB | Biogrid | false |
| CEBPA | Biogrid | false |
| ELAVL1 | Biogrid | false |
| FLNA | Intact | false |
| GATAD2B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
