---
type: protein-evaluation
gene: "CPEB4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPEB4 — REJECTED (研究热度过高 (PubMed strict=158，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPEB4 |
| 蛋白名称 | Cytoplasmic polyadenylation element-binding protein 4 |
| 蛋白大小 | 729 aa / 80.2 kDa |
| UniProt ID | Q17RY0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Golgi apparatus; 额外: Vesicles; UniProt: Cytoplasm; Cell projection, dendrite; Cell projection, dendr |
| 蛋白大小 | 10/10 | x1 | 10 | 729 aa / 80.2 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=158 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 18 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Cell projection, dendrite; Cell projection, dendritic spine; Postsynaptic density; Cell p... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 158 |
| PubMed broad count | 165 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CPEB4 deficiency promotes vasculogenic mimicry and resistance to anti-angiogenic therapy in hepatocellular carcinoma.. *Gut*. PMID: 42209191
2. SNAP23 regulates CPEB4 in the autophagy of hepatocellular carcinoma.. *Sci Rep*. PMID: 42086740
3. Genomic insights into female productivity in limousine cattle: a single-step genome-wide association on longevity, fertility, and conformation traits.. *BMC Genomics*. PMID: 41981458
4. Genome-wide association study of fitness traits in local Alpine cattle breeds: insights into longevity, fertility, and udder health.. *Animal*. PMID: 41855919
5. Stress-Induced Down-Regulation of CPEB4 Disrupts Sodium Channel Regulation and Myocardial Excitability.. *JACC Basic Transl Sci*. PMID: 41846068

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 62.4% |
| 有序区域 (pLDDT>70) 占比 | 34.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 34.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK1 | 0.000 | 0.000 | — |
| AURKA | 0.000 | 0.000 | — |
| PLK1 | 0.000 | 0.000 | — |
| CCNB2 | 0.000 | 0.000 | — |
| FMR1 | 0.000 | 0.000 | — |
| FXR1 | 0.000 | 0.000 | — |
| FXR2 | 0.000 | 0.000 | — |
| CPEB1 | 0.000 | 0.000 | — |
| DDX6 | 0.000 | 0.000 | — |
| CPEB2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q17RY0-2 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:Q8D052 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q17RY0 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q7Z5Q1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8NE35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-64083765 | psi-mi:"MI:2285"(miRNA interference luciferase rep | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 18
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 18 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 无 | pLDDT=57.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell projection, dendrite; Cell project / Nucleoplasm, Golgi apparatus; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 18 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPEB4 -- Cytoplasmic polyadenylation element-binding protein 4，研究基础较多，新颖性有限。
2. 蛋白大小729 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 158 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 158 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q17RY0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113742-CPEB4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPEB4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q17RY0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q17RY0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
