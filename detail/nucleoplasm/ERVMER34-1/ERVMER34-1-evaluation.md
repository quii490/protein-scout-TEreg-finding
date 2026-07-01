---
type: protein-evaluation
gene: "ERVMER34-1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## ERVMER34-1 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ERVMER34-1 |
| 蛋白名称 | Endogenous retroviral envelope protein HEMO |
| 蛋白大小 | 563 aa / 63.5 kDa |
| UniProt ID | Q9H9K5 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 563 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=44.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TLV/ENV_coat_polyprotein |
| PPI | 5/10 | x3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |
### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=6, broad=7
- AF pLDDT: 44.3 / PDB: 0
- InterPro: TLV/ENV_coat_polyprotein
- Pfam: 
- PPI degree=9 / ChIP: None
40360436: Combination of a therapeutic cancer vaccine targeting the endogenous retroviral  | 38408442: Human Endogenous Retroviruses in Breast Cancer: Altered Expression Pattern Impli | 33028275: Prognosis prediction model based on competing endogenous RNAs for recurrence of 
### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Endogenous retroviral envelope protein HEMO

**功能**: Endogenous envelope proteins originate from retroviral envelope proteins, which mediate receptor recognition and membrane fusion during early infection. Endogenous envelope proteins may have kept, lost or modified their original function during evolution

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018154 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LRRC32 | BioGRID | 1 |
| BTLA | BioGRID | 0 |
| TMEM106A | BioGRID | 0 |
| FBXO2 | BioGRID | 0 |
| HLA-G | BioGRID | 0 |
| FBXO6 | BioGRID | 0 |
| SLURP1 | BioGRID | 0 |
| SFTPC | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H9K5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000226887-ERVMER34-1

![](https://images.proteinatlas.org/24053/917_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/24053/917_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/24053/1026_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/24053/1026_E12_3_red_green.jpg)
![](https://images.proteinatlas.org/24053/920_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/24053/920_D11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 7**

| 41329733 | The human endogenous retroviral envelope HEMO protein interacts with BACE2: Novel partnership acquired in the primate li | Proc Natl Acad Sci U S A 2025 |
| 40360436 | Combination of a therapeutic cancer vaccine targeting the endogenous retroviral envelope protein ERVMER34-1 with immune- | J Immunother Cancer 2025 |
| 38408442 | Human Endogenous Retroviruses in Breast Cancer: Altered Expression Pattern Implicates Divergent Roles in Carcinogenesis. | Oncology 2024 |

### 深度机制分析

ERVMER34-1（563 aa, 63.5 kDa）是一个内源性逆转录病毒（ERV）包膜蛋白HEMO，源自古老逆转录病毒感染的基因组整合与驯化。其结构域架构仅包含TLV/ENV外壳多聚蛋白结构域（IPR018154），对应逆转录病毒包膜基因（env）编码的前体蛋白，该前体通常被弗林蛋白酶样蛋白酶切割为表面（SU）和跨膜（TM）亚基。AlphaFold预测pLDDT仅44.3，为所有25个蛋白中最低值之一，这种高度无序性在病毒包膜蛋白中常见——env蛋白的SU亚基通常含有高度糖基化和柔性的受体结合域，TM亚基则含有融合肽和跨膜锚定螺旋。

作为驯化的ERV蛋白，ERVMER34-1的功能已偏离其祖先的病毒入侵角色。UniProt注释确认内源性包膜蛋白可能在进化过程中保留、丢失或改变了原有功能。近年研究揭示HEMO（ERVMER34-1）与BACE2（β分泌酶2）存在灵长类谱系特异的直接相互作用（PMID:41329733），这是ERV蛋白获得宿主新功能的典型案例。BACE2是阿尔茨海默病病理中BACE1的同源蛋白，参与APP剪切，ERVMER34-1-BACE2互作的驯化意味着该ERV蛋白已被整合入宿主蛋白酶网络。

HPA将ERVMER34-1定位于Cytosol; Nucleoplasm（Approved级别），核质定位可能是ERV包膜蛋白未预期但合理的存在——在感染周期中，逆转录病毒的前整合复合物（PIC）需穿越核孔进入核质进行整合。驯化后的包膜蛋白可能在核质中保留了某些PIC相关功能或获得全新的核内角色。PPI网络（BioGRID degree=9）中，与BTLA（免疫检查点受体）、HLA-G（免疫耐受MHC I类分子）和FBXO2/FBXO6（F-box泛素连接酶底物受体）的互作提示ERVMER34-1参与免疫调控和蛋白泛素化降解通路。

在TE调控语境下，ERVMER34-1作为自身来自TE的蛋白，为理解TE驯化和TE调控提供了独特视角。其作为ERV env蛋白在核质中的存在可能通过以下途径影响TE生物学：（1）作为显性负调控因子干扰现代ERV包膜蛋白的组装或功能；（2）通过结合核内受体或转录因子间接影响TE表达；（3）作为"TE印记"被宿主免疫系统识别，参与肿瘤免疫微环境中的TE去抑制检测。治疗性癌症疫苗靶向ERVMER34-1联合免疫检查点抑制的研究（PMID:40360436）表明其作为"肿瘤TE抗原"的临床应用前景。建议通过RNA-Seq和TEtranscripts分析ERVMER34-1过表达/敲低对全基因组TE家族表达的影响，以及CUT&Tag检测其是否直接结合特定TE家族。

