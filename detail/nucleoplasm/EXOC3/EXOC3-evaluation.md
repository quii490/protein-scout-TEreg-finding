---
type: protein-evaluation
gene: "EXOC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC3 / SEC6, SEC6L1 |
| 蛋白名称 | Exocyst complex component 3 |
| 蛋白大小 | 745 aa / 85.6 kDa |
| UniProt ID | O60645 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EXOC3/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cell projection, g |
| 蛋白大小 | 10/10 | ×1 | 10 | 745 aa / 85.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010326, IPR042532; Pfam: PF06046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Uncertain |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cell projection, growth cone; Midbody; Golgi apparatus; Ce... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (1张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- exocyst (GO:0000145)
- Golgi apparatus (GO:0005794)
- growth cone (GO:0030426)
- midbody (GO:0030496)
- perinuclear region of cytoplasm (GO:0048471)
- secretory granule membrane (GO:0030667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEC6, SEC6L1 |

**关键文献**:
1. Epigenome-wide association study on diffusing capacity of the lung.. *ERJ open research*. PMID: 33748261
2. Loss of the exocyst complex component EXOC3 promotes hemostasis and accelerates arterial thrombosis.. *Blood advances*. PMID: 33560379
3. Exosome secretion related gene signature predicts chemoresistance in patients with colorectal cancer.. *Pathology, research and practice*. PMID: 38642509
4. Integrated omics analysis of coronary artery calcifications and myocardial infarction: the Framingham Heart Study.. *Scientific reports*. PMID: 38062110
5. Sec8 modulates TGF-β induced EMT by controlling N-cadherin via regulation of Smad3/4.. *Cellular signalling*. PMID: 27769780

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 62.7% |
| 置信残基 (pLDDT 70-90) 占比 | 30.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EXOC3/EXOC3-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=88.5，有序区 93.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010326, IPR042532; Pfam: PF06046 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC4 | 0.999 | 0.985 | — |
| EXOC1 | 0.999 | 0.977 | — |
| EXOC2 | 0.999 | 0.985 | — |
| EXOC7 | 0.999 | 0.928 | — |
| EXOC6 | 0.999 | 0.951 | — |
| EXOC8 | 0.999 | 0.947 | — |
| EXOC5 | 0.999 | 0.979 | — |
| EXOC6B | 0.989 | 0.907 | — |
| SNAP25 | 0.981 | 0.180 | — |
| RHOQ | 0.946 | 0.165 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXOC3-AS1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| KRT40 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SIAH1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| BUB3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Birc6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11898|pubmed:18329369 |
| MLH1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15124|pubmed:20706999 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 无 | pLDDT=88.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cell pro / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. EXOC3 — Exocyst complex component 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60645
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180104-EXOC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60645
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EXOC3/EXOC3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60645 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010326;IPR042532; |
| Pfam | PF06046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180104-EXOC3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EXOC1 | Intact, Biogrid | true |
| EXOC2 | Intact, Biogrid | true |
| EXOC4 | Intact, Biogrid | true |
| EXOC5 | Intact, Biogrid | true |
| EXOC6 | Intact, Biogrid | true |
| EXOC6B | Intact, Biogrid | true |
| EXOC7 | Intact, Biogrid | true |
| EXOC8 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
