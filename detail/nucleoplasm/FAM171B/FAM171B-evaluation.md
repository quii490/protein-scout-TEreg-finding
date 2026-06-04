---
type: protein-evaluation
gene: "FAM171B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM171B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM171B / KIAA1946 |
| 蛋白名称 | Protein FAM171B |
| 蛋白大小 | 826 aa / 92.2 kDa |
| UniProt ID | Q6P995 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171B/IF_images/HAP1_1.jpg|HAP1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171B/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; 额外: Nucleoli, Cytosol; UniProt: Cytoplasmic granule; Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 826 aa / 92.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018890, IPR049175, IPR048530; Pfam: PF20771, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Cytoplasmic granule; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- membrane (GO:0016020)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1946 |

**关键文献**:
1. FAM171B stabilizes vimentin and enhances CCL2-mediated TAM infiltration to promote bladder cancer progression.. *Journal of experimental & clinical cancer research : CR*. PMID: 37915048
2. FAM171B is a novel polyglutamine protein widely expressed in the mammalian brain.. *Brain research*. PMID: 34052262
3. Finding Potential Drug Targets for Pre-Eclampsia Using Mendelian Randomisation and Colocalisation Analysis.. *American journal of reproductive immunology (New York, N.Y. : 1989)*. PMID: 40028697
4. FAM171B as a Novel Biomarker Mediates Tissue Immune Microenvironment in Pulmonary Arterial Hypertension.. *Mediators of inflammation*. PMID: 36248192
5. Genomic analysis of drug resistant pancreatic cancer cell line by combining long non-coding RNA and mRNA expression profling.. *International journal of clinical and experimental pathology*. PMID: 25755691

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 56.1% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171B/FAM171B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018890, IPR049175, IPR048530; Pfam: PF20771, PF10577 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NWD2 | 0.515 | 0.000 | — |
| OR4L1 | 0.507 | 0.000 | — |
| H2AP | 0.480 | 0.000 | — |
| FAM187B | 0.479 | 0.000 | — |
| TMEM88B | 0.464 | 0.000 | — |
| FAM189A1 | 0.449 | 0.000 | — |
| RPRD2 | 0.442 | 0.000 | — |
| TMEM145 | 0.440 | 0.000 | — |
| IGFL4 | 0.432 | 0.000 | — |
| FRG2B | 0.430 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MPP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CAMK2D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FAM171A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGFR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BMPR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MFAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM171A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MIB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 无 | pLDDT=56.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic granule; Membrane / Nucleoplasm, Mitochondria; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FAM171B — Protein FAM171B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小826 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P995
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144369-FAM171B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM171B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P995
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM171B/FAM171B-PAE.png]]




