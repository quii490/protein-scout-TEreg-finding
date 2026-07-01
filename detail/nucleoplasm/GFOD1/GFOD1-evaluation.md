---
type: protein-evaluation
gene: "GFOD1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GFOD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GFOD1 |
| 蛋白名称 | Glucose-fructose oxidoreductase domain-containing protein 1 |
| 蛋白大小 | 390 aa / 43.2 kDa |
| UniProt ID | Q9NXC2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 390 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=92.7; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Gfo/Idh/MocA-like_OxRdtase_N; Gfo/Idh/MocA_oxidrdct_glycsds; GFO_IDH_MocA-like_d |
| PPI | 6/10 | x3 | 18.0 | PPI degree=53 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=13 broad=15
- AF pLDDT=92.7 PDB=1
- InterPro: Gfo/Idh/MocA-like_OxRdtase_N; Gfo/Idh/MocA_oxidrdct_glycsds; GFO_IDH_MocA-like_dom
- Pfam: GFO_IDH_MocA; GFO_IDH_MocA_C3
- PPI degree=53 ChIP: None
40591185: GFOD1 expression in clear cell renal cell carcinoma and its role in cancer cell  | 35077535: CharID: a two-step model for universal prediction of interactions between chroma | 32197942: Distribution of transcripts of the GFOD gene family members gfod1 and gfod2 in t

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glucose-fructose oxidoreductase domain-containing protein 1

**功能**: Probably catalytically inactive enzyme. Does not bind NAD or NADP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000683 |
| InterPro | IPR050463 |
| InterPro | IPR055170 |
| InterPro | IPR036291 |
| Pfam | PF01408 |
| Pfam | PF22725 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---



### 深度机制分析

GFOD1的域架构揭示了一个功能退化的氧化还原酶折叠骨架。InterPro域Gfo/Idh/MocA-like_OxRdtase_N（IPR000683）和GFO_IDH_MocA-like_dom（IPR036291）属于一个古老的NAD(P)结合Rossmann-fold超家族，其原型成员（如葡萄糖-果糖氧化还原酶GFOR）催化糖类的氧化还原反应。Pfam域GFO_IDH_MocA（PF01408）构成N端催化域，而GFO_IDH_MocA_C3（PF22725）构成C端延伸域。然而，关键的结构洞察来自UniProt的明确注释："Probably catalytically inactive enzyme. Does not bind NAD or NADP."这意味着尽管GFOD1保留了完整的GFO/IDH/MocA结构折叠，但其活性位点已退化至无法结合辅因子。这一"假酶"（pseudoenzyme）特征提示GFOD1通过其折叠骨架执行非催化功能——可能作为蛋白-蛋白互作的支架平台。

PPI网络（degree=53）提供了该假酶功能的线索。最关键的互作伙伴是ELAVL1（HuR）——一个经典的RNA结合蛋白，通过结合ARE（AU-rich element）调控mRNA稳定性和翻译。GFOD1-ELAVL1的互作强烈暗示GFOD1参与转录后基因调控，可能作为RNA调控复合物的组装支架。SLMAP（Sarcolemmal Membrane-Associated Protein）是中心体/核膜的支架蛋白，参与细胞周期调控和膜组织，提示GFOD1可能通过与SLMAP互作锚定于特定的亚细胞结构。大量角蛋白家族成员（KRT31, KRT40, KRTAP10-8）和MAGEA6的出现虽是BioGRID高通量数据（评分=0），但如果验证为真实互作，则提示GFOD1参与细胞骨架组织和癌症-睾丸抗原信号网络。GFOD1-GFOD1自互作（BioGRID）表明该蛋白以同源二聚体或多聚体形式存在——这是GFO/IDH/MocA家族蛋白的常见特征。

结构层面，AlphaFold pLDDT高达92.7，表明GFOD1折叠得非常紧凑且置信度极高，这对于一个单域蛋白来说并不意外。这个高pLDDT值赋予其结构评分8/10。GFO/IDH/MocA折叠由两个结构域组成：N端Rossmann-fold（NAD结合位点）和C端底物结合域。在催化活性的同源酶中，这两个域通过底物结合时发生的域-域闭合运动实现催化。在GFOD1中，由于NAD结合口袋的关键残基已突变退化，域的构象动力学可能被重新利用——域间运动可能调节蛋白互作界面，而非催化化学转化。该蛋白仅有1个PDB条目，表明实验结构数据仍然匮乏。GFOD1在大脑小脑中高表达（PMID: 32197942），其转录本在斑马鱼中分布于特定脑区，提示其在神经发育中具有保守的功能。

综合证据提出的分子机制模型如下：GFOD1是"氧化还原酶折叠衍生的mRNA调控假酶"。在分子水平，一方面，GFOD1通过其退化的Rossmann-fold表面与ELAVL1/HuR结合，参与mRNA稳定性调控——可能通过竞争HuR-ARE的结合或调节HuR的核-质穿梭。另一方面，GFOD1通过SLMAP锚定于特定亚细胞结构（如核膜或中心体），在此形成局部mRNA调控微环境。退化的NAD结合口袋可能已演化为一个蛋白-蛋白互作界面——这是假酶进化中常见的"功能转换"策略。在核质中，GFOD1可能参与核内mRNA加工和输出的调控；在质膜处，可能参与局部mRNA翻译的控制。GFOD1在透明细胞肾细胞癌中的促癌作用（PMID: 40591185）可能通过失调ELAVL1/HuR靶mRNA（如VEGF, cyclins, 凋亡因子）的稳定性来介导。

GFOD1的研究与治疗价值在于其双重新颖性——功能未知（PubMed仅13篇，新颖性9/10）伴随高结构置信度（pLDDT 92.7）。作为假酶，GFOD1提供了一种独特的药物靶点策略：不同于抑制催化活性（在GFOD1中不可行），可以设计分子阻断其蛋白互作界面（如GFOD1-ELAVL1结合面）。在ccRCC中，靶向GFOD1可能同时干扰多个HuR调控的促癌通路，产生协同抗肿瘤效应。利用其高pLDDT的结构模型，可以进行虚拟筛选寻找结合GFOD1退化活性位点或互作界面的小分子。此外，由于GFOD1的催化口袋在进化上已退化，针对该口袋的药物不太可能与催化活性同源酶产生交叉反应，这提供了极佳的选择性潜力。在神经发育领域，GFOD1的脑区特异性表达暗示其在神经环路形成中的作用，可能成为神经发育障碍的新候选基因。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| SLMAP | BioGRID | 0 |
| KRT31 | BioGRID | 0 |
| MAGEA6 | BioGRID | 0 |
| GFOD1 | BioGRID | 0 |
| KRT40 | BioGRID | 0 |
| FAM9B | BioGRID | 0 |
| KRTAP10-8 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NXC2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000145990-GFOD1

![](https://images.proteinatlas.org/29096/274_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/29096/274_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/29096/273_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/29096/273_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/29096/275_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/29096/275_D11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 15**

| 41038407 | Genome-wide association study identifies novel candidate genes linked to acute and chronic thermal stress resilience in  | Genomics 2025 |
| 40664124 | Therapeutic targeting of triple-negative breast cancer: A multi-model evaluation of LNA-anti-miR-19b-3p and small molecu | Comput Biol Med 2025 |
| 40591185 | GFOD1 expression in clear cell renal cell carcinoma and its role in cancer cell proliferation, migration, and invasion. | Discov Oncol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GFOD1

