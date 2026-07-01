---
type: protein-evaluation
gene: "CSDC2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted TE_REG_CANDIDATE]
status: shortlisted
---

## CSDC2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CSDC2 |
| 蛋白名称 | Cold shock domain-containing protein C2 |
| 蛋白大小 | 153 aa / 16.8 kDa |
| UniProt ID | Q9Y534 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) + ChIP |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 153 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=20 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=79.1; PDB=0 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | Ca-reg_mRNA-binding_domain; CSD; CSD_CS |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **131/180** | |
| **归一化总分 (÷1.83)** | | | **72.7/100** | 互证: +2 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Cytosol; Nucleoplasm (Approved) |
| PubMed | strict=20, broad=28 |
| AlphaFold | pLDDT=79.1 |
| PDB | 0 entries |
| InterPro | Ca-reg_mRNA-binding_domain; CSD; CSD_CS |
| Pfam | CSD |
| PPI | combined degree=4 |
| ChIP | Yes (TFs and others) |

### 4. 总体评价
⭐⭐⭐⭐
**72.7/100** | **nucleoplasm**
TE regulatory candidate — Ca-reg_mRNA-binding_domain; CSD; CSD_CS


### 补充分析 (UniProt API)

**蛋白全称**: Cold shock domain-containing protein C2

**功能**: RNA-binding factor which binds specifically to the very 3'-UTR ends of both histone H1 and H3.3 mRNAs, encompassing the polyadenylation signal. Might play a central role in the negative regulation of histone variant synthesis in the developing brain (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR052069 |
| InterPro | IPR011129 |
| InterPro | IPR019844 |
| InterPro | IPR002059 |
| InterPro | IPR012340 |
| Pfam | PF00313 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP2R1A | STRING | 721 |
| MEOX2 | BioGRID | 1 |
| INCA1 | BioGRID | 1 |
| MAPT | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y534-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000172346-CSDC2

![](https://images.proteinatlas.org/76549/1693_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/76549/1693_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/76549/1760_B2_13_cr594b7a19e6b1b_red_green.jpg)
![](https://images.proteinatlas.org/76549/1760_B2_19_cr594b7a225d38d_red_green.jpg)
![](https://images.proteinatlas.org/76549/1706_F1_3_cr57d84564c88f9_red_green.jpg)
![](https://images.proteinatlas.org/76549/1706_F1_13_cr57d8456c4efc3_red_green.jpg)

### PubMed 文献

**PubMed count: 28**

| 42343898 | Identification and multi-layered validation of seven diagnostic biomarkers for dilated cardiomyopathy via integrative ma | Front Cell Dev Biol 2026 |
| 42222348 | Integrating multi-omics analysis and machine learning to refine molecular subtypes and prognostic assessment of lower-gr | Mol Ther Oncol 2026 |
| 40933310 | Analysis and validation of characteristic genes in RNA sequencing datasets from heart failure patients based on multiple | Front Cardiovasc Med 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CSDC2


### 深度机制分析

CSDC2（Cold shock domain-containing protein C2）是一个小型RNA结合蛋白（153 aa, 16.8 kDa），仅含有一个冷休克结构域（CSD, Cold Shock Domain）作为其主要功能模块。InterPro结构域解析为：CSD核心折叠（IPR011129）、CSD保守序列标签（IPR019844）、Ca-reg_mRNA-binding_domain（IPR052069, 冷休克结构域在钙调控mRNA结合中的具体角色）以及核酸结合超家族折叠（IPR012340）。Pfam单一注释为CSD（PF00313）。AlphaFold预测pLDDT=79.1，对于仅含一个结构域的小蛋白而言属于中等水平——冷休克结构域本身是五条反平行β-桶（β-barrel）的紧凑折叠，理论上应有更高置信度，可能部分N端或C端尾段贡献了pLDDT下降。PDB=0，但细菌冷休克蛋白（如CspA, CspB）和真核Y-box蛋白的CSD结构已获得大量实验结构。

CSD的RNA结合模式基于保守的RNP-1和RNP-2基序，通过芳香族侧链（苯丙氨酸和酪氨酸）与RNA碱基之间的堆积相互作用（stacking interaction），以及带正电残基（精氨酸和赖氨酸）与RNA磷酸骨架的静电作用，实现序列非特异性的单链核酸绑定。CSDC2被特别注释为特异性结合组蛋白H1和H3.3 mRNA的极3'-UTR端（含多聚腺苷酸化信号），通过这一机制在中枢神经系统中负调控组蛋白变体的合成（UniProt:By similarity）。

PPI互作网络极其有限（degree=4），但STRING最大可信度互作伙伴PPP2R1A（score=721）尤为重要——PPP2R1A是蛋白磷酸酶2A（PP2A）的支架亚基（A亚基）。PP2A是细胞内主要的丝/苏氨酸蛋白磷酸酶，直接参与染色质调控（组蛋白去磷酸化）、剪接调控（SR蛋白去磷酸化）和细胞周期调控。CSDC2-PPP2R1A互作若经实验验证，意味着CSDC2可能通过PP2A的招募调控靶mRNA局部区域的磷酸化/去磷酸化平衡。BioGRID记录的其他互作伙伴（MEOX2, INCA1, MAPT）以最低置信度报告（score=0），功能意义不明确。

CSDC2已被标记为TE_REG_CANDIDATE（TE调控候选），主要依据在于：ChIP-seq数据阳性（TFs and others）——这在小蛋白和RNA结合蛋白中极为罕见，暗示CSDC2可能通过间接机制（RNA介导的染色质定位或蛋白-蛋白互作）与染色质关联。HPA显示Cytosol和Nucleoplasm（Approved）的清晰双重定位，IF图像呈现核内弥散+部分点状分布，后者可能对应RNA-蛋白复合体（RNP颗粒）或转录活跃区域。CSD结构域本身的生物学功能范围——从细菌冷休克适应性（CspA激活冷休克基因转录）到真核细胞转录/翻译调控（Y-box蛋白）——暗示CSDC2可能具有调控组蛋白mRNA加工和染色质动力学的双重角色。

PubMed研究主要来自多组学生物标志物筛选。CSDC2被多项研究鉴定为扩张型心肌病（PMID:42343898）、低级别胶质瘤（PMID:42222348）和心力衰竭（PMID:40933310）的诊断/预后生物标志物基因的成员。这些生物信息学筛选虽未直接确认CSDC2的分子机制，但一致地将CSDC2与心脏和神经系统疾病相关联。综合来看，CSDC2的深度机制模型为：CSD折叠→组蛋白H1/H3.3 mRNA 3'-UTR特异性绑合→组蛋白变体翻译负调控→中枢神经系统发育调控；核内次要功能：PP2A互作→局部磷酸化微环境调控→染色质间接关联（ChIP阳性）。作为小型RNA结合蛋白（153 aa），CSDC2具有"通过RNA调控染色质"的间接TE调控潜力——其ChIP-seq阳性可能是CSD通过结合新生RNA（nascent RNA）或R-loop结构而被交联至染色质的反映。这一机制的实验验证将决定其作为TE调控候选的优先级别。



