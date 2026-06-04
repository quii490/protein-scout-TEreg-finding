---
type: protein-evaluation
gene: "CEP85"
date: 2026-06-01
tags: [protein-scout, nucleolus, evaluation]
status: scored
---

## CEP85 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CEP85 |
| 蛋白全名 | Centrosomal protein of 85 kDa |
| 蛋白大小 | 760 aa / 85 kDa |
| UniProt ID | Q6P2H3 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt Nucleus/nucleolus ECO:0000269 + GO nucleolus IDA:HPA |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 760 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | Strict=6 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 66.9; 2 PDB |
| 调控结构域 | 6/10 | ×2 | 12.0 | Centrosome + nucleolus dual |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING moderate |
| **加权总分** | | | **132/180********** | |
| 互证加分 | | | +2.0 | Nucleolus IDA:HPA + experimental UniProt |
| **归一化总分 (÷1.83)** | | | **72.1/100********** | |

PubMed strict: 6

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Centrosome + spindle pole + **Nucleus/nucleolus (ECO:0000269)** | **Experimental** |
| GO-CC | centriole IDA; centrosome IDA:HPA; Golgi IDA:HPA; **nucleolus IDA:HPA** | **Direct assay** |
| PDB | 2 structures (2LYF NMR, 7Q0A EM) | — |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。GO-CC nucleolus IDA:HPA 提供 HPA 抗体级核仁定位实验证据。

**定位分析**: CEP85 是罕见的 centrosome + nucleolus 双定位蛋白。UniProt 明确实验级注释 Nucleus/nucleolus (ECO:0000269)。GO nucleolus IDA:HPA 进一步确认为直接实验证据。centrosome 定位与核仁定位不冲突。

![[CEP85-PAE.png]]

**PAE 状态**: 已获取。pLDDT 66.9 (mean), 20.3% >90, 39.2% 70-90, 21.3% <50。

### 4. PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| CEP250 | STRING | 0.940 |
| CNTRL | STRING | 0.876 |
| CEP135 | STRING | 0.866 |
| FGFR1OP | IntAct | two hybrid (PMID:32296183) |
| NINL | IntAct | two hybrid |

IntAct 9 条。centrosome linker 网络为主。

### 5. 总体评价
CEP85 是当前评估区间中核定位证据最强的 centrosome-nucleolus 双定位蛋白。UniProt 实验级 Nucleus/nucleolus 注释 + GO nucleolus IDA:HPA 双源互证。centrosome/nucleolus 双定位为其在细胞周期中的功能提供了有趣的生物学背景。建议作为较高优先级 nucleolus 候选。PubMed strict=6 极为新颖。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/CEP85/CEP85-PAE.png]]


#### 关键文献
| PMID | 标题 |
|---|---|
| 36718820 | circRNA-SMO upregulates CEP85 to promote proliferation and migration of glioblastoma via sponging mi |
| 29712910 | Direct binding of CEP85 to STIL ensures robust PLK4 activation and efficient centriole assembly. |
| 39932629 | Genetic insights into non-obstructive azoospermia: Implications for diagnosis and TESE outcomes. |
| 26220856 | Characterization of Cep85 - a new antagonist of Nek2A that is involved in the regulation of centroso |
| 38891632 | Integrated miRNA and mRNA Sequencing Reveals the Sterility Mechanism in Hybrid Yellow Catfish Result |


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/CEP85/CEP85-PAE.png]]
