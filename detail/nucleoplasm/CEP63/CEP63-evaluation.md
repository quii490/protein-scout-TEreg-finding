---
type: protein-evaluation
gene: "CEP63"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## CEP63 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CEP63 |
| 蛋白全名 | Centrosomal protein of 63 kDa |
| 蛋白大小 | 703 aa / 63 kDa |
| UniProt ID | Q96MT8 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | GO nucleoplasm IDA:HPA + centrosome IDA; UniProt 仅 centrosome |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 703 aa |
| 研究新颖性 | 8/10 | ×5 | 40.0 | Strict=36 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT 77.3; 3 PDB |
| 调控结构域 | 6/10 | ×2 | 12.0 | Centrosome/centriole duplication |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING moderate |
| **加权总分** | | | **117/180**** | |
| 互证加分 | | | +1.0 | GO nucleoplasm IDA:HPA |
| **归一化总分 (÷1.83)** | | | **63.9/100**** | |

PubMed strict: 36

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Centrosome/centriole/centriolar satellite (ECO:0000269) | Experimental |
| GO-CC | centrosome IDA:HPA; ciliary basal body IDA:HPA; **nucleoplasm IDA:HPA** | Direct assay |
| PDB | 3 structures (4Y3L, 4Y8T, 7Q8X) | — |

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[CEP63-PAE.png]]

**PAE 状态**: 已获取。pLDDT 77.3 (mean), 50.3% >90, 10.5% <50。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| CEP152 | STRING | 0.990 (exp 0.349) |
| CDK5RAP2 | STRING | 0.985 (exp 0.332) |
| CENPJ | STRING | 0.985 (exp 0.097) |
| DEUP1 | STRING | 0.980 |
| CEP152 | IntAct | two hybrid (PMID:32296183) |

IntAct 5 条。PPI 为 centrosome biogenesis 网络（CEP152/CDK5RAP2/CENPJ），不特指核功能。

### 5. 总体评价
CEP63 是 centrosome 复制关键调控因子。GO nucleoplasm IDA:HPA 提供核质定位实验证据。3 个 PDB 结构支持结构域折叠。中等置信度 nucleoplasm 候选。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP63/CEP63-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 35793002 | Zika virus alters centrosome organization to suppress the innate immune response. |
| 35989368 | CEP63 upregulates YAP1 to promote colorectal cancer progression through stabilizing RNA binding prot |
| 32402286 | CCDC57 Cooperates with Microtubules and Microcephaly Protein CEP63 and Regulates Centriole Duplicati |
| 38405715 | A Specialized Centrosome-Proteasome Axis Mediates Proteostasis and Influences Cardiac Stress through |
| 34041036 | Copy Number Variations of CEP63, FOSL2 and PAQR6 Serve as Novel Signatures for the Prognosis of Blad |


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP63/CEP63-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000182923-CEP63/subcellular

![](https://images.proteinatlas.org/36264/1827_B9_23_cr5ac61bc528405_red_green.jpg)
![](https://images.proteinatlas.org/36264/1827_B9_26_cr5ac61bc528414_red_green.jpg)
![](https://images.proteinatlas.org/36264/2120_G11_32_red_green.jpg)
![](https://images.proteinatlas.org/36264/2120_G11_44_red_green.jpg)
![](https://images.proteinatlas.org/36264/2132_E7_17_red_green.jpg)
![](https://images.proteinatlas.org/36264/2132_E7_61_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
