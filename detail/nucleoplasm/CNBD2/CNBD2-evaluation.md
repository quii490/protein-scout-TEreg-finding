---
type: protein-evaluation
gene: "CNBD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNBD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNBD2 / C20orf152 |
| 蛋白名称 | Cyclic nucleotide-binding domain-containing protein 2 |
| 蛋白大小 | 576 aa / 67.5 kDa |
| UniProt ID | Q96M20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Mid piece; 额外: Actin filaments, Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 576 aa / 67.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018488, IPR000595, IPR018490, IPR014710; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mid piece; 额外: Actin filaments, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf152 |

**关键文献**:
1. Morphological Observation and Transcriptome Analysis of Ciliogenesis in Urechis unicinctus (Annelida, Echiura).. *International journal of molecular sciences*. PMID: 37511295

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 19.4% |
| 置信残基 (pLDDT 70-90) 占比 | 38.5% |
| 中等置信 (pLDDT 50-70) 占比 | 18.4% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 57.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 57.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018488, IPR000595, IPR018490, IPR014710; Pfam: PF00027 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KIAA1191 | 0.585 | 0.000 | — |
| CNBD1 | 0.549 | 0.000 | — |
| IQCF1 | 0.539 | 0.000 | — |
| EPB41L1 | 0.528 | 0.000 | — |
| EXOSC8 | 0.493 | 0.494 | — |
| TERB1 | 0.478 | 0.000 | — |
| KLHL10 | 0.467 | 0.000 | — |
| TMEM109 | 0.461 | 0.000 | — |
| POLR2F | 0.456 | 0.412 | — |
| TOPAZ1 | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 无 | pLDDT=69.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoli, Mid piece; 额外: Actin filaments, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CNBD2 — Cyclic nucleotide-binding domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小576 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96M20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149646-CNBD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNBD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96M20
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000149646-CNBD2/subcellular

![](https://images.proteinatlas.org/43182/1916_G2_11_cr5c99eee7e7231_blue_red_green.jpg)
![](https://images.proteinatlas.org/43182/1916_G2_6_cr5c99eee7e67c6_blue_red_green.jpg)
![](https://images.proteinatlas.org/43182/1917_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43182/1917_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43182/2195_H1_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/43182/2195_H1_30_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96M20-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96M20 |
| SMART | SM00100; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018488;IPR000595;IPR018490;IPR014710; |
| Pfam | PF00027; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149646-CNBD2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
