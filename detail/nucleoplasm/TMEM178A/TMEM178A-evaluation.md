---
type: protein-evaluation
gene: "TMEM178A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM178A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM178A |
| 蛋白名称 | Transmembrane protein 178A |
| 蛋白大小 | 297 aa / 33.0 kDa |
| UniProt ID | Q8NBL3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 297 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PMP22/EMP/MP20/Claudin; T178A/B |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=2 broad=3
- AF pLDDT=74.4 PDB=0
- InterPro: PMP22/EMP/MP20/Claudin; T178A/B
- Pfam: Claudin_2
- PPI degree=4 ChIP: None
40497153: HIV-1 latency: From acquaintance to confidant. | 36713578: DNA methylation-based patterns for early diagnostic prediction and prognostic ev

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TMEM178A（Transmembrane protein 178A）是一个297 aa的跨膜蛋白，其结构域架构包含PMP22/EMP/MP20/Claudin超家族特征（InterPro IPR004031），以及TMEM178A/B家族特异性保守区（InterPro IPR039625）。Pfam将其归类为Claudin_2家族（PF13903），提示TMEM178A可能具有四次跨膜螺旋拓扑结构，类似于claudin紧密连接蛋白。AlphaFold2预测pLDDT=74.4，无PDB实验结构，其中等可信度的预测主要受限于跨膜区的柔性构象。

TMEM178A的PPI网络极为稀疏（degree=4），但互作伙伴的功能意义深远。与KRAS（GTPase KRas）的BioGRID互作提供了一个关键的信号通路连接——KRAS是MAPK/ERK信号通路的核心开关，其突变驱动多种癌症。TMEM178A与KRAS的膜近端互作可能在核质中影响KRAS信号输出的空间调控。与SPPL3（信号肽肽酶样3）的互作则提示TMEM178A可能经历膜内切割，释放胞内片段入核。与CISD2（线粒体外膜蛋白，调控自噬和铁代谢）的互作连接了TMEM178A与线粒体功能和细胞应激应答。

功能研究揭示TMEM178A作为破骨细胞分化的负调控因子，通过调控TNFSF11诱导的Ca²⁺内流来控制NFATC1的核转位和转录激活。这是一个直接连接跨膜信号与核内转录调控的范例——Ca²⁺信号通过钙调磷酸酶去磷酸化NFATC1，促使其核转位。TMEM178A在核质中的Approved级别定位提示其可能不仅在上游调控Ca²⁺信号，还可能直接参与核内NFATC1的调控。HIV-1潜伏期研究（PMID:33270809, PMID:40497153）中TMEM178A作为宿主因子的出现进一步支持其在核内转录调控中的潜在角色。

TMEM178A具有极高的研究新颖性（PubMed=2，得分10/10），且核定位明确（Nucleoplasm Approved，得分9/10）。其跨膜蛋白拓扑结构与核质定位的组合是反直觉的，提示可能存在非经典的核膜-内膜系统整合机制。TMEM178A作为破骨细胞-免疫交叉点的调控因子，在骨质疏松、类风湿性关节炎等骨免疫疾病中具有潜在的药物靶标价值。

### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 178A

**功能**: Acts as a negative regulator of osteoclast differentiation in basal and inflammatory conditions by regulating TNFSF11-induced Ca (2+) fluxes, thereby controlling the induction of NFATC1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004031 |
| InterPro | IPR039625 |
| Pfam | PF13903 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GSTCD | BioGRID | 0 |
| CISD2 | BioGRID | 0 |
| KRAS | BioGRID | 0 |
| SPPL3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NBL3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000152154-TMEM178A

![](https://images.proteinatlas.org/52128/1687_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52128/1687_B1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000152154-TMEM178A

![](https://images.proteinatlas.org/52128/1687_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52128/1687_B1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000152154-TMEM178A

![](https://images.proteinatlas.org/52128/1687_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52128/1687_B1_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 40497153 | HIV-1 latency: From acquaintance to confidant. | J Virus Erad 2025 |
| 36713578 | DNA methylation-based patterns for early diagnostic prediction and prognostic evaluation in colorectal cancer patients w | Front Oncol 2022 |
| 33270809 | Identification of unrecognized host factors promoting HIV-1 latency. | PLoS Pathog 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM178A

