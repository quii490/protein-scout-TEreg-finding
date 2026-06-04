---
type: protein-evaluation
gene: "CCDC88B"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC88B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC88B / BRLZ |
| 蛋白全名 | Coiled-coil domain-containing protein 88B |
| 蛋白大小 | 1476 aa / 164.8 kDa |
| UniProt ID | A6NC98 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Centrosome, Cytosol |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16 | HPA核为附加定位，主定位非核 |
| 蛋白大小 | 5/10 | x1 | 5 | 1476 aa (small or large) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=16 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=69.0)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (1条)，主要为预测 |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **115.5/180** | |
| **归一化总分 (÷1.83)** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Centrosome, Cytosol | Supported |
| UniProt | Membrane (ECO:0000250); Cytoplasm, cytoskeleton, microtubule organizing center (ECO:0000269); Endoplasmic reticulum (ECO | Swiss-Prot/TrEMBL |
| GO-CC | centrosome (IDA:HPA); cytoplasm (IBA:GO_Central); cytosol (IDA:HPA); endoplasmic reticulum (IEA:UniProtKB-SubCell); Golgi apparatus (IEA:UniProtKB-SubCell) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA核为附加定位，主定位非核

#### 3.2 蛋白大小评估

1476 aa (small or large)

**评价**: 1476 aa / 164.8 kDa，大蛋白，实验操作有一定挑战。

**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 16 |
| PubMed symbol_only | 21 |
| PubMed broad | 23 |
| 别名 | BRLZ |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 16 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **CCDC88B interacts with RASAL3 and ARHGEF2 and regulates dendritic cell function in neuroinflammation and colitis.** *Communications biology* (2024 Jan 10) PMID:38200184 -- Olivier JF et al.
2. **Identification and experimental validation of Alzheimer's disease hub genes via bioinformatics and machine learning.** *Journal of Alzheimer's disease reports* (2025 Jan-Dec) PMID:40678591 -- Hu Y et al.
3. **CCDC88B is required for mobility and inflammatory functions of dendritic cells.** *Journal of leukocyte biology* (2020 Dec) PMID:32480428 -- Olivier JF et al.
4. **CCDC88B is a novel regulator of maturation and effector functions of T cells during pathological inflammation.** *The Journal of experimental medicine* (2014 Dec 15) PMID:25403443 -- Kennedy JM et al.
5. **CCDC88B is required for pathogenesis of inflammatory bowel disease.** *Nature communications* (2017 Oct 13) PMID:29030607 -- Fodil N et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 69.0 |
| pLDDT > 90 (Very High) | 36.2% |
| pLDDT 70-90 (High) | 25.3% |
| pLDDT 50-70 (Medium) | 5.1% |
| pLDDT < 50 (Low) | 33.5% |
| 有序区域 (pLDDT>70) 占比 | 61.5% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=69.0，有序区域 62%）。作为新颖蛋白，属正常现象。

**评分: 6/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| HOOK1 | 0.768 | 0.064 | — |
| GNAI3 | 0.673 | 0.073 | — |
| COPB1 | 0.523 | 0.000 | — |
| MYH1 | 0.514 | 0.067 | — |
| GPR137 | 0.497 | 0.000 | — |
| HSPA5 | 0.493 | 0.046 | — |
| KCNK4 | 0.487 | 0.000 | — |
| PBX2 | 0.446 | 0.421 | — |
| ITSN1 | 0.441 | 0.000 | — |
| PUS7L | 0.438 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| PBX2 | 0018(two hybrid) | pubmed:14667819|mint | — |
| A0A0G2RMA5 | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| PLEKHA5 | 0398(two hybrid pooling approach) | pubmed:20936779|imex | — |
| A0A384LDE1 | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| TSHZ2 | 0397(two hybrid array) | pubmed:32296183|imex | — |
| FAM161A | 0397(two hybrid array) | pubmed:32296183|imex | — |
| SH3KBP1 | 0397(two hybrid array) | pubmed:32296183|imex | — |
| TXLNB | 0397(two hybrid array) | pubmed:32296183|imex | — |
| FAM161B | 0397(two hybrid array) | pubmed:32296183|imex | — |
| RBM7 | 0397(two hybrid array) | pubmed:32296183|imex | — |


**已知复合体成员** (GO Cellular Component):
- centrosome (IDA:HPA)
- cytoplasm (IBA:GO_Central)
- cytosol (IDA:HPA)
- endoplasmic reticulum (IEA:UniProtKB-SubCell)
- Golgi apparatus (IEA:UniProtKB-SubCell)
- membrane (HDA:UniProtKB)
- nucleoplasm (IDA:HPA)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: STRING综合分>0.7 (1条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 15 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (63.1/100)

**核心优势**:
1. Extremely novel -- PubMed=16篇
2. HPA核为附加定位，主定位非核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NC98
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC88B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NC98
- STRING: https://string-db.org/cgi/network?identifiers=CCDC88B&species=9606
