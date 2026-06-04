---
type: protein-evaluation
gene: "DNAJB14"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJB14 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB14 |
| 蛋白名称 | DnaJ homolog subfamily B member 14 |
| 蛋白大小 | 379 aa / 42.5 kDa |
| UniProt ID | Q8TBM8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 379 aa / 42.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=75.5; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 20 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Multi-omics identification and verification of Dnajb14 as a modulator of retinal ganglion cell survival in glaucoma through ferroptosis.. *J Genet Genomics*. PMID: 42202976
2. Genetic Structure and Selective Signature Analysis of Xinjiang Local Sheep Populations.. *Animals (Basel)*. PMID: 41897962
3. Unveiling DNAJB12 and DNAJB14 as crucial chaperones in hepatitis B and D virus particle morphogenesis.. *iScience*. PMID: 41684842
4. Non-genetic inactivation of caspase-3 and P53 increases cancer cell fitness by PDIA4 redistribution.. *Oncogene*. PMID: 41120732
5. The Effect of Circulating Proteins and Their Role in Mediating Adiposity's Effect on Endometrial Cancer Risk: Mendelian Randomization and Colocalization Analyses.. *Cancer Epidemiol Biomarkers Prev*. PMID: 40553479

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 37.7% |
| 置信残基 (pLDDT 70-90) 占比 | 31.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 24.0% |
| 有序区域 (pLDDT>70) 占比 | 68.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.5，有序区 68.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| SGTA | 0.000 | 0.000 | — |
| HSPH1 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA9 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA13 | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 无 | pLDDT=75.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DNAJB14 -- DnaJ homolog subfamily B member 14，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小379 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBM8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164031-DNAJB14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBM8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
