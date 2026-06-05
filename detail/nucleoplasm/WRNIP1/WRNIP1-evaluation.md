---
type: protein-evaluation
gene: "WRNIP1"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## WRNIP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WRNIP1 / WHIP |
| 蛋白全名 | ATPase WRNIP1 |
| 蛋白大小 | 665 aa / 72.1 kDa |
| UniProt ID | Q96S55 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | UniProt Nucleus; Cytoplasm, HPA Nucleoplasm |
| 蛋白大小 | 7/10 | x1 | 7.0 | 665 aa, 72.1 kDa，中等偏大 |
| 研究新颖性 | 6/10 | x5 | 30.0 | PubMed strict=54 (≤60 区间) |
| 三维结构 | 6/10 | x3 | 18.0 | PDB 2 entries (3VHS/3VHT 仅小片段 9-46aa), AF pLDDT 71.6, <50=31.1% |
| 调控结构域 | 7/10 | x2 | 14.0 | AAA+ ATPase, Zn-finger, DNA polymerase delta 调节因子 |
| PPI 网络 | 7/10 | x3 | 21.0 | STRING WRN 0.998, RAD18 0.893, POLD1/POLD2; IntAct RIGI/TOLLIP/LMNA |
| **加权总分** | | | **118/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **64.5/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt Subcellular Location | Nucleus (ECO:0000269); Cytoplasm (ECO:0000269) | 高（实验证据） |
| GO-CC | nucleus (IDA:UniProtKB), perinuclear region of cytoplasm (IDA:UniProtKB), membrane (HDA:UniProtKB) | 高 |
| HPA IF | Nucleoplasm (Approved 可靠性) | 高 |
| Literature | WRNIP1 在 DNA 复制应激时与 WRN 协同定位于核内复制叉；在先天免疫中还参与胞质 RIGI 信号 | 中-高 |

**HPA IF 状态**: IF available -- HPA 可靠性 Approved，定位 Nucleoplasm。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WRNIP1/IF_images/WRNIP1_IF_red_green.jpg]]

**结论**: WRNIP1 核质定位明确，HPA Approved 可靠性。虽有胞质功能（RIGI 抗病毒信号），但主要功能为核内 DNA 复制调节和基因组稳定性维持。UniProt 和 GO-CC 均有 IDA 实验证据支持核定位。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q96S55-F1 |
| 平均 pLDDT | 71.6 |
| pLDDT >90 | 40.2% |
| pLDDT 70-90 | 23.8% |
| pLDDT <50 | **31.1%** |
| PDB | 2 entries (3VHS 1.90A X-ray chains A/B=17-40; 3VHT 2.40A X-ray chain B=9-46) -- 仅为 N 端 Ubiquitin-like 域片段 |

AlphaFold pLDDT 71.6，<50 低置信区高达 31.1%。PDB 仅有 N 端小片段结构（17-46 aa），尽管分辨率高（1.90A），但不覆盖全长。AAA+ ATPase 域和 C 端区域预测质量中等，提示部分柔性。全长结构完全依赖 AF 预测。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WRNIP1/WRNIP1-PAE.png]]

| InterPro | Pfam |
|---|---|
| IPR003593 (AAA+ ATPase), IPR032423 (WRNIP1-like), IPR051314 (WRNIP1/AAA+), IPR003959 (AAA+ ATPase core), IPR008921 (ATPase motor), IPR021886 (MgsA AAA+), IPR027417 (P-loop NTPase), IPR006642 (Zinc finger Rad18-like), IPR040539 (WHIP N-terminal) | PF00004 (AAA), PF16193 (WHIP_N), PF12002 (MgsA_C), PF18279 |

**染色质调控潜力**: WRNIP1 通过与 WRN 解旋酶和 DNA 聚合酶 delta (POLD1/POLD2/POLD4) 的互作参与 DNA 复制起始/重启调节。在复制应激和转录相关基因组不稳定性中发挥保护作用。与 RAD18 的互作连接至 DNA 损伤耐受/跨损伤合成通路。但与染色质修饰（甲基化、乙酰化）无直接关联。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 54 |
| PubMed broad | 68 |
| 别名 | WHIP（未用于 scoring） |

关键文献：
- PMID:38488661: "WRNIP1 prevents transcription-associated genomic instability." (eLife, 2024) -- 转录相关基因组不稳定性
- PMID:28118071: "The role of WRNIP1 in genome maintenance." (Cell Cycle, 2017) -- 综述
- PMID:31061318: "WRNIP1 Controls the Amount of PrimPol." (Biol Pharm Bull, 2019) -- PrimPol 调控
- PMID:38190717: "AXL/WRNIP1 Mediates Replication Stress Response and Promotes Therapy Resistance and Metachronous Metastasis in HER2+ Breast Cancer." (Cancer Res, 2024)
- PMID:35163467: "R-Loop-Associated Genomic Instability and Implication of WRN and WRNIP1." (Int J Mol Sci, 2022)

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| WRN | STRING | 0.998 (exp 0.560, text 0.995) | Werner 解旋酶 |
| RAD18 | STRING | 0.893 (exp 0.645, text 0.708) | DNA 损伤耐受 |
| POLD2 | STRING | 0.722 (exp 0.464) | DNA pol delta 亚基 |
| POLD1 | STRING | 0.667 (exp 0.553) | DNA pol delta 催化亚基 |
| ZRANB3 | STRING | 0.683 (exp 0.098, text 0.658) | DNA 解旋酶/转位酶 |
| DNA2 | STRING | 0.683 (exp 0.250, text 0.595) | DNA 解旋酶/核酸酶 |
| PRIMPOL | STRING | 0.668 (exp 0.292, text 0.547) | Primase-polymerase |
| RIGI | IntAct | coIP (PMID:21903422) | 抗病毒先天免疫 |
| TOLLIP | IntAct | coIP (PMID:21903422) | TLR 信号 |
| LMNA | IntAct | BioID (PMID:29568061) | 核纤层蛋白 |
| KDM4A | IntAct | pull down (PMID:23871696) | H3K9/H3K36 去甲基化酶 |
| POLD1 | UniProt | 2 experiments | curated |
| RIGI | UniProt | 2 experiments | curated |

WRNIP1 的 PPI 网络跨 DNA 复制/修复和先天免疫两条不相交通路。WRN (0.998) 为核心伴侣，与 RAD18、POLD1/POLD2 构成 DNA 复制调节网络。RIGI/TOLLIP 为抗病毒信号通路。LMNA (BioID) 提示核纤层定位。KDM4A (pull down) 互作值得关注，连接至组蛋白去甲基化。

### 4. 总体评价
WRNIP1 是 DNA 复制应激和基因组稳定性的多功能 ATPase，评分中等（64.5/100）。优势包括：HPA Approved 纯核质定位、与 WRN 解旋酶强互作（0.998）、功能涉及 R-loop/转录相关基因组不稳定性（与 TE 调控间接相关）、多域结构（AAA+ ATPase + Zn-finger）。劣势包括：PubMed 54（新颖性 6/10）、蛋白偏大（665 aa）、AF 预测质量中等（pLDDT 71.6，31% <50）、PDB 仅 N 端小片段、无直接染色质修饰活性。KDM4A 互作为潜在桥梁至组蛋白去甲基化/染色质调控通路。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96S55
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96S55
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WRNIP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124535-WRNIP1

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WRNIP1/WRNIP1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96S55-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
