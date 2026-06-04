---
type: protein-evaluation
gene: "BEND6"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## BEND6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BEND6 / BEN domain-containing protein 6 / C6orf65 |
| 蛋白大小 | 279 aa / 31.2 kDa |
| UniProt ID | Q5SZJ8 |
| 评估日期 | 2026-06-01 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | UniProt Nucleus ECO:0000250; GO nucleus IBA; HPA main: Nucleoplasm + Plasma membrane (Reliability: Approved) |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 279 aa / 31.2 kDa, 偏小但可操作 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=7, broad=8 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT 71.8; PDB 7YUL (X-ray, 1.82A) + 7YUN (X-ray, 2.13A) |
| 调控结构域 | 6/10 | ×2 | 12.0 | BEN domain (PF10523); Notch signaling corepressor |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING 12 partners; IntAct 3 entries (co-IP) |
| **加权总分** | | | **120/180**** | |
| 互证加分 | | | +1.0 | BEN domain + PDB实验结构 + HPA Approved |
| **归一化总分 (÷1.83)** | | | **65.6/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 证据等级 |
|---|---|---|
| UniProt | Nucleus | ECO:0000250 (sequence similarity) |
| GO-CC | Nucleus | IBA:GO_Central (inferred from biological aspect of ancestor) |
| HPA | Nucleoplasm, Plasma membrane | Reliability: Approved |

**HPA IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BEND6/IF_images/BEND6_IF_red_green.jpg]]

**结论**: BEND6拥有HPA Approved级别的IF验证结果，主要定位于Nucleoplasm，同时显示Plasma membrane信号（可能存在膜关联或双定位）。BEN domain蛋白家族以转录调控功能著称，核定位符合功能预期。但UniProt仅标注ECO:0000250（序列相似性），直接实验证据仍待加强。**评分: 5/10**。

#### 3.2 蛋白大小评估
279 aa / 31.2 kDa，略低于300 aa的理想下限，但作为DNA结合domain蛋白仍适合常规生化实验（克隆、表达、ITC/FP DNA结合实验）。BEN domain (~100 aa)构成蛋白核心，剩余区域可能为regulatory segments。**评分: 5/10**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 7 |
| PubMed broad | 8 |
| 别名 | C6orf65 |
| 主要研究方向 | Notch信号抑制、神经干细胞自我更新、抗病毒先天免疫 |

**关键文献**:
1. Dai Q et al. (2013). "BEND6 is a nuclear antagonist of Notch signaling during self-renewal of neural stem cells." *Development*. PMID: 23571214
2. Liu K et al. (2023). "Structural insights into DNA recognition by the BEN domain of the transcription factor BANP." *J Biol Chem*. PMID: 37086783
3. Chen T et al. (2025). "BEND6 promotes RNA viruses' replication by inhibiting innate immune responses." *Sci China Life Sci*. PMID: 39821161
4. Liu XP et al. (2018). "Development and Validation of a 9-Gene Prognostic Signature in Patients With Multiple Myeloma." *Front Oncol*. PMID: 30671382
5. Chen CW et al. (2022). "RNA sequence analysis identified bone morphogenetic protein-2 (BMP2) as a biomarker underlying form deprivation myopia." *Biochem Biophys Rep*. PMID: 35494490

**评价**: BEND6仅7篇文献——极度新颖。已有核心功能论文 (Dai 2013) 证明其作为RBPJ结合转录corepressor抑制Notch信号。2025年新发表文献揭示其在抗病毒先天免疫中的新功能。BEN domain蛋白家族的整体功能认知仍在快速发展中（2023年首篇BEN domain-DNA复合物结构发表），BEND6作为该家族成员具有较高的结构生物学吸引力。**评分: 10/10**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 71.8 |
| >90 | 44.4% |
| 70–90 | 9.3% |
| 50–70 | 13.6% |
| <50 | 32.6% |
| 可用 PDB 条目 | 7YUL (X-ray, 1.82A, A=170-271); 7YUN (X-ray, 2.13A, A/B=170-271) |

**PAE 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BEND6/BEND6-PAE.png]]

**评价**: pLDDT 71.8，44.4%残基>90，折叠域质量良好。拥有两个PDB实验结构 (7YUL/7YUN)，覆盖170-271区域（C端BEN domain + adjacent区域），为BEN domain-DNA相互作用的结构基础提供了直接信息。32.6%残基<50提示N端区域可能为无序区。**评分: 7/10**。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR018379 (BEN domain), IPR037496 (BEN domain superfamily) |
| Pfam | PF10523 (BEN domain) |

**转录调控潜力**: BEND6的BEN domain (PF10523)是近年来新鉴定的DNA结合结构域，命名来源于BANP、E5R、NAC1三个初始家族成员。BEN domain直接识别特定DNA序列或染色质标记。Dai 2013证明BEND6通过与RBPJ (Notch信号转录因子) 直接互作作为转录corepressor。UniProt功能: "Acts as a corepressor of recombining binding protein suppressor hairless (RBPJ) and inhibits Notch signaling in neural stem cells, thereby opposing their self-renewal and promoting neurogenesis"。BEN domain + Notch信号调控的双重特性使其在神经发育和再生研究中具有吸引力。**评分: 6/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):
| Partner | Score | Experimental | Database | Textmining | 功能类别 |
|---|---|---|---|---|---|
| ZNF451 | 0.777 | 0 | 0 | 0.311 | SUMO E3 ligase, transcription |
| BEND5 | 0.685 | 0 | 0 | 0.685 | BEN domain family member |
| BEND7 | 0.649 | 0 | 0 | 0.648 | BEN domain family member |
| RBPJ | 0.635 | 0.292 | 0 | 0.506 | Notch signaling transcription factor |
| LTO1 | 0.610 | 0.610 | 0 | 0 | — |
| OR13G1 | 0.610 | 0.610 | 0 | 0 | Olfactory receptor |
| BANP | 0.445 | 0 | 0 | 0.445 | BEN domain TF, cell cycle |
| BEND2 | 0.432 | 0 | 0 | 0.432 | BEN domain family member |
| NACC2 | 0.431 | 0 | 0 | 0.431 | NAC family, transcriptional repressor |
| MED29 | 0.418 | 0.419 | 0 | 0 | Mediator complex subunit |
| LRRC58 | 0.415 | 0 | 0 | 0.415 | — |
| SH2D5 | 0.411 | 0 | 0 | 0.392 | — |

**IntAct 实验互作** (3 entries):
| Partner | Method | PMID | Interaction Type |
|---|---|---|---|
| MED29 | Anti tag coimmunoprecipitation (MI:0007) | PMID:33961781 | Association |
| LTO1 | Anti tag coimmunoprecipitation (MI:0007) | PMID:33961781 | Physical association |
| OR13G1 | Anti tag coimmunoprecipitation (MI:0007) | PMID:33961781 | Association |

**UniProt 注释互作**: 无记录。

**评价**: BEND6的PPI网络中，RBPJ互作 (STRING score 0.635, experimental 0.292) 是最重要的功能性互作——直接支持其Notch信号corepressor功能。BEND5、BEND7、BANP、BEND2等同家族成员互作提示BEN domain协作网络。IntAct有3个co-IP验证互作 (MED29, LTO1, OR13G1)，全部来自同一高通量研究 (PMID:33961781)。MED29为Mediator复合体亚基，若验证真实将直接链接BEND6与Pol II基础转录机器。**评分: 4/10**。

### 4. 总体评价
BEND6是BEN domain转录调控蛋白家族成员，拥有PDB实验结构覆盖BEN domain核心区域。作为Notch信号corepressor的核心功能已在神经干细胞中被初步验证 (Dai 2013)。极度新颖 (仅7篇文献)，BEN domain结构刚被解析 (2023首篇复合物结构)，具有较高的结构和功能探索价值。主要弱点是核定位证据为序列推断、蛋白偏小 (279 aa)、PPI网络有限。MED29 (Mediator complex) 互作如果验证将显著提升其转录调控重要性。


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| ZNF451 | STRING | 0.777 |
| BEND5 | STRING | 0.685 |
| BEND7 | STRING | 0.649 |
| RBPJ | STRING | 0.635 |
| LTO1 | STRING | 0.61 |
| MED29 | IntAct | psi-mi:"MI:0007"(anti tag coim |
| LTO1 | IntAct | psi-mi:"MI:0007"(anti tag coim |
| OR13G1 | IntAct | psi-mi:"MI:0007"(anti tag coim |

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BEND6/BEND6-PAE.png]]


