---
type: protein-evaluation
gene: "TOR1AIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOR1AIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOR1AIP1 / LAP1 |
| 蛋白名称 | Torsin-1A-interacting protein 1 |
| 蛋白大小 | 583 aa / 66.2 kDa |
| UniProt ID | Q5JTV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus inner membrane; Nucleus envelope; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 583 aa / 66.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 4TVS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038599, IPR008662, IPR046753, IPR046754; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Supported |
| UniProt | Nucleus inner membrane; Nucleus envelope; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LAP1 |

**关键文献**:
1. TOR1AIP1-Associated Nuclear Envelopathies.. *International journal of molecular sciences*. PMID: 37108075
2. [Congenital Myasthenic Syndromes].. *Brain and nerve = Shinkei kenkyu no shinpo*. PMID: 38191138
3. Multi-ancestry genetic analysis of gene regulation in coronary arteries prioritizes disease risk loci.. *Cell genomics*. PMID: 38190101
4. Selective loss of a LAP1 isoform causes a muscle-specific nuclear envelopathy.. *Neurogenetics*. PMID: 33405017
5. The whole blood transcriptional regulation landscape in 465 COVID-19 infected samples from Japan COVID-19 Task Force.. *Nature communications*. PMID: 35995775

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 32.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 55.6% |
| 有序区域 (pLDDT>70) 占比 | 38.9% |
| 可用 PDB 条目 | 4TVS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 38.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038599, IPR008662, IPR046753, IPR046754; Pfam: PF05609, PF20443 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TOR1A | 0.959 | 0.820 | — |
| LMNB1 | 0.783 | 0.161 | — |
| TOR3A | 0.761 | 0.292 | — |
| EMD | 0.755 | 0.126 | — |
| LMNA | 0.728 | 0.611 | — |
| TDRD5 | 0.668 | 0.000 | — |
| TOR2A | 0.657 | 0.292 | — |
| TMPO | 0.655 | 0.163 | — |
| TOR1B | 0.648 | 0.292 | — |
| TXN | 0.630 | 0.629 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q1EQW1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| CANX | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Mad2l1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SYNCRIP | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 4TVS | pLDDT=62.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Nucleus envelope; Nucleus / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TOR1AIP1 — Torsin-1A-interacting protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小583 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143337-TOR1AIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOR1AIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
