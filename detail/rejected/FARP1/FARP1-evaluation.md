---
type: protein-evaluation
gene: "FARP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FARP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FARP1 / CDEP, PLEKHC2 |
| 蛋白名称 | FERM, ARHGEF and pleckstrin domain-containing protein 1 |
| 蛋白大小 | 1045 aa / 118.6 kDa |
| UniProt ID | Q9Y4F1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cell membrane; Synapse; Synapse, synaptosome; Cytoplasm, cyt |
| 蛋白大小 | 8/10 | ×1 | 8 | 1045 aa / 118.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.0; PDB: 4H6Y |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR035899, IPR000219, IPR000798, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cell membrane; Synapse; Synapse, synaptosome; Cytoplasm, cytosol; Cell projection, filopodium; Cell ... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasmic side of plasma membrane (GO:0009898)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- dendritic spine (GO:0043197)
- extrinsic component of postsynaptic membrane (GO:0098890)
- filopodium (GO:0030175)
- glutamatergic synapse (GO:0098978)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDEP, PLEKHC2 |

**关键文献**:
1. ANKK1 Is a Wnt/PCP Scaffold Protein for Neural F-ACTIN Assembly.. *International journal of molecular sciences*. PMID: 39409035
2. Tetraspanin-enriched membrane domains regulate vascular leakage by altering membrane cholesterol accessibility to balance antagonistic GTPases.. *Nature cardiovascular research*. PMID: 40731107
3. The novel synaptogenic protein Farp1 links postsynaptic cytoskeletal dynamics and transsynaptic organization.. *The Journal of cell biology*. PMID: 23209303
4. Structural analyses of FERM domain-mediated membrane localization of FARP1.. *Scientific reports*. PMID: 29992992
5. FARP1 promotes the dendritic growth of spinal motor neuron subtypes through transmembrane Semaphorin6A and PlexinA4 signaling.. *Neuron*. PMID: 19217374

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 26.0% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 4H6Y |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.0，有序区 70.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR035899, IPR000219, IPR000798, IPR014847; Pfam: PF08736, PF09380, PF00373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.760 | 0.166 | — |
| PLEK2 | 0.695 | 0.000 | — |
| PLEK | 0.694 | 0.000 | — |
| PLXNA4 | 0.620 | 0.000 | — |
| RHOA | 0.608 | 0.162 | — |
| RHOF | 0.586 | 0.143 | — |
| RNF113B | 0.571 | 0.000 | — |
| SEMA6A | 0.565 | 0.000 | — |
| CADM1 | 0.559 | 0.000 | — |
| ANK3 | 0.525 | 0.497 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Q81VA8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| yscP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| narX | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CDC37 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| CEP170 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| NOC2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| NUP214 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 4H6Y | pLDDT=76.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Synapse; Synapse, synaptosome; Cyto / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FARP1 — FERM, ARHGEF and pleckstrin domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1045 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4F1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152767-FARP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FARP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4F1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4F1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
