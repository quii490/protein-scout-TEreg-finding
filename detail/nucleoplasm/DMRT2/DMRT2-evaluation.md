---
type: protein-evaluation
gene: "DMRT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMRT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMRT2 / DSXL2 |
| 蛋白名称 | Doublesex- and mab-3-related transcription factor 2 |
| 蛋白大小 | 561 aa / 61.8 kDa |
| UniProt ID | Q9Y5R5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; 额外: Vesicles, Centriolar satellite; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 561 aa / 61.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001275, IPR036407, IPR026607; Pfam: PF00751 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Vesicles, Centriolar satellite | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 140 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DSXL2 |

**关键文献**:
1. Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40354537
2. Dmrt2 promotes transition of endochondral bone formation by linking Sox9 and Runx2.. *Communications biology*. PMID: 33707608
3. Hmx2 and Dmrt2 Coordinate the Differentiation of Intercalated Cell Subtypes in Kidney.. *Journal of the American Society of Nephrology : JASN*. PMID: 41051882
4. Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.. *medRxiv : the preprint server for health sciences*. PMID: 40196253
5. The human doublesex-related gene, DMRT2, is homologous to a gene involved in somitogenesis and encodes a potential bicistronic transcript.. *Genomics*. PMID: 10729224

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.9 |
| 高置信度残基 (pLDDT>90) 占比 | 9.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 25.1% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 18.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.9），有序残基占 18.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001275, IPR036407, IPR026607; Pfam: PF00751 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRY | 0.808 | 0.070 | — |
| DMRT3 | 0.582 | 0.000 | — |
| ZFY | 0.514 | 0.059 | — |
| HNRNPUL2 | 0.506 | 0.095 | — |
| FOXL2 | 0.500 | 0.068 | — |
| KANK1 | 0.499 | 0.044 | — |
| NR0B1 | 0.461 | 0.049 | — |
| ASB18 | 0.453 | 0.044 | — |
| RPL7 | 0.445 | 0.095 | — |
| ACTB | 0.439 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TLE5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGED1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.9 + PDB: 无 | pLDDT=53.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli; 额外: Vesicles, Centriolar sa | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DMRT2 — Doublesex- and mab-3-related transcription factor 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小561 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5R5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173253-DMRT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMRT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5R5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173253-DMRT2/subcellular

![](https://images.proteinatlas.org/3498/1931_F3_5_red_green.jpg)
![](https://images.proteinatlas.org/3498/1931_F3_6_red_green.jpg)
![](https://images.proteinatlas.org/3498/1976_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/3498/1976_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/3498/2030_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/3498/2030_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5R5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
