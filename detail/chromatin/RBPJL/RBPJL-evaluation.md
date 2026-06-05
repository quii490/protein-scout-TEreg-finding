---
type: protein-evaluation
gene: "RBPJL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RBPJL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RBPJL / RBPL, RBPSUHL |
| 蛋白名称 | Recombining binding protein suppressor of hairless-like protein |
| 蛋白大小 | 517 aa / 56.8 kDa |
| UniProt ID | Q9UBG7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 517 aa / 56.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015350, IPR036358, IPR040159, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

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
- transcription regulator complex (GO:0005667)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RBPL, RBPSUHL |

**关键文献**:
1. Deciphering distinct genetic risk factors for FTLD-TDP pathological subtypes via whole-genome sequencing.. *Nature communications*. PMID: 40280976
2. Fam102a translocates Runx2 and Rbpjl to facilitate Osterix expression and bone formation.. *Nature communications*. PMID: 39747056
3. Transcription factor Ptf1a in development, diseases and reprogramming.. *Cellular and molecular life sciences : CMLS*. PMID: 30470852
4. Early pancreatic development requires the vertebrate Suppressor of Hairless (RBPJ) in the PTF1 bHLH complex.. *Genes & development*. PMID: 17938243
5. Deciphering Distinct Genetic Risk Factors for FTLD-TDP Pathological Subtypes via Whole-Genome Sequencing.. *medRxiv : the preprint server for health sciences*. PMID: 38978643

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 52.4% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 76.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 76.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015350, IPR036358, IPR040159, IPR013783, IPR014756; Pfam: PF09270, PF09271, PF20144 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTF1A | 0.994 | 0.331 | — |
| MAML1 | 0.975 | 0.000 | — |
| MAML2 | 0.959 | 0.000 | — |
| NOTCH2 | 0.950 | 0.289 | — |
| NOTCH3 | 0.949 | 0.289 | — |
| MAML3 | 0.946 | 0.000 | — |
| NOTCH1 | 0.942 | 0.133 | — |
| CIR1 | 0.937 | 0.080 | — |
| NOTCH4 | 0.933 | 0.133 | — |
| RBPJ | 0.930 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PCDH7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DNAJB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BORA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CELSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Tlx3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RBPJL — Recombining binding protein suppressor of hairless-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小517 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBG7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124232-RBPJL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RBPJL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBG7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UBG7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
