---
type: protein-evaluation
gene: "BOLA2B"
date: 2026-06-01
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## BOLA2B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BOLA2B / BolA-like protein 2 / BOLA2A |
| 蛋白大小 | 86 aa / 10.1 kDa |
| UniProt ID | Q9H3K6 |
| 评估日期 | 2026-06-01 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt Cytoplasm + Nucleus both ECO:0000269 (experimental); GO nucleus IDA:UniProtKB; HPA main: Nucleoplasm (Reliability: Uncertain) |
| 蛋白大小 | 2/10 | ×1 | 2.0 | 86 aa / 10.1 kDa, 极小型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=4, broad=4 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT 92.7; 82.6% >90; 无PDB实验结构 |
| 调控结构域 | 3/10 | ×2 | 6.0 | BolA-like domain (IPR002634); Fe-S cluster assembly factor |
| PPI 网络 | 6/10 | ×3 | 18.0 | STRING 15 partners (GLRX3 0.998, Fe-S pathway); IntAct 15 entries |
| **加权总分** | | | **128/180**** | |
| 互证加分 | | | +1.0 | Experimental nucleus + cytoplasm (ECO:0000269) |
| **归一化总分 (÷1.83)** | | | **69.9/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 证据等级 |
|---|---|---|
| UniProt | Cytoplasm + Nucleus | ECO:0000269 (experimental evidence) |
| GO-CC | Nucleus (IDA:UniProtKB); Cytoplasm (IDA:UniProtKB); Cytosol (IBA); Fe-S cluster assembly complex (IPI:ComplexPortal) | 多级实验证据 |
| HPA | Nucleoplasm | Reliability: Uncertain |

**HPA IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/BOLA2B/IF_images/BOLA2B_IF_red_green.jpg]]

**结论**: BOLA2B拥有实验验证的双定位——细胞质和细胞核均为ECO:0000269。GO-CC提供Cytoplasm IDA + Nucleus IDA双实验证据。HPA标注Nucleoplasm（可靠性Uncertain）。BOLA2B作为iron-sulfur cluster assembly因子，其核定位表明Fe-S cluster assembly在细胞核中的功能——这在BOLA家族中具有良好的实验支持。**评分: 7/10**。

#### 3.2 蛋白大小评估
86 aa / 10.1 kDa，为极小型蛋白。虽然表达纯化简便，但极小的分子量限制了功能域复杂性和生化操作（如WB检测难度增大）。BolA家族蛋白典型为小型 (~100 aa) 折叠蛋白。**评分: 2/10**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 4 |
| PubMed broad | 4 |
| 别名 | BOLA2A |
| 主要研究方向 | Fe-S cluster assembly、Pan-cancer分析、DNA甲基化 |

**关键文献**:
1. Liang M et al. (2023). "Integrative analysis of the role of BOLA2B in human pan-cancer." *Front Genet*. PMID: 36923798
2. Su PH et al. (2017). "Methylomics of nitroxidative stress on precancerous cells reveals DNA methylation alteration at the transition from in situ to invasive cervical cancer." *Oncotarget*. PMID: 29029430
3. Yeung E et al. (2024). "Maternal age is related to offspring DNA methylation: A meta-analysis of results from the PACE consortium." *Aging Cell*. PMID: 38808605
4. Mahfooz S et al. (2026). "Enhanced Radio-sensitization of Glioblastoma using a Dendrimer-Based Metformin Nano-formulation through Direct Tumor Suppression and Indirect Immune Modulation." *bioRxiv*. PMID: 42182373

**评价**: BOLA2B仅4篇文献，极度新颖。2023年的Pan-cancer分析为其在不同肿瘤中的表达和预后价值提供了首个系统分析框架。作为cytosolic Fe-S cluster assembly machinery的核心组分，其在核内的功能（Fe-S cluster可能在核内蛋白的DNA修复、基因调控中发挥作用）尚未被充分探索。BOLA2B与paralog BOLA2高度同源，部分文献可能未严格区分两个基因。**评分: 10/10**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 92.7 |
| >90 | 82.6% |
| 70–90 | 14.0% |
| 50–70 | 3.5% |
| <50 | 0.0% |
| 可用 PDB 条目 | 0 (无实验结构) |

**PAE 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/BOLA2B/BOLA2B-PAE.png]]

**评价**: pLDDT 92.7是本次评估中第二高的pLDDT值 (仅次于ATXN8的97.4)。82.6%残基>90，0%残基<50，表明该86 aa小型蛋白为完全折叠的紧凑结构。AlphaFold对该蛋白结构预测置信度极高。BolA折叠为alpha-beta sandwich (InterPro IPR036065)，已知结构高度保守。虽无PDB，但AlphaFold预测足以直接用于结构分析。**评分: 8/10**。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR045115 (BolA-like protein 2), IPR002634 (BolA protein), IPR036065 (BolA-like superfamily) |
| Pfam | PF01722 (BolA-like protein) |

**Fe-S cluster assembly功能**: BOLA2B的BolA-like domain (PF01722) 是胞质Fe-S cluster assembly machinery的核心组件。UniProt功能: "Acts as a cytosolic iron-sulfur (Fe-S) cluster assembly factor that facilitates [2Fe-2S] cluster insertion into a subset of cytosolic proteins. Acts together with the monothiol glutaredoxin GLRX3." BOLA2B与GLRX3形成[2Fe-2S]-bridged heterodimer，将Fe-S cluster递送给下游靶蛋白。Fe-S cluster的核内功能是新兴领域——核内Fe-S蛋白参与DNA复制 (DNA primase, DNA polymerase)、DNA修复 (XPD helicase, FANCJ)、端粒维持 (RTEL1) 和基因调控。BOLA2B的核定位使其在核内Fe-S cluster assembly和递送中可能发挥专门作用。但该蛋白本身不是classical transcriptional regulator (无DNA结合域、chromatin修饰活性)，应从Fe-S cluster metabolism而非直接转录调控角度评估。**评分: 3/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):
| Partner | Score | Experimental | Database | Textmining | 功能类别 |
|---|---|---|---|---|---|
| GLRX3 | 0.998 | 0.931 | 0.540 | 0.942 | Monothiol glutaredoxin, Fe-S cluster transfer |
| BOLA3 | 0.994 | 0 | 0.540 | 0.986 | BolA family, Fe-S cluster assembly |
| GLRX5 | 0.879 | 0 | 0.540 | 0.746 | Monothiol glutaredoxin, mitochondrial |
| CIAPIN1 | 0.844 | 0.468 | 0 | 0.716 | Fe-S cluster assembly, anamorsin |
| BOLA1 | 0.810 | 0 | 0.540 | 0.517 | BolA family member |
| ISCU | 0.764 | 0 | 0.540 | 0.496 | Fe-S cluster scaffold protein |
| STAT4 | 0.750 | 0 | 0.750 | 0 | Signal transducer, transcription |
| FDX2 | 0.743 | 0 | 0.540 | 0.405 | Ferredoxin, Fe-S protein |
| NFS1 | 0.739 | 0 | 0.540 | 0.448 | Cysteine desulfurase, Fe-S biogenesis |
| LYRM4 | 0.708 | 0 | 0.540 | 0.317 | Fe-S cluster assembly co-chaperone |
| FXN | 0.705 | 0 | 0.540 | 0.381 | Frataxin, Fe-S cluster assembly |
| NDOR1 | 0.662 | 0.292 | 0 | 0.542 | NADPH-dependent oxidoreductase, Fe-S |
| BOLA2 | 0.656 | 0 | 0.540 | 0 | Paralog, BolA family |
| NFU1 | 0.624 | 0.091 | 0 | 0.576 | Fe-S cluster scaffold/delivery |
| SLX1B | 0.610 | 0 | 0 | 0.590 | Holliday junction resolvase |

**IntAct 实验互作** (15 entries):
| Partner | Method | PMID | Interaction Type |
|---|---|---|---|
| IQCB1 | Anti tag coimmunoprecipitation (MI:0007) | PMID:21565611 | Association |
| VCAM1 | Cross-linking study (MI:0030) | PMID:22623428 | Association |
| ARRB2 | Anti tag coimmunoprecipitation (MI:0007) | PMID:17620599 | Association |
| BOLA2 | Pull down (MI:0096) | PMID:21712045 | Association |
| SOAT1 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| PARK7 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| CDK1 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| COQ2 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| DLD | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| DLST | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| COX15 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| VDAC1 | Cross-linking study (MI:0030) | PMID:29128334 | Association |
| SMARCB1 | Proximity-dependent biotin identification (MI:1314) | PMID:30108113 | Proximity |
| LRRK2 | Anti tag coimmunoprecipitation (MI:0007) | PMID:31046837 | Association |
| KLF11 | Anti tag coimmunoprecipitation (MI:0007) | PMID:31980649 | Association |

**UniProt 注释互作** (2 entries):
| Partner | Experiments | 功能类别 |
|---|---|---|
| CIAPIN1 | 2 | Fe-S cluster assembly |
| GLRX3 | 4 | Monothiol glutaredoxin, Fe-S cluster delivery |

**评价**: BOLA2B的PPI网络高度聚焦于Fe-S cluster metabolism——GLRX3 (STRING 0.998, exp 0.931) 是其最核心的functional partner (形成[2Fe-2S]-bridged heterodimer); BOLA3、BOLA1、ISCU、NFS1、FDX2、FXN、LYRM4和NFU1均为Fe-S cluster biogenesis pathway的组分。SMARCB1 (BAF47, SWI/SNF chromatin remodeler subunit) 的proximity-dependent biotin identification互作暗示核内Fe-S cluster machinery与chromatin remodeling的物理接近。CDK1和LRRK2互作链接到细胞周期和Parkinson's disease。**评分: 6/10**。

### 4. 总体评价
BOLA2B是胞质Fe-S cluster assembly machinery的核心组分，拥有实验验证的细胞质+细胞核双定位 (ECO:0000269)。pLDDT 92.7表明其结构折叠高度可信。极度新颖（仅4篇文献）。其PPI网络高度聚焦于Fe-S cluster biogenesis pathway，GLRX3是核心functional partner。BOLA2B在核内的功能是目前研究盲区——核内Fe-S cluster依赖的DNA修复、复制和染色质重塑蛋白需要Fe-S delivery system，BOLA2B可能是核内Fe-S cluster递送的关键因子。主要弱点是蛋白极小 (86 aa)、非传统转录调控因子、Fe-S cluster assembly功能可能被认为与TE regulation距离较远。但考虑到核内Fe-S protein在DNA metabolism中的广泛参与和BOLA2B的核定位实验证据，其作为TE相关调控的间歇因子值得进一步评估。


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| GLRX3 | STRING | 0.998 |
| BOLA3 | STRING | 0.994 |
| GLRX5 | STRING | 0.879 |
| CIAPIN1 | STRING | 0.844 |
| BOLA1 | STRING | 0.81 |
| IQCB1 | IntAct | psi-mi:"MI:0007"(anti tag coim |
| VCAM1 | IntAct | psi-mi:"MI:0030"(cross-linking |
| ARRB2 | IntAct | psi-mi:"MI:0007"(anti tag coim |

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/BOLA2B/BOLA2B-PAE.png]]


