---
type: protein-evaluation
gene: "EXO1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXO1 — REJECTED (研究热度过高 (PubMed strict=550，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXO1 / EXOI, HEX1 |
| 蛋白名称 | Exonuclease 1 |
| 蛋白大小 | 846 aa / 94.1 kDa |
| UniProt ID | Q9UQ84 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 846 aa / 94.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=550 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.5; PDB: 3QE9, 3QEA, 3QEB, 5UZV, 5V04, 5V05, 5V06 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036279, IPR037315, IPR008918, IPR029060, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 550 |
| PubMed broad count | 1090 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EXOI, HEX1 |

**关键文献**:
1. Promotion of DNA end resection by BRCA1-BARD1 in homologous recombination.. *Nature*. PMID: 39261729
2. Cytosolic DNA sensing by cGAS/STING promotes TRPV2-mediated Ca(2+) release to protect stressed replication forks.. *Molecular cell*. PMID: 36696898
3. Rad51 determines pathway usage in post-replication repair.. *Nature communications*. PMID: 41519855
4. Mutant huntingtin protein induces MLH1 degradation, DNA hyperexcision, and cGAS-STING-dependent apoptosis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38498709
5. PCAF promotes R-loop resolution via histone acetylation.. *Nucleic acids research*. PMID: 38936834

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.5 |
| 高置信度残基 (pLDDT>90) 占比 | 39.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 50.1% |
| 有序区域 (pLDDT>70) 占比 | 43.2% |
| 可用 PDB 条目 | 3QE9, 3QEA, 3QEB, 5UZV, 5V04, 5V05, 5V06, 5V07, 5V08, 5V09 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.5），有序残基占 43.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036279, IPR037315, IPR008918, IPR029060, IPR044752; Pfam: PF00867, PF00752 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MSH2 | 0.999 | 0.956 | — |
| MLH1 | 0.999 | 0.943 | — |
| BLM | 0.998 | 0.907 | — |
| WRN | 0.998 | 0.585 | — |
| DNA2 | 0.998 | 0.588 | — |
| RAD51 | 0.997 | 0.559 | — |
| MSH6 | 0.996 | 0.433 | — |
| PMS2 | 0.995 | 0.713 | — |
| RBBP8 | 0.995 | 0.659 | — |
| MLH3 | 0.995 | 0.396 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP82 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15766533 |
| tos | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pnn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MSH2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10856833|imex:IM-20083 |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSP31 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.5 + PDB: 3QE9, 3QEA, 3QEB, 5UZV, 5V04,  | pLDDT=63.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EXO1 — Exonuclease 1，研究基础较多，新颖性有限。
2. 蛋白大小846 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 550 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 550 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQ84
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174371-EXO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQ84
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
