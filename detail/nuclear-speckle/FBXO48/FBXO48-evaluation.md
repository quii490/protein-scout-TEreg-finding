---
type: protein-evaluation
gene: "FBXO48"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO48 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO48 / FBX48 |
| 蛋白名称 | F-box only protein 48 |
| 蛋白大小 | 155 aa / 18.2 kDa |
| UniProt ID | Q5FWF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 155 aa / 18.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX48 |

**关键文献**:
1. Design and Synthesis of AMPK Activators and GDF15 Inducers.. *Molecules (Basel, Switzerland)*. PMID: 37513338
2. Genome-wide in silico identification and characterization of the F-box gene family in water buffalo (Bubalus bubalis).. *Comparative biochemistry and physiology. Part D, Genomics & proteomics*. PMID: 41990482
3. A Fbxo48 inhibitor prevents pAMPKα degradation and ameliorates insulin resistance.. *Nature chemical biology*. PMID: 33495648
4. Genetic analysis of the FBXO48 gene in Chinese Han patients with Parkinson disease.. *Neuroscience letters*. PMID: 23485738

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 58.1% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 12.3% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.1，有序区 78.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810; Pfam: PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF684 | 0.624 | 0.000 | — |
| ETAA1 | 0.599 | 0.225 | — |
| ECT2L | 0.590 | 0.000 | — |
| OR5AP2 | 0.570 | 0.000 | — |
| FBXO47 | 0.566 | 0.000 | — |
| OR8B4 | 0.549 | 0.000 | — |
| OR1L8 | 0.511 | 0.000 | — |
| FOXD4L6 | 0.510 | 0.000 | — |
| ZNF793 | 0.500 | 0.000 | — |
| PNO1 | 0.488 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 无 | pLDDT=82.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO48 — F-box only protein 48，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小155 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5FWF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204923-FBXO48/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO48
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5FWF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
