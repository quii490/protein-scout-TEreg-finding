---
type: protein-evaluation
gene: "CNTFR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNTFR — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=103，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNTFR |
| 蛋白名称 | Ciliary neurotrophic factor receptor subunit alpha |
| 蛋白大小 | 372 aa / 40.6 kDa |
| UniProt ID | P26992 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 372 aa / 40.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=103 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.5; PDB: 1UC6, 8D74, 8D7E, 8D7H, 8D7R |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003961, IPR036116, IPR003530, IPR007110, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- ciliary neurotrophic factor receptor complex (GO:0070110)
- CNTFR-CLCF1 complex (GO:0097059)
- external side of plasma membrane (GO:0009897)
- extrinsic component of membrane (GO:0019898)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 103 |
| PubMed broad count | 197 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The ciliary neurotrophic factor and its receptor, CNTFR alpha.. *Pharmaceutica acta Helvetiae*. PMID: 10812968
2. CNTFR Genotype and Sprint/power Performance: Case-control Association and Functional Studies.. *International journal of sports medicine*. PMID: 26837930
3. Cardiotrophin-like cytokine factor 1 forms a complex with IL12/IL23p40.. *Scientific reports*. PMID: 41027981
4. Potential Risk Factors and Therapeutic Targets for Dilated Cardiomyopathy Identified Through Mendelian Randomization Analysis.. *Journal of the American Heart Association*. PMID: 41467369
5. Crisponi/cold-induced sweating syndrome: Differential diagnosis, pathogenesis and treatment concepts.. *Clinical genetics*. PMID: 31497877

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.5 |
| 高置信度残基 (pLDDT>90) 占比 | 69.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 74.7% |
| 可用 PDB 条目 | 1UC6, 8D74, 8D7E, 8D7H, 8D7R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1UC6, 8D74, 8D7E, 8D7H, 8D7R）+ AlphaFold极高置信度预测（pLDDT=82.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR003530, IPR007110, IPR036179; Pfam: PF00041 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNTF | 0.999 | 0.831 | — |
| LIFR | 0.999 | 0.510 | — |
| IL27RA | 0.995 | 0.091 | — |
| CLCF1 | 0.994 | 0.600 | — |
| IL6ST | 0.986 | 0.328 | — |
| CTF1 | 0.979 | 0.000 | — |
| LIF | 0.938 | 0.000 | — |
| IL11 | 0.937 | 0.000 | — |
| IL6R | 0.910 | 0.000 | — |
| IL6 | 0.908 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000100027.4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-14969|pubmed:20340160 |
| APPBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| "wu:fc43a03" | psi-mi:"MI:0892"(solid phase assay) | pubmed:20802085|imex:IM-17303 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.5 + PDB: 1UC6, 8D74, 8D7E, 8D7H, 8D7R | pLDDT=82.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CNTFR — Ciliary neurotrophic factor receptor subunit alpha，研究基础较多，新颖性有限。
2. 蛋白大小372 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 103 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P26992
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122756-CNTFR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNTFR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P26992
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P26992-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
