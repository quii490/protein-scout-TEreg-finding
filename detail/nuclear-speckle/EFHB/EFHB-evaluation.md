---
type: protein-evaluation
gene: "EFHB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFHB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFHB / CFAP21 |
| 蛋白名称 | EF-hand domain-containing family member B |
| 蛋白大小 | 833 aa / 93.8 kDa |
| UniProt ID | Q8N7U6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nuclear bodies, Vesicles, Connecting piece; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskel |
| 蛋白大小 | 8/10 | ×1 | 8 | 833 aa / 93.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 7UNG, 8J07 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR018247, IPR002048, IPR057428, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies, Vesicles, Connecting piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, flagellum axoneme; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axonemal A tubule inner sheath (GO:0160111)
- axonemal microtubule (GO:0005879)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFAP21 |

**关键文献**:
1. Synthesis of (E)-Ethyl-4-(2-(furan-2-ylmethylene)hydrazinyl)benzoate, crystal structure, and studies of its interactions with human serum albumin by spectroscopic fluorescence and molecular docking methods.. *Spectrochimica acta. Part A, Molecular and biomolecular spectroscopy*. PMID: 30921660
2. Integrated analysis of the whole transcriptome of skeletal muscle reveals the ceRNA regulatory network related to the formation of muscle fibers in Tan sheep.. *Frontiers in genetics*. PMID: 36330447
3. Analysis of 19 genes for association with type I diabetes in the Type I Diabetes Genetics Consortium families.. *Genes and immunity*. PMID: 19956106
4. Genetic analysis and quantitative trait loci detection of udder traits in Jersey cattle.. *BMC genomics*. PMID: 41257575

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 4.7% |
| 置信残基 (pLDDT 70-90) 占比 | 44.9% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 49.6% |
| 可用 PDB 条目 | 7UNG, 8J07 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 49.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR057428, IPR040193; Pfam: PF13499, PF25325 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR90 | 0.944 | 0.944 | — |
| PACRG | 0.929 | 0.917 | — |
| ENKUR | 0.922 | 0.896 | — |
| EFHC2 | 0.910 | 0.900 | — |
| EFHC1 | 0.909 | 0.900 | — |
| CFAP20 | 0.899 | 0.899 | — |
| CFAP45 | 0.897 | 0.884 | — |
| TUBA1A | 0.891 | 0.877 | — |
| TUBB4B | 0.887 | 0.875 | — |
| C1orf158 | 0.869 | 0.817 | — |

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
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 7UNG, 8J07 | pLDDT=62.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm / Cytosol; 额外: Nuclear bodies, Vesicles, Connecting  | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFHB — EF-hand domain-containing family member B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小833 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7U6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163576-EFHB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFHB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7U6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
