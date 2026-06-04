---
type: protein-evaluation
gene: "SPANXB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPANXB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPANXB1 / SPANXB, SPANXB2, SPANXF1 |
| 蛋白名称 | Sperm protein associated with the nucleus on the X chromosome B1 |
| 蛋白大小 | 103 aa / 11.8 kDa |
| UniProt ID | Q9NS25 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 103 aa / 11.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010007; Pfam: PF07458 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Uncertain |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPANXB, SPANXB2, SPANXF1 |

**关键文献**:
1. Histone H3.3K27M Mobilizes Multiple Cancer/Testis (CT) Antigens in Pediatric Glioma.. *Molecular cancer research : MCR*. PMID: 29453317
2. Screening and Identification of Novel Potential Biomarkers for Breast Cancer Brain Metastases.. *Frontiers in oncology*. PMID: 35096583
3. Identification of Cancer/Testis Antigens Related to Gastric Cancer Prognosis Based on Co-Expression Network and Integrated Transcriptome Analyses.. *Advanced biomedical research*. PMID: 37057240
4. Evaluating the biological functions of the prognostic genes identified by the Pathology Atlas in bladder cancer.. *Oncology reports*. PMID: 33200223
5. Cancer Testis Antigen Promotes Triple Negative Breast Cancer Metastasis and is Traceable in the Circulating Extracellular Vesicles.. *Scientific reports*. PMID: 31406142

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.0 |
| 高置信度残基 (pLDDT>90) 占比 | 15.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.0% |
| 中等置信 (pLDDT 50-70) 占比 | 31.1% |
| 低置信 (pLDDT<50) 占比 | 21.4% |
| 有序区域 (pLDDT>70) 占比 | 47.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.0），有序残基占 47.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010007; Pfam: PF07458 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPANXA1 | 0.999 | 0.000 | — |
| SPANXC | 0.787 | 0.000 | — |
| LGALS4 | 0.650 | 0.046 | — |
| SRY | 0.571 | 0.000 | — |
| GAGE2E | 0.570 | 0.000 | — |
| ARID4B | 0.468 | 0.462 | — |
| XAGE2 | 0.455 | 0.000 | — |
| GAGE2A | 0.446 | 0.000 | — |
| TP53BP1 | 0.440 | 0.439 | — |
| CTAG1B | 0.421 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| UBL5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNX32 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARID4B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PAPSS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BPGM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HMGCS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.0 + PDB: 无 | pLDDT=68.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPANXB1 — Sperm protein associated with the nucleus on the X chromosome B1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小103 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS25
- Protein Atlas: https://www.proteinatlas.org/ENSG00000227234-SPANXB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS25
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
