---
type: protein-evaluation
gene: "VWA3B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VWA3B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VWA3B |
| 蛋白名称 | von Willebrand factor A domain-containing protein 3B |
| 蛋白大小 | 1294 aa / 145.7 kDa |
| UniProt ID | Q502W6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1294 aa / 145.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032770, IPR002035, IPR036465; Pfam: PF15057, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Proteomic and structural comparison between cilia from primary ciliary dyskinesia patients with a DNAH5 defect.. *Frontiers in molecular biosciences*. PMID: 40746421
2. Transcriptomic profiling and bioinformatic insights into myocardial injury following aneurysmal subarachnoid hemorrhage.. *Frontiers in neurology*. PMID: 40630915
3. A homozygous mutation of VWA3B causes cerebellar ataxia with intellectual disability.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 26157035
4. Childhood-onset ataxia with dystonia: expanding the spectrum of VWA3B-related disorders.. *Journal of human genetics*. PMID: 41673450
5. Identification of genetic variants associated with a wide spectrum of phenotypes clinically diagnosed as Sanfilippo and Morquio syndromes using whole genome sequencing.. *Frontiers in genetics*. PMID: 37772257

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 47.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 62.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 62.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032770, IPR002035, IPR036465; Pfam: PF15057, PF13768 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAH10 | 0.637 | 0.000 | — |
| CFAP47 | 0.630 | 0.000 | — |
| TSNAXIP1 | 0.613 | 0.000 | — |
| FBXO36 | 0.603 | 0.000 | — |
| CFAP99 | 0.597 | 0.000 | — |
| CERKL | 0.594 | 0.000 | — |
| C1orf87 | 0.489 | 0.000 | — |
| TOM1L1 | 0.477 | 0.000 | — |
| OR2L2 | 0.448 | 0.000 | — |
| WDR38 | 0.442 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| INA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIRT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERPINB7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CTSH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AZGP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HAL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TGM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KPRP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SERPINA12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 无 | pLDDT=68.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VWA3B — von Willebrand factor A domain-containing protein 3B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1294 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q502W6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168658-VWA3B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VWA3B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q502W6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000168658-VWA3B/subcellular

![](https://images.proteinatlas.org/36701/430_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/36701/430_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/36701/432_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/36701/432_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/36701/441_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/36701/441_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q502W6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
