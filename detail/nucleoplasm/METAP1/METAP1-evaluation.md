---
type: protein-evaluation
gene: "METAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METAP1 / KIAA0094 |
| 蛋白名称 | Methionine aminopeptidase 1 |
| 蛋白大小 | 386 aa / 43.2 kDa |
| UniProt ID | P53582 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 386 aa / 43.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.4; PDB: 2B3H, 2B3K, 2B3L, 2G6P, 2GZ5, 2NQ6, 2NQ7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036005, IPR000994, IPR001714, IPR002467, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0094 |

**关键文献**:
1. NAC guides a ribosomal multienzyme complex for nascent protein processing.. *Nature*. PMID: 39169182
2. Proteome- and Transcriptome-Wide Genetic Analysis Identifies Biological Pathways and Candidate Drug Targets for Preeclampsia.. *Circulation. Genomic and precision medicine*. PMID: 39119725
3. Venous Endothelial Cell Transcriptomic Profiling Implicates METAP1 in Preeclampsia.. *Circulation research*. PMID: 39727051
4. Mechanism of cotranslational protein N-myristoylation in human cells.. *Molecular cell*. PMID: 40639378
5. Omics Assisted N-terminal Proteoform and Protein Expression Profiling On Methionine Aminopeptidase 1 (MetAP1) Deletion.. *Molecular & cellular proteomics : MCP*. PMID: 29317475

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.4 |
| 高置信度残基 (pLDDT>90) 占比 | 85.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 94.8% |
| 可用 PDB 条目 | 2B3H, 2B3K, 2B3L, 2G6P, 2GZ5, 2NQ6, 2NQ7, 4FLI, 4FLJ, 4FLK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2B3H, 2B3K, 2B3L, 2G6P, 2GZ5, 2NQ6, 2NQ7, 4FLI, 4FLJ, 4FLK）+ AlphaFold极高置信度预测（pLDDT=94.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036005, IPR000994, IPR001714, IPR002467, IPR031615; Pfam: PF00557, PF15801 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| METAP2 | 0.991 | 0.115 | — |
| RPL5 | 0.878 | 0.544 | — |
| RPL35 | 0.873 | 0.508 | — |
| RPL23 | 0.858 | 0.516 | — |
| RPL23A | 0.857 | 0.570 | — |
| CBWD2 | 0.843 | 0.835 | — |
| RPS3 | 0.823 | 0.295 | — |
| RPL11 | 0.806 | 0.470 | — |
| RPS18 | 0.801 | 0.292 | — |
| RPS11 | 0.788 | 0.236 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNG1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SYTL4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NBR1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZRANB1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.4 + PDB: 2B3H, 2B3K, 2B3L, 2G6P, 2GZ5,  | pLDDT=94.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
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
1. METAP1 — Methionine aminopeptidase 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小386 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53582
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164024-METAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53582
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53582-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P53582 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036005;IPR000994;IPR001714;IPR002467;IPR031615; |
| Pfam | PF00557;PF15801; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164024-METAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ZRANB1 | Intact, Biogrid | true |
| GH2 | Bioplex | false |
| GLRX3 | Intact | false |
| INCA1 | Intact | false |
| PLEKHG4 | Intact | false |
| PRKN | Biogrid | false |
| ZNG1A | Intact | false |
| ZNG1B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
