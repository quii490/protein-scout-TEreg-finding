---
type: protein-evaluation
gene: "PCYT1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCYT1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCYT1A / CTPCT, PCYT1 |
| 蛋白名称 | Choline-phosphate cytidylyltransferase A |
| 蛋白大小 | 367 aa / 41.7 kDa |
| UniProt ID | P49585 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytosol; Membrane; Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 367 aa / 41.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041723, IPR004821, IPR045049, IPR014729; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Membrane; Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- glycogen granule (GO:0042587)
- nuclear envelope (GO:0005635)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTPCT, PCYT1 |

**关键文献**:
1. Organelle-selective click labeling coupled with flow cytometry allows pooled CRISPR screening of genes involved in phosphatidylcholine metabolism.. *Cell metabolism*. PMID: 36917984
2. De novo phosphatidylcholine synthesis is required for autophagosome membrane formation and maintenance during autophagy.. *Autophagy*. PMID: 31517566
3. PCYT1A deficiency disturbs fatty acid metabolism and induces ferroptosis in the mouse retina.. *BMC biology*. PMID: 38858683
4. Methylome and transcriptome profiling revealed epigenetic silencing of LPCAT1 and PCYT1A associated with lipidome alterations in polycystic ovary syndrome.. *Journal of cellular physiology*. PMID: 33521992
5. CHKA and PCYT1A gene polymorphisms, choline intake and spina bifida risk in a California population.. *BMC medicine*. PMID: 17184542

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 50.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 26.2% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.0，有序区 70.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041723, IPR004821, IPR045049, IPR014729; Pfam: PF01467 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHKA | 0.996 | 0.000 | — |
| CEPT1 | 0.987 | 0.000 | — |
| CHPT1 | 0.984 | 0.000 | — |
| CHKB | 0.981 | 0.000 | — |
| PCYT1B | 0.974 | 0.733 | — |
| PHOSPHO1 | 0.927 | 0.000 | — |
| MAPK3 | 0.911 | 0.091 | — |
| MAPK8 | 0.909 | 0.000 | — |
| MAPK1 | 0.908 | 0.091 | — |
| MAPK9 | 0.907 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000394617.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Q81XC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| cotE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cep170 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| trpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| VKORC1L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RNF8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PCYT1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 无 | pLDDT=76.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Membrane; Endoplasmic reticulu / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PCYT1A — Choline-phosphate cytidylyltransferase A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小367 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49585
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161217-PCYT1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCYT1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49585
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000161217-PCYT1A/subcellular

![](https://images.proteinatlas.org/35428/380_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/35428/380_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/35428/382_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/35428/382_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/35428/397_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/35428/397_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49585-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
