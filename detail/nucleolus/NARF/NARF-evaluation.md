---
type: protein-evaluation
gene: "NARF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NARF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NARF |
| 蛋白名称 | Nuclear prelamin A recognition factor |
| 蛋白大小 | 456 aa / 51.2 kDa |
| UniProt ID | Q9UHQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 456 aa / 51.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050340, IPR009016, IPR004108, IPR003149; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- lamin filament (GO:0005638)
- nuclear lamina (GO:0005652)
- nuclear lumen (GO:0031981)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of susceptibility modules and characteristic genes to osteoarthritis by WGCNA.. *Annales de biologie clinique*. PMID: 39297544
2. Molecular cloning and characterization of neural activity-related RING finger protein (NARF): a new member of the RBCC family is a candidate for the partner of myosin V.. *Journal of neurochemistry*. PMID: 11432975
3. Nuclear prelamin a recognition factor and iron dysregulation in multiple sclerosis.. *Metabolic brain disease*. PMID: 31823109
4. Prenylated prelamin A interacts with Narf, a novel nuclear protein.. *The Journal of biological chemistry*. PMID: 10514485
5. Classification of subtypes and identification of dysregulated genes in sepsis.. *Frontiers in cellular and infection microbiology*. PMID: 37671148

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.8 |
| 高置信度残基 (pLDDT>90) 占比 | 65.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 12.3% |
| 有序区域 (pLDDT>70) 占比 | 82.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.8，有序区 82.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050340, IPR009016, IPR004108, IPR003149; Pfam: PF02906, PF02256 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMNA | 0.715 | 0.292 | — |
| EGLN1 | 0.653 | 0.000 | — |
| FDX1 | 0.604 | 0.487 | — |
| FDX2 | 0.597 | 0.487 | — |
| CIAO1 | 0.573 | 0.184 | — |
| NUBP1 | 0.568 | 0.288 | — |
| CIAPIN1 | 0.523 | 0.094 | — |
| MMS19 | 0.523 | 0.292 | — |
| LEF1 | 0.514 | 0.510 | — |
| NUBP2 | 0.512 | 0.288 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RGS20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DTX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CIAO3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CIAO2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCNO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NAA11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NUBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NAA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.8 + PDB: 无 | pLDDT=83.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NARF — Nuclear prelamin A recognition factor，非常新颖，仅有少数基础研究。
2. 蛋白大小456 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHQ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141562-NARF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NARF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHQ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000141562-NARF/subcellular

![](https://images.proteinatlas.org/53006/1208_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/53006/1208_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/53006/833_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/53006/833_C7_3_red_green.jpg)
![](https://images.proteinatlas.org/53006/871_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/53006/871_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHQ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHQ1 |
| SMART | SM00902; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050340;IPR009016;IPR004108;IPR003149; |
| Pfam | PF02906;PF02256; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141562-NARF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LEF1 | Biogrid | false |
| LMNA | Biogrid | false |
| PRKN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
