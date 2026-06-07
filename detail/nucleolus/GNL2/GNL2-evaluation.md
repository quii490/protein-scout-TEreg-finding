---
type: protein-evaluation
gene: "GNL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNL2 / NGP1 |
| 蛋白名称 | Nucleolar GTP-binding protein 2 |
| 蛋白大小 | 731 aa / 83.7 kDa |
| UniProt ID | Q13823 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Nucleoli rim; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 731 aa / 83.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.2; PDB: 6LSS, 6LU8, 8FKZ, 8FL0, 8FL2, 8FL3, 8FL4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030378, IPR024929, IPR006073, IPR023179, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 40.5% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 26.3% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 6LSS, 6LU8, 8FKZ, 8FL0, 8FL2, 8FL3, 8FL4, 8FL6, 8FL7, 8FL9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6LSS, 6LU8, 8FKZ, 8FL0, 8FL2, 8FL3, 8FL4, 8FL6, 8FL7, 8FL9）+ AlphaFold极高置信度预测（pLDDT=73.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030378, IPR024929, IPR006073, IPR023179, IPR012971; Pfam: PF01926, PF08153 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPF2 | 0.999 | 0.938 | — |
| GTPBP4 | 0.999 | 0.992 | — |
| RSL24D1 | 0.999 | 0.986 | — |
| NSA2 | 0.999 | 0.984 | — |
| GNL3L | 0.997 | 0.817 | — |
| GNL3 | 0.997 | 0.817 | — |
| ZNF593 | 0.997 | 0.986 | — |
| NOP53 | 0.996 | 0.970 | — |
| MRTO4 | 0.995 | 0.937 | — |
| PES1 | 0.995 | 0.937 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DDX56 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LYAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FOS | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| G3BP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| G3BP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| ESR1 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13780|pubmed:21182205 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 6LSS, 6LU8, 8FKZ, 8FL0, 8FL2,  | pLDDT=73.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli, Nucleoli rim | 一致 |
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
1. GNL2 — Nucleolar GTP-binding protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小731 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13823
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134697-GNL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13823
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000134697-GNL2/subcellular

![](https://images.proteinatlas.org/27163/212_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/27163/212_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/27163/213_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/27163/213_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/27163/214_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/27163/214_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13823-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13823 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 207..368; /note="CP-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01058" |
| InterPro | IPR030378;IPR024929;IPR006073;IPR023179;IPR012971;IPR027417;IPR050755; |
| Pfam | PF01926;PF08153; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134697-GNL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| G3BP2 | Biogrid, Opencell | true |
| KRR1 | Biogrid, Bioplex | true |
| LYAR | Intact, Biogrid, Bioplex | true |
| NIFK | Biogrid, Bioplex | true |
| NPM1 | Biogrid, Opencell | true |
| RPL11 | Biogrid, Opencell | true |
| RPL31 | Biogrid, Bioplex | true |
| RPL35 | Biogrid, Opencell, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
