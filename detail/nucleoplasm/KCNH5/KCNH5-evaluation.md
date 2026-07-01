---
type: protein-evaluation
gene: "KCNH5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KCNH5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCNH5 |
| 蛋白名称 | Voltage-gated delayed rectifier potassium channel KCNH5 |
| 蛋白大小 | 988 aa / 111.9 kDa |
| UniProt ID | Q8NCM2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Centrosome; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 988 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=23 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=72.1; PDB=6 |
| 调控结构域 | 4/10 | x2 | 8.0 | cNMP-bd_dom; cNMP-bd_dom_sf; Ion_trans_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- Centrosome; Cytosol; Nucleoplasm (Approved)
- PubMed strict=23 broad=58
- AF pLDDT=72.1 PDB=6
- InterPro: cNMP-bd_dom; cNMP-bd_dom_sf; Ion_trans_dom
- Pfam: cNMP_binding; Ion_trans; PAS_9
- PPI degree=9 ChIP: None
39434833: Voltage-gated potassium channels and genetic epilepsy. | 38708366: Clinical phenotypes of developmental and epileptic encephalopathy-related recurr | 38797494: KCNH5 deletion increases autism susceptibility by regulating neuronal growth thr

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Voltage-gated delayed rectifier potassium channel KCNH5

**功能**: Pore-forming (alpha) subunit of a voltage-gated delayed rectifier potassium channel that mediates outward-rectifying potassium currents which, on depolarization, reaches a steady-state level and do not inactivate (PubMed:11943152, PubMed:12135768, PubMed:24133262, PubMed:36928654). The kinetic is characterized by a slow activation time course and a small voltage dependence of the activation time constants, therefore, starts to open at more negative voltages (PubMed:11943152, PubMed:12135768). Th

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000595 |
| InterPro | IPR018490 |
| InterPro | IPR005821 |
| InterPro | IPR003949 |
| InterPro | IPR003938 |
| InterPro | IPR050818 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

KCNH5（Voltage-gated delayed rectifier potassium channel KCNH5）是Kv通道超家族EAG亚家族的成员，其结构域架构包括环核苷酸结合域cNMP-bd_dom（IPR000595/IPR018490）和离子转运域Ion_trans_dom（IPR005821），Pfam注释为cNMP_binding、Ion_trans和PAS_9。988个氨基酸（111.9 kDa）的巨大分子量使其成为典型的六次跨膜（6TM）电压门控钾通道α亚基，包含N端的PAS结构域、电压传感域（VSD）、孔域（PD）和C端的环核苷酸结合同源域（CNBHD）。已有6个PDB结构（PDB=6）提供了部分结构信息，但AlphaFold预测的全长pLDDT仅为72.1，提示蛋白中存在显著的无序区域，可能位于连接VSD和PD的胞内环区以及N/C端区域。

HPA免疫荧光定位显示Centrosome; Cytosol; Nucleoplasm (Approved)，这是三种亚细胞定位的叠加模式。中心体定位与KCNH5在细胞周期进程中的潜在角色相关——钾通道在中心体的聚集已报道参与有丝分裂的调控。然而，核质定位（Nucleoplasm）对电压门控钾通道来说极为不寻常。一种可能的解释是：KCNH5的C端CNBHD结构域在特定条件下被切割并转位至细胞核，充当转录调控因子——类似的机制已在其他离子通道中被描述，例如L型钙通道的C端片段可进入核内调控转录。这种" moonlighting"现象的验证需要鉴定核定位形式的蛋白是否代表全长通道或蛋白酶切片段。

PPI网络分析揭示了KCNH5与Csk、微管蛋白（TUBA1B、TUBB4B、TUBB）、热休克蛋白HSPA8以及RNA结合蛋白HNRNPL的相互作用（均为BioGRID数据）。HNRNPL的互作尤为引人注目——hnRNP L是核内pre-mRNA加工和可变剪接的重要调控因子，这为KCNH5在核质中的功能定位提供了潜在线索。此外，KCNH4的同家族互作提示Kv通道可能形成异聚体复合物。

PubMed strict=23篇文献覆盖了KCNH5在遗传性癫痫（PMID 39434833, Mol Brain, 2026）、发育性癫痫脑病（PMID 38708366）和自闭症（PMID 38797494, 2024）中的功能获得性突变研究。KCNH5缺失通过调控神经元生长增加自闭症易感性的发现（PMID 38797494）暗示该通道参与神经发育中的基因表达调控——这一功能可能通过其在核质中的定位实现。未来的机制研究应探索：（1）KCNH5核定位的分子机制和生理条件；（2）HnRNP L-KCNH5互作在RNA剪接调控中的功能；（3）癫痫相关突变是否影响其亚细胞定位分布。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CSK | BioGRID | 0 |
| TUBA1B | BioGRID | 0 |
| TUBB4B | BioGRID | 0 |
| HSPA8 | BioGRID | 0 |
| TUBB | BioGRID | 0 |
| MBP | BioGRID | 0 |
| HNRNPL | BioGRID | 0 |
| KCNH4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NCM2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140015-KCNH5

![](https://images.proteinatlas.org/72351/1797_C5_33_cr59db5c6b9a697_red_green.jpg)
![](https://images.proteinatlas.org/72351/1797_C5_54_cr59db5c6b9a0fd_red_green.jpg)
![](https://images.proteinatlas.org/72351/1843_G8_31_red_green.jpg)
![](https://images.proteinatlas.org/72351/1843_G8_32_red_green.jpg)
![](https://images.proteinatlas.org/72351/1893_N9_13_cr5bc06c2f1b41b_red_green.jpg)
![](https://images.proteinatlas.org/72351/1893_N9_18_cr5bc06c2f1b419_red_green.jpg)

### PubMed 文献

**PubMed count: 58**

| 41656275 | Crosstalk of KCNH1 and KCNH5 gain-of-function mutations leading to epilepsy and neurodevelopmental disorders. | Mol Brain 2026 |
| 41110851 | Fentanyl blockade of K(+) channels contributes to wooden chest syndrome. | J Physiol 2026 |
| 39855736 | Effect of CXCR2 Deficiency in HeLa Cell on the Regulatory Network of Coding Genes and Non-Coding RNAs. | Ann Clin Lab Sci 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNH5

