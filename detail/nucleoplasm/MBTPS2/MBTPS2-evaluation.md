---
type: protein-evaluation
gene: "MBTPS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MBTPS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MBTPS2 / S2P |
| 蛋白名称 | Membrane-bound transcription factor site-2 protease |
| 蛋白大小 | 519 aa / 57.4 kDa |
| UniProt ID | O43462 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria, Cytosol; UniProt: Membrane; Cytoplasm; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 519 aa / 57.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=67 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001193, IPR036034, IPR008915; Pfam: PF02163 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria, Cytosol | Approved |
| UniProt | Membrane; Cytoplasm; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 67 |
| PubMed broad count | 116 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: S2P |

**关键文献**:
1. Update on the Genetics of Osteogenesis Imperfecta.. *Calcified tissue international*. PMID: 39127989
2. Osteogenesis Imperfecta: Mechanisms and Signaling Pathways Connecting Classical and Rare OI Types.. *Endocrine reviews*. PMID: 34007986
3. MBTPS2, a membrane bound protease, underlying several distinct skin and bone disorders.. *Journal of translational medicine*. PMID: 33743732
4. MBTPS2 acts as a regulator of lipogenesis and cholesterol synthesis through SREBP signalling in prostate cancer.. *British journal of cancer*. PMID: 36991255
5. Integrative multiomics analysis identifies key genes regulating intramuscular fat deposition during development.. *Poultry science*. PMID: 39447331

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.1，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001193, IPR036034, IPR008915; Pfam: PF02163 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MBTPS1 | 0.979 | 0.000 | — |
| ATF6 | 0.978 | 0.000 | — |
| CREB3L3 | 0.953 | 0.000 | — |
| SREBF2 | 0.930 | 0.109 | — |
| CREB3L1 | 0.926 | 0.000 | — |
| SREBF1 | 0.923 | 0.132 | — |
| SCAP | 0.918 | 0.000 | — |
| SAMM50 | 0.906 | 0.000 | — |
| CREB3L2 | 0.901 | 0.000 | — |
| CREB3L4 | 0.886 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SARAF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADAM30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NKAIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OR6T1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BSCL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C15orf32 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAM8A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000379484 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 无 | pLDDT=87.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Golgi apparatus membrane / Nucleoplasm, Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. MBTPS2 — Membrane-bound transcription factor site-2 protease，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小519 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 67 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43462
- Protein Atlas: https://www.proteinatlas.org/ENSG00000012174-MBTPS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MBTPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43462
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000012174-MBTPS2/subcellular

![](https://images.proteinatlas.org/9486/954_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/9486/954_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/9486/956_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/9486/956_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/9486/990_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/9486/990_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43462-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43462 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001193;IPR036034;IPR008915; |
| Pfam | PF02163; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000012174-MBTPS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM8A1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
