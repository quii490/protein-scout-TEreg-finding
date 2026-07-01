---
type: protein-evaluation
gene: "PDCL"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PDCL 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PDCL |
| 蛋白名称 | Phosducin-like protein |
| 蛋白大小 | 301 aa / 34.3 kDa |
| UniProt ID | Q13371 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 301 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=32 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=76.4; PDB=12 |
| 调控结构域 | 4/10 | x2 | 8.0 | Phosducin; Phosducin-like_reg; Phosducin_N_dom_sf |
| PPI | 7/10 | x3 | 21.0 | PPI degree=132 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=32 broad=1413
- AF pLDDT=76.4 PDB=12
- InterPro: Phosducin; Phosducin-like_reg; Phosducin_N_dom_sf
- Pfam: Phosducin
- PPI degree=132 ChIP: None
35819261: Pharmacologic Targeting of TFIIH Suppresses KRAS-Mutant Pancreatic Ductal Adenoc | 32241620: PNA-Based Dynamic Combinatorial Libraries (PDCL) and screening of lectins. | 36761421: HROP68: A rare case of medullary pancreatic cancer-characterization and chemosen

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PDCL（Phosducin-like protein, Q13371）是硫氧还蛋白折叠超家族成员，其核心功能模块由IPR001200（Phosducin）和IPR024253（Phosducin-like_reg）结构域构成，PF02114 Pfam结构域覆盖其全长的绝大部分（301 aa）。Phosducin家族蛋白的标志性功能是作为G蛋白异源三聚体的分子伴侣——通过其N端硫氧还蛋白样折叠结构域（IPR036249, Phosducin_N_dom_sf）竞争性地结合G蛋白βγ亚基二聚体（Gβγ），阻止Gα与Gβγ的重组，从而负调控GPCR下游信号传导。PDCL的PPI网络中，GNB5（STRING评分998）作为G蛋白β5亚基的直接结合伙伴，以极高置信度验证了这一经典功能。同时，PDCL与CCT4（STRING 753）的强互作揭示了另一层分子逻辑：CCT4是TRiC/CCT伴侣蛋白复合体的亚基，该复合体专门负责含β-折叠蛋白（如Gβ亚基）的正确折叠，表明PDCL不仅在信号终止环节捕获Gβγ，还可能协同TRiC系统参与Gβγ的从头折叠与质量控制。

PDCL被UniProt注释为hedgehog信号通路的正调控因子并在纤毛功能调控中发挥作用，这一功能维度值得深入解析。Hedgehog信号传导高度依赖初级纤毛，其中GPCR类受体Smoothened（SMO）和G蛋白信号在纤毛内精细调控Gli转录因子的加工。PDCL通过其对G蛋白信号的调控，可能在纤毛基部或轴丝内调控G蛋白偶联信号复合体的组装与动态平衡。此外，PPI网络中的CDK15（细胞周期蛋白依赖性激酶15）和ACTL6A（肌动蛋白样蛋白6A，SWI/SNF染色质重塑复合体的亚基）暗示PDCL的功能可能延伸至细胞骨架调控和染色质重塑的交叉界面——ACTL6A参与核小体重塑，而phosducin家族蛋白在视网膜光转导中的经典角色正是通过G蛋白信号调控细胞骨架动态。

从结构角度审视，AlphaFold预测的pLDDT值为76.4，属于中等置信度区间。12个PDB条目提供了实验结构验证，使得PDCL的结构表征优于大多数人类蛋白质。pLDDT分布图（通过PAE图可推断）可能揭示N端结构域高度有序，而C端可能含有部分无序区域——这符合phosducin家族中Gβγ结合界面位于N端硫氧还蛋白折叠域的特征。部分无序的C端通常作为调控区，可能介导与其他信号蛋白（如ELAVL1/HuR RNA结合蛋白）的动态互作，或者作为翻译后修饰的靶点以调控PDCL自身的亚细胞定位和蛋白稳定性。

PPI网络中一个引人注目的节点是IKBKG（NEMO，NF-κB必需调节因子），虽然评分仅1但来自BioGRID物理互作数据。若该互作在生理条件下成立，PDCL将串联起G蛋白信号与NF-κB炎症通路，为hedgehog信号与先天性免疫的交叉调控提供一个新的分子桥梁。ENDOV（核酸内切酶V）和ELAVL1（mRNA稳定性调控因子HuR）的互作进一步暗示PDCL可能在RNA代谢层面也发挥未被认识的功能，或通过G蛋白信号间接影响mRNA的稳定性与翻译效率。综合来看，PDCL是一个以G蛋白βγ分子伴侣功能为核心、依赖CCT伴侣系统进行质量控制的信号枢纽蛋白，其在核质中的存在可能与纤毛-核信号传递（如Gli转录因子核质穿梭）或RNA结合蛋白介导的核内功能有关。该蛋白作为hedgehog通路正调控因子的特性使其成为肿瘤（尤其KRAS突变胰腺癌，见PMID 35819261）和纤毛病潜在治疗靶点，但选择性靶向PDCL需要规避其对视觉G蛋白信号（视网膜phosducin功能）的干扰。


### 补充分析 (UniProt API)

**蛋白全称**: Phosducin-like protein

**功能**: Acts as a positive regulator of hedgehog signaling and regulates ciliary function

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001200 |
| InterPro | IPR051499 |
| InterPro | IPR023196 |
| InterPro | IPR024253 |
| InterPro | IPR036249 |
| Pfam | PF02114 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GNB5 | STRING | 998 |
| PDCL3 | STRING | 767 |
| CCT4 | STRING | 753 |
| IKBKG | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| ENDOV | BioGRID | 1 |
| ACTL6A | BioGRID | 1 |
| CDK15 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q13371-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136940-PDCL

![](https://images.proteinatlas.org/21571/190_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/190_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136940-PDCL

![](https://images.proteinatlas.org/21571/190_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/190_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136940-PDCL

![](https://images.proteinatlas.org/21571/190_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/190_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/189_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21571/191_G5_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 1414**

| 42290532 | N-Heterocyclic Carbene-Palladium Complex IPent(An)-PdCl(2)-Im: Highly Efficient for Buchwald-Hartwig Amination of Hetero | Org Lett 2026 |
| 42241110 | Metalations of a Carbazole-Incorporated N-Confused Porphyrin. | Org Lett 2026 |
| 42198892 | Flexible Perovskite/Silicon Tandem Solar Cells Exceeding 30% Efficiency at Scale. | Adv Mater 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PDCL

