---
type: protein-evaluation
gene: "COMMD8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD8 |
| 蛋白名称 | COMM domain-containing protein 8 |
| 蛋白大小 | 183 aa / 21.1 kDa |
| UniProt ID | Q9NX08 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 21.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.2; PDB: 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017920, IPR047155, IPR047235, IPR055184; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Celastrol suppresses humoral immune responses and autoimmunity by targeting the COMMD3/8 complex.. *Science immunology*. PMID: 37000855
2. The COMMD3/8 complex determines GRK6 specificity for chemoattractant receptors.. *The Journal of experimental medicine*. PMID: 31088898
3. COMMD8 changes expression during initial phase of wasp venom immunotherapy.. *The journal of gene medicine*. PMID: 32559011
4. COMMD9 promotes TFDP1/E2F1 transcriptional activity via interaction with TFDP1 in non-small cell lung cancer.. *Cellular signalling*. PMID: 27871936
5. Non-Lethal heat shock induces COMMD gene activation and enhances pathogen defense in Procambarus clarkii.. *BMC genomics*. PMID: 41233790

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 66.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=87.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR047155, IPR047235, IPR055184; Pfam: PF07258, PF22838 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC22 | 0.986 | 0.840 | — |
| COMMD2 | 0.972 | 0.835 | — |
| COMMD10 | 0.970 | 0.839 | — |
| COMMD4 | 0.968 | 0.865 | — |
| COMMD5 | 0.962 | 0.832 | — |
| COMMD1 | 0.958 | 0.836 | — |
| COMMD9 | 0.955 | 0.751 | — |
| COMMD6 | 0.955 | 0.829 | — |
| COMMD3 | 0.955 | 0.837 | — |
| COMMD7 | 0.954 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NDUFA4L2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| COMMD1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELA | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ZNF474 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM167A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COMMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 8F2R, 8F2U, 8P0W | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
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
1. COMMD8 — COMM domain-containing protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX08
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169019-COMMD8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX08
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169019-COMMD8/subcellular

![](https://images.proteinatlas.org/35887/389_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/35887/389_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/35887/398_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/35887/398_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NX08-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
