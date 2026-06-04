---
type: protein-evaluation
gene: "PAGE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAGE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAGE1 / GAGE9, GAGEB1 |
| 蛋白名称 | P antigen family member 1 |
| 蛋白大小 | 146 aa / 16.1 kDa |
| UniProt ID | O75459 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 146 aa / 16.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031320, IPR008625; Pfam: PF05831 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GAGE9, GAGEB1 |

**关键文献**:
1. Expression of cancer-testis antigens in the immune microenvironment of non-small cell lung cancer.. *Molecular oncology*. PMID: 37341056
2. Identification of a seven-gene signature predicting clinical outcome of liver cancer based on tumor mutational burden.. *Human cell*. PMID: 35622212
3. m(1)A regulator-mediated methylation modification patterns correlated with autophagy to predict the prognosis of hepatocellular carcinoma.. *BMC cancer*. PMID: 38649860
4. A radiation-induced gene signature distinguishes post-Chernobyl from sporadic papillary thyroid cancers.. *Radiation research*. PMID: 18088181
5. Development and evaluation of a risk score model based on a WNT score gene-associated signature for predicting the clinical outcome and the tumour microenvironment of hepatocellular carcinoma.. *International journal of immunopathology and pharmacology*. PMID: 38054921

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 95.2% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 2.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 2.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031320, IPR008625; Pfam: PF05831 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAGE2 | 0.946 | 0.000 | — |
| KLK3 | 0.678 | 0.000 | — |
| MAGEA1 | 0.545 | 0.000 | — |
| EFNA5 | 0.541 | 0.000 | — |
| GAGE12F | 0.512 | 0.000 | — |
| MAGEC2 | 0.492 | 0.000 | — |
| MAGEB2 | 0.470 | 0.000 | — |
| MAGEA12 | 0.467 | 0.000 | — |
| CTAG2 | 0.464 | 0.000 | — |
| PAGE5 | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TMEM60 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC1A1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TFRC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DDX49 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC2A5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM254 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLPP4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MGST3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 无 | pLDDT=60.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center; 额外: Nucleoplasm, Mitoch | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PAGE1 — P antigen family member 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小146 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75459
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068985-PAGE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAGE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75459
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
