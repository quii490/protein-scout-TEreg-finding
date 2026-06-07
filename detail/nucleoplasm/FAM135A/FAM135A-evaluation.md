---
type: protein-evaluation
gene: "FAM135A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM135A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM135A / KIAA1411 |
| 蛋白名称 | Protein FAM135A |
| 蛋白大小 | 1515 aa / 169.8 kDa |
| UniProt ID | Q9P2D6 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM135A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM135A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1515 aa / 169.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029058, IPR022122, IPR007751, IPR044294; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.5/180** | |
| **归一化总分** | | | **69.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1411 |

**关键文献**:
1. GRPR-induced FAM135A expression promote perineural invasion in prostate cancer.. *Molecular cancer*. PMID: 41250119
2. Deciphering novel common gene signatures for rheumatoid arthritis and systemic lupus erythematosus by integrative analysis of transcriptomic profiles.. *PloS one*. PMID: 36928613
3. Identification of candidate genes that underlie the QTL on chromosome 1 that mediates genetic differences in stress-ethanol interactions.. *Physiological genomics*. PMID: 25991709
4. Whole-Genome Resequencing Reveals Population Structure and Loci Associated with Growth and Meat-Quality Traits in Meigu Yanying Chickens.. *Animals : an open access journal from MDPI*. PMID: 41751003
5. Construction of miRNA-target networks using microRNA profiles of CVB3-infected HeLa cells.. *Scientific reports*. PMID: 31784561

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 30.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 51.0% |
| 有序区域 (pLDDT>70) 占比 | 45.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM135A/FAM135A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 45.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR022122, IPR007751, IPR044294; Pfam: PF12394, PF05057 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RND1 | 0.579 | 0.161 | — |
| ENSP00000497305 | 0.570 | 0.000 | — |
| FAM81A | 0.442 | 0.000 | — |
| ZNF727 | 0.434 | 0.000 | — |
| ABHD16B | 0.407 | 0.000 | — |
| MTRNR2L12 | 0.400 | 0.000 | — |
| ABHD13 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCBD1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EEA1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RAB5A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRAF3IP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| BET1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 无 | pLDDT=59.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM135A — Protein FAM135A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1515 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2D6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082269-FAM135A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM135A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2D6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM135A/FAM135A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2D6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR022122;IPR007751;IPR044294; |
| Pfam | PF12394;PF05057; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000082269-FAM135A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLNS1A | Opencell | false |
| GLUL | Opencell | false |
| LAMP1 | Biogrid | false |
| RAB5A | Biogrid | false |
| RAB9A | Biogrid | false |
| RPL11 | Opencell | false |
| TUBA1B | Opencell | false |
| UBA52 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
