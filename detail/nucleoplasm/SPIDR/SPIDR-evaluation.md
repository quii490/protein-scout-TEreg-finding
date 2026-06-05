---
type: protein-evaluation
gene: "SPIDR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPIDR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPIDR / KIAA0146 |
| 蛋白名称 | DNA repair-scaffolding protein |
| 蛋白大小 | 915 aa / 100.3 kDa |
| UniProt ID | Q14159 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 915 aa / 100.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR053054, IPR028026, IPR028032; Pfam: PF14950, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear chromosome (GO:0000228)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0146 |

**关键文献**:
1. SPIDR enables multiplexed mapping of RNA-protein interactions and uncovers a mechanism for selective translational suppression upon cell stress.. *Cell*. PMID: 40701149
2. Exploring the structural landscape of DNA maintenance proteins.. *Nature communications*. PMID: 39237506
3. SWS1-complex in premature ovarian insufficiency: SWSAP1 as a new POI gene.. *Human reproduction (Oxford, England)*. PMID: 40991243
4. Novel variants associated with premature ovarian insufficiency in Russian adolescents.. *Frontiers in endocrinology*. PMID: 41393291
5. Scaffolding protein SPIDR/KIAA0146 connects the Bloom syndrome helicase with homologous recombination repair.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 23509288

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 19.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 41.4% |
| 有序区域 (pLDDT>70) 占比 | 50.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 50.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053054, IPR028026, IPR028032; Pfam: PF14950, PF14951 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SWSAP1 | 0.899 | 0.609 | — |
| RAD51 | 0.884 | 0.292 | — |
| FIGNL1 | 0.870 | 0.510 | — |
| RMI1 | 0.680 | 0.292 | — |
| BLM | 0.671 | 0.292 | — |
| RMI2 | 0.663 | 0.292 | — |
| TOP3A | 0.647 | 0.292 | — |
| ZSWIM7 | 0.637 | 0.610 | — |
| XRCC3 | 0.628 | 0.000 | — |
| PLA2G10 | 0.617 | 0.617 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLA2G10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSWIM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAM83F | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SWSAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 无 | pLDDT=62.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPIDR — DNA repair-scaffolding protein，非常新颖，仅有少数基础研究。
2. 蛋白大小915 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14159
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164808-SPIDR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPIDR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14159
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000164808-SPIDR/subcellular

![](https://images.proteinatlas.org/41582/836_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/41582/836_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/41582/847_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/41582/847_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/41582/857_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/41582/857_C6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14159-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
