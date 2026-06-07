---
type: protein-evaluation
gene: "GBX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GBX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GBX1 |
| 蛋白名称 | Homeobox protein GBX-1 |
| 蛋白大小 | 363 aa / 37.6 kDa |
| UniProt ID | Q14549 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 363 aa / 37.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.1; PDB: 2M34, 2ME0, 2ME6, 2N8G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042982, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Isolation and expression of the homeobox gene Gbx1 during mouse development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 14745958
2. Cloning and embryonic expression analysis of the mouse Gbx1 gene.. *Gene expression patterns : GEP*. PMID: 12799077
3. De Novo Variant in GBX1 Gene Associated With Developmental Delay and Focal Epilepsy.. *Molecular genetics & genomic medicine*. PMID: 40519143
4. Real-time PCR quantification of gene expression in embryonic mouse tissue.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 24318815
5. Cloning, expression and relationship of zebrafish gbx1 and gbx2 genes to Fgf signaling.. *Mechanisms of development*. PMID: 12963112

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 35.5% |
| 低置信 (pLDDT<50) 占比 | 43.0% |
| 有序区域 (pLDDT>70) 占比 | 21.5% |
| 可用 PDB 条目 | 2M34, 2ME0, 2ME6, 2N8G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.1），有序残基占 21.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042982, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LHX8 | 0.904 | 0.085 | — |
| SOHLH1 | 0.827 | 0.000 | — |
| IQCA1L | 0.554 | 0.045 | — |
| LHX6 | 0.495 | 0.085 | — |
| LHX5 | 0.464 | 0.085 | — |
| ZNF879 | 0.402 | 0.057 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DNAJC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GABPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| QPRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PKMYT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 7
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.1 + PDB: 2M34, 2ME0, 2ME6, 2N8G | pLDDT=59.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 6 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GBX1 — Homeobox protein GBX-1，非常新颖，仅有少数基础研究。
2. 蛋白大小363 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14549
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164900-GBX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GBX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14549
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14549-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14549 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042982;IPR001356;IPR020479;IPR017970;IPR009057; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164900-GBX1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
