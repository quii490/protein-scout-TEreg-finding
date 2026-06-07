---
type: protein-evaluation
gene: "KTI12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KTI12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KTI12 |
| 蛋白名称 | Protein KTI12 homolog |
| 蛋白大小 | 354 aa / 38.6 kDa |
| UniProt ID | Q96EK9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles, Cytoplasmic bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 354 aa / 38.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013641, IPR027417; Pfam: PF08433 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytoplasmic bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. tRNA binding to Kti12 is crucial for wobble uridine modification by Elongator.. *Nucleic acids research*. PMID: 40226916
2. Physical and functional interaction between Elongator and the chromatin-associated Kti12 protein.. *The Journal of biological chemistry*. PMID: 15772087
3. Overexpression of GhKTI12 Enhances Seed Yield and Biomass Production in Nicotiana Tabacum.. *Genes*. PMID: 35327981
4. DRL1, a homolog of the yeast TOT4/KTI12 protein, has a function in meristem activity and organ growth in plants.. *The Plant cell*. PMID: 12615938
5. Kti12, a PSTK-like tRNA dependent ATPase essential for tRNA modification by Elongator.. *Nucleic acids research*. PMID: 30916349

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 43.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 24.9% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.2，有序区 69.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013641, IPR027417; Pfam: PF08433 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELP3 | 0.926 | 0.594 | — |
| ELP1 | 0.909 | 0.456 | — |
| ELP4 | 0.831 | 0.129 | — |
| DPH3 | 0.809 | 0.000 | — |
| ELP5 | 0.752 | 0.413 | — |
| CTU1 | 0.730 | 0.110 | — |
| MOCS3 | 0.728 | 0.071 | — |
| PSTK | 0.693 | 0.000 | — |
| URM1 | 0.684 | 0.000 | — |
| SGCE | 0.673 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ELP3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| GPR35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CRM1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| Mgtor | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| piwi | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| LOC100278925 | psi-mi:"MI:0018"(two hybrid) | pubmed:36581701|imex:IM-29553 |
| LOC100502172 | psi-mi:"MI:0018"(two hybrid) | pubmed:36581701|imex:IM-29553 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 无 | pLDDT=74.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles, Cytoplasmic bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KTI12 — Protein KTI12 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EK9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198841-KTI12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KTI12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EK9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000198841-KTI12/subcellular

![](https://images.proteinatlas.org/31203/1443_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/31203/1443_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/31203/1479_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/31203/1479_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/31203/1516_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/31203/1516_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EK9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96EK9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013641;IPR027417; |
| Pfam | PF08433; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198841-KTI12/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELP1 | Biogrid | false |
| ELP3 | Biogrid | false |
| FHL3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
