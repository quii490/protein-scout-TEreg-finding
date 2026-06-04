---
type: protein-evaluation
gene: "C1orf162"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C1orf162 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C1orf162 |
| 蛋白名称 | Transmembrane protein C1orf162 |
| 蛋白大小 | 155 aa / 16.9 kDa |
| UniProt ID | Q8NEQ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 155 aa / 16.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037763 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Non-alcoholic fatty liver disease and heart failure: A comprehensive bioinformatics and Mendelian randomization analysis.. *ESC heart failure*. PMID: 39143741
2. Identification of hub genes for early detection of bone metastasis in breast cancer.. *Frontiers in endocrinology*. PMID: 36246872
3. Bioinformatics analysis of the genes associated with co-occurrence of heart failure and lung cancer.. *Experimental biology and medicine (Maywood, N.J.)*. PMID: 37073135
4. Exploring the molecular targets and mechanism of S. miltiorrhiza-C. aromatica in treating polycystic ovary syndrome based on network pharmacology.. *Annals of translational medicine*. PMID: 36846000
5. A combination analysis based on bioinformatics tools reveals new signature genes related to maternal obesity and fetal programming.. *Frontiers in medicine*. PMID: 39296904

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 65.2% |
| 低置信 (pLDDT<50) 占比 | 9.0% |
| 有序区域 (pLDDT>70) 占比 | 25.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 25.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037763 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYROBP | 0.676 | 0.000 | — |
| FCER1G | 0.635 | 0.000 | — |
| LILRB2 | 0.613 | 0.000 | — |
| MS4A6A | 0.531 | 0.000 | — |
| HCST | 0.477 | 0.000 | — |
| LST1 | 0.453 | 0.000 | — |
| MS4A7 | 0.450 | 0.000 | — |
| GIMAP4 | 0.426 | 0.000 | — |
| RNF11 | 0.420 | 0.420 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KIAA1143 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRNN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CORO1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MBOAT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 5
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 9 + 5 interactions | 数据充分 |

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
1. C1orf162 — Transmembrane protein C1orf162，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小155 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEQ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143110-C1orf162/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C1orf162
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEQ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
