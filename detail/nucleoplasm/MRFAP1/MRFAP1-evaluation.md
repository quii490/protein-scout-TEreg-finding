---
type: protein-evaluation
gene: "MRFAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MRFAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MRFAP1 / PAM14, PGR1 |
| 蛋白名称 | MORF4 family-associated protein 1 |
| 蛋白大小 | 127 aa / 14.7 kDa |
| UniProt ID | Q9Y605 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 127 aa / 14.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.9; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029254; Pfam: PF15155 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAM14, PGR1 |

**关键文献**:
1. Characterization of MRFAP1 turnover and interactions downstream of the NEDD8 pathway.. *Molecular & cellular proteomics : MCP*. PMID: 22038470
2. MRFAP1 plays a protective role in neddylation inhibitor MLN4924-mediated gastric cancer cell death.. *European review for medical and pharmacological sciences*. PMID: 30556867
3. FBXW8-dependent degradation of MRFAP1 in anaphase controls mitotic cell death.. *Oncotarget*. PMID: 29228602
4. Selection of new appropriate reference genes for RT-qPCR analysis via transcriptome sequencing of cynomolgus monkeys (Macaca fascicularis).. *PloS one*. PMID: 23613744
5. Characterization of native protein complexes and protein isoform variation using size-fractionation-based quantitative proteomics.. *Molecular & cellular proteomics : MCP*. PMID: 24043423

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.7% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 20.5% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 77.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 中等质量（pLDDT=81.9，有序区 77.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029254; Pfam: PF15155 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MORF4L1 | 0.987 | 0.893 | — |
| MORF4L2 | 0.953 | 0.872 | — |
| MRGBP | 0.837 | 0.464 | — |
| MRFAP1L1 | 0.721 | 0.686 | — |
| ARL1 | 0.605 | 0.000 | — |
| C1orf43 | 0.542 | 0.000 | — |
| ARFGAP2 | 0.541 | 0.000 | — |
| PHF12 | 0.526 | 0.317 | — |
| KAT6B | 0.523 | 0.000 | — |
| RB1 | 0.517 | 0.516 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRRAP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CACNA1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MORF4L1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MORF4L2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| lon | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000422065.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ABI1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 无 | pLDDT=81.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. MRFAP1 — MORF4 family-associated protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小127 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y605
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179010-MRFAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MRFAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y605
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:57:47
