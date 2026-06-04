---
type: protein-evaluation
gene: "DNAH12"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAH12 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAH12 / DHC3, DLP12, DNAH12L, DNAH7L, DNAHC3 |
| 蛋白名称 | Dynein axonemal heavy chain 12 |
| 蛋白大小 | 3092 aa / 356.9 kDa |
| UniProt ID | Q6ZR08 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAH12/IF_images/GAMG_1.jpg|GAMG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome, Mid piece, Principal piece; 额外: Cytosol; UniProt: Cell projection, cilium, flagellum |
| 📏 蛋白大小 | 0/10 | ×1 | 0 | 3092 aa / 356.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.2; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003593, IPR035699, IPR041658, IPR042219, IPR026 |
| 🔗 PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 5 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Mid piece, Principal piece; 额外: Cytosol | Approved |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (1张)

**GO Cellular Component**:
- axonemal dynein complex (GO:0005858)
- microtubule (GO:0005874)
- sperm flagellum (GO:0036126)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DHC3, DLP12, DNAH12L, DNAH7L, DNAHC3, DNHD2 |

**关键文献**:
1. What Happened in the Hippocampal Axon in a Rat Model of Posttraumatic Stress Disorder.. *Cellular and molecular neurobiology*. PMID: 32930942
2. Identification of different lung adenocarcinoma subtypes in combination with antidiuretic hormone-related genes and creation of an associated index to predict prognosis and guide immunotherapy.. *Computational biology and chemistry*. PMID: 40412340
3. Further evidence from DNAH12 supports favorable fertility outcomes of infertile males with dynein axonemal heavy chain gene family variants.. *iScience*. PMID: 39071892
4. The essential role of cytoskeleton and ciliary abnormalities in the development of congenital pulmonary airway malformations.. *Pediatric surgery international*. PMID: 41264116
5. IQUB mutation induces radial spoke 1 deficiency causing asthenozoospermia with normal sperm morphology in humans and mice.. *Cell communication and signaling : CCS*. PMID: 39849482

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 53.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.2，有序区 85.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR035699, IPR041658, IPR042219, IPR026983; Pfam: PF12774, PF12775, PF12780 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAH6 | 0.981 | 0.000 | — |
| DNAH1 | 0.980 | 0.000 | — |
| DNAH5 | 0.947 | 0.000 | — |
| DNAH14 | 0.946 | 0.000 | — |
| DNAI1 | 0.883 | 0.263 | — |
| DNAI2 | 0.870 | 0.263 | — |
| DNAH2 | 0.852 | 0.000 | — |
| CCDC114 | 0.808 | 0.185 | — |
| DNAH9 | 0.795 | 0.000 | — |
| DNAH8 | 0.794 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NES | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| OCIAD2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| MAK | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| COQ8B | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 10 / 15 = 67%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 67%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 无 | pLDDT=83.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Centrosome, Mid piece, Principal piece; 额外: Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAH12 — Dynein axonemal heavy chain 12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小3092 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZR08
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174844-DNAH12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAH12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZR08
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:16:39




