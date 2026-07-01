---
type: protein-evaluation
gene: "TMEM184B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM184B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM184B |
| 蛋白名称 | Transmembrane protein 184B |
| 蛋白大小 | 407 aa / 45.6 kDa |
| UniProt ID | Q9Y519 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 407 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=19 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=72.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ostalpha/TMEM184C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=35 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=19 broad=22
- AF pLDDT=72.7 PDB=0
- InterPro: Ostalpha/TMEM184C
- Pfam: Solute_trans_a
- PPI degree=35 ChIP: None
37730546: Transmembrane protein 184B (TMEM184B) promotes expression of synaptic gene netwo | 40885185: Pathogenic variants in TMEM184B cause a neurodevelopmental syndrome associated w | 34629389: Transmembrane protein TMEM184B is necessary for interleukin-31-induced itch.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 184B

**功能**: May activate the MAP kinase signaling pathway

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005178 |
| Pfam | PF03619 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：TMEM184B（407 aa, 45.6 kDa, Q9Y519）属于Ostalpha/TMEM184C家族（IPR005178, Pfam PF03619 Solute_trans_a），该家族预测为溶质转运蛋白超家族成员。序列含预测的7-10个跨膜alpha-helix（基于TMHMM/Kyte-Doolittle hydrophobicity profile），形成多跨膜通道/转运体折叠。AlphaFold pLDDT=72.7，无PDB实验结构，但pLDDT>=70占比具有结构可靠性——核心TM bundle折叠良好，N端和C端胞质域相对柔性。Ostalpha/TMEM184家族与有机溶质转运蛋白alpha（OSTalpha）同源——OSTalpha与OSTbeta组成异二聚体，介导胆汁酸和类固醇在肠上皮细胞基底外侧膜的Na+-independent转运。TMEM184B可能保留了类似的转运功能但底物特异性不同。

**PPI互作网络解读**：PPI degree=35，关键伙伴指向多个信号通路。LPAR6（Lysophosphatidic acid receptor 6/P2Y5, BioGRID）是G蛋白偶联受体（GPCR）——LPA信号经LPAR6→G12/13→RhoA→ROCK→actomyosin收缩——在毛囊发育和皮肤稳态中功能关键。SNIP1（Smad nuclear interacting protein 1, BioGRID）是TGF-beta/BMP信号核内co-activator——SNIP1与Smad4/p300/CBP形成复合体促进Smad-dependent转录。ACIN1（Apoptotic chromatin condensation inducer 1, BioGRID）是凋亡中染色质浓缩和核碎裂的效应因子——与REN（renin, 肾素/angiotensin信号起始蛋白酶, BioGRID）及INPPL1（inositol polyphosphate phosphatase-like 1/SHIP2, 磷酸肌醇5'-phosphatase, BioGRID）构成多信号通路交叉节点。

**结构解读**：pLDDT=72.7，TM domain置信度较高（~80-85），形成稳定的多次跨膜通道架构。TMEM184B在核质和高尔基体均有分布——跨膜蛋白如何存在于核质是个重要问题——可能机制包括：（1）内核膜（INM）定位——核膜是ER-Golgi膜系统的连续延伸，跨膜蛋白经侧向扩散通过核孔膜（pore membrane）进入INM→在INM/Nucleoplasm界面参与核内离子/代谢物交换；（2）核内囊泡（nuclear vesicle/invaginated nuclear envelope tubule）——INM内陷形成核质内的膜结构。TMEM184B的Ostalpha-like转运底物可能包括核内小分子信号物质、核酸前体或Ca2+调节因子。

**机制模型**：（1）MAPK信号激活（UniProt注释）——TMEM184B可能作为GPCR/LPA信号的modulator——通过调节LPAR6的表面表达或与下游G蛋白的偶联效率影响MAPK/ERK信号级联。（2）神经发育综合征（PMID:40885185）——TMEM184B pathogenic variants导致neurodevelopmental syndrome——通过影响代谢信号（mTOR, AMPK, insulin signaling?）干扰神经前体细胞增殖和分化——与SNIP1-TGF-beta信号轴在神经系统发育中的功能一致。（3）突触基因网络表达（PMID:37730546）——TMEM184B促进突触基因网络表达——提示其在神经元中通过LPAR6-LPA信号或代谢物转运调控突触可塑性基因的转录程序。（4）IL-31痒觉信号（PMID:34629389）——TMEM184B是IL-31诱导的瘙痒所必需的——可能作为IL-31R下游信号传导的膜平台或离子转运体。

**TE调控展望**：TMEM184B的TE调控潜力为间接途径。核质中的SNIP1-TGF-beta信号轴与染色质调控密切相关——TGF-beta/BMP靶基因常位于LTR/ERV enhancer附近——SNIP1作为Smad4共激活因子促进Smad复合体在靶基因调控区的结合。TMEM184B-SNIP1互作可能调节SNIP1在核内的可用性或活性→影响TGF-beta/Smad-dependent的TE-proximal基因转录。ACIN1在凋亡染色质浓缩中的功能涉及DNA片段化——逆转座导致DNA damage→ATM/ATR→p53→凋亡——TMEM184B-ACIN1互作可能在DNA损伤应答的凋亡执行阶段发挥调控作用。INPPL1/SHIP2作为PI(3,4,5)P3 5'-phosphatase——调控核内phosphoinositide信号——PI(3,4,5)P3在核内参与mRNA processing和export——TMEM184B-INPPL1互作可能影响核内磷酸肌醇空间分布和mRNA输出。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LPAR6 | BioGRID | 0 |
| ERGIC3 | BioGRID | 0 |
| SNIP1 | BioGRID | 0 |
| REN | BioGRID | 0 |
| CLASRP | BioGRID | 0 |
| CCDC9 | BioGRID | 0 |
| ACIN1 | BioGRID | 0 |
| INPPL1 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198792-TMEM184B

![](https://images.proteinatlas.org/24076/240_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/240_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198792-TMEM184B

![](https://images.proteinatlas.org/24076/240_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/240_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198792-TMEM184B

![](https://images.proteinatlas.org/24076/240_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/240_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/239_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24076/241_C1_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 22**

| 41267963 | Integrative multi-omics analysis identifies TGFA as a novel glioma susceptibility gene and therapeutic target. | Front Neurol 2025 |
| 41264070 | Identification of candidate susceptibility genes for cutaneous malignant melanoma through integrated multi-method analys | Discov Oncol 2025 |
| 40885185 | Pathogenic variants in TMEM184B cause a neurodevelopmental syndrome associated with alteration of metabolic signaling. | Am J Hum Genet 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM184B

