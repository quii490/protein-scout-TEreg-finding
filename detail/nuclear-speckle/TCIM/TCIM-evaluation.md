---
type: protein-evaluation
gene: "TCIM"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCIM 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCIM / C8orf4, TC1 |
| 蛋白名称 | Transcriptional and immune response regulator |
| 蛋白大小 | 106 aa / 12.3 kDa |
| UniProt ID | Q9NR00 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus speckle; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 106 aa / 12.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020282, IPR039580; Pfam: PF15063 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus speckle; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 160 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf4, TC1 |

**关键文献**:
1. Lifestyle management in polycystic ovary syndrome - beyond diet and physical activity.. *BMC endocrine disorders*. PMID: 36647089
2. The MIND diet, brain transcriptomic alterations, and dementia.. *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 39129336
3. Integration of osimertinib-targeted EGFR gene-associated differential gene expression in constructing a prognostic model for lung adenocarcinoma.. *Functional & integrative genomics*. PMID: 39661202
4. Elevated phagocytic capacity directs innate spinal cord repair.. *bioRxiv : the preprint server for biology*. PMID: 38915507
5. Identifying a CD8T cell signature in the tumor microenvironment to forecast gastric cancer outcomes from sequencing data.. *Journal of gastrointestinal oncology*. PMID: 39554559

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 30.2% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 32.1% |
| 低置信 (pLDDT<50) 占比 | 1.9% |
| 有序区域 (pLDDT>70) 占比 | 66.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 66.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020282, IPR039580; Pfam: PF15063 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAG4 | 0.880 | 0.000 | — |
| LSM1 | 0.798 | 0.000 | — |
| CBY1 | 0.669 | 0.000 | — |
| NOTCH2 | 0.565 | 0.000 | — |
| BAG2 | 0.495 | 0.000 | — |
| LSM6 | 0.478 | 0.000 | — |
| LSM8 | 0.474 | 0.000 | — |
| LSM3 | 0.470 | 0.000 | — |
| LSM7 | 0.465 | 0.000 | — |
| LSM2 | 0.463 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| livM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ACO2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SPOP | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| SMARCA4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| FBXW7 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| EGFR | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| AKT1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| BRAF | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| PTEN | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| PTPN11 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus speckle; Nu / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. TCIM — Transcriptional and immune response regulator，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小106 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NR00
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176907-TCIM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCIM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NR00
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000176907-TCIM/subcellular

![](https://images.proteinatlas.org/27188/1126_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/27188/1126_C5_4_red_green.jpg)
![](https://images.proteinatlas.org/27188/1276_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/27188/1276_C3_8_red_green.jpg)
![](https://images.proteinatlas.org/27188/214_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/27188/214_C12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NR00-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NR00 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR020282;IPR039580; |
| Pfam | PF15063; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176907-TCIM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXW7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
