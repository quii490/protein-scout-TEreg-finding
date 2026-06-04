---
type: protein-evaluation
gene: "KLLN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLLN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLLN |
| 蛋白名称 | Killin |
| 蛋白大小 | 178 aa / 20.0 kDa |
| UniProt ID | B2CW77 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 178 aa / 20.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.9; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. EBF2 Links KMT2D-Mediated H3K4me1 to Suppress Pancreatic Cancer Progression via Upregulating KLLN.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38015024
2. Cancer-predisposition gene KLLN maintains pericentric H3K9 trimethylation protecting genomic stability.. *Nucleic acids research*. PMID: 26673699
3. KSRP modulates melanoma growth and efficacy of vemurafenib.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 31269460
4. Germline and somatic KLLN alterations in breast cancer dysregulate G2 arrest.. *Human molecular genetics*. PMID: 23446638
5. Germline PTEN, SDHB-D, and KLLN alterations in endometrial cancer patients with Cowden and Cowden-like syndromes: an international, multicenter, prospective study.. *Cancer*. PMID: 25376524

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.6% |
| 中等置信 (pLDDT 50-70) 占比 | 53.9% |
| 低置信 (pLDDT<50) 占比 | 45.5% |
| 有序区域 (pLDDT>70) 占比 | 0.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.9），有序残基占 0.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTEN | 0.516 | 0.000 | — |
| SEC23B | 0.507 | 0.000 | — |
| SLC16A12 | 0.473 | 0.000 | — |
| SDHB | 0.437 | 0.000 | — |
| SLITRK6 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 5，IntAct interactions: 0
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.9 + PDB: 无 | pLDDT=50.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 5 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KLLN — Killin，非常新颖，仅有少数基础研究。
2. 蛋白大小178 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=50.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B2CW77
- Protein Atlas: https://www.proteinatlas.org/ENSG00000227268-KLLN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLLN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2CW77
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
