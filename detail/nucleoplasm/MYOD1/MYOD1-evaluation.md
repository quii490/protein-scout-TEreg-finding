---
type: protein-evaluation
gene: "MYOD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MYOD1 — REJECTED (研究热度过高 (PubMed strict=797，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYOD1 / BHLHC1, MYF3, MYOD |
| 蛋白名称 | Myoblast determination protein 1 |
| 蛋白大小 | 320 aa / 34.5 kDa |
| UniProt ID | P15172 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 34.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=797 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR022032, IPR002546, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- euchromatin (GO:0000791)
- myofibril (GO:0030016)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 797 |
| PubMed broad count | 1948 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHC1, MYF3, MYOD |

**关键文献**:
1. Cicero Predicts cis-Regulatory DNA Interactions from Single-Cell Chromatin Accessibility Data.. *Molecular cell*. PMID: 30078726
2. Chromatin-dependent motif syntax defines differentiation trajectories.. *Molecular cell*. PMID: 40780181
3. Biological Role and Clinical Implications of MYOD1(L122R) Mutation in Rhabdomyosarcoma.. *Cancers*. PMID: 36980529
4. PRMT5 mediates FoxO1 methylation and subcellular localization to regulate lipophagy in myogenic progenitors.. *Cell reports*. PMID: 37883229
5. CTRP9 as a myokine mitigates sarcopenia via the LAMP-2A/NLRP3 pathway.. *Cell death & disease*. PMID: 41057318

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 30.6% |
| 低置信 (pLDDT<50) 占比 | 41.9% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR022032, IPR002546, IPR039704; Pfam: PF01586, PF00010, PF12232 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCF3 | 0.993 | 0.795 | — |
| EP300 | 0.991 | 0.837 | — |
| SMARCD3 | 0.990 | 0.325 | — |
| TCF12 | 0.989 | 0.922 | — |
| TCF4 | 0.972 | 0.437 | — |
| KAT2B | 0.972 | 0.824 | — |
| MEF2A | 0.967 | 0.045 | — |
| TBP | 0.960 | 0.071 | — |
| MRLN | 0.958 | 0.000 | — |
| SMARCA4 | 0.957 | 0.632 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIRT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12887892 |
| KAT2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12887892 |
| Id2 | psi-mi:"MI:0090"(protein complementation assay) | pubmed:21209940|imex:IM-17261 |
| KPNA3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| POLR2G | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PSME2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| C2orf88 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ENSMUSP00000072330.2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| EBI-2639862 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| Smad3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 无 | pLDDT=61.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MYOD1 — Myoblast determination protein 1，研究基础较多，新颖性有限。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 797 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 797 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15172
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129152-MYOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15172
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
