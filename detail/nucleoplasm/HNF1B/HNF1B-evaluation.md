---
type: protein-evaluation
gene: "HNF1B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HNF1B — REJECTED (研究热度过高 (PubMed strict=499，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HNF1B / TCF2 |
| 蛋白名称 | Hepatocyte nuclear factor 1-beta |
| 蛋白大小 | 557 aa / 61.3 kDa |
| UniProt ID | P35680 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 557 aa / 61.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=499 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 2DA6, 2H8R, 5K9S |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR039066, IPR006899, IPR044869, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 499 |
| PubMed broad count | 1531 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF2 |

**关键文献**:
1. HNF1B-associated renal and extra-renal disease-an expanding clinical spectrum.. *Nature reviews. Nephrology*. PMID: 25536396
2. A single-cell multiomic analysis of kidney organoid differentiation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37155865
3. Genetics of Mayer-Rokitansky-Küster-Hauser (MRKH) syndrome: advancements and implications.. *Frontiers in endocrinology*. PMID: 38699388
4. Statistical evidence for high-penetrance MODY-causing genes in a large population-based cohort.. *Endocrinology, diabetes & metabolism*. PMID: 36208030
5. Single-Cell Transcriptomics Reveals a Conserved Metaplasia Program in Pancreatic Injury.. *Gastroenterology*. PMID: 34695382

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 26.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 57.3% |
| 有序区域 (pLDDT>70) 占比 | 36.3% |
| 可用 PDB 条目 | 2DA6, 2H8R, 5K9S |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 36.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR039066, IPR006899, IPR044869, IPR023219; Pfam: PF04814, PF04812 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HNF1A | 0.961 | 0.805 | — |
| ONECUT1 | 0.956 | 0.000 | — |
| PCBD1 | 0.892 | 0.771 | — |
| PTF1A | 0.891 | 0.000 | — |
| PKHD1 | 0.852 | 0.000 | — |
| HNF4A | 0.851 | 0.085 | — |
| UMOD | 0.805 | 0.045 | — |
| PDX1 | 0.803 | 0.000 | — |
| NEUROD1 | 0.762 | 0.000 | — |
| GCK | 0.759 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ribF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VAC14 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OTX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BPIFA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OXER1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UFSP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MLLT10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C10orf55 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP26-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USP54 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 2DA6, 2H8R, 5K9S | pLDDT=60.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HNF1B — Hepatocyte nuclear factor 1-beta，研究基础较多，新颖性有限。
2. 蛋白大小557 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 499 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 499 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35680
- Protein Atlas: https://www.proteinatlas.org/ENSG00000275410-HNF1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HNF1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35680
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000275410-HNF1B/subcellular

![](https://images.proteinatlas.org/2083/1032_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/2083/1032_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/2083/1842_B2_93_red_green.jpg)
![](https://images.proteinatlas.org/2083/1842_B2_94_red_green.jpg)
![](https://images.proteinatlas.org/2083/2145_E7_31_red_green.jpg)
![](https://images.proteinatlas.org/2083/2145_E7_53_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35680-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
