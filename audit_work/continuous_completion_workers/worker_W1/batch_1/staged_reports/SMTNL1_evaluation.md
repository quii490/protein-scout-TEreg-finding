---
type: protein-evaluation
gene: "SMTNL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SMTNL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMTNL1 |
| 蛋白名称 | Smoothelin-like protein 1 |
| 蛋白大小 | 494 aa / 53.0 kDa |
| UniProt ID | A8MU46 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, myofibril; Cytoplasm, myofibril, sarcomere, I ban |
| 蛋白大小 | 10/10 | ×1 | 10 | 494 aa / 53.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001715, IPR036872, IPR050540; Pfam: PF00307 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, myofibril; Cytoplasm, myofibril, sarcomere, I band; Cytoplasm, myofibril, sarcomere, M li... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- contractile muscle fiber (GO:0043292)
- cytoplasm (GO:0005737)
- I band (GO:0031674)
- M band (GO:0031430)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Smoothelins and the Control of Muscle Contractility.. *Advances in pharmacology (San Diego, Calif.)*. PMID: 29310803
2. Smoothelin-Like Protein 1 Regulates Development and Metabolic Transformation of Skeletal Muscle in Hyperthyroidism.. *Frontiers in endocrinology*. PMID: 34675885
3. Mechanisms by which smoothelin-like protein 1 reverses insulin resistance in myotubules and mice.. *Molecular and cellular endocrinology*. PMID: 35508278
4. Smoothelin-like protein 1 promotes insulin sensitivity and modulates the contractile properties of endometrial epithelial cells with insulin resistance.. *Frontiers in endocrinology*. PMID: 38883605
5. Deletion of the protein kinase A/protein kinase G target SMTNL1 promotes an exercise-adapted phenotype in vascular smooth muscle.. *The Journal of biological chemistry*. PMID: 18310078

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.9 |
| 高置信度残基 (pLDDT>90) 占比 | 21.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 61.7% |
| 有序区域 (pLDDT>70) 占比 | 23.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.9），有序残基占 23.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001715, IPR036872, IPR050540; Pfam: PF00307 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1R12A | 0.803 | 0.000 | — |
| PRKG1 | 0.799 | 0.000 | — |
| SMTN | 0.727 | 0.000 | — |
| PDLIM3 | 0.714 | 0.000 | — |
| SMTNL2 | 0.615 | 0.000 | — |
| PDLIM5 | 0.605 | 0.000 | — |
| LDB3 | 0.592 | 0.000 | — |
| PDLIM1 | 0.580 | 0.000 | — |
| PDLIM7 | 0.576 | 0.000 | — |
| MYO3A | 0.572 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SH3GL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CEP250 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADAMTS13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.9 + PDB: 无 | pLDDT=55.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril; Cytoplasm, myofibril, sarcom / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SMTNL1 — Smoothelin-like protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小494 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MU46
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214872-SMTNL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMTNL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MU46
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
