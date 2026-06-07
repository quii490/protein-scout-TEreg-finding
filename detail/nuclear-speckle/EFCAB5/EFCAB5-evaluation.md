---
type: protein-evaluation
gene: "EFCAB5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFCAB5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFCAB5 |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 5 |
| 蛋白大小 | 1503 aa / 173.4 kDa |
| UniProt ID | A4FU69 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1503 aa / 173.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018247, IPR002048, IPR029016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic architecture of epigenetic and neuronal ageing rates in human brain regions.. *Nature communications*. PMID: 28516910
2. Clinical implications and molecular mechanism of long noncoding RNA LINC00518 and protein-coding genes in skin cutaneous melanoma by genome‑wide investigation.. *Archives of dermatological research*. PMID: 39987414
3. Gene-Set Enrichment Analysis for Identifying Genes and Biological Activities Associated with Growth Traits in Dromedaries.. *Animals : an open access journal from MDPI*. PMID: 35049806
4. Proximity labeling of axonemal protein CFAP91 identifies EFCAB5 that regulates sperm motility.. *Nature communications*. PMID: 40931011

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.7 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 43.7% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 27.6% |
| 有序区域 (pLDDT>70) 占比 | 62.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.7），有序残基占 62.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018247, IPR002048, IPR029016 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NSRP1 | 0.725 | 0.000 | — |
| NPHP3-ACAD11 | 0.546 | 0.054 | — |
| CCDC116 | 0.511 | 0.000 | — |
| TOR2A | 0.456 | 0.000 | — |
| ERICH6 | 0.449 | 0.000 | — |
| C6orf226 | 0.447 | 0.000 | — |
| WDR90 | 0.438 | 0.229 | — |
| CCDC105 | 0.438 | 0.123 | — |
| OPRM1 | 0.426 | 0.000 | — |
| TCF23 | 0.423 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.7 + PDB: 无 | pLDDT=67.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies; 额外: Mitochondria | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. EFCAB5 — EF-hand calcium-binding domain-containing protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1503 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4FU69
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176927-EFCAB5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFCAB5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4FU69
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000176927-EFCAB5/subcellular

![](https://images.proteinatlas.org/22852/1364_H7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22852/1364_H7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/22852/195_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22852/195_B1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22852/197_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22852/197_B1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A4FU69-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A4FU69 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 869..904; /note="EF-hand"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR018247;IPR002048;IPR029016; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176927-EFCAB5/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
