---
type: protein-evaluation
gene: "PACS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PACS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PACS1 / KIAA1175 |
| 蛋白名称 | Phosphofurin acidic cluster sorting protein 1 |
| 蛋白大小 | 963 aa / 104.9 kDa |
| UniProt ID | Q6VY07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm, Vesicles; UniProt: Golgi apparatus, trans-Golgi network |
| 蛋白大小 | 8/10 | ×1 | 8 | 963 aa / 104.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019381, IPR057541; Pfam: PF25332, PF10254 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Golgi apparatus, trans-Golgi network | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- COPI-coated vesicle (GO:0030137)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 138 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1175 |

**关键文献**:
1. New Candidates for Autism/Intellectual Disability Identified by Whole-Exome Sequencing.. *International journal of molecular sciences*. PMID: 34948243
2. PACS1 Neurodevelopmental Disorder.. **. PMID: 32672908
3. iPSC-derived models of PACS1 syndrome reveal transcriptional and functional deficits in neuron activity.. *Nature communications*. PMID: 38280846
4. Do PACS1 variants impeding adaptor protein binding predispose to syndromic intellectual disability?. *American journal of medical genetics. Part A*. PMID: 37141437
5. PACS1 is an HIV-1 cofactor that functions in Rev-mediated nuclear export of viral RNA.. *Virology*. PMID: 31759187

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 30.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 47.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 47.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019381, IPR057541; Pfam: PF25332, PF10254 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FURIN | 0.964 | 0.292 | — |
| WDR37 | 0.934 | 0.859 | — |
| PKD2 | 0.856 | 0.000 | — |
| CSNK2A1 | 0.807 | 0.292 | — |
| SORL1 | 0.795 | 0.292 | — |
| FGFR1OP | 0.780 | 0.780 | — |
| BCAP31 | 0.769 | 0.000 | — |
| TGOLN2 | 0.761 | 0.000 | — |
| GGA3 | 0.606 | 0.292 | — |
| ARF6 | 0.595 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CEP43 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR37 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| FAAP100 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPP1CA | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPP1R7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPP1CB | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 无 | pLDDT=64.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network / Plasma membrane; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. PACS1 — Phosphofurin acidic cluster sorting protein 1，研究基础较多，新颖性有限。
2. 蛋白大小963 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6VY07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175115-PACS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PACS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6VY07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000175115-PACS1/subcellular

![](https://images.proteinatlas.org/75046/1923_H2_12_cr5cd29609acda8_blue_red_green.jpg)
![](https://images.proteinatlas.org/75046/1923_H2_5_cr5cd29609ac8ff_blue_red_green.jpg)
![](https://images.proteinatlas.org/75046/2034_F11_24_cr604746b1ae525_blue_red_green.jpg)
![](https://images.proteinatlas.org/75046/2034_F11_2_cr604746b1ae540_blue_red_green.jpg)
![](https://images.proteinatlas.org/75046/2162_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75046/2162_F11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6VY07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6VY07 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019381;IPR057541; |
| Pfam | PF25332;PF10254; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175115-PACS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GGA3 | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| CSNK2B | Intact | false |
| FURIN | Biogrid | false |
| HTT | Intact | false |
| PPP1R7 | Intact | false |
| PTPRG | Intact | false |
| SNCA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
