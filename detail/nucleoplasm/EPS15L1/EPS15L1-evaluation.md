---
type: protein-evaluation
gene: "EPS15L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPS15L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPS15L1 / EPS15R |
| 蛋白名称 | Epidermal growth factor receptor substrate 15-like 1 |
| 蛋白大小 | 864 aa / 94.3 kDa |
| UniProt ID | Q9UBC2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPS15L1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPS15L1/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cell membrane; Nucleus; Membrane, coated pit |
| 蛋白大小 | 8/10 | ×1 | 8 | 864 aa / 94.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR018247, IPR002048, IPR000261, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Cell membrane; Nucleus; Membrane, coated pit | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- clathrin coat of coated pit (GO:0030132)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- presynapse (GO:0098793)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EPS15R |

**关键文献**:
1. The landscape of long noncoding RNA-involved and tumor-specific fusions across various cancers.. *Nucleic acids research*. PMID: 33275145
2. Mutagenesis Screen Identifies agtpbp1 and eps15L1 as Essential for T lymphocyte Development in Zebrafish.. *PloS one*. PMID: 26161877
3. Analysis of Human Papilloma Virus Content and Integration in Mucoepidermoid Carcinoma.. *Viruses*. PMID: 36366450
4. Analysis of potential genes, immunological and antioxidant profiles associated with trypanosomiasis susceptibility in dromedary camels.. *Veterinary parasitology*. PMID: 39059159
5. Stable and EGF-Induced Temporal Interactome Profiling of CBL and CBLB Highlights Their Signaling Complex Diversity.. *Journal of proteome research*. PMID: 34134489

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.8 |
| 高置信度残基 (pLDDT>90) 占比 | 18.8% |
| 置信残基 (pLDDT 70-90) 占比 | 29.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 39.7% |
| 有序区域 (pLDDT>70) 占比 | 48.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPS15L1/EPS15L1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=65.8），有序残基占 48.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR000261, IPR018159; Pfam: PF12763 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS15 | 0.990 | 0.700 | — |
| ITSN2 | 0.986 | 0.875 | — |
| STON2 | 0.984 | 0.794 | — |
| EPN1 | 0.981 | 0.480 | — |
| EPN2 | 0.973 | 0.297 | — |
| EPN3 | 0.969 | 0.297 | — |
| FCHO1 | 0.959 | 0.452 | — |
| ITSN1 | 0.955 | 0.875 | — |
| AP2S1 | 0.946 | 0.795 | — |
| AP2B1 | 0.933 | 0.770 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Eps15 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:9446614 |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| ITSN2 | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| Zwint | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| hutU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cbl | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |
| Cblb | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.8 + PDB: 无 | pLDDT=65.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Nucleus; Membrane, coated pit / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. EPS15L1 — Epidermal growth factor receptor substrate 15-like 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小864 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127527-EPS15L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPS15L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBC2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPS15L1/EPS15L1-PAE.png]]




