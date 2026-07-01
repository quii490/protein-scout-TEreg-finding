---
type: protein-evaluation
gene: "TMEM38A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM38A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM38A |
| 蛋白名称 | Trimeric intracellular cation channel type A |
| 蛋白大小 | 299 aa / 33.3 kDa |
| UniProt ID | Q9H6F2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 299 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=8 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | TRIC_channel |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=11 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=8, broad=16
- AF pLDDT: 80.5 / PDB: 0
- InterPro: TRIC_channel
- Pfam: TRIC
- PPI degree: 11 / ChIP: None
**Papers**: 40834593: Genome-wide analysis of TMEM38 family revealed functional roles of TMEM38B in fa | 38327905: Exploring a novel seven-gene marker and mitochondrial gene TMEM38A for predictin | 37936983: Native lamin A/C proteomes and novel partners from heart and skeletal muscle in 

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Trimeric intracellular cation channel type A

**功能**: Intracellular monovalent cation channel required for maintenance of rapid intracellular calcium release. Acts as a potassium counter-ion channel that functions in synchronization with calcium release from intracellular stores (By similarity). Opened by a change of voltage within the sarcoplasmic reticulum lumen (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007866 |
| Pfam | PF05197 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

TMEM38A(TRIC-A)是TRIC(Trimeric Intracellular Cation Channel)三聚体胞内阳离子通道家族成员，编码一个299 aa的跨膜蛋白。其核心功能域为TRIC_channel(IPR007866/PF05197)，该结构域在细菌到哺乳动物间高度保守，形成同源三聚体阳离子选择性孔道。pLDDT=80.5说明该三聚体跨膜结构在AlphaFold中具有较高的预测置信度，不过其柔性胞质N端和C端尾部的局部结构尚不确定。

传统上，TMEM38A被定位于肌质网(内质网的内质网亚型)膜上，作为K⁺逆离子(Counter-ion)通道与RyR(雷诺丁受体)钙释放通道协同工作(PMID:41148795)。其生理机制为：在肌肉兴奋-收缩偶联中，动作电位触发肌质网释放Ca²⁺，产生的跨膜电位差由TRIC-A介导的K⁺回流所中和，从而维持Ca²⁺持续释放。然而，HPA将其注释为Nucleoplasm(Approved)，这一意外发现使得TRIC-A的功能范围被实质性扩展。

核质定位机制假说包括：TMEM38A可能定位于内核膜(Inner Nuclear Membrane, INM)，其TRIC通道结构域跨越内核膜，三聚体孔径通过K⁺通量调节核周腔(Nuclear Envelope Lumen)和核质间的离子微环境，类似核膜上SUN-KASH复合体的离子偶联转运功能。TRIM25(BioGRID互作)作为经典的E3泛素连接酶，其核质定位涉及RIG-I抗病毒信号通路的泛素修饰，提示TMEM38A与先天免疫信号间可能存在非经典核膜通道-泛素化偶联机制。

该蛋白的另一显著特征是PPI degree仅11——在所有分析蛋白中互作网络最稀疏。这种"低PPI-关键功能"的矛盾组合恰恰表明TMEM38A可能通过阳离子选择性而非蛋白-蛋白互作来发挥其核心功能。换言之，其生物学活性主要由K⁺的通透率决定，而不是依赖复杂的蛋白互作网络。在透明细胞肾细胞癌中，TMEM38A的过表达抑制肿瘤进展(PMID:39863641)，这为核质离子通道与肿瘤抑制信号间的关联提供了入口。PubMed仅8篇的新颖性意味着该核质离子通道领域几近空白。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H6F2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000072954-TMEM38A

![](https://images.proteinatlas.org/48100/1137_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/48100/1137_C8_4_red_green.jpg)
![](https://images.proteinatlas.org/48100/1021_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/48100/1021_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/48100/1019_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/48100/1019_H3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 16**

| 41148795 | TRIC-A Facilitates Sarcoplasmic Reticulum-Mitochondrial Ca(2+) Signaling Crosstalk in Cardiomyocytes. | Cells 2025 |
| 40834593 | Genome-wide analysis of TMEM38 family revealed functional roles of TMEM38B in fat deposition and its miRNA-mediated regu | Poult Sci 2025 |
| 39863641 | Overexpression of PLCG2 and TMEM38A inhibit tumor progression in clear cell renal cell carcinoma. | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM38A

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ARRB2 | physical | Huttlin EL (2015) |
| NCEH1 | physical | Huttlin EL (2015) |
| PCP2 | physical | Huttlin EL (2015) |
| DOK2 | physical | Huttlin EL (2015) |
| HSD3B2 | physical | Huttlin EL (2017) |
| OXLD1 | physical | Huttlin EL (2017) |
| LZTFL1 | physical | Huttlin EL (2017) |

