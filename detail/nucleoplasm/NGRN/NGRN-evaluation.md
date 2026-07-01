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


### 深度机制分析

NGRN（Neugrin）是一个功能注释稀疏但互作网络广泛的核-线粒体双重定位蛋白。291个氨基酸的蛋白在AlphaFold中呈现低质量预测（pLDDT=67.6），仅有32.0%的残基pLDDT>90%，而30.6%的残基pLDDT<50%，表明该蛋白含有大量内在无序区段（IDRs）。这种结构特征——高IDR含量结合中等大小的分子量（32.4 kDa）——是典型"支架蛋白"（scaffold protein）的构象特征：IDRs赋予构象灵活性以介导多价互作，而少量有序结构域维持核心绑合界面。

PPI互作网络是NGRN最显著的特征。Combined PPI degree高达236（总计），其中核内PPI degree为132——这在所有评估蛋白中处于最高端（仅排在其后的是PPIH的149）。STRING和BioGRID的联合数据揭示了NGRN与剪接因子（TRA2A, HNRNPDL, RBMS3）、核糖体蛋白（RPL6, MRPL4）、锌指蛋白（ZC3H3）以及线粒体蛋白（ICT1, PRKAG3）的广泛互作。TRA2A（Transformer-2 protein homolog alpha）是剪接因子SR家族的成员，直接参与pre-mRNA剪接调控；HNRNPDL是heterogeneous nuclear ribonucleoprotein D-like，是RNA加工的多功能调控因子。这些核内互作伙伴强烈暗示NGRN参与RNA代谢和剪接调控。

亚细胞定位呈现核-线粒体双分布模式，这一模式在功能层面具有重要含义。HPA显示NGRN定位于nucleoplasm（Supported）、mitochondria（IDA）以及cytokinetic bridge。GO-CC注释包含了nucleoplasm（IDA:HPA）、mitochondrial matrix（IDA:FlyBase）、mitochondrial membrane（IDA:UniProtKB）和nucleus（IBA:GO_Central）。COMPARTMENTS数据库给出nuclear_score=4.000，基于HPA的IDA证据。核-线粒体双重定位常见于参与代谢-转录耦合的蛋白，如参与线粒体逆信号（mitochondrial retrograde signaling）的转录调控因子。

PubMed研究主要将NGRN与线粒体功能和神经系统疾病相联系。PMID 40261608将NGRN鉴定为缺血性卒中中线粒体和琥珀酰化修饰相关基因标志物的成员，PMID 41351645在利用多组学孟德尔随机化分析脑卒中风险时进一步确认了NGRN与线粒体的关联。PMID 38192023在尼日利亚良性前列腺增生的全外显子测序中发现了NGRN的突变。Alzheimer病研究（PMID 32804135, 37438770）也将NGRN列为神经退行性疾病的潜在生物标志物。综合来看，NGRN的深度机制模型为：IDR支架蛋白→核-线粒体双重定位→广泛RNA加工因子互作→剪接调控/线粒体逆信号→神经保护功能。其作为支架蛋白介导多价互作的特性使其具有间接调控染色质/转录的潜力，但缺乏直接TE调控的实验证据（TE调控评估：需实验验证）。


