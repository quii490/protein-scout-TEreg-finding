---
type: protein-evaluation
gene: "PCDHGA7"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA7 |
| 蛋白名称 | Protocadherin gamma-A7 |
| 蛋白大小 | 932 aa / 101.7 kDa |
| UniProt ID | Q9Y5G6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 932 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=74.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=24 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=1 broad=1
- AF pLDDT=74.0 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=24 ChIP: None
30121367: Protocadherin γ-A7 is down-regulated in colorectal cancer and associated with th

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A7

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCDHGB1 | BioGRID | 0 |
| PCDHGA5 | BioGRID | 0 |
| LTBP1 | BioGRID | 0 |
| ATP2B2 | BioGRID | 0 |
| PCDHGA6 | BioGRID | 0 |
| SLITRK3 | BioGRID | 0 |
| SDCBP | BioGRID | 0 |
| DPP6 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5G6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA7

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000253537-PCDHGA7

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed

**Count: 1**

| PMID | Title |
|---|---|
| 30121367 | Protocadherin γ-A7 is down-regulated in colorectal cancer and associated with the prognosis in patients with wild-type KRAS. |


### 深度机制分析

PCDHGA7（Protocadherin gamma-A7）属于原钙粘蛋白γ基因簇（PCDHG，位于5q31.3）的22个串联排列成员之一，该成员的典型结构域架构包含六个钙粘蛋白（Cadherin）胞外重复单元（EC1-EC6）：分别由IPR002126 Cadherin-like_dom、IPR015919 Cadherin-like_sf（超家族）和IPR020894 Cadherin_C（C端胞外重复）注释，Pfam对应条目为Cadherin（PF00028）、Cadherin_2和Cadherin_C_2。每个EC重复约110 aa，折叠为免疫球蛋白样希腊钥匙β-桶拓扑，EC1-EC2之间的钙离子结合位点（由保守的DXD、DXNDN和DXD基序构成）介导Ca2+依赖的同嗜性反式二聚化。932 aa赋予了PCDHGA7胞外域的充分延伸长度（约35 nm），远大于经典钙粘蛋白的胞外长度（约22 nm），提示其在突触间隙中可实现更灵活的跨间隙识别。AlphaFold v6预测pLDDT=74.0，无PDB实验结构（得分5/10），有序区域的高置信度主要源于钙粘蛋白EC重复单元内在的紧凑且保守折叠模式。

PCDHG基因簇的核心机制创新在于其"启动子选择"策略实现单细胞表达多样性。每个PCDHG神经元仅表达22个γ-Pcdh可变外显子中的1-3个（通过DNA去甲基化驱动的启动子激活），而后通过反式剪接将选定的可变外显子与下游恒定外显子拼接。这种组合方式理论上可在不同神经元上产生>2,000种不同Pcdh-γ同工型的表面表达组合，进而通过同工型特异性的同嗜性相互作用驱动神经元自我回避（self-avoidance）和突触特异性。PCDHGA7在此框架中提供了第A7号胞外识别界面——其胞外域序列的细微差异决定了识别特定同工型组合的突触前伙伴神经元。PPI数据中PCDHGA7的24个互作伙伴以同家族成员（PCDHGB1、PCDHGA5、PCDHGA6）为主，这正是上述顺式多聚化（同一神经元表面γ-Pcdh同工型间的异源相聚集成簇）和反式识别（跨突触间隙的同工型特异性结合）的结构基础。

从结直肠癌研究（PMID:30121367）中获得的一个重要线索是PCDHGA7启动子在肿瘤中高甲基化导致表达下调，且与KRAS野生型患者预后相关。这一表观遗传沉默现象提供了PCDHG基因簇启动子甲基化作为癌症生物标志的初步证据——在神经元之外的组织中，PCDHG启动子通常处于高甲基化沉默状态；肿瘤中的异常去甲基化可能导致PCDHGA7的异位表达，改变细胞粘附特性并影响肿瘤侵袭性。这也间接暗示PCDHGA7在细胞-细胞接触依赖的信号转导（如接触抑制）中可能有未被发现的功能。

核质定位信号（HPA为胞质、核质、质膜、囊泡，Uncertain）在PCDHGA7的机制背景中仅具有边际意义。大量PCDHG功能研究聚焦于细胞表面，且PCDHGA7的跨膜域和胞内域在序列上不具备任何已知的核定位信号样基序。观察到的核质信号几乎可以确定是膜蛋白在内质网-高尔基体合成运输通路的沿途标记。综合得分67.8/100反映了其在极度新颖（PubMed严格=1篇）和结构质量（pLDDT=74.0）上的优势，以及核定位特异性仅7/10（Uncertain级别）的限制。PCDHGA7的真正科学前沿在于PCDHG启动子选择机制的表观遗传调控——即何种染色质因子决定了不同γ-Pcdh可变启动子在单个神经元中的特异性激活或沉默，这一问题直接关系到神经元自我识别这一大脑最底层逻辑的分子基础。
