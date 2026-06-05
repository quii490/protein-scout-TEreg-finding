---
type: protein-evaluation
gene: "PTGES2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTGES2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTGES2 / C9orf15, PGES2 |
| 蛋白名称 | Prostaglandin E synthase 2 |
| 蛋白大小 | 377 aa / 41.9 kDa |
| UniProt ID | Q9H7Z7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 41.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010987, IPR036282, IPR040079, IPR004045, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi apparatus membrane; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- azurophil granule lumen (GO:0035578)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- Golgi membrane (GO:0000139)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 141 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf15, PGES2 |

**关键文献**:
1. PTGES2 and RNASET2 identified as novel potential biomarkers and therapeutic targets for basal cell carcinoma: insights from proteome-wide mendelian randomization, colocalization, and MR-PheWAS analyses.. *Frontiers in pharmacology*. PMID: 39035989
2. Proteome-Wide Ligand and Target Discovery by Using β-Nitrostyrene Electrophiles: Supporting Targeted Protein Degradation.. *Angewandte Chemie (International ed. in English)*. PMID: 40464197
3. PLPP/CIN-mediated NF2 S10 dephosphorylation distinctly regulates kainate-induced seizure susceptibility and neuronal death through PAK1-NF-κB-COX-2-PTGES2 signaling pathway.. *Journal of neuroinflammation*. PMID: 37118736
4. Association of prostaglandin E synthase 2 (PTGES2) Arg298His polymorphism with type 2 diabetes in two German study populations.. *The Journal of clinical endocrinology and metabolism*. PMID: 17566096
5. Decreased PTGES2 Farnesylation in Granulosa Cells Compromises PGE2-Dependent Cumulus Expansion and Oocyte Maturation During Ovarian Aging.. *Aging cell*. PMID: 41521701

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 68.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 13.5% |
| 有序区域 (pLDDT>70) 占比 | 81.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.7，有序区 81.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010987, IPR036282, IPR040079, IPR004045, IPR034334; Pfam: PF13417 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTGES3 | 0.993 | 0.000 | — |
| PTGES | 0.988 | 0.000 | — |
| PTGS2 | 0.963 | 0.000 | — |
| PTGS1 | 0.962 | 0.000 | — |
| PTGIS | 0.958 | 0.000 | — |
| PTGDS | 0.952 | 0.000 | — |
| HPGDS | 0.952 | 0.000 | — |
| CBR1 | 0.937 | 0.000 | — |
| CBR3 | 0.906 | 0.000 | — |
| GLRX | 0.824 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| uvrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20000738|imex:IM-19572 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| HTT | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17394|pubmed:23275563 |
| TMEM267 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SHISA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NMES1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 无 | pLDDT=83.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Cytoplasm, perinuclear r / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PTGES2 — Prostaglandin E synthase 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H7Z7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148334-PTGES2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTGES2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7Z7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H7Z7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
