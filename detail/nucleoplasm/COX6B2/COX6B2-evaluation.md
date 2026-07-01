---
type: protein-evaluation
gene: "COX6B2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## COX6B2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | COX6B2 |
| 蛋白名称 | Cytochrome c oxidase subunit 6B2 |
| 蛋白大小 | 88 aa / 10.5 kDa |
| UniProt ID | Q6YFQ2 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 88 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=15 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | COX6B-like; CX6/COA6-like_sf; Cyt_c_oxidase_su6B |
| PPI | 5/10 | x3 | 15.0 | PPI degree=46 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |
### 3. 分析
- HPA: Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed: strict=15, broad=25
- AF pLDDT: 89.1 / PDB: 0
- InterPro: COX6B-like; CX6/COA6-like_sf; Cyt_c_oxidase_su6B
- Pfam: COX6B
- PPI degree=46 / ChIP: None
37061993: Metabolic Reprogramming Driven by IGF2BP3 Promotes Acquired Resistance to EGFR I | 40263598: SDCBP/Syntenin-1 stabilizes BACH1 by disassembling the SCF(FBXO22)-BACH1 complex | 40956396: WGCNA-Based Identification of Hub Genes and Key Pathways Involved in Obesity.
### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cytochrome c oxidase subunit 6B2

**功能**: Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over t

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR048280 |
| InterPro | IPR036549 |
| InterPro | IPR003213 |
| Pfam | PF02297 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FRMD6 | BioGRID | 0 |
| TENC1 | BioGRID | 0 |
| PROP1 | BioGRID | 0 |
| PTEN | BioGRID | 0 |


### 深度机制分析

**结构域架构**：COX6B2（88 aa，10.5 kDa）是本批次中最小蛋白，含Cyt_c_oxidase_su6B结构域（IPR003213，PF02297 COX6B），属于COX6B-like（IPR048280）和CX6/COA6-like_sf（IPR036549）折叠家族。作为线粒体呼吸链复合体IV（细胞色素c氧化酶）的核基因组编码亚基，COX6B2与COX6B1具有旁系同源（paralog）关系。COX6B亚基位于复合体IV的基质侧表面，横跨膜间空间暴露于线粒体基质环境，主要功能是稳定复合体IV二聚体的四级结构和为细胞色素c提供结合平台。

**PPI互作网络解读**：PPI degree=46，显著互作包括：PTEN（BioGRID，经典的PI3K/AKT通路抑制性磷酸酶和肿瘤抑制因子）、FRMD6（FERM域的Hippo通路调控因子）、TENC1（Tensin家族蛋白，整合素-细胞骨架连接蛋白）、PROP1（Prophet of Pit1，垂体特异性同源域转录因子）。PTEN互作是最值得关注的非经典连接——PTEN定位于质膜和内质网-线粒体接触位点，参与线粒体代谢和氧化磷酸化的调控，COX6B2可能通过与PTEN的互作参与线粒体能量代谢的肿瘤特异性重编程。

**结构解读**：AlphaFold pLDDT=89.1（本批次中最高之一），预测质量极佳。COX6B2形成紧凑的球状折叠，由两段反平行β-片层和C端α-螺旋组成。高pLDDT值反映该小蛋白折叠为稳定、刚性的结构域——这也解释了为何COX6B2仅88个氨基酸仍能发挥作为复合体IV稳定因子的作用。保守的半胱氨酸残基（Cys-Xn-Cys基序）可能参与金属离子（Zn^2+）配位以稳定局部构象，或形成分子内二硫键。

**机制模型**：COX6B2的主要功能框架为：（1）线粒体中作为复合体IV的结构性亚基，与13个其他亚基共同组装成~200 kDa的复合体IV单体，进一步二聚化形成超级复合物（respirasome，复合体I+III_2+IV）；（2）COX6B2与COX6B1的组织表达差异——COX6B1广泛表达（housekeeping），而COX6B2在特定组织中表达（如睾丸、某些肿瘤），提示COX6B2可能参与组织特异性的氧化磷酸化调谐；（3）在核质中的定位（Cytosol; Nucleoplasm; Plasma membrane Approved）代表非经典（non-canonical）的非线粒体分布——可能通过MTD（mitochondrial targeting domain）的部分降解或选择性转录/翻译起始产生缺乏线粒体靶向信号的异构体。

**TE调控展望**：COX6B2的TE调控潜力极低。然而，癌细胞的代谢重编程（Warburg效应）与LINE-1激活之间已被报告存在相关性（PMID:37061993发现IGF2BP3驱动的代谢重编程促进EGFR TKI耐药，其中可能涉及逆向转座事件）。COX6B2作为代谢重编程的标志物（在多种肿瘤中过表达），其表达水平可能间接反映TE激活所依赖的代谢环境。在评估肿瘤样本中TE表达与代谢标志物的相关性时，COX6B2可作为对照标记使用。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6YFQ2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000160471-COX6B2

![](https://images.proteinatlas.org/35014/380_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/35014/380_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/35014/1044_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/35014/1044_C9_3_red_green.jpg)
![](https://images.proteinatlas.org/35014/382_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/35014/382_E6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 25**

| 41697440 | Comprehensive analysis of disulfidptosis-related genes identifies clinically actionable prognostic biomarkers in cholang | Discov Oncol 2026 |
| 41591382 | Volatile gas exposure correlates with self-reported liver condition: insights from NHANES 2009-2018 and Mendelian random | Biomarkers 2026 |
| 41419202 | The cytochrome c oxidase subunit COX6B1 is required for redox-sensitive early assembly and late stabilization of complex | J Biol Chem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/COX6B2

