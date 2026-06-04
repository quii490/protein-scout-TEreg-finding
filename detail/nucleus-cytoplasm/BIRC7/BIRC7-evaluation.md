---
type: protein-evaluation
gene: "BIRC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BIRC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BIRC7 / KIAP, LIVIN, MLIAP, RNF50 |
| 蛋白名称 | Baculoviral IAP repeat-containing protein 7 |
| 蛋白大小 | 298 aa / 32.8 kDa |
| UniProt ID | Q96CA5 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:37:57 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm; UniProt: Nucleus, C... |
| 蛋白大小 | 10/10 | x1 | 10 | 298 aa / 32.8 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=42 篇 (41-60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=71.7; PDB: 1OXN, 1OXQ, ... |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 5; Pfam: 2; IPR001370, IPR050784... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **133.5/180** | |
| **归一化总分 (/1.83)** | | | **73.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Centrosome, Cytosol | Enhanced |
| UniProt | Nucleus, Cytoplasm, Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 298 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 286 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAP, LIVIN, MLIAP, RNF50 |

**关键文献**:
1. Livin/BIRC7 gene expression as a possible diagnostic biomarker for endometrial hyperplasia and carcinoma.. *Journal, genetic engineering & biotechnology*. PMID: 34568983
2. BIRC7 and KLF4 expression in benign and malignant lesions of pancreas and their clinicopathological significance.. *Cancer biomarkers : section A of Disease markers*. PMID: 27802195
3. Expression of BIRC7 protein and mRNA in non-Hodgkin's lymphoma.. *Leukemia & lymphoma*. PMID: 16840203
4. BIRC7 is Beneficial for Melanoma Progression and Hypoxic Response.. *Clinical, cosmetic and investigational dermatology*. PMID: 35747741
5. BIRC7 promotes epithelial-mesenchymal transition and metastasis in papillary thyroid carcinoma through restraining autophagy.. *American journal of cancer research*. PMID: 32064154

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 47.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 34.9% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 1OXN, 1OXQ, 1OY7, 1TW6, 2I3H, 2I3I, 3F7G, 3F7H, 3F7I, 3GT9, 3GTA, 3UW5, 4AUQ |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=71.7），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001370, IPR050784, IPR001841, IPR013083, IPR017907; Pfam: PF00653, PF13920 |

**染色质调控潜力分析**: 存在 7 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CASP9 | 0.998 | 0.862 | -- |
| CASP7 | 0.993 | 0.485 | -- |
| CASP3 | 0.992 | 0.727 | -- |
| UBE2D2 | 0.989 | 0.964 | -- |
| DIABLO | 0.988 | 0.907 | -- |
| DIABLO-2 | 0.971 | 0.766 | -- |
| UBC | 0.955 | 0.948 | -- |
| RPS27A | 0.944 | 0.940 | -- |
| BIRC6 | 0.922 | 0.091 | -- |
| UBB | 0.920 | 0.905 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CASP9 | pull down | pubmed:11801603 |
| DIABLO | pull down | pubmed:11801603 |
| HTRA2 | pull down | pubmed:11801603 |
| CASP3 | enzymatic study | pubmed:11084335 |
| HIP2 | two hybrid array | imex:IM-11696|pubmed:19549727 |
| TLE5 | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| PHF1 | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| DDX6 | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| BIRC2 | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| TSGA10IP | two hybrid array | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 1OXN, 1OXQ, 1OY7 | pLDDT=71.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 73.0/100

**核心优势**:
1. 蛋白大小298 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. 已有PDB实验结构：1OXN, 1OXQ, 1OY7。
3. 存在 7 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96CA5
- Protein Atlas: https://www.proteinatlas.org/search/BIRC7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BIRC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96CA5
- STRING: https://string-db.org/network/9606.BIRC7
- Packet data timestamp: 2026-06-03 03:37:57
