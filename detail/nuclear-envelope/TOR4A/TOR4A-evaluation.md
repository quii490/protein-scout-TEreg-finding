---
type: protein-evaluation
gene: "TOR4A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOR4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOR4A / C9orf167 |
| 蛋白名称 | Torsin-4A |
| 蛋白大小 | 423 aa / 46.9 kDa |
| UniProt ID | Q9NXH8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 46.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR027417, IPR010448; Pfam: PF06309 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- extracellular region (GO:0005576)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- platelet alpha granule lumen (GO:0031093)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf167 |

**关键文献**:
1. Delta and Notch-like epidermal growth factor-related receptor suppresses human glioma growth by inhibiting oncogene TOR4A.. *Journal of cancer research and therapeutics*. PMID: 36204885
2. Quantitative Proteomics of Human Fibroblasts with I1061T Mutation in Niemann-Pick C1 (NPC1) Protein Provides Insights into the Disease Pathogenesis.. *Molecular & cellular proteomics : MCP*. PMID: 25873482
3. Exploring the transcriptomic landscape of moyamoya disease and systemic lupus erythematosus: insights into crosstalk genes and immune relationships.. *Frontiers in immunology*. PMID: 39290707

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 54.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.2，有序区 73.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR027417, IPR010448; Pfam: PF06309 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCYT2 | 0.538 | 0.000 | — |
| TMEM59L | 0.522 | 0.000 | — |
| C20orf27 | 0.522 | 0.000 | — |
| CPNE1 | 0.515 | 0.000 | — |
| PDLIM2 | 0.491 | 0.000 | — |
| JCAD | 0.490 | 0.000 | — |
| PTPN23 | 0.475 | 0.000 | — |
| SUMF1 | 0.451 | 0.000 | — |
| TOR1AIP2 | 0.444 | 0.000 | — |
| SPART | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TTMP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SFTPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BTNL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEUROG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADAM30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENPP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FCER1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AFG2B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 13
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 无 | pLDDT=79.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TOR4A — Torsin-4A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXH8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198113-TOR4A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOR4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXH8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198113-TOR4A/subcellular

![](https://images.proteinatlas.org/44913/1589_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/44913/1589_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/44913/1660_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/44913/1660_A5_6_red_green.jpg)
![](https://images.proteinatlas.org/44913/566_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/44913/566_A1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NXH8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
