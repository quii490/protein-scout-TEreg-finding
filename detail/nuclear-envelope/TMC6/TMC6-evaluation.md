---
type: protein-evaluation
gene: "TMC6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMC6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMC6 / EVER1, EVIN1 |
| 蛋白名称 | Transmembrane channel-like protein 6 |
| 蛋白大小 | 805 aa / 90.0 kDa |
| UniProt ID | Q7Z403 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane; Nu |
| 蛋白大小 | 8/10 | ×1 | 8 | 805 aa / 90.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038900, IPR012496; Pfam: PF07810 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nuclear membrane (GO:0031965)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 90 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EVER1, EVIN1 |

**关键文献**:
1. Epidermodysplasia verruciformis.. *Current problems in dermatology*. PMID: 24643182
2. TMC6 functions as a GPCR-like receptor to sense noxious heat via Gαq signaling.. *Cell discovery*. PMID: 38886367
3. Contribution of TMC6 and TMC8 (EVER1 and EVER2) variants to cervical cancer susceptibility.. *International journal of cancer*. PMID: 21387292
4. Expression of a TMC6-TMC8-CIB1 heterotrimeric complex in lymphocytes is regulated by each of the components.. *The Journal of biological chemistry*. PMID: 32917726
5. Recent advances in cutaneous HPV infection.. *The Journal of dermatology*. PMID: 36601717

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 43.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 67.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.3，有序区 67.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038900, IPR012496; Pfam: PF07810 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC30A1 | 0.969 | 0.000 | — |
| SYNGR2 | 0.907 | 0.000 | — |
| STAT3 | 0.894 | 0.079 | — |
| EZH2 | 0.850 | 0.071 | — |
| HAVCR2 | 0.793 | 0.107 | — |
| CANX | 0.741 | 0.070 | — |
| TMC8 | 0.740 | 0.000 | — |
| TK1 | 0.713 | 0.000 | — |
| HNRNPL | 0.678 | 0.296 | — |
| NPM1 | 0.665 | 0.042 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PXK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CBARP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HSPA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZBTB2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| TTMP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SGCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TSPAN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.3 + PDB: 无 | pLDDT=72.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TMC6 — Transmembrane channel-like protein 6，非常新颖，仅有少数基础研究。
2. 蛋白大小805 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z403
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141524-TMC6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMC6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z403
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z403-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z403 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038900;IPR012496; |
| Pfam | PF07810; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141524-TMC6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| B4GAT1 | Bioplex | false |
| C3orf52 | Bioplex | false |
| CLEC14A | Bioplex | false |
| FASLG | Bioplex | false |
| GP5 | Bioplex | false |
| GP9 | Bioplex | false |
| GPR182 | Bioplex | false |
| JPH3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
