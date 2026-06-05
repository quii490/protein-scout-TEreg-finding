---
type: protein-evaluation
gene: "GEMIN7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GEMIN7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GEMIN7 |
| 蛋白名称 | Gem-associated protein 7 |
| 蛋白大小 | 131 aa / 14.5 kDa |
| UniProt ID | Q9H840 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus, nucleoplasm; Nucleus, gem; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 131 aa / 14.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.3; PDB: 1Y96, 7BBL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR047575, IPR020338, IPR024642; Pfam: PF11095 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分** | | | **77.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, gem; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Gemini of Cajal bodies (GO:0097504)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- Sm-like protein family complex (GO:0120114)
- SMN complex (GO:0032797)
- SMN-Sm protein complex (GO:0034719)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Role of survival motor neuron complex components in small nuclear ribonucleoprotein assembly.. *The Journal of biological chemistry*. PMID: 19321448
2. Identification and characterization of Gemin7, a novel component of the survival of motor neuron complex.. *The Journal of biological chemistry*. PMID: 12065586
3. Gemin8 is required for the architecture and function of the survival motor neuron complex.. *The Journal of biological chemistry*. PMID: 17023415
4. The Gemin6-Gemin7 heterodimer from the survival of motor neurons complex has an Sm protein-like structure.. *Structure (London, England : 1993)*. PMID: 15939020
5. The construction and validation of an RNA binding protein-related prognostic model for bladder cancer.. *BMC cancer*. PMID: 33685397

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 57.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 24.4% |
| 低置信 (pLDDT<50) 占比 | 11.5% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 1Y96, 7BBL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1Y96, 7BBL）+ AlphaFold高质量预测（pLDDT=80.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047575, IPR020338, IPR024642; Pfam: PF11095 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRAP | 0.999 | 0.865 | — |
| GEMIN8 | 0.999 | 0.982 | — |
| GEMIN6 | 0.999 | 0.991 | — |
| DDX20 | 0.999 | 0.847 | — |
| GEMIN2 | 0.999 | 0.835 | — |
| GEMIN4 | 0.997 | 0.778 | — |
| GEMIN5 | 0.997 | 0.675 | — |
| SMN1 | 0.994 | 0.847 | — |
| SNRPE | 0.984 | 0.526 | — |
| SNRPD1 | 0.966 | 0.479 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GEMIN6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GOLM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| vpr | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| SMN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19928837|imex:IM-18940 |
| DDX20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STRAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GEMIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GEMIN8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Snrnp70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 1Y96, 7BBL | pLDDT=80.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, gem; Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GEMIN7 — Gem-associated protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小131 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H840
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142252-GEMIN7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GEMIN7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H840
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000142252-GEMIN7/subcellular

![](https://images.proteinatlas.org/52075/767_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/52075/767_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/52075/779_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/52075/779_H5_4_red_green.jpg)
![](https://images.proteinatlas.org/52075/865_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/52075/865_D1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H840-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
