---
type: protein-evaluation
gene: "DHX36"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHX36 — REJECTED (研究热度过高 (PubMed strict=137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX36 |
| 蛋白名称 | ATP-dependent DNA/RNA helicase DHX36 |
| 蛋白大小 | 1008 aa / 114.8 kDa |
| UniProt ID | Q9H2U1 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DHX36/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DHX36/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytosol; Cytoplasm, Stress gr |
| 蛋白大小 | 8/10 | ×1 | 8 | 1008 aa / 114.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=137 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytosol; Cytoplasm, Stress granule; Nucleus speckle; Chromosome, telo... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 137 |
| PubMed broad count | 158 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DHX36 is a regulatory switch in the interferon-mediated antiviral response.. *Sci Adv*. PMID: 42213826
2. Non-telomeric TRF2 regulates differentiation-associated genes to maintain neural stem cell identity.. *J Cell Biol*. PMID: 41984089
3. Extreme Kinetic Stability and RNase Resistance of Human Telomerase RNA G-Quadruplexes Overcome by DHX36 Helicase.. *Adv Sci (Weinh)*. PMID: 41691481
4. Ultra-low-input rG4-seq reveals the RNA G-quadruplex regulome in gene expression and genome integrity.. *Nucleic Acids Res*. PMID: 41591846
5. Mitochondria-Associated Endoplasmic Reticulum Membrane Biomarkers in Coronary Heart Disease and Atherosclerosis: A Transcriptomic and Mendelian Randomization Study.. *Curr Issues Mol Biol*. PMID: 41614904

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 57.7% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 79.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DHX36/DHX36-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=82.4，有序区 79.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDX21 | 0.000 | 0.000 | — |
| DDX1 | 0.000 | 0.000 | — |
| DDX56 | 0.000 | 0.000 | — |
| MYD88 | 0.000 | 0.000 | — |
| IRF7 | 0.000 | 0.000 | — |
| DHX9 | 0.000 | 0.000 | — |
| DDX3X | 0.000 | 0.000 | — |
| DDX41 | 0.000 | 0.000 | — |
| DDX17 | 0.000 | 0.000 | — |
| DDX60 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H2U1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9BZ23 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P35232 | psi-mi:"MI:0034"(display technology) | pubmed:- |
| uniprotkb:Q9H2U1-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 无 | pLDDT=82.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytosol; Cytoplasm, / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DHX36 — ATP-dependent DNA/RNA helicase DHX36，研究基础较多，新颖性有限。
2. 蛋白大小1008 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 137 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2U1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174953-DHX36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2U1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DHX36/DHX36-PAE.png]]




