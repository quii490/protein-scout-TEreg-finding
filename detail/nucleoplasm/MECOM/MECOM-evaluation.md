---
type: protein-evaluation
gene: "MECOM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MECOM — REJECTED (研究热度过高 (PubMed strict=204，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MECOM / EVI1, MDS1, PRDM3 |
| 蛋白名称 | Histone-lysine N-methyltransferase MECOM |
| 蛋白大小 | 1230 aa / 138.1 kDa |
| UniProt ID | Q03112 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1230 aa / 138.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=204 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.4; PDB: 6BW3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044411, IPR001214, IPR046341, IPR050331, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 204 |
| PubMed broad count | 801 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EVI1, MDS1, PRDM3 |

**关键文献**:
1. Fate and state transitions during human blood vessel organoid development.. *Cell*. PMID: 40250419
2. Hematologic Cancer after Gene Therapy for Cerebral Adrenoleukodystrophy.. *The New England journal of medicine*. PMID: 39383458
3. Directed Differentiation of Human Induced Pluripotent Stem Cells to Heart Valve Cells.. *Circulation*. PMID: 38357822
4. The microprotein HDSP promotes gastric cancer progression through activating the MECOM-SPINK1-EGFR signaling axis.. *Nature communications*. PMID: 39333095
5. A landscape of germ line mutations in a cohort of inherited bone marrow failure patients.. *Blood*. PMID: 29146883

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 66.1% |
| 有序区域 (pLDDT>70) 占比 | 25.8% |
| 可用 PDB 条目 | 6BW3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.4），有序残基占 25.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044411, IPR001214, IPR046341, IPR050331, IPR036236; Pfam: PF21549, PF00096, PF13912 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTBP1 | 0.994 | 0.726 | — |
| RUNX1 | 0.988 | 0.067 | — |
| HDAC1 | 0.968 | 0.633 | — |
| CTBP2 | 0.958 | 0.070 | — |
| HDAC2 | 0.929 | 0.239 | — |
| MAPK8 | 0.905 | 0.055 | — |
| MAPK9 | 0.901 | 0.055 | — |
| RBBP4 | 0.876 | 0.744 | — |
| KAT2B | 0.861 | 0.539 | — |
| SMAD3 | 0.858 | 0.523 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ctbp2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11328817|imex:IM-19966| |
| UXT | psi-mi:"MI:0018"(two hybrid) | pubmed:17635584|imex:IM-19070 |
| CLIC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CTBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERMAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPDEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| L3MBTL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RABGAP1L | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| PIK3R3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.4 + PDB: 6BW3 | pLDDT=50.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MECOM — Histone-lysine N-methyltransferase MECOM，研究基础较多，新颖性有限。
2. 蛋白大小1230 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 204 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 204 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03112
- Protein Atlas: https://www.proteinatlas.org/ENSG00000085276-MECOM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MECOM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03112
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
