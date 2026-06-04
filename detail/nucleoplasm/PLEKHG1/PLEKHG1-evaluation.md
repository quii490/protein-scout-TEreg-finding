---
type: protein-evaluation
gene: "PLEKHG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHG1 / KIAA1209 |
| 蛋白名称 | Pleckstrin homology domain-containing family G member 1 |
| 蛋白大小 | 1385 aa / 155.4 kDa |
| UniProt ID | Q9ULL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1385 aa / 155.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1209 |

**关键文献**:
1. Risk Variants Associated With Normal Pressure Hydrocephalus: Genome-Wide Association Study in the FinnGen Cohort.. *Neurology*. PMID: 39141892
2. PLEKHG1: New Potential Candidate Gene for Periventricular White Matter Abnormalities.. *Genes*. PMID: 39202455
3. Gene-Centric Analysis of Preeclampsia Identifies Maternal Association at PLEKHG1.. *Hypertension (Dallas, Tex. : 1979)*. PMID: 29967039
4. Cancer type and gene signatures associated with breakthrough infections following COVID-19 mRNA vaccination.. *NPJ vaccines*. PMID: 40341527
5. The Rho guanine nucleotide exchange factor PLEKHG1 is activated by interaction with and phosphorylation by Src family kinase member FYN.. *The Journal of biological chemistry*. PMID: 35031323

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.8 |
| 高置信度残基 (pLDDT>90) 占比 | 18.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 64.0% |
| 有序区域 (pLDDT>70) 占比 | 27.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.8），有序残基占 27.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR043324; Pfam: PF00621, PF22697 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.729 | 0.473 | — |
| RAC1 | 0.644 | 0.384 | — |
| TEX51 | 0.571 | 0.000 | — |
| IYD | 0.567 | 0.000 | — |
| BCAS3 | 0.508 | 0.000 | — |
| PLEK | 0.502 | 0.000 | — |
| PLEK2 | 0.492 | 0.000 | — |
| MTHFD1L | 0.485 | 0.000 | — |
| ARMT1 | 0.472 | 0.000 | — |
| OXNAD1 | 0.471 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000512689.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0H2W8G8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ARPC1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| FARSA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| GSN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| MCM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| NACA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PLG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SPANXN5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SRRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.8 + PDB: 无 | pLDDT=49.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PLEKHG1 — Pleckstrin homology domain-containing family G member 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1385 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120278-PLEKHG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
