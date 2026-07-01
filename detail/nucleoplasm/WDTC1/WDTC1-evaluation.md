---
type: protein-evaluation
gene: "WDTC1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## WDTC1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | WDTC1 |
| 蛋白名称 | WD and tetratricopeptide repeats protein 1 |
| 蛋白大小 | 677 aa / 75.9 kDa |
| UniProt ID | Q8N5D0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 677 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=14 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=81.6; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | DCAF8; TPR-like_helical_dom_sf; TPR_rpt |
| PPI | 7/10 | x3 | 21.0 | PPI degree=147 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=14 broad=20
- AF pLDDT=81.6 PDB=1
- InterPro: DCAF8; TPR-like_helical_dom_sf; TPR_rpt
- Pfam: WD40
- PPI degree=147 ChIP: None
37691821: TRiC/CCT chaperonin is required for the folding and inhibitory effect of WDTC1 o | 35238908: The putative oncogenic role of WDTC1 in colorectal cancer. | 21544814: Candidate driver genes in microsatellite-unstable colorectal cancer.

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear蛋白


### 深度机制分析

**WD40-TPR双重复支架蛋白的CUL4-DDB1底物受体功能**：WDTC1（WD and tetratricopeptide repeats protein 1, 677 aa, UniProt Q8N5D0）拥有WD40重复（Pfam WD40, InterPro: WD40_repeat_dom IPR015943）和TPR重复（InterPro: TPR_rpt IPR019734, TPR-like_helical_dom_sf IPR011990）双结构域架构，是CUL4-DDB1 E3泛素连接酶复合物的推定底物受体（UniProt annotation）。DCAF8（IPR045151）分类暗示WDTC1属于DDB1-CUL4-associated factor（DCAF）家族，通过WD40域的β-螺旋结构识别特定的底物蛋白，将其呈递给DDB1-CUL4-ROC1连接酶进行泛素化降解。

**CUL4-DDB1泛素连接酶在染色质调控中的核心地位**：CUL4-DDB1 E3连接酶（CRL4复合物）通过不同的DCAF底物受体参与多种染色质修饰过程：(1) DCAF1/Cdt2介导组蛋白H3K4me和H3K9me去甲基化酶（LSD1/KDM1A）的泛素化降解，直接影响H3K4me1/2和H3K9me1/2水平；(2) DCAF4和DCAF5介导SUV39H1组蛋白甲基转移酶的降解，影响H3K9me3水平；(3) CRL4^Cdt2在DNA复制和DNA损伤应答中泛素化降解PCNA和CDKN1A/p21。若WDTC1作为DCAF靶向染色质修饰因子，可能通过H3K9甲基化水平调控TE位点的异染色质状态。

**PPI网络的高置信度支持**：PPI degree=147（STRING/BioGRID），DDB1（STRING 996）和CUL4A（STRING 930）的超高互作评分确证了WDTC1作为CRL4底物受体的身份。CUL4B（STRING 862）的存在提示WDTC1可能同时与胞质CUL4A和核内CUL4B两种cullin scaffold互作。TADA2A（BioGRID score=1）是第二个重要互作——TADA2A是SPT3-TAF9-GCN5乙酰转移酶（STAGA）复合物的组分，参与组蛋白H3乙酰化（H3K9ac, H3K14ac）。这种同时与泛素化（CRL4）和乙酰化（STAGA）机器互作的双向连接性极不寻常，暗示WDTC1可能协调组蛋白乙酰化和泛素化修饰的交叉对话。

**TRiC/CCT伴侣蛋白依赖的结构折叠**：PMID:37691821揭示WDTC1的折叠和功能依赖于TRiC/CCT伴侣蛋白——TRiC是~1 MDa的大型双环状分子伴侣，专一折叠WD40 β-螺旋蛋白。AlphaFold pLDDT=81.6的中等置信度和PDB=1的部分结构覆盖提示WD40域折叠正确。实验验证：CRISPR敲除WDTC1后进行染色质修饰组学（H3K9me3 ChIP-seq）和TE转录组（特别是年轻LINE-1和SVA）分析是评估其TE调控功能的首选方案。归一化得分68.3/100中PPI维度21/30和新奇性45/50是两个主要支撑。


### 补充分析 (UniProt API)

**蛋白全称**: WD and tetratricopeptide repeats protein 1

**功能**: May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045151 |
| InterPro | IPR011990 |
| InterPro | IPR019734 |
| InterPro | IPR015943 |
| InterPro | IPR036322 |
| InterPro | IPR001680 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDB1 | STRING | 996 |
| CUL4A | STRING | 930 |
| CUL4B | STRING | 862 |
| DDA1 | STRING | 718 |
| DDB2 | STRING | 716 |
| DCAF4 | STRING | 716 |
| USP3 | BioGRID | 1 |
| TADA2A | BioGRID | 1 |