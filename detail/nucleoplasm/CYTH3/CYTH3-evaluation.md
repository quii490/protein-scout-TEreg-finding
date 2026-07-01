---
type: protein-evaluation
gene: "CYTH3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CYTH3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CYTH3 |
| 蛋白名称 | Cytohesin-3 |
| 蛋白大小 | 400 aa / 46.3 kDa |
| UniProt ID | O43739 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 400 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=84.2; PDB=3 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PH-like_dom_sf; PH_domain; Sec7_C_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Supported)
- PubMed strict=7 broad=13
- AF pLDDT=84.2 PDB=3
- InterPro: PH-like_dom_sf; PH_domain; Sec7_C_sf
- Pfam: PH; Sec7
- PPI degree=39 ChIP: None
34413360: A machine learning approach to identify predictive molecular markers for cisplat | 40834973: Heat stress-induced genomic instability in neural stem cells and its association | 33649051: Host Genome-Wide Association Study of Infant Susceptibility to Shigella-Associat

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cytohesin-3

**功能**: Promotes guanine-nucleotide exchange on ARF1 and ARF6. Promotes the activation of ARF factors through replacement of GDP with GTP. Plays a role in the epithelial polarization (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011993 |
| InterPro | IPR001849 |
| InterPro | IPR023394 |
| InterPro | IPR000904 |
| InterPro | IPR035999 |
| Pfam | PF00169 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

CYTH3（Cytohesin-3），又名ARNO3或GRP1，属于cytohesin/ARNO家族的鸟嘌呤核苷酸交换因子（GEF）。其结构域架构由两个功能模块组成：（1）中央的Sec7催化域（IPR000904/IPR035999 / Pfam Sec7, PF00169）——通过促进GDP解离和GTP结合来激活ARF小GTP酶；（2）C端的PH结构域（IPR001849 / Pfam PH, PF00169），介导膜磷脂酰肌醇磷酸的结合和膜招募。400个氨基酸（46.3 kDa）的分子量和pLDDT=84.2的结构置信度指示一个结构紧凑、折叠良好的双结构域蛋白。PDB数据库中有3个条目的结构信息支持了这一点。

CYTH3通过PH结构域与磷脂酰肌醇-3,4,5-三磷酸（PIP3）和磷脂酰肌醇-4,5-二磷酸（PI(4,5)P2）的互作被招募到细胞膜上，随后通过Sec7域激活ARF1和ARF6（替换GDP为GTP）。ARF1主要调控高尔基体的膜运输，ARF6则负责质膜内吞和肌动蛋白细胞骨架重塑。这一功能模块使得CYTH3成为整合磷脂酰肌醇信号和ARF GTP酶功能的核心节点——将脂质信号的"读"（PH域）与膜运输的"写"（Sec7/ARF活性）有机衔接。HPA免疫荧光显示Cytosol; Nucleoplasm (Supported)，其核质定位可能与核内的ARF GTP酶或磷脂酰肌醇信号有关。

PPI网络揭示了CYTH3在支架蛋白介导的信号复合体中的功能。STRING数据显示TAMALIN（876分）和GRASP（876分）是最高置信度的互作伙伴——两者均为突触后密度的支架蛋白，提示CYTH3在神经元突触中的功能。PIK3CB（736分）的互作将CYTH3与PI3K/AKT信号通路直接连接——PI3K催化PIP2到PIP3的转化，而PIP3正是CYTH3 PH域的膜招募信号。BioGRID数据补充了CALCOCO1、OIP5、WDR83和GPS2等互作因子。其中GPS2（G蛋白通路抑制因子2）是一个核内转录辅抑制因子，参与核受体信号调控和HDAC去乙酰化酶复合体的组装——GPS2的核内互作为CYTH3核质定位的功能提供了潜在的桥接点。

从TE调控机制分析，CYTH3的影响可通过多条路径实现。其一，ARF GTP酶（CYTH3的直接底物）调控核膜的内膜系统运输，核内ARF1参与有丝分裂中核膜的重组和核孔复合体组装——核膜完整性是核内组织（包括异染色质锚定和TE沉默）的基础。其二，PIK3CB-CYTH3的互作将PI3K/AKT信号与ARF调控衔接，AKT已知磷酸化多种转录因子和表观遗传调控因子（如EZH2、DNMT1），间接影响TE的转录活性。其三，GPS2-CYTH3的核内互作值得进一步验证——GPS2是转座子沉默因子KAP1/TRIM28复合体的组分，若CYTH3通过GPS2参与该复合体的组装或调控，这将是该蛋白在TE调控中最重要的机制连接。

PubMed strict=7篇文献提示研究新颖性高但基础薄弱。未来研究可围绕：（1）通过荧光显微镜和亚细胞分级确认CYTH3的核内稳态浓度；（2）Co-IP验证CYTH3与GPS2/KAP1复合体的互作；（3）利用ARF-GEF活性抑制剂（如SecinH3）分析CYTH3在TE转录调控中的功能是否需要其GEF催化活性。PPI degree=39和互作网络中支架蛋白（TAMALIN/GRASP）的显著参与提示CYTH3可能主要作为信号复合体中的支架/组织者而非独立的催化实体发挥功能。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TAMALIN | STRING | 876 |
| GRASP | STRING | 876 |
| PLEK | STRING | 827 |
| PIK3CB | STRING | 736 |
| CALCOCO1 | BioGRID | 1 |
| OIP5 | BioGRID | 1 |
| WDR83 | BioGRID | 1 |
| GPS2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43739-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000008256-CYTH3

![](https://images.proteinatlas.org/13979/160_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/160_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000008256-CYTH3

![](https://images.proteinatlas.org/13979/160_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/160_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000008256-CYTH3

![](https://images.proteinatlas.org/13979/160_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/160_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/105_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/13979/107_D7_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 13**

| 40834973 | Heat stress-induced genomic instability in neural stem cells and its association with neuronal developmental deficits. | Brain Res Bull 2025 |
| 39806399 | Longitudinal DNA methylation profiles in saliva of offspring from mothers with gestational diabetes: associations with e | Cardiovasc Diabetol 2025 |
| 38455128 | Identification of immune cell-related prognostic genes characterized by a distinct microenvironment in hepatocellular ca | World J Clin Oncol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CYTH3

