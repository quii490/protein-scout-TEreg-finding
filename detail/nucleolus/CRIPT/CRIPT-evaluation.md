---
type: protein-evaluation
gene: "CRIPT"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRIPT 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRIPT |
| 蛋白名称 | Cysteine-rich PDZ-binding protein |
| 蛋白大小 | 101 aa / 11.2 kDa |
| UniProt ID | Q9P021 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm; UniProt: Cytoplasm; Synapse; Cell projection, dendritic spine |
| 蛋白大小 | 8/10 | x1 | 8 | 101 aa / 11.2 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=78.8; PDB: 7DVQ |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR019367; Pfam: PF10235 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Synapse; Cell projection, dendritic spine | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- dendritic shaft (GO:0043198)
- dendritic spine (GO:0043197)
- glutamatergic synapse (GO:0098978)
- neuronal cell body (GO:0043025)
- postsynaptic density (GO:0014069)
- postsynaptic density, intracellular component (GO:0099092)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 86 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Structure of the activated human minor spliceosome.. *Science (New York, N.Y.)*. PMID: 33509932
2. CRIPT exonic deletion and a novel missense mutation in a female with short stature, dysmorphic features, microcephaly, and pigmentary abnormalities.. *American journal of medical genetics. Part A*. PMID: 27250922
3. Interaction Between CRIPT and PSD-95 Is Required for Proper Dendritic Arborization in Hippocampal Neurons.. *Molecular neurobiology*. PMID: 32157575
4. Functional interplay between protein domains in a supramodular structure involving the postsynaptic density protein PSD-95.. *The Journal of biological chemistry*. PMID: 31831623
5. Microtubule binding by CRIPT and its potential role in the synaptic clustering of PSD-95.. *Nature neuroscience*. PMID: 10570482

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.7% |
| 中等置信 (pLDDT 50-70) 占比 | 25.7% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 7DVQ |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=78.8，有序区 68.3%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019367; Pfam: PF10235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLG4 | 0.996 | 0.660 | — |
| ARMC7 | 0.942 | 0.922 | — |
| PHF5A | 0.905 | 0.900 | — |
| SF3B1 | 0.900 | 0.900 | — |
| SF3B3 | 0.900 | 0.900 | — |
| RNF113A | 0.900 | 0.900 | — |
| PRPF8 | 0.900 | 0.900 | — |
| SF3B2 | 0.900 | 0.900 | — |
| RBM48 | 0.865 | 0.800 | — |
| SCNM1 | 0.854 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 7DVQ | pLDDT=78.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Synapse; Cell projection, dendritic spi / Nucleoli fibrillar center; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CRIPT -- Cysteine-rich PDZ-binding protein，非常新颖，仅有少数基础研究。
2. 蛋白大小101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P021
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119878-CRIPT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRIPT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P021
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
