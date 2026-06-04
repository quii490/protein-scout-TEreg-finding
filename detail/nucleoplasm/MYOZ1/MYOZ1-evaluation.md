---
type: protein-evaluation
gene: "MYOZ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYOZ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYOZ1 / MYOZ |
| 蛋白名称 | Myozenin-1 |
| 蛋白大小 | 299 aa / 31.7 kDa |
| UniProt ID | Q9NP98 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cell projection, pseudopodium |
| 蛋白大小 | 10/10 | ×1 | 10 | 299 aa / 31.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 7A8T, 7A8U, 7ANK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008438; Pfam: PF05556 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cell projection, pseudopodium | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- nucleus (GO:0005634)
- pseudopodium (GO:0031143)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MYOZ |

**关键文献**:
1. Genome-wide association and Mendelian randomisation analysis provide insights into the pathogenesis of heart failure.. *Nature communications*. PMID: 31919418
2. Integrated Proteomic and Metabolomic Analysis of Muscle Atrophy Induced by Hindlimb Unloading.. *Biomolecules*. PMID: 39858409
3. MYOZ1 Gene Promotes Muscle Growth and Development in Meat Ducks.. *Genes*. PMID: 36140742
4. Inhibiting Myozenin 1 Attenuated Muscular Dystrophy Pathology in mdx Mice by Enhancing Calcineurin Activity.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 41482823
5. The Expression of Myoz1 and ApoB is Positively Correlated with Meat Quality of Broiler Chicken.. *Veterinary medicine international*. PMID: 36624802

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 2.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 45.8% |
| 低置信 (pLDDT<50) 占比 | 37.1% |
| 有序区域 (pLDDT>70) 占比 | 17.0% |
| 可用 PDB 条目 | 7A8T, 7A8U, 7ANK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 17.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008438; Pfam: PF05556 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTN2 | 0.998 | 0.926 | — |
| MYOT | 0.987 | 0.000 | — |
| TCAP | 0.985 | 0.510 | — |
| FLNC | 0.980 | 0.626 | — |
| SYNPO2L | 0.933 | 0.000 | — |
| LDB3 | 0.914 | 0.000 | — |
| TNNC2 | 0.883 | 0.000 | — |
| ACTN3 | 0.872 | 0.084 | — |
| MYLPF | 0.869 | 0.000 | — |
| MYH7 | 0.819 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PNKP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ACTN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ACTN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| TRAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA6A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ACTN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PNMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 7A8T, 7A8U, 7ANK | pLDDT=57.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cell projection, pseudopodium / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MYOZ1 — Myozenin-1，非常新颖，仅有少数基础研究。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NP98
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177791-MYOZ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYOZ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NP98
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
