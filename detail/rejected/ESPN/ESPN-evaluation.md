---
type: protein-evaluation
gene: "ESPN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ESPN — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESPN / DFNB36 |
| 蛋白名称 | Espin |
| 蛋白大小 | 854 aa / 91.7 kDa |
| UniProt ID | B1AK53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Cytoplasm, cytoskeleton; Cell projection, stereocilium; Cell |
| 蛋白大小 | 8/10 | ×1 | 8 | 854 aa / 91.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR052420, IPR003124; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cell projection, stereocilium; Cell projection, microvillus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- brush border (GO:0005903)
- cytoplasm (GO:0005737)
- filamentous actin (GO:0031941)
- microvillus (GO:0005902)
- stereocilium (GO:0032420)
- stereocilium tip (GO:0032426)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 278 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DFNB36 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Molecular Analysis of Twelve Pakistani Families with Nonsyndromic or Syndromic Hearing Loss.. *Genetic testing and molecular biomarkers*. PMID: 28281779
3. ESPN activates ZEB1-mediated EMT through the PI3K/AKT/mTOR axis to promote osteosarcoma metastasis.. *Journal of translational medicine*. PMID: 40346630
4. Shh agonist enhances maturation in homotypic Lgr5-positive inner ear organoids.. *Theranostics*. PMID: 40365278
5. The antagonistic transcription factors, EspM and EspN, regulate the ESX-1 secretion system in M. marinum.. *mBio*. PMID: 38445877

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 37.1% |
| 有序区域 (pLDDT>70) 占比 | 52.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.0），有序残基占 52.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR052420, IPR003124; Pfam: PF12796, PF13637, PF02205 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYO3B | 0.985 | 0.797 | — |
| MYO3A | 0.972 | 0.487 | — |
| MYO15A | 0.970 | 0.126 | — |
| EPS8 | 0.959 | 0.045 | — |
| WHRN | 0.958 | 0.099 | — |
| FSCN1 | 0.949 | 0.166 | — |
| EPS8L2 | 0.949 | 0.045 | — |
| TWF2 | 0.926 | 0.100 | — |
| MYO1A | 0.880 | 0.000 | — |
| MYO7A | 0.878 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| TTC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SHKBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| GOLGA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAD51 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| IPO4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SMARCD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RABGAP1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EEF1AKMT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.0 + PDB: 无 | pLDDT=68.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell projection, stereoci / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ESPN — Espin，非常新颖，仅有少数基础研究。
2. 蛋白大小854 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B1AK53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187017-ESPN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B1AK53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
