---
type: protein-evaluation
gene: "DNAJC21"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC21 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC21 / DNAJA5 |
| 蛋白名称 | DnaJ homolog subfamily C member 21 |
| 蛋白大小 | 531 aa / 62.0 kDa |
| UniProt ID | Q5F1R6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 531 aa / 62.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051964, IPR001623, IPR018253, IPR036869, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- ribosome (GO:0005840)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DNAJA5 |

**关键文献**:
1. Shwachman-Diamond Syndrome.. **. PMID: 20301722
2. A landscape of germ line mutations in a cohort of inherited bone marrow failure patients.. *Blood*. PMID: 29146883
3. Protein and gene levels of DNAJC21 and RNF5 as drug targets for immune thrombocytopenia: optimized post-GWAS insights.. *Hematology (Amsterdam, Netherlands)*. PMID: 41175382
4. Shwachman-Diamond Syndrome: Molecular Mechanisms and Current Perspectives.. *Molecular diagnosis & therapy*. PMID: 30413969
5. Identification of prospective novel drug targets for immune thrombocytopenia by integrating plasma proteome.. *Hematology (Amsterdam, Netherlands)*. PMID: 40810909

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 32.4% |
| 有序区域 (pLDDT>70) 占比 | 60.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.2，有序区 60.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051964, IPR001623, IPR018253, IPR036869, IPR003604; Pfam: PF00226, PF12171, PF21884 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NMD3 | 0.821 | 0.477 | — |
| SBDS | 0.786 | 0.000 | — |
| EIF6 | 0.750 | 0.255 | — |
| EFL1 | 0.724 | 0.000 | — |
| SRP54 | 0.722 | 0.000 | — |
| PA2G4 | 0.718 | 0.483 | — |
| HSPA4 | 0.717 | 0.099 | — |
| ZNF622 | 0.705 | 0.468 | — |
| DNAJC24 | 0.687 | 0.053 | — |
| DNAJC2 | 0.640 | 0.260 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| MTERF1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CTCF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| HTT | psi-mi:"MI:0018"(two hybrid) | pubmed:17500595|imex:IM-21753 |
| RPL10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 无 | pLDDT=71.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleolus / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DNAJC21 — DnaJ homolog subfamily C member 21，非常新颖，仅有少数基础研究。
2. 蛋白大小531 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5F1R6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168724-DNAJC21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5F1R6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000168724-DNAJC21/subcellular

![](https://images.proteinatlas.org/40789/418_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/40789/418_H9_4_red_green.jpg)
![](https://images.proteinatlas.org/40789/424_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/40789/424_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/40789/429_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/40789/429_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5F1R6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
