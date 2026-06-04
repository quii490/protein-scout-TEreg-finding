---
type: protein-evaluation
gene: "TPR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TPR — REJECTED (研究热度过高 (PubMed strict=1603，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPR |
| 蛋白名称 | Nucleoprotein TPR |
| 蛋白大小 | 2363 aa / 267.3 kDa |
| UniProt ID | P12270 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus; Nucleus membrane; Nucleus envelope; Nucleus, nuclea |
| 蛋白大小 | 2/10 | ×1 | 2 | 2363 aa / 267.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1603 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 5TO5, 5TO6, 5TO7, 5TVB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057974, IPR012929, IPR057577; Pfam: PF25481, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Enhanced |
| UniProt | Nucleus; Nucleus membrane; Nucleus envelope; Nucleus, nuclear pore complex; Cytoplasm; Cytoplasm, cy... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- kinetochore (GO:0000776)
- mitotic spindle (GO:0072686)
- nuclear envelope (GO:0005635)
- nuclear inclusion body (GO:0042405)
- nuclear membrane (GO:0031965)
- nuclear periphery (GO:0034399)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1603 |
| PubMed broad count | 6044 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The human nucleoporin Tpr protects cells from RNA-mediated replication stress.. *Nature communications*. PMID: 34168151
2. TPR is required for cytoplasmic chromatin fragment formation during senescence.. *eLife*. PMID: 39625470
3. TPR-containing proteins control protein organization and homeostasis for the endoplasmic reticulum.. *Critical reviews in biochemistry and molecular biology*. PMID: 31023093
4. Identification and Functional Analysis of Tomato TPR Gene Family.. *International journal of molecular sciences*. PMID: 33451131
5. AIP and its interacting partners.. *The Journal of endocrinology*. PMID: 21454441

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 1.4% |
| 置信残基 (pLDDT 70-90) 占比 | 49.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 37.9% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 5TO5, 5TO6, 5TO7, 5TVB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057974, IPR012929, IPR057577; Pfam: PF25481, PF25785, PF07926 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUP153 | 0.999 | 0.717 | — |
| NUP98 | 0.994 | 0.644 | — |
| RANBP2 | 0.990 | 0.206 | — |
| NUP50 | 0.981 | 0.000 | — |
| MAD1L1 | 0.973 | 0.622 | — |
| NUP107 | 0.972 | 0.789 | — |
| NUP85 | 0.967 | 0.427 | — |
| NUP93 | 0.966 | 0.480 | — |
| SEH1L | 0.966 | 0.310 | — |
| MCM3AP | 0.964 | 0.417 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRDX2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NUA | psi-mi:"MI:0018"(two hybrid) | pubmed:17513499|imex:IM-19373 |
| Kdm6a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11982|pubmed:17825402 |
| ENSMUSP00000112606.3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| GOLGA2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| GSC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| WDR5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| SF1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:26420826|imex:IM-23671 |
| ARHGAP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAGR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 5TO5, 5TO6, 5TO7, 5TVB | pLDDT=60.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus membrane; Nucleus envelope; Nucle / Nuclear membrane | 一致 |
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
1. TPR — Nucleoprotein TPR，研究基础较多，新颖性有限。
2. 蛋白大小2363 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 1603 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1603 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P12270
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047410-TPR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P12270
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
