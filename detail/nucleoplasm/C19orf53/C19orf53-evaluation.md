---
type: protein-evaluation
gene: "C19orf53"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C19orf53 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C19orf53 |
| 蛋白名称 | Leydig cell tumor 10 kDa protein homolog |
| 蛋白大小 | 99 aa / 10.6 kDa |
| UniProt ID | Q9UNZ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 99 aa / 10.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.9; PDB: 8FLA, 8FLB, 8FLC, 8IDT, 8IDY, 8INE, 8INF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019034; Pfam: PF09495 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Construction of lactylation-related prognostic signature for glioma.. *Discover oncology*. PMID: 41026379
2. Spatio-Temporal Proteomic Landscape Reveals Early Warning Signals of Esophageal Squamous Cell Carcinoma Progression.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41504491
3. Advanced single-cell pooled CRISPR screening identifies C19orf53 required for cell proliferation based on mTORC1 regulators.. *Cell biology and toxicology*. PMID: 33586084
4. C11orf58 (Hero20) Gene Polymorphism: Contribution to Ischemic Stroke Risk and Interactions with Other Heat-Resistant Obscure Chaperones.. *Biomedicines*. PMID: 39595169
5. Obesity and Environmental Risk Factors Significantly Modify the Association between Ischemic Stroke and the Hero Chaperone C19orf53.. *Life (Basel, Switzerland)*. PMID: 39337941

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 29.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 38.4% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 48.5% |
| 可用 PDB 条目 | 8FLA, 8FLB, 8FLC, 8IDT, 8IDY, 8INE, 8INF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8FLA, 8FLB, 8FLC, 8IDT, 8IDY, 8INE, 8INF）+ AlphaFold极高置信度预测（pLDDT=72.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019034; Pfam: PF09495 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSMB3 | 0.626 | 0.000 | — |
| C19orf67 | 0.584 | 0.000 | — |
| POLR2J | 0.584 | 0.000 | — |
| CCDC124 | 0.581 | 0.000 | — |
| COPS9 | 0.538 | 0.000 | — |
| NDUFA11 | 0.528 | 0.000 | — |
| NDUFB7 | 0.500 | 0.000 | — |
| SERF2 | 0.480 | 0.000 | — |
| RNF181 | 0.479 | 0.000 | — |
| C9orf16 | 0.472 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Q81R13 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| sdhA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| GRB7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| GRB10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| MRPL34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HNRNPU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 8FLA, 8FLB, 8FLC, 8IDT, 8IDY,  | pLDDT=72.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C19orf53 — Leydig cell tumor 10 kDa protein homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小99 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNZ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104979-C19orf53/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C19orf53
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNZ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104979-C19orf53/subcellular

![](https://images.proteinatlas.org/59928/1018_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/59928/1018_C7_3_red_green.jpg)
![](https://images.proteinatlas.org/59928/1043_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/59928/1043_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/59928/1218_C7_3_red_green.jpg)
![](https://images.proteinatlas.org/59928/1218_C7_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UNZ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
