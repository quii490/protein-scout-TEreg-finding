---
type: protein-evaluation
gene: "FAM168A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM168A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM168A / KIAA0280, TCRP1 |
| 蛋白名称 | Protein FAM168A |
| 蛋白大小 | 244 aa / 26.2 kDa |
| UniProt ID | Q92567 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168A/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 244 aa / 26.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029247; Pfam: PF14944 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0280, TCRP1 |

**关键文献**:
1. Two-stage genome-wide association study for the identification of causal variants underlying hoof disorders in cattle.. *Journal of dairy science*. PMID: 32229114
2. FAM168A participates in the development of chronic myeloid leukemia via BCR-ABL1/AKT1/NFκB pathway.. *BMC cancer*. PMID: 31291942
3. Weighted single-step GWAS identified candidate genes associated with carcass traits in a Chinese yellow-feathered chicken population.. *Poultry science*. PMID: 38134459
4. Composite selection signal analysis: Uncovering candidate genes and quantitative trait loci in Indian sheep breeds.. *PloS one*. PMID: 41880302
5. FAM168B identified as a novel candidate target for chimeric antigen receptor T cell-based cancer therapy.. *Discover oncology*. PMID: 41591662

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.2% |
| 中等置信 (pLDDT 50-70) 占比 | 25.0% |
| 低置信 (pLDDT<50) 占比 | 73.8% |
| 有序区域 (pLDDT>70) 占比 | 1.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168A/FAM168A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=45.7），有序残基占 1.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029247; Pfam: PF14944 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WWP2 | 0.795 | 0.786 | — |
| AKT1 | 0.579 | 0.166 | — |
| MT1X | 0.544 | 0.000 | — |
| UBASH3B | 0.528 | 0.521 | — |
| POLR2B | 0.483 | 0.479 | — |
| POLR2D | 0.479 | 0.479 | — |
| POLR2C | 0.477 | 0.473 | — |
| ARHGAP35 | 0.455 | 0.000 | — |
| WWP1 | 0.450 | 0.446 | — |
| RECQL5 | 0.450 | 0.446 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000064778.4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SNRPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| OTUB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| UBE2V1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| UBASH3B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BOLL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRR20D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DCUN1D1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.7 + PDB: 无 | pLDDT=45.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FAM168A — Protein FAM168A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小244 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92567
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054965-FAM168A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM168A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92567
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168A/FAM168A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92567 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029247; |
| Pfam | PF14944; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000054965-FAM168A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1orf94 | Intact | false |
| CALCOCO2 | Intact | false |
| DAB1 | Intact | false |
| DAZAP2 | Intact | false |
| DTX2 | Intact | false |
| HGS | Biogrid | false |
| KLHL42 | Intact | false |
| NAF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
