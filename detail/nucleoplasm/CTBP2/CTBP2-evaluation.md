---
type: protein-evaluation
gene: "CTBP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTBP2 — REJECTED (研究热度过高 (PubMed strict=268，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTBP2 |
| 蛋白名称 | C-terminal-binding protein 2 |
| 蛋白大小 | 445 aa / 48.9 kDa |
| UniProt ID | P56545 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Synapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 445 aa / 48.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=268 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.4; PDB: 2OME, 4LCJ, 6WKW, 8ATI |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043322, IPR051638, IPR006139, IPR029753, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Synapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- synapse (GO:0045202)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 268 |
| PubMed broad count | 442 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Increased mitophagy protects cochlear hair cells from aminoglycoside-induced damage.. *Autophagy*. PMID: 35471096
2. Garcinia cambogia attenuates adipogenesis by affecting CEBPB and SQSTM1/p62-mediated selective autophagic degradation of KLF3 through RPS6KA1 and STAT3 suppression.. *Autophagy*. PMID: 34101546
3. Oncogene EVI1 drives acute myeloid leukemia via a targetable interaction with CTBP2.. *Science advances*. PMID: 38748792
4. CTBP1 and CTBP2 mutations underpinning neurological disorders: a systematic review.. *Neurogenetics*. PMID: 36331689
5. CtBP1/2 oligomerization promotes G9a-Mediated transcriptional repression.. *The Journal of biological chemistry*. PMID: 41419197

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 73.9% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 74.3% |
| 可用 PDB 条目 | 2OME, 4LCJ, 6WKW, 8ATI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2OME, 4LCJ, 6WKW, 8ATI）+ AlphaFold高质量预测（pLDDT=83.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043322, IPR051638, IPR006139, IPR029753, IPR006140; Pfam: PF00389, PF02826 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTBP1 | 0.999 | 0.895 | — |
| RBBP8 | 0.996 | 0.420 | — |
| ZEB1 | 0.989 | 0.818 | — |
| ZNF217 | 0.989 | 0.836 | — |
| KLF3 | 0.988 | 0.613 | — |
| HDAC2 | 0.980 | 0.509 | — |
| HDAC1 | 0.974 | 0.331 | — |
| KLF8 | 0.968 | 0.386 | — |
| TCF7 | 0.965 | 0.131 | — |
| MECOM | 0.958 | 0.070 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000357816.5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NRIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TEAD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NOL4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AKTIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAI2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TGIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BAZ2B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCNH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| BCL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 2OME, 4LCJ, 6WKW, 8ATI | pLDDT=83.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Synapse / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTBP2 — C-terminal-binding protein 2，研究基础较多，新颖性有限。
2. 蛋白大小445 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 268 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 268 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56545
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175029-CTBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56545
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000175029-CTBP2/subcellular

![](https://images.proteinatlas.org/31916/950_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/31916/950_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56545-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P56545 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043322;IPR051638;IPR006139;IPR029753;IPR006140;IPR036291; |
| Pfam | PF00389;PF02826; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175029-CTBP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCL3 | Intact, Biogrid | true |
| CCNH | Intact, Biogrid | true |
| CTBP1 | Intact, Biogrid, Opencell | true |
| DCAF7 | Biogrid, Opencell | true |
| EP300 | Biogrid, Opencell | true |
| FHL3 | Intact, Biogrid | true |
| FOXP2 | Intact, Biogrid | true |
| HDAC1 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
