---
type: protein-evaluation
gene: "ELFN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELFN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELFN1 / PPP1R28 |
| 蛋白名称 | Protein ELFN1 |
| 蛋白大小 | 828 aa / 90.5 kDa |
| UniProt ID | P0C7U0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cell Junctions; UniProt: Membrane; Cell projection, dendrite; Cell projection, axon |
| 蛋白大小 | 8/10 | ×1 | 8 | 828 aa / 90.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000483, IPR055106, IPR001611, IPR003591, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions | Approved |
| UniProt | Membrane; Cell projection, dendrite; Cell projection, axon | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon terminus (GO:0043679)
- dendrite (GO:0030425)
- excitatory synapse (GO:0060076)
- glutamatergic synapse (GO:0098978)
- plasma membrane (GO:0005886)
- postsynaptic density membrane (GO:0098839)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 101 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPP1R28 |

**关键文献**:
1. Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD.. *Nature*. PMID: 40533550
2. Role of long non-coding RNA ELFN1-AS1 in carcinogenesis.. *Discover oncology*. PMID: 38478184
3. ELFN1 deficiency: The mechanistic basis and phenotypic spectrum of a neurodevelopmental disorder with epilepsy.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 40576023
4. Profiling the Impact of mGlu(7)/Elfn1 Protein Interactions on the Pharmacology of mGlu(7) Allosteric Modulators.. *ACS chemical neuroscience*. PMID: 40689847
5. ELFN1 is a new extracellular matrix (ECM)-associated protein.. *Life sciences*. PMID: 38986898

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 43.4% |
| 有序区域 (pLDDT>70) 占比 | 42.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 42.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR055106, IPR001611, IPR003591, IPR032675; Pfam: PF22986, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRM6 | 0.696 | 0.126 | — |
| CACNA1F | 0.677 | 0.074 | — |
| GRM7 | 0.664 | 0.126 | — |
| TRPM1 | 0.558 | 0.000 | — |
| IGSF9B | 0.549 | 0.067 | — |
| EGFLAM | 0.527 | 0.067 | — |
| GRM8 | 0.523 | 0.126 | — |
| GAD1 | 0.464 | 0.069 | — |
| GRIN2B | 0.459 | 0.000 | — |
| KCNC3 | 0.449 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| ELFN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 无 | pLDDT=61.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cell projection, dendrite; Cell projecti / Nucleoplasm, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. ELFN1 — Protein ELFN1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小828 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C7U0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000225968-ELFN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELFN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C7U0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
