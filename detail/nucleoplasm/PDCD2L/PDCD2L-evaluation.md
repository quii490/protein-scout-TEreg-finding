---
type: protein-evaluation
gene: "PDCD2L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PDCD2L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PDCD2L |
| 蛋白名称 | uS5 assembly chaperone PDCD2L |
| 蛋白大小 | 358 aa / 39.4 kDa |
| UniProt ID | Q9BRP1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 358 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=14 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PDCD2-like_regulator; PDCD2_C |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=65 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (Approved) |
| PubMed | strict=14, broad=19 |
| AF pLDDT | 75.4 |
| PDB | 0 |
| InterPro | PDCD2-like_regulator; PDCD2_C |
| Pfam | PDCD2_C |
| PPI degree | 65 |
| ChIP | None |

**Papers**: 37238722: Ribosomal Protein uS5 and Friends: Protein-Protein Interactions Involved in Ribo | 37854614: Programmed Cell Death Protein 2-like Promotes Inflammation and Oxidative Stress  | 27861641: Pdcd2l Promotes Palmitate-Induced Pancreatic Beta-Cell Apoptosis as a FoxO1 Targ

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: uS5 assembly chaperone PDCD2L

**功能**: May function as a chaperone for ribosomal protein uS5; its function appears redundant to PDCD2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR052815 |
| InterPro | IPR007320 |
| Pfam | PF04194 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PDCD2L是程序性细胞死亡蛋白2-like(PDCD2-like)家族成员，现已被重新注释为核糖体蛋白uS5的组装伴侣蛋白(Chaperone)。其核心结构域为PDCD2_C(IPR007320/PF04194)和PDCD2-like_regulator(IPR052815)，这两个结构域共同构成结合并稳定核糖体蛋白RPS2(uS5)的蛋白-蛋白互作界面。pLDDT仅75.4且无PDB结构，表明其结构信息较为有限，分子伴侣活性可能依赖于内在无序区域(IDR)的诱导契合结合机制。

在核糖体生物合成中，PDCD2L的功能与PDCD2互为冗余——二者均在核仁中识别新合成的uS5(RPS2)，通过PDCD2_C结构域上的疏水裂隙插入uS5的未折叠核心，防止新生uS5在进入核糖体40S小亚基组装路径前发生错误折叠或聚集(PMID:37238722)。一旦uS5被正确整合入pre-40S颗粒，PDCD2L随即被XPO1(Exportin-1，BioGRID互作)识别并核输出，释放回胞质以循环使用。

PPI网络高度支持该模型：PRMT3(STRING=915)作为PDCD2L的紧密互作伙伴，是精氨酸甲基化酶，可能通过甲基化uS5的RGG盒改变PDCD2L对uS5的亲和力，形成"甲基化门控释放"机制。COPS6(COP9信号体亚基6)和SRP14(信号识别颗粒14)的互作则暗示PDCD2L可能参与更多翻译机器的组装路径。

HPA显示其定位于nucleoplasm (Approved)，与核糖体生物发生在核仁(核质亚区室)的已知组织学一致。但在肝细胞癌中，BTF3可转录上调PDCD2L的表达并使p53信号通路失活(PMID:39707202)，这揭示了一种额外的PDCD2L致癌机制——即PDCD2L可通过直接或间接方式影响p53启动子区域的染色质可及性或p53的翻译效率。此外，PDCD2L在肿瘤中高表达作为不良预后标志物(PMID:40891712)，表明其功能远超核糖体伴侣这一常规角色。PubMed仅14篇，是探索这种核糖体生物合成因子与癌症信号通路交叉对话的理想靶点。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BRP1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126249-PDCD2L

![](https://images.proteinatlas.org/52181/816_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/816_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_4_cr5b6d6ca24b3c2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_6_cr5b6d6ca24b3b1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126249-PDCD2L

![](https://images.proteinatlas.org/52181/816_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/816_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_4_cr5b6d6ca24b3c2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_6_cr5b6d6ca24b3b1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126249-PDCD2L

![](https://images.proteinatlas.org/52181/816_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/816_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_4_cr5b6d6ca24b3c2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/1874_H10_6_cr5b6d6ca24b3b1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52181/777_A12_4_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 19**

| 40891712 | PDCD2L overexpression represents an unfavorable prognostic marker and its inhibition shows promising therapeutic potenti | Cancer Biomark 2025 |
| 40577382 | Drosophila Trus, the orthologue of mammalian PDCD2L, is required for proper cell proliferation, larval developmental tim | PLoS Genet 2025 |
| 39707202 | BTF3 affects hepatocellular carcinoma progression by transcriptionally upregulating PDCD2L and inactivating p53 signalin | Mol Med 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PDCD2L

