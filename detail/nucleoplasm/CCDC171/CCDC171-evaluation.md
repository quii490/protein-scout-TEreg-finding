---
type: protein-evaluation
gene: "CCDC171"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC171 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC171 / C9orf93 |
| 蛋白名称 | Coiled-coil domain-containing protein 171 |
| 蛋白大小 | 1326 aa / 152.8 kDa |
| UniProt ID | Q6TFL3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1326 aa / 152.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038820 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf93 |

**关键文献**:
1. Integrative multi-omics analysis deciphers the regulatory mechanisms of egg weight traits in chickens.. *Poultry science*. PMID: 40961765
2. Investigating the shared genetic architecture between attention-deficit/hyperactivity disorder and risk taking behavior: A large-scale genomewide cross-trait analysis.. *Journal of affective disorders*. PMID: 38565336
3. Gene-diet interaction effects on BMI levels in the Singapore Chinese population.. *Nutrition journal*. PMID: 29477148
4. Identification and functional validation of genetic variants in potential miRNA target sites of established BMI genes.. *International journal of obesity (2005)*. PMID: 31745258
5. Germline polymorphisms in an enhancer of PSIP1 are associated with progression-free survival in epithelial ovarian cancer.. *Oncotarget*. PMID: 26840454

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 3.5% |
| 置信残基 (pLDDT 70-90) 占比 | 60.8% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 17.4% |
| 有序区域 (pLDDT>70) 占比 | 64.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.2，有序区 64.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038820 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTC39B | 0.529 | 0.045 | — |
| SNAPC3 | 0.484 | 0.000 | — |
| FREM1 | 0.460 | 0.000 | — |
| DEPP1 | 0.459 | 0.000 | — |
| ZNF654 | 0.431 | 0.053 | — |
| IGSF22 | 0.426 | 0.107 | — |
| DENND4C | 0.422 | 0.000 | — |
| CCDC169 | 0.419 | 0.000 | — |
| CLCN3 | 0.414 | 0.093 | — |
| CCDC190 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| S100A10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CRY1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27254|pubmed:23133559 |
| CSNK2B | psi-mi:"MI:0030"(cross-linking study) | pubmed:36876296|imex:IM-30472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 5
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 无 | pLDDT=71.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 11 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC171 — Coiled-coil domain-containing protein 171，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1326 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6TFL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164989-CCDC171/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC171
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6TFL3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
