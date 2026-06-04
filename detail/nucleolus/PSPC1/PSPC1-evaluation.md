---
type: protein-evaluation
gene: "PSPC1"
date: 2026-06-01
tags: [protein-scout, nucleolus, evaluation]
status: scored
---

## PSPC1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PSPC1 / PSP1 |
| 蛋白全名 | Paraspeckle component 1 |
| 蛋白大小 | 523 aa / 58.7 kDa |
| UniProt ID | Q8WXF1 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt Nucleus speckle+Nucleolus (ECO:0000269)；GO-CC paraspeckles IDA, nucleoplasm IDA, fibrillar center IDA；HPA Enhanced, Nucleoplasm+Nucleoli fibrillar center |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 523 aa, 58.7 kDa，中等大小 RNA 结合蛋白 |
| 研究新颖性 | 2/10 | ×5 | 10.0 | PubMed strict=81, broad=118 |
| 三维结构 | 6/10 | ×3 | 18.0 | AlphaFold pLDDT 72.8 (pct>90: 48.6%)；PDB 3 个结构 (X-ray, 1.90-3.17A) |

![[PSPC1-PAE.png]]
| 调控结构域 | 6/10 | ×2 | 12.0 | RRM (PF00076) ×2, NOPS domain (PF08075)；RNA-binding, paraspeckle formation |
| PPI 网络 | 7/10 | ×3 | 21.0 | NONO (UniProt 17 exp, STRING failed), SFPQ (UniProt 4 exp)；IntAct 15 条多种方法验证 |
| **加权总分** | | | **99/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **54.1/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus speckle (ECO:0000269 ×3), Nucleus nucleolus (ECO:0000269), Nucleus matrix (ECO:0000250), Cytoplasm (ECO:0000250) | 高 |
| GO-CC | paraspeckles (IDA:FlyBase), nucleoplasm (IDA:HPA), fibrillar center (IDA:HPA), nuclear speck, nuclear matrix | 高 |
| Protein Atlas (IF) | HPA Enhanced, Nucleoplasm (main) + Nucleoli fibrillar center | 高 (Enhanced 可信度) |

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PSPC1/IF_images/PSPC1_IF_471_A12_1_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


**结论**: PSPC1 是已知的 paraspeckle 核心组分，核定位证据极为充分（GO paraspeckles IDA + HPA Enhanced）。在核仁中定位于 fibrillar center，与其参与 rDNA 转录调控的功能一致。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q8WXF1-F1 |
| 平均 pLDDT | 72.8 |
| pLDDT >90 | 48.6% |
| pLDDT 70-90 | 9.4% |
| pLDDT <50 | 35.6% |
| PDB | 3 个 (3SDE/1.90A, 5IFN/3.17A, 5WPA/2.29A)，均覆盖 aa 61-320 (RRM 区域) |
| InterPro | IPR012975 (NOPS), IPR012677 (RRM), IPR034522, IPR034523, IPR035979, IPR000504 |
| Pfam | PF08075 (NOPS), PF00076 (RRM) |

**AlphaFold PAE 状态**: PAE 已下载。pLDDT 中等 (72.8)，约 35.6% 残基 pLDDT <50，提示存在显著无序区域（可能为 C-terminal low complexity region）。

![[PSPC1-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 81 |
| PubMed broad | 118 |
| 别名 | PSP1（未用于 scoring） |

关键文献：PSPC1 与 NONO、SFPQ 共同组成 paraspeckle 核心蛋白复合体（PMID:20573717, 22416126）。近年在肿瘤生物学中受关注，包括 GBM (PMID:35910786)、胰腺癌转移 (PMID:38360141)、phase separation 与转录 (PMID:34916619)。文献量较高（strict=81），研究新颖性偏低。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| NONO | UniProt+IntAct | 17 exp (UniProt), Y2H+Co-IP | Paraspeckle core |
| SFPQ | UniProt | 4 exp | Paraspeckle core |
| DISC1 | UniProt+IntAct | 3 exp, fragment pooling | Neuronal |
| NUDT21 | UniProt | 3 exp | mRNA processing |
| SMAD2/SMAD3 | IntAct | TAP (PMID:18729074) | TGF-beta signaling |
| CUL3 | IntAct | TAP (PMID:21145461) | Ubiquitin E3 ligase |
| ESR1 | IntAct | TAP (PMID:31527615) | Nuclear receptor |

STRING 不可用 (502)。UniProt 记录的实验互作丰富 (NONO 17 次实验)，IntAct 有 15 条多方法互作记录。PPI 网络核心围绕 paraspeckle/DNA 病毒先天免疫的 NONO-SFPQ-PSPC1 复合体。

### 4. 总体评价
PSPC1 是 paraspeckle 核心蛋白，核定位证据极其充分（HPA Enhanced + GO-CC IDA），PPI 网络以实验互作为主（NONO-SFPQ-PSPC1 核心复合体）。主要不足是文献量较高（strict=81），研究新颖性仅 2/10，且 AlphaFold 结构预测置信度中等（pLDDT 72.8, 35.6% <50）。作为已知的 paraspeckle 组分，其功能已被广泛研究，新颖性有限。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXF1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PSPC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121390-PSPC1

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PSPC1/PSPC1-PAE.png]]

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PSPC1/PSPC1-PAE.png]]
