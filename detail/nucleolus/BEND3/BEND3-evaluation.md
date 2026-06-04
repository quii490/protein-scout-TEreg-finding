---
type: protein-evaluation
gene: "BEND3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEND3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEND3 / KIAA1553 |
| 蛋白名称 | BEN domain-containing protein 3 |
| 蛋白大小 | 828 aa / 94.5 kDa |
| UniProt ID | Q5T5X7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 828 aa / 94.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 5JNO, 7W27 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018379, IPR033583; Pfam: PF10523 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- heterochromatin (GO:0000792)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 165 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1553 |

**关键文献**:
1. Highly enriched BEND3 prevents the premature activation of bivalent genes during differentiation.. *Science (New York, N.Y.)*. PMID: 35143257
2. Role of Transcription Factor BEND3 and Its Potential Effect on Cancer Progression.. *Cancers*. PMID: 37509346
3. Exosomes activate hippocampal microglia in atrial fibrillation through long-distance heart-brain communication.. *BMC cardiovascular disorders*. PMID: 39516720
4. Bivalent chromatin: a developmental balancing act tipped in cancer.. *Biochemical Society transactions*. PMID: 38385532
5. Integrated Pan-Cancer Profiling and Breast Cancer Validation Identify BEND3 as a Potential Prognostic and Immune Biomarker.. *Breast cancer (Dove Medical Press)*. PMID: 41497890

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 20.7% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 39.6% |
| 有序区域 (pLDDT>70) 占比 | 50.5% |
| 可用 PDB 条目 | 5JNO, 7W27 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 50.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018379, IPR033583; Pfam: PF10523 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERCC6L | 0.912 | 0.900 | — |
| CLDN5 | 0.577 | 0.000 | — |
| USP21 | 0.487 | 0.420 | — |
| MDC1 | 0.483 | 0.439 | — |
| BAZ2A | 0.478 | 0.292 | — |
| NACC2 | 0.465 | 0.045 | — |
| TJP1 | 0.446 | 0.000 | — |
| OCLN | 0.445 | 0.000 | — |
| RTN4IP1 | 0.440 | 0.000 | — |
| ZBTB10 | 0.425 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000411268.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| USP21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SUMO1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| RIOK2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| PDIA6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| MORN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 5JNO, 7W27 | pLDDT=64.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BEND3 — BEN domain-containing protein 3，研究基础较多，新颖性有限。
2. 蛋白大小828 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T5X7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178409-BEND3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEND3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T5X7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
