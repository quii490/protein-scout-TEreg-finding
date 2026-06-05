---
type: protein-evaluation
gene: "CLXN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLXN — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLXN / EFCAB1, ODAD5 |
| 蛋白名称 | Calaxin |
| 蛋白大小 | 211 aa / 24.5 kDa |
| UniProt ID | Q9HAE3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cell projection, ci |
| 蛋白大小 | 10/10 | ×1 | 10 | 211 aa / 24.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR018247, IPR002048, IPR028846; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cell projection, cilium; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cilium (GO:0005929)
- sperm flagellum (GO:0036126)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EFCAB1, ODAD5 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. Pathogenic variants in CLXN encoding the outer dynein arm docking-associated calcium-binding protein calaxin cause primary ciliary dyskinesia.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 36727596
3. Dopamine receptor D2 regulates genes involved in germ cell movement and sperm motility in rat testes†.. *Biology of reproduction*. PMID: 37956402

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 77.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 88.6% |
| 可用 PDB 条目 | 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 88.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR028846; Pfam: PF13499 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HERC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCYL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AKAP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HDAC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PACSIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNX9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 7
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 8J07 | pLDDT=89.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cell proj / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 7 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLXN — Calaxin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小211 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAE3
- Protein Atlas: https://www.proteinatlas.org/search/CLXN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLXN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAE3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mid piece (approved)。来源: https://www.proteinatlas.org/ENSG00000034239-CLXN/subcellular

![](https://images.proteinatlas.org/23527/216_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23527/216_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23527/2169_B3_35_red_green.jpg)
![](https://images.proteinatlas.org/23527/2169_B3_49_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HAE3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
