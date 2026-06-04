---
type: protein-evaluation
gene: "DLGAP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLGAP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLGAP2 / C8orf68, DAP2, ERICH1-AS1 |
| 蛋白名称 | Disks large-associated protein 2 |
| 蛋白大小 | 1054 aa / 117.6 kDa |
| UniProt ID | Q9P1A6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Postsynaptic density; Synapse |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1054 aa / 117.6 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.4; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005026; Pfam: PF03359 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Postsynaptic density; Synapse | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- glutamatergic synapse (GO:0098978)
- neurofilament (GO:0005883)
- plasma membrane (GO:0005886)
- postsynaptic density (GO:0014069)
- postsynaptic specialization (GO:0099572)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf68, DAP2, ERICH1-AS1 |

**关键文献**:
1. Role of the DLGAP2 gene encoding the SAP90/PSD-95-associated protein 2 in schizophrenia.. *PloS one*. PMID: 24416398
2. Genotype-dependent epigenetic regulation of DLGAP2 in alcohol use and dependence.. *Molecular psychiatry*. PMID: 31745236
3. DNA methylation at DLGAP2 and risk for relapse in alcohol dependence during acamprosate treatment.. *Drug and alcohol dependence*. PMID: 38364647
4. Altered synaptic protein expression, aberrant spine morphology, and impaired spatial memory in Dlgap2 mutant mice, a genetic model of autism spectrum disorder.. *Cerebral cortex (New York, N.Y. : 1991)*. PMID: 36169576
5. Autism-associated gene Dlgap2 mutant mice demonstrate exacerbated aggressive behaviors and orbitofrontal cortex deficits.. *Molecular autism*. PMID: 25071926

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 73.8% |
| 有序区域 (pLDDT>70) 占比 | 14.2% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.4），有序残基占 14.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005026; Pfam: PF03359 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHANK3 | 0.988 | 0.861 | — |
| SHANK2 | 0.969 | 0.304 | — |
| DLG4 | 0.891 | 0.328 | — |
| DLGAP4 | 0.880 | 0.614 | — |
| DLG3 | 0.872 | 0.641 | — |
| DLGAP3 | 0.868 | 0.507 | — |
| SYNGAP1 | 0.865 | 0.240 | — |
| PTCHD1 | 0.853 | 0.000 | — |
| NLGN4X | 0.841 | 0.000 | — |
| SHANK1 | 0.841 | 0.290 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlg1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlg3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Shank1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10488079 |
| Dlgap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10488079 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.4 + PDB: 无 | pLDDT=48.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic density; Synapse / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLGAP2 — Disks large-associated protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1054 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1A6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198010-DLGAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLGAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1A6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:15:33
