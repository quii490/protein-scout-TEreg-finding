---
type: protein-evaluation
gene: "FAM220A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM220A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM220A / C7orf70, SIPAR |
| 蛋白名称 | Protein FAM220A |
| 蛋白大小 | 259 aa / 28.0 kDa |
| UniProt ID | Q7Z4H9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM220A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM220A/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle,  |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 28.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040355, IPR029155; Pfam: PF15487 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle, acrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf70, SIPAR |

**关键文献**:
1. Comparative transcriptome analysis between rhesus macaques ( Macaca mulatta) and crab-eating macaques ( M. fascicularis).. *Zoological research*. PMID: 38485500
2. Exploration of signature-related FAM genes and correlation between FAM50A expression and the pathogenesis and prognosis of hepatocellular carcinoma.. *Translational cancer research*. PMID: 40950660
3. Dyrk1a Phosphorylation of α-Synuclein Mediating Apoptosis of Dopaminergic Neurons in Parkinson's Disease.. *Parkinson's disease*. PMID: 37469393
4. Dual inhibition of endothelial miR-92a-3p and miR-489-3p reduces renal injury-associated atherosclerosis.. *Atherosclerosis*. PMID: 30731284

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.0% |
| 中等置信 (pLDDT 50-70) 占比 | 30.1% |
| 低置信 (pLDDT<50) 占比 | 69.9% |
| 有序区域 (pLDDT>70) 占比 | 0.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM220A/FAM220A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=47.5），有序残基占 0.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040355, IPR029155; Pfam: PF15487 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPAG7 | 0.952 | 0.000 | — |
| CD34 | 0.495 | 0.000 | — |
| C7orf26 | 0.474 | 0.000 | — |
| OR51Q1 | 0.449 | 0.045 | — |
| PAWR | 0.449 | 0.000 | — |
| TBCCD1 | 0.440 | 0.000 | — |
| FAM222A | 0.439 | 0.000 | — |
| C7orf25 | 0.433 | 0.053 | — |
| ANKRD13D | 0.425 | 0.052 | — |
| ZNF142 | 0.419 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEK6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TEKT4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 2
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.5 + PDB: 无 | pLDDT=47.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory / Vesicles | 一致 |
| PPI | STRING + IntAct | 13 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM220A — Protein FAM220A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=47.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4H9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178397-FAM220A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM220A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4H9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM220A/FAM220A-PAE.png]]




