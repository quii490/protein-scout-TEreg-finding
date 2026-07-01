---
type: protein-evaluation
gene: "NGRN"
date: 2026-06-26
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NGRN 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NGRN / FI58G; HT020 |
| 蛋白名称 | Neugrin |
| 蛋白大小 | 291.0 aa / 32.4 kDa |
| UniProt ID | Q9NPE2 |
| 评估日期 | 2026-06-26 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | HPA Supported+UniProt IDA; Cytokinetic bridge; Mitochondria; Nucleoplasm |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 291 aa, 偏小 |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed strict=15 篇，非常新颖 |
| 🏗️ 三维结构 | 3/10 | ×3 | 9.0 | AF pLDDT=67.6, 低质量 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | 2 个 domain, 非经典调控类型 |
| 🔗 PPI | 9/10 | ×3 | 27.0 | Combined PPI degree=236 (很高) |
| **加权总分** | | | **130/180**** | |
| **归一化总分 (÷1.83)** | | | **72.7/100**** | 互证: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据) |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Cytokinetic bridge; Mitochondria; Nucleoplasm | Supported |
| UniProt | SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:11118320}. | 已标注 |

COMPARTMENTS nuclear_score=4.000: score=4.0; evidence=IDA; sources=HPA

**GO 定位/功能**:
- GO:0005576: extracellular region (IEA:UniProtKB-SubCell)
- GO:0005759: mitochondrial matrix (IDA:FlyBase)
- GO:0031966: mitochondrial membrane (IDA:UniProtKB)
- GO:0005739: mitochondrion (IDA:HPA)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IBA:GO_Central)

IF 图像请参见: [https://www.proteinatlas.org/ENSG00000182768-NGRN/subcellular](https://www.proteinatlas.org/ENSG00000182768-NGRN/subcellular)

**PAE 图**: ![](https://alphafold.ebi.ac.uk/files/AF-Q9NPE2-F1-predicted_aligned_error_v6.png)

**结论**: HPA Supported+UniProt IDA; Cytokinetic bridge; Mitochondria; Nucleoplasm。**评分: 8**。

#### 3.2 蛋白大小评估
291 aa, 偏小。**评分: 7**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 15 |
| PubMed broad | 33 |
| Hotness | 较多 |

**关键文献**:
1. Wang L et al.. "Identification of Mitochondrial and Succinylation Modification-Related Gene Signature in Ischemic Stroke.". *Molecular neurobiology*. PMID: 40261608
2. Tang X et al.. "Identification of Mitochondria-Related Genes Associated with Stroke Risk Through Multi-omics Summary Data-Based MR Analysis.". *Molecular neurobiology*. PMID: 41351645
3. White JA et al.. "Whole-exome sequencing of Nigerian benign prostatic hyperplasia reveals increased alterations in apoptotic pathways.". *The Prostate*. PMID: 38192023
4. Zhang M et al.. "BACE1 and Other Alzheimer's-Related Biomarkers in Cerebrospinal Fluid and Plasma Distinguish Alzheimer's Disease Patients from Cognitively-Impaired Neurosyphilis Patients.". *Journal of Alzheimer's disease : JAD*. PMID: 32804135
5. Luckett ES et al.. "Longitudinal APOE4- and amyloid-dependent changes in the blood transcriptome in cognitively intact older adults.". *Alzheimer's research & therapy*. PMID: 37438770

**评价**: PubMed strict=15 篇，非常新颖。**评分: 9**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 67.6 |
| >90% | 32.0% |
| 70-90% | 10.0% |
| 50-70% | 27.5% |
| <50% | 30.6% |

**评价**: AF pLDDT=67.6, 低质量。**评分: 3**。

#### 3.5 结构域分析

**评价**: 2 个 domain, 非经典调控类型。**评分: 5**。

#### 3.6 PPI 互作网络
Combined PPI degree (human): 236
Total nuclear PPI degree: 132  (STRING Nuclear: 3 + BioGRID Nuclear: 129)

**评价**: Combined PPI degree=236 (很高)。**评分: 9**。

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + UniProt + GO-CC | 一致 |
| 结构域 | InterPro + Pfam | 一致 |
| PPI | STRING + BioGRID | 有数据 |

**互证加分**: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据)

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**归一化总分**: 72.7/100

**定位分类**: nucleoplasm

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ICT1 | BioGRID | 0 |
| PRKAG3 | BioGRID | 0 |
| RBMS3 | BioGRID | 0 |
| TRA2A | BioGRID | 0 |
| RPL6 | BioGRID | 0 |
| HNRNPDL | BioGRID | 0 |
| ZC3H3 | BioGRID | 0 |
| MRPL4 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/41367/557_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41367/557_D11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41367/493_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41367/493_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/76267/1719_B2_19_cr5804907328f94_blue_red_green.jpg)
![](https://images.proteinatlas.org/76267/1719_B2_28_cr5804907c233ab_blue_red_green.jpg)


### 5. 数据来源

- UniProt REST API
- AlphaFold Protein Structure Database
- PubMed E-utilities
- STRING/BioGRID protein-protein interaction
- Human Protein Atlas (HPA)
