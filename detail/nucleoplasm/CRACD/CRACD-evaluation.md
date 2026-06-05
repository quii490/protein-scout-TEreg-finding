---
type: protein-evaluation
gene: "CRACD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRACD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRACD / CRAD, KIAA1211 |
| 蛋白名称 | Capping protein-inhibiting regulator of actin dynamics |
| 蛋白大小 | 1233 aa / 136.8 kDa |
| UniProt ID | Q6ZU35 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 5/10 | x1 | 5 | 1233 aa / 136.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=54.1; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052853, IPR028030; Pfam: PF15262 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRAD, KIAA1211 |

**关键文献**:
1. Actin dysregulation induces neuroendocrine plasticity and immune evasion: a vulnerability of small cell lung cancer.. *Nature communications*. PMID: 41353272
2. Cracd Marks the First Wave of Meiosis during Spermatogenesis and Is Mis-Expressed in Azoospermia Mice.. *Journal of developmental biology*. PMID: 32962040
3. CRACD loss induces neuroendocrine cell plasticity of lung adenocarcinoma.. *Cell reports*. PMID: 38796854
4. CRACD suppresses neuroendocrinal plasticity of lung adenocarcinoma.. *bioRxiv : the preprint server for biology*. PMID: 37131761
5. CD47 and IFT57 Are Colinear Genes That Are Highly Coexpressed in Most Cancers and Exhibit Parallel Cancer-Specific Correlations with Survival.. *International journal of molecular sciences*. PMID: 39201643

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.1 |
| 高置信度残基 (pLDDT>90) 占比 | 6.9% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 17.8% |
| 低置信 (pLDDT<50) 占比 | 61.0% |
| 有序区域 (pLDDT>70) 占比 | 21.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.1），有序残基占 21.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052853, IPR028030; Pfam: PF15262 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAPZA2 | 0.635 | 0.572 | — |
| RNF157 | 0.547 | 0.000 | — |
| CAPZB | 0.482 | 0.474 | — |
| COL22A1 | 0.459 | 0.146 | — |
| PAICS | 0.452 | 0.000 | — |
| MAPK8 | 0.424 | 0.072 | — |
| ARL9 | 0.417 | 0.102 | — |
| CDH12 | 0.414 | 0.046 | — |
| BORCS8 | 0.401 | 0.000 | — |
| FAM122C | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.1 + PDB: 无 | pLDDT=54.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CRACD -- Capping protein-inhibiting regulator of actin dynamics，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1233 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZU35
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109265-CRACD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRACD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZU35
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000109265-CRACD/subcellular

![](https://images.proteinatlas.org/48148/1189_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/48148/1189_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/48148/1219_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/48148/1219_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/48148/1269_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/48148/1269_D1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZU35-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
