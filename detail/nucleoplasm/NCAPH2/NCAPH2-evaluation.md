---
type: protein-evaluation
gene: "NCAPH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCAPH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCAPH2 / CAPH2 |
| 蛋白名称 | Condensin-2 complex subunit H2 |
| 蛋白大小 | 605 aa / 68.2 kDa |
| UniProt ID | Q6IBW4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cell Junctions, Cytokinetic bridge; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 605 aa / 68.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.4; PDB: 9F5W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031737, IPR031719, IPR009378, IPR031739; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions, Cytokinetic bridge | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- condensed nuclear chromosome (GO:0000794)
- condensin complex (GO:0000796)
- intercellular bridge (GO:0045171)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAPH2 |

**关键文献**:
1. Condensin II subunit NCAPH2 associates with shelterin protein TRF1 and is required for telomere stability.. *Journal of cellular physiology*. PMID: 31026066
2. The Condensin II complex regulates essential gene expression programs during erythropoiesis.. *Development (Cambridge, England)*. PMID: 40260585
3. Associations Between Levels of Peripheral NCAPH2 Promoter Methylation and Different Stages of Alzheimer's Disease: A Cross-Sectional Study.. *Journal of Alzheimer's disease : JAD*. PMID: 36806511
4. Splice variants of the condensin II gene Ncaph2 include alternative reading frame translations of exon 1.. *The FEBS journal*. PMID: 22333158
5. Development and validation of metabolic models for predicting survival and immune status of hepatocellular carcinoma patients.. *Advances in clinical and experimental medicine : official organ Wroclaw Medical University*. PMID: 37166013

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 31.7% |
| 中等置信 (pLDDT 50-70) 占比 | 19.7% |
| 低置信 (pLDDT<50) 占比 | 35.4% |
| 有序区域 (pLDDT>70) 占比 | 44.9% |
| 可用 PDB 条目 | 9F5W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.4），有序残基占 44.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031737, IPR031719, IPR009378, IPR031739; Pfam: PF16858, PF16869, PF06278 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMC4 | 0.999 | 0.857 | — |
| NCAPD3 | 0.999 | 0.911 | — |
| NCAPG2 | 0.999 | 0.899 | — |
| SMC2 | 0.990 | 0.858 | — |
| NCAPD2 | 0.977 | 0.095 | — |
| NCAPH | 0.916 | 0.000 | — |
| NCAPG | 0.891 | 0.226 | — |
| LPCAT3 | 0.797 | 0.000 | — |
| TERF1 | 0.713 | 0.292 | — |
| LMF2 | 0.698 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FOLR1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PA | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| LMO2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CTXN3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| VAMP5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| EMD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM14C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARLN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBIAD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| APOD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.4 + PDB: 9F5W | pLDDT=62.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Cell Junctions, Cytokinetic bridg | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NCAPH2 — Condensin-2 complex subunit H2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小605 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IBW4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000025770-NCAPH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCAPH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IBW4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000025770-NCAPH2/subcellular

![](https://images.proteinatlas.org/67932/1250_A3_4_red_green.jpg)
![](https://images.proteinatlas.org/67932/1250_A3_5_red_green.jpg)
![](https://images.proteinatlas.org/67932/1255_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/67932/1255_A3_4_red_green.jpg)
![](https://images.proteinatlas.org/67932/1284_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/67932/1284_H11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IBW4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
