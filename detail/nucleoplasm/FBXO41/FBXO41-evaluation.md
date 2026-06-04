---
type: protein-evaluation
gene: "FBXO41"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO41 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO41 / FBX41, KIAA1940 |
| 蛋白名称 | F-box only protein 41 |
| 蛋白大小 | 875 aa / 94.5 kDa |
| UniProt ID | Q8TF61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 875 aa / 94.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 8S1R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR057038, IPR052283, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX41, KIAA1940 |

**关键文献**:
1. Neuronal F-Box protein FBXO41 regulates synaptic transmission and hippocampal network maturation.. *iScience*. PMID: 35372812
2. F-box protein FBXO41 plays vital role in arsenic trioxide-mediated autophagic death of cancer cells.. *Toxicology and applied pharmacology*. PMID: 35278439
3. OTX2 expression contributes progression of gastric cancer in young adults.. *Scientific reports*. PMID: 40341176
4. Loss of the neuron-specific F-box protein FBXO41 models an ataxia-like phenotype in mice with neuronal migration defects and degeneration in the cerebellum.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 26063905
5. Genetic Analysis of FBXO2, FBXO6, FBXO12, and FBXO41 Variants in Han Chinese Patients with Sporadic Parkinson's Disease.. *Neuroscience bulletin*. PMID: 28341977

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 42.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 39.0% |
| 有序区域 (pLDDT>70) 占比 | 56.0% |
| 可用 PDB 条目 | 8S1R |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 56.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR057038, IPR052283, IPR032675; Pfam: PF12937, PF23165 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.843 | 0.331 | — |
| CUL1 | 0.792 | 0.074 | — |
| NEDD8 | 0.515 | 0.070 | — |
| UBE2M | 0.510 | 0.000 | — |
| CAND1 | 0.506 | 0.000 | — |
| DCUN1D3 | 0.499 | 0.000 | — |
| NAE1 | 0.499 | 0.000 | — |
| UBA3 | 0.499 | 0.000 | — |
| SMARCD2 | 0.470 | 0.000 | — |
| FBXO21 | 0.461 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15070733|imex:IM-19870 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| Tsc1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Dlgap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Shank3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| BMI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |
| SYNGAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| ENST00000521871 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 8S1R | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO41 — F-box only protein 41，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小875 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TF61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163013-FBXO41/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO41
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TF61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
