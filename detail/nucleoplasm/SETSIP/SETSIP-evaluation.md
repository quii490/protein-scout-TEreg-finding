---
type: protein-evaluation
gene: "SETSIP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## SETSIP 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SETSIP |
| 蛋白名称 | Protein SETSIP |
| 蛋白大小 | 292 aa / 33.6 kDa |
| UniProt ID | P0DME0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Lipid droplets; Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 292 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=78.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | NAP-like_sf; NAP_family |
| PPI | 5/10 | x3 | 15.0 | PPI degree=24 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
HPA: Lipid droplets; Nucleoplasm (Supported)
PubMed: strict=4, broad=4
AF pLDDT: 78.0  PDB: 0
InterPro: NAP-like_sf; NAP_family
Pfam: NAP
PPI degree: 24  ChIP: None
**Papers**: 35853810: Mechanism of TLR4 mediated immune effect in transfusion-induced acute lung injur | 40480957: Unveiling the Potential Binding Targets of Celastrol in Colorectal Cancer: A Pro | 29511484: Protein profiling of infected human gastric epithelial cells with an Iranian Hel

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

SETSIP（Protein SETSIP）是一个292 aa的转录激活因子，其核心结构域为NAP家族保守区（Pfam NAP, PF00956, InterPro IPR002164），属于NAP样超家族折叠（InterPro IPR037231）。NAP（Nucleosome Assembly Protein）家族以参与核小体装配和组蛋白伴侣功能著称，SETSIP可能通过这一结构域与染色质相互作用。AlphaFold2预测pLDDT=78.0（得分6/10），无PDB实验结构，整体折叠可信度中等偏高。

SETSIP的PPI网络度为24，互作伙伴呈现出显著的转录调控和发育信号偏向。与TCF3（转录因子3，Wnt/β-catenin通路抑制因子）的BioGRID互作（score=1）提示SETSIP可能参与Wnt信号通路的核内调控。与EP300（p300组蛋白乙酰转移酶，经典转录辅激活因子）的BioGRID互作（score=1）提供了一个关键的机制连接——EP300通过乙酰化组蛋白和转录因子激活转录，SETSIP作为转录激活因子可能在核内与EP300协同增强靶基因的表达。与SP110（核体蛋白，干扰素诱导的转录调控因子）的互作则连接SETSIP与免疫信号的核内应答。

SETSIP的核心功能机制已在细胞重编程领域获得初步阐明。UniProt功能注释指出，SETSIP作为转录激活因子参与体细胞重编程的早期阶段，促进蛋白质诱导的多能干细胞（PiPS）向内皮细胞分化，并在体外诱导形成血管样管结构。SETSIP通过与VE-cadherin基因启动子结合，直接诱导血管内皮钙粘蛋白的表达。这是核质中转录调控功能的高度直接证据。PMID:22869753的研究首次描述了成纤维细胞通过直接重编程形成具有血管生成能力的血管内皮细胞的完整过程。

SETSIP的极高研究新颖性（PubMed=4，得分10/10）与明确的转录激活功能形成了有吸引力的研究组合。在核质Supported级别定位的背景下，SETSIP的NAP家族结构域可能介导其在核内的染色质靶向——NAP结构域通常识别组蛋白H2A-H2B二聚体或四聚体，SETSIP可能通过这一机制被招募至特定染色质位点。PMID:40480957将SETSIP鉴定为雷公藤红素在结直肠癌中的潜在结合靶标，为SETSIP的化学干预提供了可能。SETSIP在脂滴和核质的双定位提示其可能作为脂质代谢和核内基因表达的协调节点。

### 补充分析 (UniProt API)

**蛋白全称**: Protein SETSIP

**功能**: Plays a role as a transcriptional activator involved in the early stage of somatic cell reprogramming. Promotes the differentiation of protein-induced pluripotent stem (PiPS) cells into endothelial cells and the formation of vascular-like tubes (in vitro). Involved in the transcription induction of vascular endothelial-cadherin (VE-cadherin) expression. Associates to the VE-cadherin gene promoter

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037231 |
| InterPro | IPR002164 |
| Pfam | PF00956 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TCF3 | BioGRID | 1 |
| P3H1 | BioGRID | 1 |
| PPP3CA | BioGRID | 1 |
| TSN | BioGRID | 1 |
| RECQL4 | BioGRID | 1 |
| NR2C2 | BioGRID | 1 |
| EP300 | BioGRID | 1 |
| SP110 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P0DME0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SETSIP

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000230667-SETSIP

![](https://images.proteinatlas.org/63683/1152_C1_3_red_green.jpg)
![](https://images.proteinatlas.org/63683/1152_C1_4_red_green.jpg)
![](https://images.proteinatlas.org/63683/1178_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/63683/1178_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/63683/1156_C1_5_red_green.jpg)
![](https://images.proteinatlas.org/63683/1156_C1_6_red_green.jpg)

### PubMed

**Count: 4**

| PMID | Title |
|---|---|
| 40480957 | Unveiling the Potential Binding Targets of Celastrol in Colorectal Cancer: A Proteomic Profiling Approach Integrating Cellular Thermal Shift Assay and |
| 35853810 | Mechanism of TLR4 mediated immune effect in transfusion-induced acute lung injury based on Slit2/Robo4 signaling pathway. |
| 29511484 | Protein profiling of infected human gastric epithelial cells with an Iranian Helicobacter pylori clinical isolate. |
| 22869753 | Direct reprogramming of fibroblasts into endothelial cells capable of angiogenesis and reendothelialization in tissue-engineered vessels. |


