---
type: protein-evaluation
gene: "DDI2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDI2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDI2 |
| 蛋白名称 | Protein DDI1 homolog 2 |
| 蛋白大小 | 399 aa / 44.5 kDa |
| UniProt ID | Q5TDH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytosol; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 399 aa / 44.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.5; PDB: 2N7D, 4RGH, 5K57 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057273, IPR033882, IPR019103, IPR021109, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm, cytosol; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sugar-mediated non-canonical ubiquitination impairs Nrf1/NFE2L1 activation.. *Molecular cell*. PMID: 39116872
2. Activating the NFE2L1-ubiquitin-proteasome system by DDI2 protects from ferroptosis.. *Cell death and differentiation*. PMID: 39384955
3. K48- and K63-linked ubiquitin chain interactome reveals branch- and length-specific ubiquitin interactors.. *Life science alliance*. PMID: 38803224
4. DDI2 promotes tumor metastasis and resists antineoplastic drugs-induced apoptosis in colorectal cancer.. *Apoptosis : an international journal on programmed cell death*. PMID: 36520320
5. DDI2 protease controls embryonic development and inflammation via TCF11/NRF1.. *iScience*. PMID: 39328932

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 15.5% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 2N7D, 4RGH, 5K57 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2N7D, 4RGH, 5K57）+ AlphaFold高质量预测（pLDDT=79.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057273, IPR033882, IPR019103, IPR021109, IPR000626; Pfam: PF09668, PF24669, PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSC1A1 | 0.924 | 0.000 | — |
| UBC | 0.908 | 0.889 | — |
| RPS27A | 0.875 | 0.856 | — |
| UBB | 0.855 | 0.840 | — |
| RAD23B | 0.851 | 0.709 | — |
| RAD23A | 0.801 | 0.589 | — |
| PSMD14 | 0.764 | 0.485 | — |
| PSMD2 | 0.733 | 0.405 | — |
| NFE2L1 | 0.724 | 0.000 | — |
| NGLY1 | 0.724 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| NRIP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBL4A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LRRC41 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CPNE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 2N7D, 4RGH, 5K57 | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Chromosome / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DDI2 — Protein DDI1 homolog 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TDH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197312-DDI2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TDH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000197312-DDI2/subcellular

![](https://images.proteinatlas.org/43119/716_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/43119/716_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/43119/719_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/43119/719_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/43119/764_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/43119/764_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5TDH0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
