---
type: protein-evaluation
gene: "CEP68"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## CEP68 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CEP68 |
| 蛋白全名 | Centrosomal protein of 68 kDa |
| 蛋白大小 | 757 aa / 68 kDa |
| UniProt ID | Q76N32 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | GO nucleoplasm IDA:HPA + centrosome IDA; UniProt 仅 centrosome |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 757 aa |
| 研究新颖性 | 8/10 | ×5 | 40.0 | Strict=22 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT 48.7 (low) |
| 调控结构域 | 5/10 | ×2 | 10.0 | Centrosome/centriolar satellite |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING moderate |
| **加权总分** | | | **106/180**** | |
| 互证加分 | | | +1.0 | GO nucleoplasm IDA:HPA |
| **归一化总分 (÷1.83)** | | | **57.9/100**** | |

PubMed strict: 22

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Centrosome (ECO:0000269) | Experimental |
| GO-CC | centrosome IDA; centriolar satellite IDA:HPA; **nucleoplasm IDA:HPA** | Direct assay |

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

![[CEP68-PAE.png]]

**PAE 状态**: 已获取。pLDDT 48.7 (mean, very low), 63.3% <50。蛋白高度无序。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| CNTRL | STRING | 0.995 (exp 0.575) |
| CEP250 | STRING | 0.990 |
| CEP350 | STRING | 0.952 |
| PCNT | STRING | 0.929 |
| CNTRL | IntAct | two hybrid |

IntAct 6 条。centrosome linker 网络。

### 5. 总体评价
CEP68 是 centrosome/centriolar satellite 蛋白。GO nucleoplasm IDA:HPA 提供核质证据。pLDDT 极低提示高度无序。低置信度 nucleoplasm。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP68/CEP68-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 40416952 | A cross-tissue transcriptome-wide association study identifies novel susceptibility genes for atrial |
| 25679029 | Solving the centriole disengagement puzzle. |
| 18042621 | Cep68 and Cep215 (Cdk5rap2) are required for centrosome cohesion. |
| 21072201 | Genome-wide and follow-up studies identify CEP68 gene variants associated with risk of aspirin-intol |
| 25704143 | Cep68 can be regulated by Nek2 and SCF complex. |


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CEP68/CEP68-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000011523-CEP68/subcellular

![](https://images.proteinatlas.org/40493/2146_E10_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/40493/2146_E10_79_blue_red_green.jpg)
![](https://images.proteinatlas.org/40493/2165_G3_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/40493/2165_G3_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/40493/2176_G3_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/40493/2176_G3_64_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQ79 |
| SMART | SM00179; |
| UniProt Domain [FT] | DOMAIN 559..605; /note="EGF-like" |
| InterPro | IPR027039;IPR001881;IPR018097;IPR013517;IPR028994;IPR049883;IPR011519; |
| Pfam | PF07645;PF13517;PF07593; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000011523-CEP68/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTRC | Intact | false |
| CDK5RAP2 | Intact | false |
| CTBP1 | Biogrid | false |
| MCM7 | Biogrid | false |
| PCNT | Intact | false |
| PLK1 | Intact | false |
| USHBP1 | Intact | false |
| VHL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
