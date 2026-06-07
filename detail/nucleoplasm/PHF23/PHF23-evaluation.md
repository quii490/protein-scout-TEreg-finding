---
type: protein-evaluation
gene: "PHF23"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHF23 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHF23 |
| 蛋白名称 | PHD finger protein 23 |
| 蛋白大小 | 403 aa / 43.8 kDa |
| UniProt ID | Q9BUL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 403 aa / 43.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.3; PDB: 6WXK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011011, IPR001965, IPR019787, IPR013083; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mitophagy in degenerative joint diseases.. *Autophagy*. PMID: 32967533
2. The phenylalanine-and-glycine repeats of NUP98 oncofusions form condensates that selectively partition transcriptional coactivators.. *Molecular cell*. PMID: 39922194
3. Dual mechanism of autophagy gene repression by PHF23 and therapeutic potential of its inhibition in protein aggregation disorders.. *Nucleic acids research*. PMID: 41359382
4. Structure, function, and pathology of PHF23.. *Frontiers in cell and developmental biology*. PMID: 41268576
5. An Epigenetic Mechanism Underlying Chromosome 17p Deletion-Driven Tumorigenesis.. *Cancer discovery*. PMID: 32978226

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.3 |
| 高置信度残基 (pLDDT>90) 占比 | 14.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 45.2% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 21.6% |
| 可用 PDB 条目 | 6WXK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.3），有序残基占 21.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011011, IPR001965, IPR019787, IPR013083; Pfam: PF13831 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRSAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRSS23 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1D | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SIN3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAP30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARID4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BRMS1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIN3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAP130 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUDS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.3 + PDB: 6WXK | pLDDT=60.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PHF23 — PHD finger protein 23，非常新颖，仅有少数基础研究。
2. 蛋白大小403 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000040633-PHF23/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF23
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF23/IF_images/PHF23_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000040633-PHF23/subcellular

![](https://images.proteinatlas.org/52410/783_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/52410/783_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/52410/785_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/52410/785_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/52410/868_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/52410/868_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BUL5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BUL5 |
| SMART | SM00249; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF13831; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000040633-PHF23/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASP6 | Intact | false |
| CYCS | Intact | false |
| FGFR3 | Intact | false |
| GSN | Intact | false |
| HCCS | Biogrid | false |
| HDAC1 | Opencell | false |
| HRAS | Intact | false |
| KLF11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
