---
type: protein-evaluation
gene: "TEAD4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEAD4 — REJECTED (研究热度过高 (PubMed strict=340，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEAD4 / RTEF1, TCF13L1, TEF3 |
| 蛋白名称 | Transcriptional enhancer factor TEF-3 |
| 蛋白大小 | 434 aa / 48.3 kDa |
| UniProt ID | Q15561 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 434 aa / 48.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=340 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.2; PDB: 5GZB, 5NO6, 5OAQ, 6GE3, 6GE4, 6GE5, 6GE6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000818, IPR038096, IPR050937, IPR027255, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 340 |
| PubMed broad count | 558 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RTEF1, TCF13L1, TEF3 |

**关键文献**:
1. Inhibition of ferroptosis and iron accumulation alleviates pulmonary fibrosis in a bleomycin model.. *Redox biology*. PMID: 36302319
2. Defining a TFAP2C-centered transcription factor network during murine peri-implantation.. *Developmental cell*. PMID: 38574734
3. Interferon-γ induces tumor resistance to anti-PD-1 immunotherapy by promoting YAP phase separation.. *Molecular cell*. PMID: 33606996
4. TEAD4 functions as a prognostic biomarker and triggers EMT via PI3K/AKT pathway in bladder cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 35581606
5. NR5A2 connects zygotic genome activation to the first lineage segregation in totipotent embryos.. *Cell research*. PMID: 37935903

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 46.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |
| 可用 PDB 条目 | 5GZB, 5NO6, 5OAQ, 6GE3, 6GE4, 6GE5, 6GE6, 6GEC, 6GEE, 6GEG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5GZB, 5NO6, 5OAQ, 6GE3, 6GE4, 6GE5, 6GE6, 6GEC, 6GEE, 6GEG）+ AlphaFold极高置信度预测（pLDDT=75.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000818, IPR038096, IPR050937, IPR027255, IPR016361; Pfam: PF01285, PF17725 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAP1 | 0.999 | 0.992 | — |
| WWTR1 | 0.998 | 0.934 | — |
| VGLL4 | 0.991 | 0.927 | — |
| VGLL1 | 0.985 | 0.888 | — |
| TEAD1 | 0.922 | 0.835 | — |
| TEAD2 | 0.912 | 0.809 | — |
| FAM181A | 0.907 | 0.907 | — |
| FAM181B | 0.901 | 0.900 | — |
| SMAD3 | 0.899 | 0.000 | — |
| MCAT | 0.887 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WWTR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP55 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000352926.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCDC125 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SESTD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VTA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 5GZB, 5NO6, 5OAQ, 6GE3, 6GE4,  | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TEAD4 — Transcriptional enhancer factor TEF-3，研究基础较多，新颖性有限。
2. 蛋白大小434 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 340 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 340 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15561
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197905-TEAD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEAD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15561
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
