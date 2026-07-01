---
type: protein-evaluation
gene: "CEP19"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## CEP19 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CEP19 |
| 蛋白名称 | Centrosomal protein of 19 kDa |
| 蛋白全名 | Centrosomal protein of 19 kDa |
| 蛋白大小 | 170 aa / 19 kDa |
| UniProt ID | Q96LK0 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | GO nucleoplasm IDA:HPA + centrosome/centriole IDA; UniProt 仅 centrosome |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 170 aa, very small |
| 研究新颖性 | 10/10 | ×5 | 50.0 | Strict=15 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 82.8 |
| 调控结构域 | 5/10 | ×2 | 10.0 | Centrosome/ciliogenesis |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING limited; IntAct 有限 |
| **加权总分** | | | **127/180**** | |
| 互证加分 | | | +1.0 | GO nucleoplasm IDA:HPA |
| **归一化总分 (÷1.83)** | | | **69.4/100**** | |

PubMed strict: 15

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Centrosome/centriole/spindle pole/cilium (ECO:0000269) | Experimental |
| GO-CC | centriole IDA; centrosome IDA:HPA; **nucleoplasm IDA:HPA** | Direct assay |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[CEP19-PAE.png]]

**PAE 状态**: 已获取 PAE 图像。AlphaFold pLDDT 82.8 (mean), 54.2% >90。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| ANKRD26 | STRING | 0.982 (database) |
| CCDC61 | STRING | 0.981 |
| CEP295 | STRING | 0.980 |
| FGFR1OP | IntAct | two hybrid array |
| ANAPC15 | IntAct | two hybrid array |

IntAct 6 条记录。UniProt 无 interaction 记录。PPI 方向为 centrosome/ciliogenesis 网络，不特异地支持核功能。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FGFR1OP | STRING | 952 |
| CEP350 | STRING | 877 |
| KXD1 | BioGRID | 1 |
| CREB3L2 | BioGRID | 1 |
| REL | BioGRID | 1 |
| VCP | BioGRID | 1 |
| ZBTB14 | BioGRID | 1 |
| CALCOCO1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。
![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96LK0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CEP19

### PubMed

**Count: 20**

| PMID | Title |
|---|---|
| 41582264 | Does Cognitive Behavior Therapy Change Socially Anxious Adolescents' Behavior during a Public Speaking Task? |
| 41218617 | Prognostic Significance of Actinin-4 Protein Expression and Gene Amplification in Endometrial Carcinoma. |
| 39712340 | Whole exome sequencing revealed new variants and haplotypes associated with monogenic obesity. |
| 38991980 | Architecture of RabL2-associated complexes at the ciliary base: A structural modeling perspective: Deciphering the structural organization of ciliary  |
| 38585545 | Severe Early-Onset Obesity and Diabetic Ketoacidosis due to a Novel Homozygous c.169C>T p.Arg57* Variant in CEP19 Gene. |




### ESMFold 结构预测

| 指标 | 数值 |
|---|---|
| 平均 pLDDT | 0.76 |
| >0.9 | 0.0% |
| <0.5 | 6.7% |
| 残基数 | 163 |

ESMFold 从头折叠验证。PDB: `detail/_esm_structures/CEP19_esmfold.pdb`
