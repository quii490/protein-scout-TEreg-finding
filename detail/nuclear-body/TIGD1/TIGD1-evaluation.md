---
type: protein-evaluation
gene: "TIGD1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## TIGD1 (Tigger transposable element-derived protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | TIGD1 |
| 蛋白全称 | Tigger transposable element-derived protein 1 |
| UniProt ID | Q96MW7 |
| 蛋白大小 | 591 aa / 65.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 591 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR050863; InterPro:IPR004875; InterPro:IPR009057; InterPro:IPR006600; InterPro:IPR007889; InterPro:IPR036397 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |
| InterPro | IPR007889 |
| InterPro | IPR036397 |
| Pfam | PF04218 |
| Pfam | PF03184 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

**结构域架构**：TIGD1（Tigger transposable element-derived protein 1, 591 aa, 65.0 kDa）是TE来源的蛋白质——由Tigger DNA转座子（Tc1/mariner超家族）驯化（domestication）而来，含DDE/DDE转座酶催化保守基序。结构域包括HTH psq-type（aa 6-57, PROSITE PRU00320）识别DNA，HTH CENPB-type（aa 70-149, HTH DNA-binding domain of CENPB）为着丝粒蛋白B同源DNA结合域——直接结合17 bp CENP-B box motif（TTCGNNNNANNCGGGA），DDE-1 endonuclease（aa 178-403）为催化核心——含Asp-Asp-Glu catalytic triad（DDE motif）介导Mg2+依赖的DNA切割和链转移。AlphaFold可用但pLDDT未在报告中给出。PPI（degree有限）以DNA/chromatin蛋白为核心：APP（BioGRID）、MKI67/Ki-67（BioGRID, cell proliferation marker）、MSX2（BioGRID, homeobox transcription factor）、CEBPB（BioGRID, bZIP transcription factor）。PubMed 17篇主要集中在癌症预后标记物：41775084揭示TIGD基因在肝癌中的单细胞分析和预后价值（Transl Oncol 2026），40565566报道TIGD1作为pan-cancer biomarker和免疫调节因子（Genes 2025），39734333发现TIGD1在肺癌中的生物标记潜力（Turk J Med Sci 2024）。核定位：HPA显示nucleoplasm和nuclear bodies定位。

**TE调控展望**：TIGD1是从Tigger DNA转座子"驯化"来的domesticated transposase——这种分子驯化（molecular domestication）事件在演化中产生了许多宿主转录因子（如CENPB, RAG1/2, THAP9, SETMAR）。TIGD1的CENPB-type HTH domain与CENPB（着丝粒结合因子）高度同源——CENPB通过结合alphoid satellite DNA上的CENP-B box在centromere/kinetochore组装中起核心作用——TIGD1可能类似性地识别TE来源的DNA序列并在特定的genomic loci上作为transcriptional regulator。其DDE催化域是否保留了DNA切割活性（即作为functional transposase）是完全未知的关键问题——若保留，TIGD1可能参与体细胞转座或其他形式的genome rearrangement。TIGD1作为TE驯化产物本身调控宿主基因组中的TE——这是"TE fighting TE"的分子例子。在肝癌和肺癌中的预后价值暗示TIGD1的deregulation可能影响cancer genome中的TE表达谱。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000221944-TIGD1
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/41717/1060_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/41717/1060_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/41717/1137_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/41717/1137_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/41717/1888_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/41717/1888_F6_4_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00674; |
| InterPro | IPR050863;IPR004875;IPR009057;IPR006600;IPR007889;IPR036397; |
| Pfam | PF04218;PF03184;PF03221; |
| UniProt Domain | DOMAIN 6..57; /note="HTH psq-type"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00320"; DOMAIN 70..149; /note="HTH CENPB-type"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00583"; DOMAIN 178..403; /note="DDE-1"; /evidence="ECO:0000255" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| ZNF131 | BioGRID | 1 |
| MKI67 | BioGRID | 1 |
| CALM2 | BioGRID | 1 |
| CALM3 | BioGRID | 1 |
| MIF | BioGRID | 1 |
| MSX2 | BioGRID | 1 |
| CEBPB | BioGRID | 1 |


### PubMed 文献

**PubMed count: 17**

| 41775084 | Single-cell analysis of TIGD genes in hepatocellular carcinoma: Prognostic value and functional characterization. | Transl Oncol 2026 |
| 40565566 | Beyond Transposons: TIGD1 as a Pan-Cancer Biomarker and Immune Modulator. | Genes (Basel) 2025 |
| 39734333 | Investigating the biomarker potential and molecular targets of TIGD1 in lung cancer using bioinformatics. | Turk J Med Sci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD1

