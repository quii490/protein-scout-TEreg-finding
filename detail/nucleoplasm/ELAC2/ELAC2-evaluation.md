---
type: protein-evaluation
gene: "ELAC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELAC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELAC2 / HPC2 |
| 蛋白名称 | Zinc phosphodiesterase ELAC protein 2 |
| 蛋白大小 | 826 aa / 92.2 kDa |
| UniProt ID | Q9BQ52 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELAC2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELAC2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Mitochondrion; Mitochondrion matrix, mitochondrion nucleoid; |
| 蛋白大小 | 8/10 | ×1 | 8 | 826 aa / 92.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=92 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.8; PDB: 8CBL, 8RR1, 8RR3, 8RR4, 8Z0P, 8Z1F, 8Z1G |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036866, IPR047151, IPR027794; Pfam: PF23023, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Mitochondrion; Mitochondrion matrix, mitochondrion nucleoid; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- mitochondrial nucleoid (GO:0042645)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 92 |
| PubMed broad count | 138 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HPC2 |

**关键文献**:
1. Fast Degradation of MecciRNAs by SUPV3L1/ELAC2 Provides a Novel Opportunity to Tackle Heart Failure With Exogenous MecciRNA.. *Circulation*. PMID: 39973625
2. ELAC2/RNaseZ-linked cardiac hypertrophy in Drosophila melanogaster.. *Disease models & mechanisms*. PMID: 34338278
3. ELAC2 polymorphisms and prostate cancer risk: a meta-analysis based on 18 case-control studies.. *Prostate cancer and prostatic diseases*. PMID: 20231859
4. Mutations in ELAC2 associated with hypertrophic cardiomyopathy impair mitochondrial tRNA 3'-end processing.. *Human mutation*. PMID: 31045291
5. Molecular basis of human nuclear and mitochondrial tRNA 3' processing.. *Nature structural & molecular biology*. PMID: 39747487

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 81.9% |
| 可用 PDB 条目 | 8CBL, 8RR1, 8RR3, 8RR4, 8Z0P, 8Z1F, 8Z1G, 9EY0, 9EY1, 9EY2 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELAC2/ELAC2-PAE.png]]

**评价**: PDB实验结构（8CBL, 8RR1, 8RR3, 8RR4, 8Z0P, 8Z1F, 8Z1G, 9EY0, 9EY1, 9EY2）+ AlphaFold极高置信度预测（pLDDT=82.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036866, IPR047151, IPR027794; Pfam: PF23023, PF13691 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELAC1 | 0.928 | 0.000 | — |
| SUPV3L1 | 0.864 | 0.000 | — |
| EXOG | 0.857 | 0.841 | — |
| TRMT10C | 0.853 | 0.312 | — |
| ENDOG | 0.853 | 0.841 | — |
| DCLRE1A | 0.824 | 0.000 | — |
| CPSF3 | 0.794 | 0.000 | — |
| RNASEL | 0.766 | 0.045 | — |
| TRNT1 | 0.757 | 0.000 | — |
| PRORP | 0.728 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ASCC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NDUFA7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CUX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GOLM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PUF60 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RNF123 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRMT10C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 8CBL, 8RR1, 8RR3, 8RR4, 8Z0P,  | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Mitochondrion matrix, mitochondrion / Nucleoplasm | 一致 |
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
1. ELAC2 — Zinc phosphodiesterase ELAC protein 2，研究基础较多，新颖性有限。
2. 蛋白大小826 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 92 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ52
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006744-ELAC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELAC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ52
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELAC2/ELAC2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ52 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036866;IPR047151;IPR027794; |
| Pfam | PF23023;PF13691; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000006744-ELAC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DNAJC7 | Biogrid, Opencell | true |
| BAG2 | Bioplex | false |
| BHLHA15 | Bioplex | false |
| CS | Biogrid | false |
| GLYATL1 | Bioplex | false |
| GRSF1 | Biogrid | false |
| HARS1 | Biogrid | false |
| HSCB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
