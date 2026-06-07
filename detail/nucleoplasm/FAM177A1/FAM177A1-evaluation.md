---
type: protein-evaluation
gene: "FAM177A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM177A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM177A1 / C14orf24 |
| 蛋白名称 | Protein FAM177A1 |
| 蛋白大小 | 213 aa / 23.8 kDa |
| UniProt ID | Q8N128 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM177A1/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM177A1/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 213 aa / 23.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028260; Pfam: PF14774 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf24 |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. Loss of function of FAM177A1, a Golgi complex localized protein, causes a novel neurodevelopmental disorder.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 38767059
3. VPS13B is localized at the interface between Golgi cisternae and is a functional partner of FAM177A1.. *The Journal of cell biology*. PMID: 39331042
4. FAM177A1 Inhibits IL-1β-Induced Signaling by Impairing TRAF6-Ubc13 Association.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 34799425
5. Integration of transcriptomics and long-read genomics prioritizes structural variants in rare disease.. *Genome research*. PMID: 40113264

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.9% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 38.0% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM177A1/FAM177A1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028260; Pfam: PF14774 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRP54 | 0.541 | 0.000 | — |
| KRTAP13-4 | 0.506 | 0.000 | — |
| FAM204A | 0.473 | 0.434 | — |
| ODR4 | 0.467 | 0.467 | — |
| VPS13B | 0.457 | 0.435 | — |
| C19orf18 | 0.447 | 0.000 | — |
| RHOJ | 0.444 | 0.444 | — |
| MED29 | 0.441 | 0.000 | — |
| SYAP1 | 0.437 | 0.000 | — |
| FAM222B | 0.430 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK38L | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| JAGN1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SGPL1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ELOVL4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PBX3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DPM3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MRPS31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHOJ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 无 | pLDDT=63.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM177A1 — Protein FAM177A1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小213 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N128
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151327-FAM177A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM177A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N128
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM177A1/FAM177A1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N128 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028260; |
| Pfam | PF14774; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151327-FAM177A1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOXE3 | Bioplex | false |
| LORICRIN | Bioplex | false |
| TRAF6 | Biogrid | false |
| TUBB2B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
