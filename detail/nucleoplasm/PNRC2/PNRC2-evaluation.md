---
type: protein-evaluation
gene: "PNRC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PNRC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PNRC2 |
| 蛋白名称 | Proline-rich nuclear receptor coactivator 2 |
| 蛋白大小 | 139 aa / 15.6 kDa |
| UniProt ID | Q9NPJ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Nucleus; Cytoplasm, P-body |
| 蛋白大小 | 8/10 | ×1 | 8 | 139 aa / 15.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 4B6H, 5KQ1, 5KQ4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028322, IPR026780; Pfam: PF15365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Cytoplasm, P-body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- P-body (GO:0000932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nuclear receptor coactivator PNRC2 regulates energy expenditure and adiposity.. *The Journal of biological chemistry*. PMID: 17971453
2. Pnrc2 promotes rapid mRNA decay and coordinately supports early development with P-body factors Ddx6 and Ddx61.. *bioRxiv : the preprint server for biology*. PMID: 40463158
3. Pumilio response and AU-rich elements drive rapid decay of Pnrc2-regulated cyclic gene transcripts.. *Developmental biology*. PMID: 32246943
4. Dissecting the functions of SMG5, SMG7, and PNRC2 in nonsense-mediated mRNA decay of human cells.. *RNA (New York, N.Y.)*. PMID: 29348139
5. Structural basis of the PNRC2-mediated link between mrna surveillance and decapping.. *Structure (London, England : 1993)*. PMID: 23085078

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 18.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 58.3% |
| 低置信 (pLDDT<50) 占比 | 9.4% |
| 有序区域 (pLDDT>70) 占比 | 32.4% |
| 可用 PDB 条目 | 4B6H, 5KQ1, 5KQ4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 32.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028322, IPR026780; Pfam: PF15365 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCP1A | 0.999 | 0.986 | — |
| UPF1 | 0.981 | 0.292 | — |
| SMG5 | 0.974 | 0.000 | — |
| DCP2 | 0.934 | 0.777 | — |
| ESRRG | 0.912 | 0.422 | — |
| SMG7 | 0.891 | 0.000 | — |
| SMG6 | 0.853 | 0.000 | — |
| SMG8 | 0.842 | 0.000 | — |
| COMMD7 | 0.827 | 0.000 | — |
| UPF2 | 0.827 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DCP1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BANP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ESRRG | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GALK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ELAVL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EDC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DCP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 4B6H, 5KQ1, 5KQ4 | pLDDT=67.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, P-body / Nucleoplasm; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PNRC2 — Proline-rich nuclear receptor coactivator 2，非常新颖，仅有少数基础研究。
2. 蛋白大小139 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPJ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189266-PNRC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PNRC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPJ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPJ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000189266-PNRC2/subcellular

![](https://images.proteinatlas.org/45837/737_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/45837/737_F4_4_red_green.jpg)
![](https://images.proteinatlas.org/45837/763_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/45837/763_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/45837/837_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/45837/837_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
