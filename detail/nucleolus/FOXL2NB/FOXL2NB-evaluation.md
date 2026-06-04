---
type: protein-evaluation
gene: "FOXL2NB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FOXL2NB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXL2NB / C3orf72 |
| 蛋白名称 | FOXL2 neighbor protein |
| 蛋白大小 | 175 aa / 18.6 kDa |
| UniProt ID | Q6ZUU3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 175 aa / 18.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.3; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- fibrillar center (GO:0001650)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf72 |

**关键文献**:
1. Transcriptional signature of induced neurons differentiates virologically suppressed people with HIV from people without HIV.. *JCI insight*. PMID: 41324907
2. Identification of Key Carcinogenic Genes in Colon Adenocarcinoma.. *Iranian journal of public health*. PMID: 35866125
3. A Transcriptional Signature of Induced Neurons Differentiates Virologically Suppressed People Living With HIV from People Without HIV.. *bioRxiv : the preprint server for biology*. PMID: 39484396
4. A six-mRNA prognostic model to predict survival in head and neck squamous cell carcinoma.. *Cancer management and research*. PMID: 30588115

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.3% |
| 中等置信 (pLDDT 50-70) 占比 | 34.9% |
| 低置信 (pLDDT<50) 占比 | 62.9% |
| 有序区域 (pLDDT>70) 占比 | 2.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.3），有序残基占 2.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFPL1 | 0.582 | 0.000 | — |
| FAM71E1 | 0.578 | 0.000 | — |
| KCNJ18 | 0.571 | 0.000 | — |
| SPINK6 | 0.512 | 0.000 | — |
| ZNF853 | 0.507 | 0.000 | — |
| ZNF570 | 0.507 | 0.000 | — |
| LRRC23 | 0.447 | 0.000 | — |
| GPATCH4 | 0.416 | 0.000 | — |
| PCOLCE2 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 9，IntAct interactions: 0
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.3 + PDB: 无 | pLDDT=48.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 9 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FOXL2NB — FOXL2 neighbor protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUU3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206262-FOXL2NB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXL2NB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUU3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
