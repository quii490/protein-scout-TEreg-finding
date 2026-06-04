---
type: protein-evaluation
gene: "ERG28"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERG28 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERG28 / C14orf1 |
| 蛋白名称 | Ergosterol biosynthetic protein 28 homolog |
| 蛋白大小 | 140 aa / 15.9 kDa |
| UniProt ID | Q9UKR5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 140 aa / 15.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005352; Pfam: PF03694 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- transport vesicle (GO:0030133)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf1 |

**关键文献**:
1. The Non Catalytic Protein ERG28 has a Functional Role in Cholesterol Synthesis and is Coregulated Transcriptionally.. *Journal of lipid research*. PMID: 36216146
2. DNA repair genes RAD52 and SRS2, a cell wall synthesis regulator gene SMI1, and the membrane sterol synthesis scaffold gene ERG28 are important in efficient Agrobacterium-mediated yeast transformation with chromosomal T-DNA.. *BMC microbiology*. PMID: 27038795
3. Integrative exploration of the mutual gene signatures and immune microenvironment between benign prostate hyperplasia and castration-resistant prostate cancer.. *The aging male : the official journal of the International Society for the Study of the Aging Male*. PMID: 36974949
4. The molecular mechanism of a cis-regulatory adaptation in yeast.. *PLoS genetics*. PMID: 24068973
5. The ERG28-encoded protein, Erg28p, interacts with both the sterol C-4 demethylation enzyme complex as well as the late biosynthetic protein, the C-24 sterol methyltransferase (Erg6p).. *Biochimica et biophysica acta*. PMID: 15522820

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 85.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.1，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005352; Pfam: PF03694 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D3DLU4 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:16300994|imex:IM-19950 |
| ENSP00000256319.6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ALDH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CSTF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HNRNPH3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LSM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NSF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| POLR3F | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SAT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 无 | pLDDT=93.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERG28 — Ergosterol biosynthetic protein 28 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小140 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKR5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133935-ERG28/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERG28
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKR5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
