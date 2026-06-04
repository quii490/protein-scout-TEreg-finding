---
type: protein-evaluation
gene: "TEX11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEX11 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX11 / ZIP4 |
| 蛋白名称 | Testis-expressed protein 11 |
| 蛋白大小 | 940 aa / 107.9 kDa |
| UniProt ID | Q8IYF3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 940 aa / 107.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013940, IPR042861, IPR011990, IPR019734; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- central element (GO:0000801)
- chromosome (GO:0005694)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZIP4 |

**关键文献**:
1. Identification and functional analysis of Tex11 and Meig1 in spermatogenesis of Hyriopsis cumingii.. *Frontiers in physiology*. PMID: 36091389
2. A novel TEX11 mutation induces azoospermia: a case report of infertile brothers and literature review.. *BMC medical genetics*. PMID: 29661171
3. Novel mutations of TEX11 are associated with non-obstructive azoospermia.. *Frontiers in endocrinology*. PMID: 37124723
4. Scrutinizing the human TEX genes in the context of human male infertility.. *Andrology*. PMID: 37594251
5. Downregulation of TEX11 promotes S-Phase progression and proliferation in colorectal cancer cells through the FOXO3a/COP1/c-Jun/p21 axis.. *Oncogene*. PMID: 36258021

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.0 |
| 高置信度残基 (pLDDT>90) 占比 | 56.0% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.0，有序区 89.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013940, IPR042861, IPR011990, IPR019734; Pfam: PF08631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BORCS8 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| TCHP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| POM121 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| C2CD6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CFAP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VIL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RIBC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NRIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STMN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF414 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.0 + PDB: 无 | pLDDT=86.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TEX11 — Testis-expressed protein 11，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小940 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYF3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120498-TEX11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYF3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
