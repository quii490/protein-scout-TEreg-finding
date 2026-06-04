---
type: protein-evaluation
gene: "DENND5B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DENND5B — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND5B |
| 蛋白名称 | DENN domain containing 5B |
| 蛋白大小 | 1309 aa / 149.3 kDa |
| UniProt ID | G3V1S3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Microtubules; UniProt: Membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 1309 aa / 149.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=20 篇 (<=20->10) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 4/10 | x2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 21 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 20 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DENND5B disruption results in reduced body fat and increased intestinal fatty acid oxidation by activation of autophagy.. *J Lipid Res*. PMID: 41985842
2. Interstitial 12p Deletion Syndrome: Revised Minimal Critical Region and Review of the Literature.. *Genes (Basel)*. PMID: 41595523
3. Impaired Chylomicron Secretion Results in Reduced Body Fat and Increased Intestinal Fatty Acid Oxidation by Activation of Autophagy.. *bioRxiv*. PMID: 41332592
4. Role of DENN Domain-Containing Protein 5b (dennd5b) during early embryonic development of zebrafish.. *Mol Biol Rep*. PMID: 40996562
5. Identification of biological pathways and putative candidate genes for residual feed intake in a tropically adapted beef cattle breed by plasma proteome analysis.. *J Proteomics*. PMID: 39638144

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC35D1 | 0.000 | 0.000 | — |
| SLC35D2 | 0.000 | 0.000 | — |
| SMAP1 | 0.000 | 0.000 | — |
| ITFG1 | 0.000 | 0.000 | — |
| ZMAT4 | 0.000 | 0.000 | — |
| VOPP1 | 0.000 | 0.000 | — |
| DENND4B | 0.000 | 0.000 | — |
| SLC24A3 | 0.000 | 0.000 | — |
| C5orf63 | 0.000 | 0.000 | — |
| DENND1C | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A0A6L7H1G2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q6ZUT9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:G3V1S3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6ZUT9-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 21，IntAct interactions: 6
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 21 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Microtubules | 一致 |
| PPI | STRING + IntAct | 21 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DENND5B -- DENN domain containing 5B，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小1309 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/G3V1S3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170456-DENND5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/G3V1S3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
