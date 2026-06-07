---
type: protein-evaluation
gene: "HLTF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HLTF — REJECTED (研究热度过高 (PubMed strict=141，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HLTF / HIP116A, RNF80, SMARCA3, SNF2L3, ZBU1 |
| 蛋白名称 | DNA-dependent ATPase/E3 ubiquitin-protein ligase HLTF |
| 蛋白大小 | 1009 aa / 113.9 kDa |
| UniProt ID | Q14527 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1009 aa / 113.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=141 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 2MZN, 4HRE, 4HRH, 4S0N, 4XZF, 4XZG, 5BNH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014001, IPR001650, IPR014905, IPR027417, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nuclear matrix (GO:0016363)
- nuclear replication fork (GO:0043596)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 141 |
| PubMed broad count | 247 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HIP116A, RNF80, SMARCA3, SNF2L3, ZBU1 |

**关键文献**:
1. A comprehensive genetic catalog of human double-strand break repair.. *Science (New York, N.Y.)*. PMID: 41037600
2. The levels of p53 govern the hierarchy of DNA damage tolerance pathway usage.. *Nucleic acids research*. PMID: 38321962
3. USP37 counteracts HLTF to protect damaged replication forks and promote survival of BRCA1-deficient cells and PARP inhibitor resistance.. *Nucleic acids research*. PMID: 40548939
4. Acetyltransferase NAT10 inhibits T-cell immunity and promotes nasopharyngeal carcinoma progression through DDX5/HMGB1 axis.. *Journal for immunotherapy of cancer*. PMID: 39939141
5. HLTF disrupts Cas9-DNA post-cleavage complexes to allow DNA break processing.. *Nature communications*. PMID: 38987539

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 17.4% |
| 置信残基 (pLDDT 70-90) 占比 | 44.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 26.2% |
| 有序区域 (pLDDT>70) 占比 | 61.9% |
| 可用 PDB 条目 | 2MZN, 4HRE, 4HRH, 4S0N, 4XZF, 4XZG, 5BNH, 5K5F, 6KCS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 61.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014001, IPR001650, IPR014905, IPR027417, IPR038718; Pfam: PF00271, PF08797, PF00176 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD18 | 0.996 | 0.869 | — |
| UBE2N | 0.996 | 0.847 | — |
| UBE2V2 | 0.990 | 0.791 | — |
| PCNA | 0.973 | 0.917 | — |
| S100A10 | 0.963 | 0.928 | — |
| RAD51 | 0.920 | 0.766 | — |
| FANCM | 0.853 | 0.333 | — |
| HERC2 | 0.822 | 0.068 | — |
| MUS81 | 0.798 | 0.295 | — |
| RPA1 | 0.793 | 0.646 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CIAO1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HSPA8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SULT1C2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CDK9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| UBE2Z | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| USP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| S100a10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23415230|imex:IM-20914 |
| Anxa2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23415230|imex:IM-20914 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 2MZN, 4HRE, 4HRH, 4S0N, 4XZF,  | pLDDT=68.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HLTF — DNA-dependent ATPase/E3 ubiquitin-protein ligase HLTF，研究基础较多，新颖性有限。
2. 蛋白大小1009 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 141 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 141 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14527
- Protein Atlas: https://www.proteinatlas.org/ENSG00000071794-HLTF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HLTF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14527
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000071794-HLTF/subcellular

![](https://images.proteinatlas.org/15284/126_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/15284/126_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/15284/1891_F6_23_cr5bbcaa8fe600d_red_green.jpg)
![](https://images.proteinatlas.org/15284/1891_F6_4_cr5bbcaa8fe4c34_red_green.jpg)
![](https://images.proteinatlas.org/15284/201_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/15284/201_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14527-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14527 |
| SMART | SM00487;SM00490;SM00910;SM00184; |
| UniProt Domain [FT] | DOMAIN 435..606; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 837..996; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR014001;IPR001650;IPR014905;IPR027417;IPR038718;IPR049730;IPR000330;IPR050628;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00271;PF08797;PF00176;PF13923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000071794-HLTF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PCNA | Intact, Biogrid | true |
| RAD18 | Intact, Biogrid | true |
| UBE2N | Intact, Biogrid | true |
| CHFR | Biogrid | false |
| ETAA1 | Biogrid | false |
| H2AC4 | Biogrid | false |
| H4C1 | Biogrid | false |
| MYC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
