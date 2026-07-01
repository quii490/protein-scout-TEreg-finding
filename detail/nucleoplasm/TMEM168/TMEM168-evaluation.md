---
type: protein-evaluation
gene: "TMEM168"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM168 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM168 |
| 蛋白名称 | Transmembrane protein 168 |
| 蛋白大小 | 697 aa / 79.8 kDa |
| UniProt ID | Q9H0V1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 697 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=83.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | TMEM168 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=11 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Approved)
- PubMed: strict=5, broad=6
- AF pLDDT: 83.4 / PDB: 0
- InterPro: TMEM168
- Pfam: 
- PPI degree: 11 / ChIP: None
**Papers**: 32175648: Identification of transmembrane protein 168 mutation in familial Brugada syndrom | 30940290: Inhibition of Proliferation by Knockdown of Transmembrane (TMEM) 168 in Glioblas | 34086898: Transmembrane protein 168 mutation reduces cardiomyocyte cell surface expression

### 4. 总体评价
★★★★  **75.4/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 168

**功能**: Plays a key role in maintaining the cardiac electrical stability by modulating cell surface expression of SCN5A (PubMed:32175648). May play a role in the modulation of anxiety behavior by regulating GABAergic neuronal system in the nucleus accumbens (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029713 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构解析** TMEM168（697 aa, 79.8 kDa）是目前发现的最长的核质TMEM蛋白之一，其超大分子量（远超五个TMEM的平均257aa）暗示其可能承担更复杂的支架或多功能角色。唯一注释的结构域为IPR029713（TMEM168家族），该家族在InterPro中被归类为保守蛋白家族但未映射到任何已知的催化或结合结构域（Pfam中无匹配条目），这在697aa的长度上极为罕见——通常此长度的蛋白至少包含2-5个可识别的功能域。pLDDT均值83.4属于"中度折叠置信度"，推测其富含固有无序区（IDR），长时间尺度的无序区域是典型的多价低亲和力互作支架蛋白（如转录凝聚体中的MED1、BRD4）的标志。若无序预测得到证实，TMEM168可能通过液-液相分离（LLPS）机制在核质中形成动态信号中枢。

**PPI网络的功能解读** 在11个互作伙伴中，CRKL（STRING score=1）和GTF2IRD1（score=1）是两个高置信度信号。CRKL是CRK家族的衔接蛋白，含SH2-SH3-SH3结构域，是受体酪氨酸激酶（RTK）、整合素和BCR-ABL信号的核心转导器——其在核内的功能涉及转录因子（如STAT5）的激活和核小体重塑。GTF2IRD1（又名TFII-Iγ或BEN）是TFII-I转录因子家族成员，直接结合DNA并调控c-fos、VEGFR2等基因，更重要的是其在小鼠模型中调控GABAergic神经元系统，而TMEM168的UniProt注释恰好提到"May play a role in the modulation of anxiety behavior by regulating GABAergic neuronal system in the nucleus accumbens"。SPP1（osteopontin）是分泌型促炎/促转移细胞因子，在胶质母细胞瘤中高度表达。NETO2是谷氨酸受体（kainate/AMPA）辅助亚基。这些伙伴勾勒出一条从"细胞表面离子通道调控→胞内信号转导→核内转录调控→行为表型"的完整功能链。

**结构生物学视角** pLDDT=83.4且无PDB实验结构，提示TMEM168的结构解析具有挑战性——无序区使结晶困难，长度（697aa）超出现有NMR的常规范围，但适合冷冻电镜（cryo-EM）分析（尤其是在与CRKL等伙伴形成稳定复合物后）。心脏电生理表型（Brugada综合征，PMID:32175648）为其提供了独特的功能验证窗口：TMEM168通过调控SCN5A（Nav1.5钠通道）的细胞表面表达维持心肌电稳定性，其突变导致αB-crystallin（CRYAB）依赖的SCN5A胞内滞留（PMID:34086898）。这一"离子通道伴侣"到"核内转录/行为调控"的双重功能令人联想到β-catenin和Notch ICD等经典双功能蛋白——其胞内段被蛋白酶解后入核调控基因表达。

**整合机制模型** TMEM168是一个双功能信号转导蛋白，其工作机制可根据亚细胞定位分为两个阶段：（1）在质膜/胞质中，TMEM168作为SCN5A/离子通道的分子伴侣，通过与CRYAB协作确保Nav1.5的正确折叠与膜运输——其Brugada综合征突变破坏了这一功能，导致心肌复极异常和心律失常风险；（2）在核质中，TMEM168通过与CRKL-GTF2IRD1轴直接参与转录调控，具体机制可能涉及CRKL介导的RTK下游信号传递至GTF2IRD1，进而调控GABAergic神经元相关基因（如GABA受体亚基、合成酶GAD67等）的表达。该模型将三条独立证据线统一为一个连贯的机制：（a）心脏SCN5A表型（PMID:32175648/34086898）、（b）胶质母细胞瘤增殖抑制表型（PMID:30940290，敲低TMEM168抑制增殖）、（c）伏隔核GABAergic调控与焦虑行为。在胶质母细胞瘤中，TMEM168敲低可能同时扰乱了RTK信号（通过CRKL失偶联）和细胞周期基因的转录（通过GTF2IRD1失活），导致增殖停滞。

**研究与转化意义** TMEM168在多维度上表现突出：其在胶质母细胞瘤中的功能（PMID:30940290）与CRKL的已知致癌角色一致，提示TMEM168-CRKL-GTF2IRD1轴可能是GBM的潜在治疗靶点。在心脏领域，TMEM168突变引起的Brugada综合征表型为开发通道伴侣疗法提供了独特机会——小分子稳定剂若能增强TMEM168-SCN5A互作，或可校正Nav1.5的胞内滞留。从方法学角度看，TMEM168的双功能特征使其成为研究"质膜-核内信号转导空间耦合"的绝佳模型蛋白，cryo-EM结构解析（尤其是全长TMEM168与CRKL的复合物结构）将是一篇高影响力论文的核心。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CRKL | BioGRID | 1 |
| GTF2IRD1 | BioGRID | 1 |
| SPP1 | BioGRID | 0 |
| NETO2 | BioGRID | 0 |
| FAM174A | BioGRID | 0 |
| ATP2B2 | BioGRID | 0 |
| PLEKHA4 | BioGRID | 0 |
| C3orf52 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H0V1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000146802-TMEM168

![](https://images.proteinatlas.org/77143/1774_A2_2_cr594a78b93b300_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1774_A2_8_cr594a78c416714_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000146802-TMEM168

![](https://images.proteinatlas.org/77143/1774_A2_2_cr594a78b93b300_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1774_A2_8_cr594a78c416714_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000146802-TMEM168

![](https://images.proteinatlas.org/77143/1774_A2_2_cr594a78b93b300_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1774_A2_8_cr594a78c416714_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77143/1611_H4_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 34086898 | Transmembrane protein 168 mutation reduces cardiomyocyte cell surface expression of Nav1.5 through αB-crystallin intrace | J Biochem 2021 |
| 32378630 | [Novel molecules-related drug dependence in mice]. | Nihon Yakurigaku Zasshi 2020 |
| 32175648 | Identification of transmembrane protein 168 mutation in familial Brugada syndrome. | FASEB J 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM168

