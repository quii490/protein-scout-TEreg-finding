---
type: protein-evaluation
gene: "GPM6B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPM6B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPM6B / M6B |
| 蛋白名称 | Neuronal membrane glycoprotein M6-b |
| 蛋白大小 | 265 aa / 29.0 kDa |
| UniProt ID | Q13491 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 265 aa / 29.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001614, IPR018237; Pfam: PF01275 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane raft (GO:0045121)
- myelin sheath (GO:0043209)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: M6B |

**关键文献**:
1. GPM6B regulates osteoblast function and induction of mineralization by controlling cytoskeleton and matrix vesicle release.. *Journal of bone and mineral research : the official journal of the American Society for Bone and Mineral Research*. PMID: 21638316
2. A mutant allele of glycoprotein M6-B (Gpm6b) facilitates behavioral flexibility but increases delay discounting.. *Genes, brain, and behavior*. PMID: 35243767
3. Predominant monomorphism of the RIT2 and GPM6B exceptionally long GA blocks in human and enriched divergent alleles in the disease compartment.. *Genetica*. PMID: 34984576
4. Identification of GPM6A and GPM6B as potential new human lymphoid leukemia-associated oncogenes.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 24916915
5. Gpm6b deficiency impairs sensorimotor gating and modulates the behavioral response to a 5-HT2A/C receptor agonist.. *Behavioural brain research*. PMID: 24768641

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 38.9% |
| 置信残基 (pLDDT 70-90) 占比 | 41.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.6% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 80.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.3，有序区 80.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001614, IPR018237; Pfam: PF01275 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLRA2 | 0.692 | 0.000 | — |
| GDI1 | 0.691 | 0.000 | — |
| NTNG2 | 0.685 | 0.000 | — |
| NTNG1 | 0.678 | 0.000 | — |
| PTPRZ1 | 0.663 | 0.000 | — |
| GRPR | 0.660 | 0.047 | — |
| GLUD2 | 0.649 | 0.000 | — |
| SLC6A4 | 0.649 | 0.254 | — |
| HCCS | 0.613 | 0.000 | — |
| TRAPPC2 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| ERGIC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NME2P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STX1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MTNR1B | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:26514267|imex:IM-24624 |
| TM9SF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 无 | pLDDT=82.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPM6B — Neuronal membrane glycoprotein M6-b，非常新颖，仅有少数基础研究。
2. 蛋白大小265 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13491
- Protein Atlas: https://www.proteinatlas.org/ENSG00000046653-GPM6B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPM6B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13491
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13491-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
