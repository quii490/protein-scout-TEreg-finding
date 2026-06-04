---
type: protein-evaluation
gene: "DUSP28"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP28 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP28 |
| 蛋白名称 | Dual specificity phosphatase 28 |
| 蛋白大小 | 176 aa / 18.3 kDa |
| UniProt ID | Q4G0W2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 176 aa / 18.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DUSP family phosphatases in cell signaling, inflammation, and chronic diseases.. *J Biomed Sci*. PMID: 42087139
2. Corrigendum to "Scattered DUSP28 is a novel biomarker responsible for aggravating malignancy via the autocrine and paracrine signaling in metastatic pancreatic cancer" [Cancer Lett. 456 (2019 Aug 1) 1-12].. *Cancer Lett*. PMID: 38044256
3. DUSP28 promotes cell proliferation, migration, and invasion by Akt/β-catenin/Slug axis in breast cancer.. *Acta Biochim Pol*. PMID: 36520087
4. Integrated Bioinformatic Analysis Identifies TIPIN as a Prognostic Biomarker in Hepatocellular Carcinoma.. *Dis Markers*. PMID: 35082931
5. Scattered DUSP28 is a novel biomarker responsible for aggravating malignancy via the autocrine and paracrine signaling in metastatic pancreatic cancer.. *Cancer Lett*. PMID: 30902562

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 80.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.1，有序区 83.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AK2 | 0.000 | 0.000 | — |
| ZC3H15 | 0.000 | 0.000 | — |
| METTL22 | 0.000 | 0.000 | — |
| C1QTNF8 | 0.000 | 0.000 | — |
| PMPCA | 0.000 | 0.000 | — |
| WDR33 | 0.000 | 0.000 | — |
| AFG3L2 | 0.000 | 0.000 | — |
| GAB2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q4G0W2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 3
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 无 | pLDDT=90.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 8 + 3 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DUSP28 — Dual specificity phosphatase 28，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4G0W2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188542-DUSP28/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP28
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4G0W2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
