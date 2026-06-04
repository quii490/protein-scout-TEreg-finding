---
type: protein-evaluation
gene: "NEUROD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEUROD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEUROD4 / ATH3, ATOH3, BHLHA4 |
| 蛋白名称 | Neurogenic differentiation factor 4 |
| 蛋白大小 | 331 aa / 37.0 kDa |
| UniProt ID | Q9HD90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 37.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050359, IPR036638, IPR022575, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 93 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATH3, ATOH3, BHLHA4 |

**关键文献**:
1. Molecular Mechanisms Underlying Ascl1-Mediated Astrocyte-to-Neuron Conversion.. *Stem cell reports*. PMID: 33577795
2. FOXO1 regulates expression of Neurod4 in the pituitary gland.. *Molecular and cellular endocrinology*. PMID: 38142853
3. Brn3a and Islet1 act epistatically to regulate the gene expression program of sensory differentiation.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 21734270
4. Multi-site phosphorylation regulates NeuroD4 activity during primary neurogenesis: a conserved mechanism amongst proneural proteins.. *Neural development*. PMID: 26084567
5. MiR-137 attenuates spinal cord injury by modulating NEUROD4 through reducing inflammation and oxidative stress.. *European review for medical and pharmacological sciences*. PMID: 29687839

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.7 |
| 高置信度残基 (pLDDT>90) 占比 | 25.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 25.1% |
| 低置信 (pLDDT<50) 占比 | 43.8% |
| 有序区域 (pLDDT>70) 占比 | 31.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.7），有序残基占 31.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050359, IPR036638, IPR022575, IPR016637; Pfam: PF00010, PF12533 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXN4 | 0.944 | 0.000 | — |
| ASCL1 | 0.801 | 0.094 | — |
| ISL1 | 0.771 | 0.048 | — |
| LHX3 | 0.721 | 0.000 | — |
| HOXB2 | 0.659 | 0.045 | — |
| VSX2 | 0.653 | 0.000 | — |
| PAX6 | 0.644 | 0.045 | — |
| PROX1 | 0.629 | 0.000 | — |
| HOXA2 | 0.609 | 0.045 | — |
| POU4F2 | 0.594 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GABRB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGEB4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| POTEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SRP19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCF12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADPRS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.7 + PDB: 无 | pLDDT=62.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NEUROD4 — Neurogenic differentiation factor 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HD90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123307-NEUROD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEUROD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HD90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
