---
type: protein-evaluation
gene: "PRR11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR11 |
| 蛋白名称 | Proline-rich protein 11 |
| 蛋白大小 | 360 aa / 40.1 kDa |
| UniProt ID | Q96HE9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 40.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.2; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A targetable PRR11-DHODH axis drives ferroptosis- and temozolomide-resistance in glioblastoma.. *Redox biology*. PMID: 38838551
2. PRR11 in Malignancies: Biological Activities and Targeted Therapies.. *Biomolecules*. PMID: 36551227
3. Expression of PRR11 protein and its correlation with pancreatic cancer and effect on survival.. *Oncology letters*. PMID: 28599413
4. PRR11 and SKA2 gene pair is overexpressed and regulated by p53 in breast cancer.. *BMB reports*. PMID: 30760381
5. PRR11 is a prognostic biomarker and correlates with immune infiltrates in bladder urothelial carcinoma.. *Scientific reports*. PMID: 36739300

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.2 |
| 高置信度残基 (pLDDT>90) 占比 | 9.4% |
| 置信残基 (pLDDT 70-90) 占比 | 34.2% |
| 中等置信 (pLDDT 50-70) 占比 | 33.3% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 43.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.2），有序残基占 43.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKA2 | 0.617 | 0.000 | — |
| H1-1 | 0.564 | 0.563 | — |
| GTSE1 | 0.513 | 0.000 | — |
| CKAP2L | 0.513 | 0.000 | — |
| KIF14 | 0.472 | 0.000 | — |
| PRDM15 | 0.460 | 0.456 | — |
| KIF23 | 0.445 | 0.000 | — |
| SORD | 0.443 | 0.443 | — |
| KIF18B | 0.440 | 0.000 | — |
| STAU1 | 0.423 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| IL4R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OSBPL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NVL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DKC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DUSP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SF3B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.2 + PDB: 无 | pLDDT=66.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PRR11 — Proline-rich protein 11，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HE9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068489-PRR11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HE9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96HE9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
