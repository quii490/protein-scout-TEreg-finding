---
type: protein-evaluation
gene: "MATR3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MATR3 — REJECTED (研究热度过高 (PubMed strict=140，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MATR3 / KIAA0723 |
| 蛋白名称 | Matrin-3 |
| 蛋白大小 | 847 aa / 94.6 kDa |
| UniProt ID | P43243 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus matrix |
| 蛋白大小 | 8/10 | ×1 | 8 | 847 aa / 94.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=140 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034928, IPR034930, IPR000690, IPR003604, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- nuclear inner membrane (GO:0005637)
- nuclear matrix (GO:0016363)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 140 |
| PubMed broad count | 195 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0723 |

**关键文献**:
1. MATR3 promotes liver cancer progression by suppressing DHX58-mediated type I interferon response.. *Cancer letters*. PMID: 39276912
2. DDX1 methylation mediated MATR3 splicing regulates intervertebral disc degeneration by initiating chromatin reprogramming.. *Nature communications*. PMID: 40610464
3. Amyotrophic Lateral Sclerosis Overview.. **. PMID: 20301623
4. A protein assembly mediates Xist localization and gene silencing.. *Nature*. PMID: 32908311
5. ALS-associated RNA-binding proteins promote UNC13A transcription through REST downregulation.. *The EMBO journal*. PMID: 40707625

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 35.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 55.5% |
| 有序区域 (pLDDT>70) 占比 | 37.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 37.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034928, IPR034930, IPR000690, IPR003604, IPR012677 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TARDBP | 0.995 | 0.515 | — |
| NONO | 0.993 | 0.205 | — |
| SFPQ | 0.974 | 0.441 | — |
| HNRNPA1 | 0.950 | 0.620 | — |
| RBM14 | 0.949 | 0.588 | — |
| HNRNPC | 0.946 | 0.460 | — |
| HNRNPM | 0.928 | 0.446 | — |
| PSPC1 | 0.923 | 0.000 | — |
| HNRNPK | 0.923 | 0.677 | — |
| HNRNPH1 | 0.911 | 0.432 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000482895.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PCBP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 无 | pLDDT=57.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus matrix / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MATR3 — Matrin-3，研究基础较多，新颖性有限。
2. 蛋白大小847 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 140 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 140 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43243
- Protein Atlas: https://www.proteinatlas.org/ENSG00000015479-MATR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MATR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43243
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
