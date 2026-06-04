---
type: protein-evaluation
gene: "CDK5RAP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDK5RAP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=185，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDK5RAP2 |
| 蛋白名称 | CDK5 regulatory subunit-associated protein 2 |
| 蛋白大小 | 1893 aa / 215.0 kDa |
| UniProt ID | Q96SN8 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDK5RAP2/IF_images/U-251MG_1.jpg|U 251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome, Basal body; 额外: Cell Junctions, Cytosol, Equator; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1893 aa / 215.0 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=185 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.1; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **51.0/180** | |
| **归一化总分** | | | **28.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body; 额外: Cell Junctions, Cytosol, Equatorial segment, Mid piece, Principal piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Golgi appara... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 185 |
| PubMed broad count | 206 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Selective disruption of microtubule formation at the nuclear envelope impairs the bone resorption capacity of osteoclasts.. *J Cell Sci*. PMID: 41355489
2. Rare genetic causes of primary microcephaly in two Saudi families identified via whole-exome sequencing: Genomic and phenotypic delineation of pathogenic CDK5RAP2 and CIT variants.. *Mol Genet Metab Rep*. PMID: 42079399
3. Phosphorylation remodels the mitotic centrosome matrix to generate bipartite γ-tubulin complex docking sites.. *Sci Adv*. PMID: 42202035
4. Genetic and genomic analyses of the effect of heat stress, measured as temperature-humidity index, on cow fertility in Australian Holstein cattle.. *J Dairy Sci*. PMID: 41850387
5. Cell Cycle-Specific Regulation of Centrosome Clustering Dynamics in Cancer Cells by the Multifunctional Kinesin HSET.. *Adv Sci (Weinh)*. PMID: 41787955

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 2.8% |
| 置信残基 (pLDDT 70-90) 占比 | 43.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 43.8% |
| 有序区域 (pLDDT>70) 占比 | 46.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDK5RAP2/CDK5RAP2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=59.1），有序残基占 46.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP152 | 0.000 | 0.000 | — |
| PCNT | 0.000 | 0.000 | — |
| TUBGCP2 | 0.000 | 0.000 | — |
| CENPJ | 0.000 | 0.000 | — |
| CEP192 | 0.000 | 0.000 | — |
| MZT2A | 0.000 | 0.000 | — |
| STIL | 0.000 | 0.000 | — |
| AKAP9 | 0.000 | 0.000 | — |
| MCPH1 | 0.000 | 0.000 | — |
| ASPM | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P26641 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96SN8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q14194 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q5RL73 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9UKR5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P54257 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q92993 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y383 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9H213 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P21246 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.1 + PDB: 无 | pLDDT=59.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body; 额外: Cell Junctions, Cytoso | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐ (REJECTED)

**核心优势**:
1. CDK5RAP2 — CDK5 regulatory subunit-associated protein 2，研究基础较多，新颖性有限。
2. 蛋白大小1893 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 185 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96SN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136861-CDK5RAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDK5RAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96SN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CDK5RAP2/CDK5RAP2-PAE.png]]




