---
type: protein-evaluation
gene: "SYCP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYCP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYCP2 / SCP2 |
| 蛋白名称 | Synaptonemal complex protein 2 |
| 蛋白大小 | 1530 aa / 175.6 kDa |
| UniProt ID | Q9BX26 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1530 aa / 175.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024835, IPR041322, IPR040560; Pfam: PF18581, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- condensed chromosome, centromeric region (GO:0000779)
- lateral element (GO:0000800)
- nucleus (GO:0005634)
- synaptonemal complex (GO:0000795)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCP2 |

**关键文献**:
1. Meiotic protein SYCP2 confers resistance to DNA-damaging agents through R-loop-mediated DNA repair.. *Nature communications*. PMID: 38383600
2. A homozygous frameshift variant in SYCP2 caused meiotic arrest and non-obstructive azoospermia.. *Clinical genetics*. PMID: 37337432
3. Unveiling the expression and mechanistic role of SYCP2 in cervical lesions.. *Discover oncology*. PMID: 41182523
4. Protein SYCP2 provides a link between transverse filaments and lateral elements of mammalian synaptonemal complexes.. *Chromosoma*. PMID: 19034475
5. ABL1-mediated tyrosine phosphorylation of SYCP2 contributes to transcription-coupled homologous recombination and platinum resistance in ovarian cancer.. *NAR cancer*. PMID: 40918650

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 24.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 62.2% |
| 有序区域 (pLDDT>70) 占比 | 35.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 35.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024835, IPR041322, IPR040560; Pfam: PF18581, PF18584 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCP3 | 0.998 | 0.230 | — |
| SYCP1 | 0.991 | 0.000 | — |
| TEX11 | 0.961 | 0.000 | — |
| SYCE2 | 0.904 | 0.000 | — |
| SYCE1 | 0.901 | 0.000 | — |
| TEX12 | 0.900 | 0.000 | — |
| SYCE3 | 0.893 | 0.000 | — |
| ADARB1 | 0.862 | 0.000 | — |
| STAG3 | 0.855 | 0.000 | — |
| SMC1B | 0.800 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ligA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 无 | pLDDT=54.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SYCP2 — Synaptonemal complex protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1530 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BX26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196074-SYCP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYCP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BX26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
