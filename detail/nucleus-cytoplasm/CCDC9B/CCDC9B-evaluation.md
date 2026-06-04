---
type: protein-evaluation
gene: "CCDC9B"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC9B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC9B / C15orf52 |
| 蛋白全名 | Coiled-coil domain-containing protein 9B |
| 蛋白大小 | 534 aa / 57.3 kDa |
| UniProt ID | Q6ZUT6 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm, Cytosol |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 534 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=2 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=53.6)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (11条) |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(7条) (+0.5) |
| **加权总分** | | | **129.5/180** | |
| **归一化总分 (÷1.83)** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | 无 | |

暂无PAE图

HPA IF 图像可用 (8张)，待下载。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

534 aa (200-800 aa ideal range)

**评价**: 534 aa / 57.3 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 2 |
| PubMed symbol_only | 2 |
| PubMed broad | 2 |
| 别名 | C15orf52 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 2 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.** *Scientific reports* (2022 Nov 7) PMID:36344539 -- Al-Kasbi G et al.
2. **Epigenetic inactivation of the 5-methylcytosine RNA methyltransferase NSUN7 is associated with clinical outcome and therapeutic vulnerability in liver cancer.** *Molecular cancer* (2023 May 12) PMID:37173708 -- Ortiz-Barahona V et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 53.6 |
| pLDDT > 90 (Very High) | 6.2% |
| pLDDT 70-90 (High) | 8.6% |
| pLDDT 50-70 (Medium) | 32.2% |
| pLDDT < 50 (Low) | 53.0% |
| 有序区域 (pLDDT>70) 占比 | 14.8% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=53.6，有序区域 15%）。作为新颖蛋白，属正常现象。

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
| KRBA1 | 0.633 | 0.071 | — |
| FAM86B1 | 0.507 | 0.000 | — |
| IQCC | 0.507 | 0.000 | — |
| TMEM51 | 0.480 | 0.000 | — |
| PROSER3 | 0.480 | 0.000 | — |
| LYSMD4 | 0.478 | 0.000 | — |
| KRBA2 | 0.456 | 0.058 | — |
| DCTN5 | 0.423 | 0.071 | — |
| LEPROT | 0.413 | 0.000 | — |
| THOC7 | 0.408 | 0.402 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| THOC1 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| THOC7 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| BMI1 | 0006(anti bait coimmunoprecipitation) | pubmed:34316702|imex | — |
| EBI-2532212 | 0007(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed | — |
| EBI-2532478 | 0007(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed | — |
| EBI-2532663 | 0007(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed | — |


**已知复合体成员** (GO Cellular Component):
- 无GO-CC注释

**PPI 互证分析**:
- STRING partners (score>0.4): 11
- IntAct 物理互作: 6
- 调控相关比例: 0/11 (0%)

**评价**: 仅有低置信度STRING关联 (11条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 11 + 6 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(7条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (70.8/100)

**核心优势**:
1. Extremely novel -- PubMed=2篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUT6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC9B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUT6
- STRING: https://string-db.org/cgi/network?identifiers=CCDC9B&species=9606
