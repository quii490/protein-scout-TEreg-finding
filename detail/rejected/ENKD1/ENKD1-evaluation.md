---
type: protein-evaluation
gene: "ENKD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ENKD1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ENKD1 / C16orf48 |
| 蛋白名称 | Enkurin domain-containing protein 1 |
| 蛋白大小 | 346 aa / 38.8 kDa |
| UniProt ID | Q9H0I2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Centrosome, Basal body; 额外: Primary cilium; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 346 aa / 38.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027012, IPR052102; Pfam: PF13864 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Centrosome, Basal body; 额外: Primary cilium | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtu... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 9+0 non-motile cilium (GO:0097731)
- axoneme (GO:0005930)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- cilium (GO:0005929)
- cytoplasmic microtubule (GO:0005881)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf48 |

**关键文献**:
1. CYLD Maintains Retinal Homeostasis by Deubiquitinating ENKD1 and Promoting the Phagocytosis of Photoreceptor Outer Segments.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39373352
2. ENKD1 is a centrosomal and ciliary microtubule-associated protein important for primary cilium content regulation.. *The FEBS journal*. PMID: 35072334
3. ENKD1 attenuates antibacterial immunity by facilitating TRIM21-mediated RUBCN degradation to suppress LC3-associated phagocytosis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41187080
4. HDAC6 deacetylates ENKD1 to regulate mitotic spindle behavior and corneal epithelial homeostasis.. *EMBO reports*. PMID: 40155750
5. Upregulation of ENKD1 disrupts cellular homeostasis to promote lymphoma development.. *Journal of cellular physiology*. PMID: 36960713

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.3 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 26.6% |
| 中等置信 (pLDDT 50-70) 占比 | 26.9% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 63.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.3，有序区 63.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027012, IPR052102; Pfam: PF13864 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GFOD2 | 0.760 | 0.000 | — |
| CLHC1 | 0.561 | 0.000 | — |
| TMEM129 | 0.560 | 0.000 | — |
| CALY | 0.474 | 0.000 | — |
| ANKRD13D | 0.454 | 0.000 | — |
| C1orf35 | 0.439 | 0.000 | — |
| PNMA1 | 0.430 | 0.424 | — |
| SLC49A3 | 0.427 | 0.000 | — |
| STAC3 | 0.420 | 0.133 | — |
| SCRN1 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP70 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PDLIM7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSC22D4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.3 + PDB: 无 | pLDDT=76.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Plasma membrane, Centrosome, Basal body; 额外: Prima | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ENKD1 — Enkurin domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小346 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 深度机制分析

ENKD1（346 aa, pLDDT=76.3, IntAct 15条互作）是Enkurin结构域蛋白1。其结构域由Enkurin保守域（IPR027012、PF13864）和IRE1样激酶域（IPR052102）组成，SMART注释检出模块。ENKD1的核心功能覆盖中心体稳态、初级纤毛发生和有丝分裂纺锤体调控。其中心体/初级纤毛富集（GO:centrosome, GO:ciliary basal body, GO:centriole）与Enkurin家族蛋白在微管组织和钙信号调控中的功能一致。

从PPI互作网络角度，ENKD1的IntAct实验互作包含CEP70（中心体蛋白70, 酵母双杂交验证, PMID:16189514）、DVL2（Dishevelled-2）、多个PDZ支架蛋白（PDLIM7, MAGI1类）以及转录调控因子（TSC22D4、RBPMS和MDFI）。RBPMS（RNA结合蛋白）和MDFI（MyoD家族抑制因子）的实验互作提示ENKD1可能通过转录因子信号调控通路参与核内基因表达调控。DVL2作为Wnt/PCP和Wnt/β-catenin通路的关键信号中间体，在中心体/基体富集时调节平面细胞极性——DVL2与ENKD1的中心体共定位可能在纤毛依赖的Hedgehog信号和Wnt信号整合中发挥作用。

从TE调控角度，ENKD1评分63.1/100但核定位仅为2/10，已被淘汰。淘汰原因主要是HPA定位显示质膜、中心体和基体信号（不包含Nucleoplasm），与TE调控所需的最小核定位要求不符。即使IntAct检出与RBPMS和MDFI的互作，这些互作可能在中心粒/基体富集的局部信号域中发生而非核内。ENKD1对TE调控的潜在贡献仅限于中心体/纤毛功能障碍→Hh/Wnt通路扰动→ERV LTR活性的远端级联效应，这一因果链过于间接且缺乏实验证据支撑。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0I2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124074-ENKD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ENKD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0I2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-07-01）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0I2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
