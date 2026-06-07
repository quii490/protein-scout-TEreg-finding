---
type: protein-evaluation
gene: "PYHIN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYHIN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PYHIN1 / IFIX |
| 蛋白名称 | Pyrin and HIN domain-containing protein 1 |
| 蛋白大小 | 492 aa / 55.1 kDa |
| UniProt ID | Q6K0P9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Nucleus, nucleoplasm; Nucleus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 492 aa / 55.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004020, IPR011029, IPR040205, IPR004021, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleoplasm; Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IFIX |

**关键文献**:
1. PYHIN1 correlates with CD8+ T cells infiltration and confers good patient survival in oral cancer.. *Journal of dental sciences*. PMID: 35028083
2. DNA sensor-associated type I interferon signaling is increased in ulcerative colitis and induces JAK-dependent inflammatory cell death in colonic organoids.. *American journal of physiology. Gastrointestinal and liver physiology*. PMID: 36165492
3. [Interferon-related gene array in predicting the efficacy of interferon therapy in chronic hepatitis B].. *Sheng wu yi xue gong cheng xue za zhi = Journal of biomedical engineering = Shengwu yixue gongchengxue zazhi*. PMID: 36854551
4. Mouse pyrin and HIN domain family member 1 (pyhin1) protein positively regulates LPS-induced IFN-β and NO production in macrophages.. *Innate immunity*. PMID: 23606517
5. PYHIN1 regulates pro-inflammatory cytokine induction rather than innate immune DNA sensing in airway epithelial cells.. *The Journal of biological chemistry*. PMID: 32102850

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 49.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 37.4% |
| 有序区域 (pLDDT>70) 占比 | 57.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.7，有序区 57.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004020, IPR011029, IPR040205, IPR004021, IPR012340; Pfam: PF02760, PF02758 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEFV | 0.788 | 0.000 | — |
| TRIM26 | 0.636 | 0.603 | — |
| SERPINB5 | 0.621 | 0.125 | — |
| MDM2 | 0.619 | 0.414 | — |
| DCAF1 | 0.609 | 0.605 | — |
| HP1BP3 | 0.592 | 0.510 | — |
| PYCARD | 0.546 | 0.000 | — |
| GZMK | 0.538 | 0.000 | — |
| GZMA | 0.533 | 0.000 | — |
| IL2RB | 0.522 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DUSP14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CALML3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| S100A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLCD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CALHM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VSIG8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HEPHL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 无 | pLDDT=71.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleoplasm; Nucleu / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PYHIN1 — Pyrin and HIN domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小492 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6K0P9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163564-PYHIN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PYHIN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6K0P9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000163564-PYHIN1/subcellular

![](https://images.proteinatlas.org/51224/1944_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/51224/1944_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/51224/1953_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/51224/1953_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6K0P9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6K0P9 |
| SMART | SM01289; |
| UniProt Domain [FT] | DOMAIN 1..88; /note="Pyrin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00061"; DOMAIN 199..399; /note="HIN-200"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00106" |
| InterPro | IPR004020;IPR011029;IPR040205;IPR004021;IPR012340; |
| Pfam | PF02760;PF02758; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163564-PYHIN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGRN | Biogrid | false |
| ATRX | Biogrid | false |
| BAZ1A | Biogrid | false |
| BAZ1B | Biogrid | false |
| BAZ2A | Biogrid | false |
| C1QBP | Biogrid | false |
| CBX5 | Biogrid | false |
| CTCF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
