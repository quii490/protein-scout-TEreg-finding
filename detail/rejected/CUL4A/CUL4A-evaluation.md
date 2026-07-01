---
type: protein-evaluation
gene: "CUL4A"
date: 2026-06-26
tags: [protein-scout, nuclear-protein, evaluation, rejected]
status: rejected
---

## CUL4A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CUL4A / nan |
| 蛋白大小 | 667.0 aa / 77.7 kDa |
| UniProt ID | A0A0A0MR50 |
| 评估日期 | 2026-06-26 |

### 2. 评分总览 (新权重)

**淘汰原因**: PubMed >100, 研究过于成熟

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | HPA Approved+; Nucleoplasm |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 667 aa, 实验优势区间 |
| 🆕 研究新颖性 | 0/10 | ×5 | 0.0 | PubMed strict=300 篇 >100，触发淘汰 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | AF pLDDT=86.9, 高质量预测 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | 13 个 domain, 非经典调控类型 |
| 🔗 PPI | 10/10 | ×3 | 30.0 | Combined PPI degree=873 (极高) |
| **加权总分** | | | **106/180**** | |
| **归一化总分 (÷1.83)** | | | **淘汰**** | 互证: +2 (HPA+UniProt一致; 多源证据) |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus {ECO:0000256|ARBA:ARBA00004123}.. | 已标注 |

COMPARTMENTS nuclear_score=4.000: score=4.0; evidence=TAS; sources=Reactome;UniProt

**GO 定位/功能**:
- GO:0031464: Cul4A-RING E3 ubiquitin ligase complex (IEA:UniProtKB-ARBA)
- GO:0031465: Cul4B-RING E3 ubiquitin ligase complex (IEA:UniProtKB-ARBA)
- GO:0005737: cytoplasm (IEA:UniProtKB-SubCell)
- GO:0005634: nucleus (IEA:UniProtKB-SubCell)

IF 图像请参见: [https://www.proteinatlas.org/ENSG00000139842-CUL4A/subcellular](https://www.proteinatlas.org/ENSG00000139842-CUL4A/subcellular)

**PAE 图**: ![](https://alphafold.ebi.ac.uk/files/AF-A0A0A0MR50-F1-predicted_aligned_error_v6.png)

**结论**: HPA Approved+; Nucleoplasm。**评分: 9**。

#### 3.2 蛋白大小评估
667 aa, 实验优势区间。**评分: 9**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 300 |
| PubMed broad | 460 |
| Hotness | 较少 |

**关键文献**:
1. Ito T et al.. "Identification of a primary target of thalidomide teratogenicity.". *Science (New York, N.Y.)*. PMID: 20223979
2. Cui H et al.. "DTL promotes cancer progression by PDCD4 ubiquitin-dependent degradation.". *Journal of experimental & clinical cancer research : CR*. PMID: 31409387
3. Cao K et al.. "Analysis of multiple programmed cell death-related prognostic genes and functional validations of necroptosis-associated genes in oesophageal squamous cell carcinoma.". *EBioMedicine*. PMID: 38101299
4. Zein L et al.. "Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.". *Autophagy*. PMID: 39744815
5. Llerena Schiffmacher DA et al.. "The small CRL4(CSA) ubiquitin ligase component DDA1 regulates transcription-coupled repair dynamics.". *Nature communications*. PMID: 39075067

**评价**: PubMed strict=300 篇 >100，触发淘汰。**评分: 0**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 86.9 |
| >90% | 51.4% |
| 70-90% | 41.5% |
| 50-70% | 5.5% |
| <50% | 1.5% |

**评价**: AF pLDDT=86.9, 高质量预测。**评分: 7**。

#### 3.5 结构域分析
- **InterPro**: ; ; ; ; 
- **Pfam**: ; ; 

**评价**: 13 个 domain, 非经典调控类型。**评分: 5**。

#### 3.6 PPI 互作网络
Combined PPI degree (human): 873
Total nuclear PPI degree: 650  (STRING Nuclear: 104 + BioGRID Nuclear: 546)

**评价**: Combined PPI degree=873 (极高)。**评分: 10**。

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + UniProt + GO-CC | 一致 |
| 结构域 | InterPro + Pfam | 一致 |
| PPI | STRING + BioGRID | 有数据 |

**互证加分**: +2 (HPA+UniProt一致; 多源证据)

### 4. 总体评价

**淘汰**: PubMed >100。完整评估记录保留供审计。

### 5. 数据来源

- UniProt REST API
- AlphaFold Protein Structure Database
- PubMed E-utilities
- STRING/BioGRID protein-protein interaction
- Human Protein Atlas (HPA)
