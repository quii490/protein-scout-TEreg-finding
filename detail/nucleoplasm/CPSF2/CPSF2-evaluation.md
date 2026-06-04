---
type: protein-evaluation
gene: "CPSF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPSF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPSF2 |
| 蛋白名称 | Cleavage and polyadenylation specificity factor subunit 2 |
| 蛋白大小 | 782 aa / 88.5 kDa |
| UniProt ID | Q9P2I0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 782 aa / 88.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=80.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 29 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Identification of functional genetic components modulating toxicity response to PFOS using genome-wide CRISPR screens in HepG2/C3A cells.. *Arch Toxicol*. PMID: 41588257
2. Genome-wide association analysis to identify candidate genes for growth rate traits in Chinese endemic geese.. *BMC Genomics*. PMID: 41663928
3. Identification of Functional Genetic Components Modulating Toxicity Response to PFOS using Genome-wide CRISPR Screens in HepG2/C3A cells.. *bioRxiv*. PMID: 41446233
4. Comprehensive Analysis of RNA Modifications Related Genes in the Diagnosis and Subtype Classification of Dilated Cardiomyopathy.. *J Inflamm Res*. PMID: 40395552
5. A pan-cancer analysis of the core pre-mRNA 3' end processing factors, and their association with prognosis, tumor microenvironment, and potential targets.. *Sci Rep*. PMID: 39075070

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 15.6% |
| 有序区域 (pLDDT>70) 占比 | 79.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.8，有序区 79.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPSF1 | 0.000 | 0.000 | — |
| CPSF4 | 0.000 | 0.000 | — |
| WDR33 | 0.000 | 0.000 | — |
| CPSF3 | 0.000 | 0.000 | — |
| FIP1L1 | 0.000 | 0.000 | — |
| SYMPK | 0.000 | 0.000 | — |
| CSTF2 | 0.000 | 0.000 | — |
| PCF11 | 0.000 | 0.000 | — |
| CSTF1 | 0.000 | 0.000 | — |
| WDR82 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9P2I0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 无 | pLDDT=80.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CPSF2 -- Cleavage and polyadenylation specificity factor subunit 2，非常新颖，仅有少数基础研究。
2. 蛋白大小782 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2I0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165934-CPSF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPSF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2I0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
