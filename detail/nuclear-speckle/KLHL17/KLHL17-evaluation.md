---
type: protein-evaluation
gene: "KLHL17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL17 / AF |
| 蛋白名称 | Kelch-like protein 17 |
| 蛋白大小 | 642 aa / 69.9 kDa |
| UniProt ID | Q6TDP4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Postsynaptic density; Synapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 642 aa / 69.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 6HRL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR011043, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Uncertain |
| UniProt | Postsynaptic density; Synapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- extracellular space (GO:0005615)
- postsynaptic density (GO:0014069)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AF |

**关键文献**:
1. Allelic effects on KLHL17 expression underlie a pancreatic cancer genome-wide association signal at chr1p36.33.. *Nature communications*. PMID: 40307206
2. KLHL17/Actinfilin, a brain-specific gene associated with infantile spasms and autism, regulates dendritic spine enlargement.. *Journal of biomedical science*. PMID: 33256713
3. Autism-related KLHL17 and SYNPO act in concert to control activity-dependent dendritic spine enlargement and the spine apparatus.. *PLoS biology*. PMID: 37651441
4. KLHL17 differentially controls the expression of AMPA- and KA-type glutamate receptors to regulate dendritic spine enlargement.. *Journal of neurochemistry*. PMID: 38898681
5. Upregulation of KLHL17 promotes the proliferation and migration of non-small cell lung cancer by activating the Ras/MAPK signaling pathway.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 35978057

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 74.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 86.6% |
| 可用 PDB 条目 | 6HRL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 86.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR011043, IPR015915; Pfam: PF07707, PF00651, PF01344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.740 | 0.127 | — |
| PDZK1 | 0.613 | 0.340 | — |
| KLHL3 | 0.596 | 0.575 | — |
| DCN | 0.593 | 0.583 | — |
| SYNGAP1 | 0.580 | 0.095 | — |
| GRIK1 | 0.566 | 0.095 | — |
| FBXL17 | 0.564 | 0.478 | — |
| SAMD11 | 0.530 | 0.000 | — |
| KARS1 | 0.526 | 0.000 | — |
| KLHL2 | 0.516 | 0.490 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDZK1P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXL17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VHL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATXN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| TARDBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| PRKN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 6HRL | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Postsynaptic density; Synapse / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL17 — Kelch-like protein 17，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小642 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6TDP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187961-KLHL17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6TDP4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (uncertain)。来源: https://www.proteinatlas.org/ENSG00000187961-KLHL17/subcellular

![](https://images.proteinatlas.org/31251/321_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/31251/321_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/31251/323_E6_4_red_green.jpg)
![](https://images.proteinatlas.org/31251/323_E6_5_red_green.jpg)
![](https://images.proteinatlas.org/31251/326_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/31251/326_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6TDP4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
