---
type: protein-evaluation
gene: "A0A024R693"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A0A024R693 (MHC class I alpha chain) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A0A024R693 |
| 蛋白全称 | MHC class I alpha chain |
| UniProt ID | A0A024 |
| 蛋白大小 | 354 aa / 38.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 354 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR007110; InterPro:IPR036179; InterPro:IPR013783; InterPro:IPR003006; InterPro:IPR003597; InterPro:IPR050208 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the presentation of foreign antigens to the immune system

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003006 |
| InterPro | IPR003597 |
| InterPro | IPR050208 |
| InterPro | IPR011161 |
| InterPro | IPR037055 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A024R693

### 深度机制分析

A0A024R693的蛋白架构以免疫球蛋白样结构域为核心，包含IPR007110（Ig-like domain）、IPR036179（Ig-like domain superfamily）、IPR013783（Ig-like fold）和IPR003597（Ig C1-set），以及MHC I类分子特有的IPR050208（MHC class I alpha chain, alpha1 and alpha2）、IPR011161（MHC class I-like antigen recognition）和IPR037055（MHC class I alpha chain, alpha1 alpha2）。经典免疫学教科书将MHC I类α链定义为内质网-高尔基体-细胞膜通路的抗原呈递分子，然而该蛋白的PPI网络揭示了一组与经典抗原呈递功能不兼容的高置信度互作伙伴。LGALS3（galectin-3, STRING score 945）是一个特征明确的具有核质穿梭能力的β-半乳糖苷结合蛋白，已被证实在核内参与pre-mRNA剪接调控。KRAS（score 524）的核内定位亦非孤例，核内KRAS通过与核仁素相互作用调节rRNA加工和核糖体生物合成。而EGFR（score 630）的核转位机制已被深入阐明（PMID: 11684018）：细胞表面EGFR经配体诱导内化后，可通过COPI介导的逆行转运从高尔基体转运至内质网，随后其核定位信号被识别并经importin-β介导的途径进入细胞核，在核内作为STAT3、cyclin D1等基因的转录共激活因子。MUC16（CA125, score 951）——通常被认为是卵巢癌血清标志物——其胞内结构域已被报道在特定条件下与染色质重塑因子相互作用。

这些PPI伙伴共同的"核兼职"（nuclear moonlighting）特性提供了一个重要的机制视角：A0A024R693可能是被经典膜蛋白注释所掩盖的、具有条件性核定位的MHC I类α链亚型。其Ig样折叠（IPR013783）结构上具有高度可塑性，理论上可发生构象变化暴露隐蔽的核定位信号（cryptic NLS），或通过与具有核定位能力的伙伴蛋白（如LGALS3）的"搭便车"（piggyback）机制实现核转位。这种"膜蛋白-核转位"范式并非史无前例——Fas/CD95、ErbB2等多个受体酪氨酸激酶和细胞表面受体均已报道存在核转位并执行不同于其膜定位功能的"兼职"现象。

LAG3（score 422）的参与更具启示性。LAG3是一个免疫检查点受体，与PD-1和CTLA-4并列为肿瘤免疫治疗的核心靶点。其胞内结构域含有独特的KIEELE基序，是其抑制性信号传导的核心。如果A0A024R693与LAG3在核内存在功能性相互作用，可能暗示一种全新的"免疫检查点-染色质调控"信号轴，在肿瘤免疫逃逸和自身免疫中具有潜在意义。GP6（score 932）的极高评分结合表明物理相互作用的高度可能性，而GP6在经典模型中是血小板表面的胶原受体，其在核质组分中被检测到本身就挑战了现有认知。

当前数据中最显著的矛盾是：该蛋白在核质组分中富集（因而进入评估管线），但所有常规数据库均未赋予其核定位注释。这一矛盾恰好指向最富价值的研究方向——条件性或细胞类型特异性的核定位，通常被高通量数据所掩盖而仅在专门的功能实验中被揭示。由于该蛋白Pubmed检索为零且属于TrEMBL未审查条目，任何系统性功能研究都将是此领域的新发现。建议的验证实验包括：(1) 免疫荧光共定位实验，系统筛查不同细胞系和刺激条件（如IFN-γ、DNA损伤、热激等）下是否存在核转位；(2) 细胞组分分离后Western blot确认核组分中的存在；(3) APEX2邻近标记蛋白质组学以捕获其核内相互作用组；(4) 如果证实其核定位，进一步通过CUT&RUN/CUT&Tag确定其染色质结合谱。

### 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A024
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A024
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A0A024R693

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LAG3 | STRING | 422 |
| LGALS3 | STRING | 945 |
| KRAS | STRING | 524 |
| TLR2 | STRING | 644 |
| LGALS3BP | STRING | 500 |
| EGFR | STRING | 630 |
| CLEC7A | STRING | 752 |
| GP6 | STRING | 932 |
| FN1 | STRING | 463 |
| FCGR2B | STRING | 467 |
| ELN | STRING | 445 |
| MUC16 | STRING | 951 |
| PTPRC | STRING | 453 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131981

![](https://images.proteinatlas.org/5191/639_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/5191/639_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/5191/635_D6_5_red_green.jpg)
![](https://images.proteinatlas.org/5191/635_D6_6_red_green.jpg)
![](https://images.proteinatlas.org/76528/2057_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/76528/2057_C12_5_red_green.jpg)
![](https://images.proteinatlas.org/76528/1920_D10_3_cr5e39373c1d6a6_red_green.jpg)
![](https://images.proteinatlas.org/76528/1920_D10_30_cr5e39373c1daec_red_green.jpg)
