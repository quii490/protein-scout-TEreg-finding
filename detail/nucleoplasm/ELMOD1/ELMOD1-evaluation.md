---
type: protein-evaluation
gene: "ELMOD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELMOD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELMOD1 |
| 蛋白名称 | ELMO domain-containing protein 1 |
| 蛋白大小 | 334 aa / 39.1 kDa |
| UniProt ID | Q8N336 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELMOD1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELMOD1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 39.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006816, IPR050868; Pfam: PF04727 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cilium (GO:0005929)
- glutamatergic synapse (GO:0098978)
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The ARF GAPs ELMOD1 and ELMOD3 act at the Golgi and cilia to regulate ciliogenesis and ciliary protein traffic.. *Molecular biology of the cell*. PMID: 34818063
2. ELMO Domain Containing 1 (ELMOD1) Gene Mutation Is Associated with Mental Retardation and Autism Spectrum Disorder.. *Journal of molecular neuroscience : MN*. PMID: 31327155
3. ELMOD1 Stimulates ARF6-GTP Hydrolysis to Stabilize Apical Structures in Developing Vestibular Hair Cells.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 29222402
4. ELMOD2 is an Arl2 GTPase-activating protein that also acts on Arfs.. *The Journal of biological chemistry*. PMID: 17452337
5. Characterization of recombinant ELMOD (cell engulfment and motility domain) proteins as GTPase-activating proteins (GAPs) for ARF family GTPases.. *The Journal of biological chemistry*. PMID: 24616099

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.5% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELMOD1/ELMOD1-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 91.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006816, IPR050868; Pfam: PF04727 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELMOD3 | 0.790 | 0.000 | — |
| SCIMP | 0.594 | 0.000 | — |
| SLC35F2 | 0.575 | 0.000 | — |
| ARL2 | 0.569 | 0.000 | — |
| POGLUT3 | 0.554 | 0.000 | — |
| RASA1 | 0.522 | 0.000 | — |
| DOCK1 | 0.513 | 0.000 | — |
| ARL3 | 0.500 | 0.000 | — |
| ELMO2 | 0.489 | 0.000 | — |
| ELMO3 | 0.486 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| THG1L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| S100A10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LDHC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRC15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PKP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PBLD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DSG4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMED7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RHOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITM2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-29868|pubmed:34446781 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 10
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 无 | pLDDT=90.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ELMOD1 — ELMO domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N336
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110675-ELMOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELMOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N336
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELMOD1/ELMOD1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N336 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 133..314; /note="ELMO"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00664" |
| InterPro | IPR006816;IPR050868; |
| Pfam | PF04727; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110675-ELMOD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RHOA | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
