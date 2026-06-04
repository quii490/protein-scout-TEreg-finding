---
type: protein-evaluation
gene: "MIIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MIIP / IIP45 |
| 蛋白名称 | Migration and invasion-inhibitory protein |
| 蛋白大小 | 388 aa / 42.8 kDa |
| UniProt ID | Q5JXC2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 388 aa / 42.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031466; Pfam: PF15734 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IIP45 |

**关键文献**:
1. MIIP, a cytoskeleton regulator that blocks cell migration and invasion, delays mitosis, and suppresses tumorogenesis.. *Current protein & peptide science*. PMID: 21190522
2. Inhibition of invasion and metastasis in choriocarcinoma by migration and invasion inhibitory protein.. *Placenta*. PMID: 36379183
3. Altered expression and loss of heterozygosity of the migration and invasion inhibitory protein (MIIP) gene in breast cancer.. *Oncology reports*. PMID: 25873164
4. MIIP accelerates epidermal growth factor receptor protein turnover and attenuates proliferation in non-small cell lung cancer.. *Oncotarget*. PMID: 26824318
5. PKCε phosphorylates MIIP and promotes colorectal cancer metastasis through inhibition of RelA deacetylation.. *Nature communications*. PMID: 29038521

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 27.6% |
| 低置信 (pLDDT<50) 占比 | 45.6% |
| 有序区域 (pLDDT>70) 占比 | 26.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.5），有序残基占 26.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031466; Pfam: PF15734 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IGFBP2 | 0.862 | 0.000 | — |
| TNFRSF8 | 0.604 | 0.000 | — |
| STK16 | 0.587 | 0.587 | — |
| PPP1CA | 0.543 | 0.140 | — |
| HDAC6 | 0.523 | 0.292 | — |
| ICAM1 | 0.523 | 0.000 | — |
| RELA | 0.502 | 0.000 | — |
| KIAA2013 | 0.499 | 0.000 | — |
| RHOT2 | 0.496 | 0.000 | — |
| PID1 | 0.476 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000235332.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RCN1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ADAMTSL4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EIF3E | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| EFHC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CCDC120 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.5 + PDB: 无 | pLDDT=56.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MIIP — Migration and invasion-inhibitory protein，非常新颖，仅有少数基础研究。
2. 蛋白大小388 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JXC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116691-MIIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JXC2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
