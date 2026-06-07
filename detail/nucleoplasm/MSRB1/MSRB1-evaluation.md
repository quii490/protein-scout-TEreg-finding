---
type: protein-evaluation
gene: "MSRB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MSRB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSRB1 |
| 蛋白名称 | MSRB1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | MSRB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=75 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 75 |
| PubMed broad count | 160 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Shikonin attenuates acetaminophen-induced acute liver injury via inhibition of oxidative stress and inflammation.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 30818140
2. Regulation of protein function by reversible methionine oxidation and the role of selenoprotein MsrB1.. *Antioxidants & redox signaling*. PMID: 26181576
3. The selenoprotein methionine sulfoxide reductase B1 (MSRB1).. *Free radical biology & medicine*. PMID: 36084791
4. Transcription factor KLF5 regulates MsrB1 to promote colorectal cancer progression by inhibiting ferroptosis through β-catenin.. *Free radical biology & medicine*. PMID: 40210135
5. Effect of Exogenous Zinc on MsrB1 Expression and Protein Oxidation in Human Lens Epithelial Cells.. *Biological trace element research*. PMID: 30306419

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MSRA | 0.910 | 0.075 | — |
| SELENOK | 0.865 | 0.000 | — |
| SELENOO | 0.862 | 0.000 | — |
| SELENOT | 0.837 | 0.000 | — |
| GPX3 | 0.830 | 0.000 | — |
| GPX2 | 0.828 | 0.000 | — |
| SEPHS2 | 0.812 | 0.000 | — |
| TXNRD2 | 0.811 | 0.000 | — |
| SELENOS | 0.802 | 0.000 | — |
| GPX7 | 0.800 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Psat | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM27 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| IFT88 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| "BcDNA:AT27976" | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| ENST00000361871 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. MSRB1 — MSRB1 (UniProt未获取)，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 75 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/MSRB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198736-MSRB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSRB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/MSRB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000198736-MSRB1/subcellular

![](https://images.proteinatlas.org/43463/738_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/43463/738_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/43463/750_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/43463/750_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/43463/864_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/43463/864_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZV6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..106; /note="MsrB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01126" |
| InterPro | IPR002579;IPR052150;IPR011057; |
| Pfam | PF01641; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198736-MSRB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLU | Biogrid | false |
| CYSRT1 | Intact | false |
| IFT88 | Intact | false |
| INCA1 | Intact | false |
| TRIM27 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
