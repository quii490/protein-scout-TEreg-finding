---
type: protein-evaluation
gene: "EXOSC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC7 / KIAA0116, RRP42 |
| 蛋白名称 | Exosome complex component RRP42 |
| 蛋白大小 | 291 aa / 31.8 kDa |
| UniProt ID | Q15024 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC7/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC7/IF_images/A-549_1.jpg|A-549]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus, nucleolus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 31.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.3; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001247, IPR015847, IPR036345, IPR050590, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus, nucleolus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasmic exosome (RNase complex) (GO:0000177)
- cytosol (GO:0005829)
- exosome (RNase complex) (GO:0000178)
- nuclear exosome (RNase complex) (GO:0000176)
- nucleolar exosome (RNase complex) (GO:0101019)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0116, RRP42 |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. The new landscape of differentially expression proteins in placenta tissues of gestational diabetes based on iTRAQ proteomics.. *Placenta*. PMID: 36473392
3. ZNF692 organizes a hub specialized in 40S ribosomal subunit maturation enhancing translation in rapidly proliferating cells.. *Cell reports*. PMID: 37851577
4. Characterization of RNA Processing Genes in Colon Cancer for Predicting Clinical Outcomes.. *Biomarker insights*. PMID: 39161926
5. Comprehensive bioinformatics analysis of EXOSC family genes in lung adenocarcinoma.. *Discover oncology*. PMID: 42171853

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.3 |
| 高置信度残基 (pLDDT>90) 占比 | 33.3% |
| 置信残基 (pLDDT 70-90) 占比 | 56.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 1.7% |
| 有序区域 (pLDDT>70) 占比 | 89.7% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC7/EXOSC7-PAE.png]]

**评价**: PDB实验结构（2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P）+ AlphaFold极高置信度预测（pLDDT=84.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001247, IPR015847, IPR036345, IPR050590, IPR027408; Pfam: PF01138, PF03725 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DIS3L | 0.999 | 0.998 | — |
| EXOSC4 | 0.999 | 0.999 | — |
| EXOSC8 | 0.999 | 0.997 | — |
| EXOSC6 | 0.999 | 0.997 | — |
| EXOSC5 | 0.999 | 0.997 | — |
| DIS3 | 0.999 | 0.999 | — |
| EXOSC10 | 0.999 | 0.998 | — |
| EXOSC9 | 0.999 | 0.997 | — |
| EXOSC1 | 0.999 | 0.997 | — |
| MPHOSPH6 | 0.999 | 0.980 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| DXO | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12419256 |
| EXOSC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12419256 |
| MTMR3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12419256 |
| IP6K1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Hnrnpk | psi-mi:"MI:0096"(pull down) | pubmed:16518874|imex:IM-11840 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| UBE2Q1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.3 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=84.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm; Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EXOSC7 — Exosome complex component RRP42，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15024
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075914-EXOSC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15024
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC7/EXOSC7-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15024 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001247;IPR015847;IPR036345;IPR050590;IPR027408;IPR020568; |
| Pfam | PF01138;PF03725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000075914-EXOSC7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DIS3L | Biogrid, Bioplex | true |
| EXOSC1 | Intact, Biogrid, Bioplex | true |
| EXOSC10 | Intact, Biogrid | true |
| EXOSC2 | Intact, Biogrid, Bioplex | true |
| EXOSC3 | Biogrid, Bioplex | true |
| EXOSC4 | Intact, Biogrid, Bioplex | true |
| EXOSC5 | Biogrid, Bioplex | true |
| EXOSC6 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
