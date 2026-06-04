---
type: protein-evaluation
gene: "AGPAT3"
date: 2026-06-02
tags: [protein-scout, nuclear-envelope, evaluation]
status: scored
---

## AGPAT3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AGPAT3 / LPAAT3 |
| 蛋白全名 | 1-acyl-sn-glycerol-3-phosphate acyltransferase gamma |
| 蛋白大小 | 376 aa / 43.4 kDa |
| UniProt ID | Q9NRZ7 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | UniProt: ER membrane + Nucleus envelope (ECO:0000269); GO-CC: nuclear envelope (IDA), ER membrane (IDA); HPA 无 IF |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 376 aa, 43.4 kDa, 中等大小 |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=38, ≤40 |
| 三维结构 | 6/10 | ×3 | 18.0 | AlphaFold mean pLDDT 94.6 (极高); 无 PDB |

![[AGPAT3-PAE.png]]
| 调控结构域 | 3/10 | ×2 | 6.0 | IPR032098, IPR002123, PF16076+PF01553 — 酰基转移酶结构域; 代谢酶 |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING 以 database 功能关联为主 (AGPAT family/MBOAT/CDS); IntAct 含 Y2H + co-IP |
| **加权总分** | | | **105/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **57.4/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Endoplasmic reticulum membrane (ECO:0000269); Nucleus envelope (ECO:0000269) | 高（实验验证） |
| GO-CC | nuclear envelope (IDA:UniProtKB), endoplasmic reticulum membrane (IDA:UniProtKB), Golgi membrane (TAS), endomembrane system (IBA), membrane (HDA), plasma membrane (HDA) | 高 |
| Protein Atlas (IF) | HPA 无 IF 图像（no_image_detected） | 未确认 |

**HPA IF 状态**: no_image_detected — HPA 未检测到可用 IF 图像。核定位基于 UniProt + GO-CC。

**结论**: AGPAT3 核定位证据明确且独特——作为核膜（nuclear envelope）定位蛋白，UniProt 和 GO-CC 均以实验级别证据（ECO:0000269, IDA）确认。GO-CC 含 nuclear envelope (IDA:UniProtKB)，同时分布 ER membrane/Golgi membrane 等多个内膜系统。HPA 无 IF 验证。核膜定位（而非核质或核仁）在筛选体系中属于特殊类别，定位明确但非经典核蛋白概念。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9NRZ7-F1 |
| 平均 pLDDT | 94.6 |
| pLDDT >90 | 93.9% |
| pLDDT 70-90 | 2.7% |
| PDB | 无 |
| InterPro | IPR032098 (Acyltransferase, LPLAT), IPR002123 (Phospholipid/glycerol acyltransferase) |
| Pfam | PF16076 (Acyltransf_C), PF01553 (Acyltransferase) |

**AlphaFold PAE 状态**: PAE 已下载，模型置信度极高（mean pLDDT 94.6, >90 占 93.9%）。膜蛋白折叠预测可靠，但无 PDB 实验结构验证。
![[AGPAT3-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 38 |
| PubMed broad | 61 |
| 别名 | LPAAT3（未用于 scoring） |

关键文献：AGPAT3 文献量中等偏低（strict=38）。核心方向包括：脂质代谢和铁死亡（ferroptosis）相关磷脂重塑（PMID:40934923, 41807033）、神经疾病（AGPAT3 功能丧失变异导致智力障碍和视网膜色素变性，PMID:37821758）、糖尿病心肌病中 SREBP1 泛素化降解（PMID:37899701）。作为溶血磷脂酸酰基转移酶，AGPAT3 参与 de novo 磷脂合成途径，催化 LPA→PA 转化，偏好花生四烯酰辅酶 A。功能和铁死亡/脂质氧化/膜磷脂重塑相关。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| AGPAT1 | STRING | 0.979 (database 0.9, textmining 0.802) | AGPAT family |
| AGPAT2 | STRING | 0.970 (database 0.9, textmining 0.717) | AGPAT family |
| MBOAT2 | STRING | 0.959 (database 0.9, exp 0.169) | Acyltransferase |
| CDS2 | STRING | 0.939 (database 0.922) | Phospholipid synthesis |
| CDS1 | STRING | 0.938 (database 0.922) | Phospholipid synthesis |
| AGPAT4 | STRING | 0.937 (database 0.9) | AGPAT family |
| MBOAT7 | STRING | 0.931 (database 0.9) | Acyltransferase |
| AGPAT5 | STRING | 0.929 (database 0.9) | AGPAT family |
| MBOAT1 | STRING | 0.922 (database 0.9) | Acyltransferase |
| PLPP5 | STRING | 0.921 (database 0.914, exp 0.065) | Phospholipid phosphatase |

PPI 网络以 database 功能关联为主（AGPAT family、MBOAT 家族、CDS 等磷脂代谢酶），实验互作证据薄弱。STRING 最高分来自 database 而非实验通道。IntAct 含 15 条互作，主要为高通量 Y2H（有果蝇 ortholog 数据）和 co-IP（YIPF3, GPR89A, TOM1L1 等）。互作网络反映了 AGPAT3 在磷脂代谢网络中的位置，但不提供核定位或调控信息。

**UniProt 记录互作**: ABHD16A, AQP6, BNIP2, CREB3L1, FAM133A 等 17 条（均为 3 experiments Y2H）。

### 4. 总体评价
AGPAT3 是一个独特的核膜蛋白候选（57.4/100）。核心优势：核膜定位（UniProt + GO-CC 双确认，ECO:0000269/IDA 证据级别）、极高 AF 置信度（pLDDT 94.6）、中等偏低文献量（PM=38）。核心弱点：无 PDB 实验结构、PPI 以代谢网络关联为主（实验互作弱）、HPA 无 IF 验证、作为代谢酶而非经典转录或染色质调控因子，功能与核膜定位的关系需要进一步确定。作为 nuclear-envelope 类别候选，定位特殊性是其核心价值。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRZ7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRZ7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGPAT3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160216-AGPAT3（无 IF 原图）

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AGPAT3/AGPAT3-PAE.png]]

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/AGPAT3/AGPAT3-PAE.png]]
