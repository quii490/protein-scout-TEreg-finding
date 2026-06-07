---
type: protein-evaluation
gene: "FAM104A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM104A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM104A / FAM104A |
| 蛋白名称 | Protein VCF1 |
| 蛋白大小 | 186 aa / 19.5 kDa |
| UniProt ID | Q969W3 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM104A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM104A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 186 aa / 19.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029222; Pfam: PF15434 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

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

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM104A |

**关键文献**:
1. Identification of Renal Transplantation Rejection Biomarkers in Blood Using the Systems Biology Approach.. *Iranian biomedical journal*. PMID: 38224029
2. VCF1 is a p97/VCP cofactor promoting recognition of ubiquitylated p97-UFD1-NPL4 substrates.. *Nature communications*. PMID: 38503733
3. The FAM104 proteins VCF1/2 promote the nuclear localization of p97/VCP.. *eLife*. PMID: 37713320

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 8.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 73.1% |
| 低置信 (pLDDT<50) 占比 | 11.8% |
| 有序区域 (pLDDT>70) 占比 | 15.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM104A/FAM104A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 15.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029222; Pfam: PF15434 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.864 | 0.862 | — |
| CCDC127 | 0.848 | 0.000 | — |
| UBXN2B | 0.839 | 0.838 | — |
| CNOT10 | 0.779 | 0.000 | — |
| TADA2B | 0.748 | 0.000 | — |
| SUPT7L | 0.744 | 0.000 | — |
| MTO1 | 0.743 | 0.000 | — |
| UBXN6 | 0.742 | 0.692 | — |
| ASB7 | 0.718 | 0.000 | — |
| NSFL1C | 0.654 | 0.623 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBXN2B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VCF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| UBXN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSFL1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000403627 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 无 | pLDDT=61.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM104A — Protein VCF1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小186 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969W3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133193-FAM104A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM104A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969W3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM104A/FAM104A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q969W3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029222; |
| Pfam | PF15434; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133193-FAM104A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBXN2B | Intact, Biogrid | true |
| VCP | Intact, Biogrid | true |
| NSFL1C | Biogrid | false |
| PRKACA | Intact | false |
| SERPINH1 | Intact | false |
| TGFBR2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
