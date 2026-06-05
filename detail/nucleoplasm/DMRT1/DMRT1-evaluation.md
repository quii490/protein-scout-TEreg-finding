---
type: protein-evaluation
gene: "DMRT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DMRT1 — REJECTED (研究热度过高 (PubMed strict=727，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMRT1 / DMT1 |
| 蛋白名称 | Doublesex- and mab-3-related transcription factor 1 |
| 蛋白大小 | 373 aa / 39.5 kDa |
| UniProt ID | Q9Y5R6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 39.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=727 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 4YJ0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001275, IPR036407, IPR026607, IPR022114; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- female germ cell nucleus (GO:0001674)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 727 |
| PubMed broad count | 1119 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DMT1 |

**关键文献**:
1. Gonadal transcriptome analysis of Opsariichthys bidens reveals sex-associated genes.. *Comparative biochemistry and physiology. Part D, Genomics & proteomics*. PMID: 39667087
2. DMRT1 is a testis-determining gene in rabbits and is also essential for female fertility.. *eLife*. PMID: 37847154
3. Sex determination and maintenance: the role of DMRT1 and FOXL2.. *Asian journal of andrology*. PMID: 28091399
4. AMHY and sex determination in egg-laying mammals.. *Genome biology*. PMID: 40426235
5. Genetic Regulation of Avian Testis Development.. *Genes*. PMID: 34573441

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.1% |
| 中等置信 (pLDDT 50-70) 占比 | 34.9% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 16.8% |
| 可用 PDB 条目 | 4YJ0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 16.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001275, IPR036407, IPR026607, IPR022114; Pfam: PF00751, PF12374 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOX9 | 0.959 | 0.070 | — |
| SRY | 0.955 | 0.065 | — |
| KANK1 | 0.916 | 0.044 | — |
| GATA4 | 0.891 | 0.048 | — |
| SOX3 | 0.888 | 0.065 | — |
| AMH | 0.847 | 0.000 | — |
| DOCK8 | 0.846 | 0.000 | — |
| NR5A1 | 0.844 | 0.000 | — |
| FOXL2 | 0.837 | 0.045 | — |
| DHH | 0.781 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sox9 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-12116|pubmed:20005806 |
| TRIM29 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM68 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PIEZO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MECR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 4YJ0 | pLDDT=56.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DMRT1 — Doublesex- and mab-3-related transcription factor 1，研究基础较多，新颖性有限。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 727 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 727 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5R6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137090-DMRT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMRT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5R6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5R6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
