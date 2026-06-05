---
type: protein-evaluation
gene: "SPEF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPEF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPEF2 / KIAA1770, KPL2 |
| 蛋白名称 | Sperm flagellar protein 2 |
| 蛋白大小 | 1822 aa / 209.8 kDa |
| UniProt ID | Q9C093 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Primary cilium, Flagellar centriole; 额外: Nuclear bodies, Cyt; UniProt: Cell projection, cilium, flagellum; Cytoplasm; Golgi apparat |
| 蛋白大小 | 5/10 | ×1 | 5 | 1822 aa / 209.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010441, IPR001715, IPR036872, IPR011992, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Primary cilium, Flagellar centriole; 额外: Nuclear bodies, Cytosol, Mid piece | Supported |
| UniProt | Cell projection, cilium, flagellum; Cytoplasm; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- Golgi apparatus (GO:0005794)
- manchette (GO:0002177)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1770, KPL2 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. Cilia-related protein SPEF2 regulates osteoblast differentiation.. *Scientific reports*. PMID: 29339787
3. SPEF2- and HYDIN-Mutant Cilia Lack the Central Pair-associated Protein SPEF2, Aiding Primary Ciliary Dyskinesia Diagnostics.. *American journal of respiratory cell and molecular biology*. PMID: 31545650
4. Expression of SPEF2 during mouse spermatogenesis and identification of IFT20 as an interacting protein.. *Biology of reproduction*. PMID: 19889948
5. The ciliary protein Spef2 stimulates acinar Ampkα/Sirt1 signaling and ameliorates acute pancreatitis and associated lung injury.. *Annals of translational medicine*. PMID: 35965828

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.5 |
| 高置信度残基 (pLDDT>90) 占比 | 14.8% |
| 置信残基 (pLDDT 70-90) 占比 | 51.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 66.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.5，有序区 66.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010441, IPR001715, IPR036872, IPR011992, IPR027417; Pfam: PF00406, PF06294, PF24082 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADK | 0.930 | 0.067 | — |
| SPAG6 | 0.786 | 0.106 | — |
| CFAP54 | 0.744 | 0.102 | — |
| CFAP43 | 0.735 | 0.000 | — |
| ARMC2 | 0.717 | 0.049 | — |
| SPAG17 | 0.714 | 0.125 | — |
| DNAI1 | 0.708 | 0.045 | — |
| TTC21A | 0.699 | 0.000 | — |
| IFT20 | 0.699 | 0.049 | — |
| CFAP70 | 0.683 | 0.079 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| cdc5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:11884590 |
| dre4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| prp17 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| prp19 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| cwf2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| saf1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| cwf10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21386897|imex:IM-17268 |
| APOA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| IGHA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| KATNAL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.5 + PDB: 无 | pLDDT=70.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum; Cytoplasm; Gol / Primary cilium, Flagellar centriole; 额外: Nuclear b | 一致 |
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
1. SPEF2 — Sperm flagellar protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1822 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C093
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152582-SPEF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPEF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C093
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Primary cilium (supported)。来源: https://www.proteinatlas.org/ENSG00000152582-SPEF2/subcellular

![](https://images.proteinatlas.org/40343/2185_D3_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/40343/2185_D3_50_blue_red_green.jpg)
![](https://images.proteinatlas.org/40343/2186_B2_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/40343/2186_B2_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/40343/2202_B3_24_blue_red_green.jpg)
![](https://images.proteinatlas.org/40343/2202_B3_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C093-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
