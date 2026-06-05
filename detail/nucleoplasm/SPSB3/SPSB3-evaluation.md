---
type: protein-evaluation
gene: "SPSB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPSB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPSB3 / C16orf31, SSB3 |
| 蛋白名称 | SPRY domain-containing SOCS box protein 3 |
| 蛋白大小 | 355 aa / 39.4 kDa |
| UniProt ID | Q6PJ21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 355 aa / 39.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.7; PDB: 8OKX, 8OL1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001870, IPR043136, IPR013320, IPR050672, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分** | | | **77.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul5-RING ubiquitin ligase complex (GO:0031466)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf31, SSB3 |

**关键文献**:
1. The CRL5-SPSB3 ubiquitin ligase targets nuclear cGAS for degradation.. *Nature*. PMID: 38418882
2. SPSB3 targets SNAIL for degradation in GSK-3β phosphorylation-dependent manner and regulates metastasis.. *Oncogene*. PMID: 29059170
3. Weighted gene co-expression network analysis reveals specific modules and biomarkers in Parkinson's disease.. *Neuroscience letters*. PMID: 32276105
4. Spsb3 is not essential for spermatogenesis and male fertility in mice.. *American journal of translational research*. PMID: 40225996
5. The E3 Ligases Spsb1 and Spsb4 Regulate RevErbα Degradation and Circadian Period.. *Journal of biological rhythms*. PMID: 31607207

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 61.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 8OKX, 8OL1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8OKX, 8OL1）+ AlphaFold高质量预测（pLDDT=76.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR013320, IPR050672, IPR001496; Pfam: PF00622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOC | 0.806 | 0.531 | — |
| CUL5 | 0.791 | 0.401 | — |
| CISH | 0.764 | 0.000 | — |
| ELOB | 0.713 | 0.188 | — |
| RNF7 | 0.627 | 0.142 | — |
| UBE2M | 0.522 | 0.000 | — |
| COMMD3 | 0.517 | 0.000 | — |
| NEDD8 | 0.515 | 0.000 | — |
| CCDC22 | 0.513 | 0.000 | — |
| UBE2F | 0.511 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CSNK2B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| GNPTG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUMBL | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZNF396 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DOCK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDK13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UXS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPGR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 8OKX, 8OL1 | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Mitochondria | 一致 |
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
1. SPSB3 — SPRY domain-containing SOCS box protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PJ21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162032-SPSB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPSB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PJ21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000162032-SPSB3/subcellular

![](https://images.proteinatlas.org/46602/783_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46602/783_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46602/785_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46602/785_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46602/865_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46602/865_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PJ21-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
