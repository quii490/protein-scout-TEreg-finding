---
type: protein-evaluation
gene: "NDUFA9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NDUFA9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NDUFA9 / NDUFS2L |
| 蛋白名称 | NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 9, mitochondrial |
| 蛋白大小 | 377 aa / 42.5 kDa |
| UniProt ID | Q16795 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Mitochondrion matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 42.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.6; PDB: 5XTB, 5XTD, 5XTH, 5XTI, 9CWT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051207, IPR001509, IPR036291; Pfam: PF01370 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial matrix (GO:0005759)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- respiratory chain complex I (GO:0045271)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 107 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NDUFS2L |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. Autophagy deficiency abolishes liver mitochondrial DNA segregation.. *Autophagy*. PMID: 35220898
3. NDUFA9 and its crotonylation modification promote browning of white adipocytes by activating mitochondrial function in mice.. *The international journal of biochemistry & cell biology*. PMID: 38657899
4. Gene knockout using transcription activator-like effector nucleases (TALENs) reveals that human NDUFA9 protein is essential for stabilizing the junction between membrane and matrix arms of complex I.. *The Journal of biological chemistry*. PMID: 23223238
5. Proteomic Analysis Reveals Oxidative Phosphorylation and JAK-STAT Pathways Mediated Pathogenesis of Pemphigus Vulgaris.. *Experimental dermatology*. PMID: 39373252

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 84.9% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 8.8% |
| 有序区域 (pLDDT>70) 占比 | 90.7% |
| 可用 PDB 条目 | 5XTB, 5XTD, 5XTH, 5XTI, 9CWT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5XTB, 5XTD, 5XTH, 5XTI, 9CWT）+ AlphaFold极高置信度预测（pLDDT=89.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051207, IPR001509, IPR036291; Pfam: PF01370 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFV3 | 0.999 | 0.998 | — |
| NDUFB10 | 0.999 | 0.999 | — |
| NDUFA2 | 0.999 | 0.999 | — |
| NDUFS2 | 0.999 | 0.999 | — |
| NDUFS5 | 0.999 | 0.998 | — |
| UQCR10 | 0.999 | 0.998 | — |
| NDUFA8 | 0.999 | 0.991 | — |
| NDUFA10 | 0.999 | 0.998 | — |
| NDUFS8 | 0.999 | 0.999 | — |
| NDUFB6 | 0.999 | 0.943 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tsp42Ej | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10927 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| alphaTub84D | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PolH | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CIAO1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGED1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| MME | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17342744 |
| NDUFS2 | psi-mi:"MI:0276"(blue native page) | pubmed:15250827 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 5XTB, 5XTD, 5XTH, 5XTI, 9CWT | pLDDT=89.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NDUFA9 — NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 9, mitochondrial，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16795
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139180-NDUFA9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NDUFA9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16795
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000139180-NDUFA9/subcellular

![](https://images.proteinatlas.org/73212/1398_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/73212/1398_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/73212/1403_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/73212/1403_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/73212/1475_H10_3_red_green.jpg)
![](https://images.proteinatlas.org/73212/1475_H10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16795-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
