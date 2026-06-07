---
type: protein-evaluation
gene: "BCORL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BCORL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCORL1 |
| 蛋白名称 | BCL-6 corepressor-like protein 1 |
| 蛋白大小 | 1785 aa / 190.6 kDa |
| UniProt ID | Q5H9F3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1785 aa / 190.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=38.5; PDB: 4HPM, 5JH5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR047144, IPR032365, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 161 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Clinical and Molecular Determinants of Clonal Evolution in Aplastic Anemia and Paroxysmal Nocturnal Hemoglobinuria.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 36054881
2. Impact of myelodysplasia-related gene mutations and residual mutations at remission in venetoclax/azacitidine for AML.. *Leukemia*. PMID: 40259101
3. BCOR gene alterations in hematologic diseases.. *Blood*. PMID: 33945606
4. BCOR, BCORL1, and BCL6 Mutations in Pediatric Leukemias.. *Cancers*. PMID: 40805145
5. Novel and recurrent hemizygous variants in BCORL1 cause oligoasthenoteratozoospermia by interfering transcription.. *Andrology*. PMID: 39189935

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 38.5 |
| 高置信度残基 (pLDDT>90) 占比 | 5.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 87.2% |
| 有序区域 (pLDDT>70) 占比 | 11.4% |
| 可用 PDB 条目 | 4HPM, 5JH5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=38.5），有序残基占 11.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR047144, IPR032365, IPR038227; Pfam: PF12796, PF16553 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCGF1 | 0.996 | 0.984 | — |
| KDM2B | 0.988 | 0.943 | — |
| SKP1 | 0.966 | 0.881 | — |
| RYBP | 0.920 | 0.819 | — |
| YAF2 | 0.908 | 0.780 | — |
| CTBP1 | 0.901 | 0.642 | — |
| PCGF3 | 0.838 | 0.765 | — |
| RING1 | 0.830 | 0.363 | — |
| PCGF2 | 0.806 | 0.761 | — |
| RNF2 | 0.800 | 0.626 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCGF1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-25601|pubmed:27505670 |
| FBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCGF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCGF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RYBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BAG4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCGF3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| PCGF5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=38.5 + PDB: 4HPM, 5JH5 | pLDDT=38.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. BCORL1 — BCL-6 corepressor-like protein 1，研究基础较多，新颖性有限。
2. 蛋白大小1785 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=38.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5H9F3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000085185-BCORL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCORL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5H9F3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000085185-BCORL1/subcellular

![](https://images.proteinatlas.org/68568/1469_F10_5_red_green.jpg)
![](https://images.proteinatlas.org/68568/1469_F10_7_red_green.jpg)
![](https://images.proteinatlas.org/68568/1478_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/68568/1478_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/68568/1520_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/68568/1520_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5H9F3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5H9F3 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR047144;IPR032365;IPR038227; |
| Pfam | PF12796;PF16553; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000085185-BCORL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX6 | Biogrid | false |
| CTBP1 | Biogrid | false |
| KLF15 | Biogrid | false |
| PCGF1 | Biogrid | false |
| PCGF2 | Biogrid | false |
| PCGF3 | Biogrid | false |
| PCGF5 | Biogrid | false |
| PCGF6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
