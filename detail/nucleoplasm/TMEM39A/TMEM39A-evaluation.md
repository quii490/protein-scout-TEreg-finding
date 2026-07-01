---
type: protein-evaluation
gene: "TMEM39A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM39A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM39A |
| 蛋白名称 | Transmembrane protein 39A |
| 蛋白大小 | 488 aa / 55.7 kDa |
| UniProt ID | Q9NV64 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 488 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=21 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Uncharacterised_TMEM39 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=48 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=21 broad=25
- AF pLDDT=73.5 PDB=0
- InterPro: Uncharacterised_TMEM39
- Pfam: Tmp39
- PPI degree=48 ChIP: None
36921576: ARMH3-mediated recruitment of PI4KB directs Golgi-to-endosome trafficking and ac | 28744351: TMEM39A and Human Diseases: A Brief Review. | 33902726: Sex-specific DNA methylation differences in Alzheimer's disease pathology.

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


**蛋白全称**: Transmembrane protein 39A

**功能**: Regulates autophagy by controlling the spatial distribution and levels of the intracellular phosphatidylinositol 4-phosphate (PtdIns(4)P) pools (PubMed:31806350). Modulates (PtdIns(4)P) levels by regulating the ER-to-Golgi trafficking of the phosphatidylinositide phosphatase SACM1L (PubMed:31806350)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019397 |
| Pfam | PF10271 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SYNE4 | BioGRID | 1 |
| MPPE1 | BioGRID | 1 |
| CDH5 | BioGRID | 1 |
| ZDHHC12 | BioGRID | 1 |
| ADAM33 | BioGRID | 1 |
| TNFSF13B | BioGRID | 0 |
| IL9R | BioGRID | 0 |
| BTNL8 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM39A（488 aa，55.7 kDa）是内质网-高尔基体脂质转运调控蛋白，含TMEM39特征结构域（IPR019397, Pfam PF10271/Tmp39）。AlphaFold pLDDT=73.5——虽PDB为0，但预测质量良好（有序残基>70%占比估算在60-70%）。TMEM39结构域预测为多跨膜螺旋束（transmembrane helical bundle），含7-9个跨膜α-螺旋（TM1-TM7/9），其两侧有较短的腔内/胞质亲水环——拓扑学为III型跨膜蛋白（N端朝向胞质, C端朝向ER腔内）。跨膜螺旋由典型的疏水（Leu/Ile/Val/Ala/Phe, 平均疏水性GES scale>1.6 kcal/mol）组成，近膜侧的碱性残基（Lys/Arg, "positive-inside rule"）锚定于内质网膜的胞质叶。多跨膜结构赋予TMEM39A在脂双层中的稳态锚定和脂质转运/传感功能——跨膜螺旋束内含保守的极性和芳香族残基（Ser, Thr, Tyr, Trp）形成脂质结合腔（lipid binding cavity），可结合磷脂酰肌醇-4-磷酸（PtdIns(4)P, PI4P）的肌醇环和甘油骨架。跨膜区段的膜拓扑和螺旋间盐桥/氢键网络维持TMEM39A在ER膜中的折叠密度和ER exit site（ERES）的稳定驻留。

**PPI互作网络解读**：PPI网络以膜蛋白和细胞连接蛋白为主，反映TMEM39A在内膜系统和细胞表面蛋白运输中的功能。SYNE4（KASH家族nesprin-4, 核外膜蛋白, 连接细胞骨架actin/plectin至核膜）和ZDHHC12（DHHC12棕榈酰转移酶, 催化底物Cys的S-棕榈酰化, 赋予膜锚定和脂筏定位）为膜蛋白伙伴，提示TMEM39A参与核膜-ER交界和蛋白脂修饰网络。CDH5（VE-cadherin, 内皮细胞黏附连接钙黏蛋白）和ADAM33（ADAM家族去整合素金属蛋白酶33, 哮喘易感基因产物）为细胞表面/胞外基质蛋白，TMEM39A可能调控其在内质网→高尔基体→细胞膜的早期分泌运输（COPII coat machinery）中的转运效率。TNFSF13B（BAFF/BLyS, B细胞激活因子）和IL9R（白介素9受体）为经典分泌通路蛋白。TMEM39A的BioGRID互作图谱反映其作为新膜蛋白的互作特征——倾向于广泛但浅层的膜蛋白网络（膜蛋白BioGRID互作常规技术偏倚, AP-MS/MS富集膜蛋白的局限性），缺乏胞质可溶性蛋白的深层互作覆盖。

**结构解读**：TMEM39A通过跨膜结构整合PI4P脂质代谢和囊泡出芽。跨膜螺旋束围成的含极性残基的中央腔形成PI4P脂质结合位点——PI4P的肌醇环上的4位磷酸与TMEM39A的保守Arg和Lys残基形成盐桥/氢键，甘油脂二酰甘油（DAG）骨架深入跨膜螺旋的疏水凹槽。PI4P为内质网-高尔基体界面膜微区（ER-Golgi intermediate compartment, ERGIC）和高尔基体顺面cisterna的主要磷酸肌醇——PI4P浓度沿ER→Golgi→PM轴递增，由PI4K（PI4KIIα/IIβ/IIIα/IIIβ, 高尔基体/PM）合成和SACM1L（ER PtdIns(4)P磷酸酶）去除的动态平衡维持。TMEM39A的功能核心为调控SACM1L的ER-高尔基体运输——TMEM39A结合PI4P后，跨膜构象转变为"open"状态，促进SACM1L从ER膜经COPII囊泡出口至高尔基体（PMID:31806350）。当高尔基体SACM1L浓度增加→高尔基体PI4P被降解→高尔基体PI4P浓度下降→高尔基体-内体运输和自噬体形成受影响（PI4P为GGA/AP-1网格蛋白衔接蛋白和ATG9/ATG16L1自噬蛋白的膜招募锚点）。

**机制模型**：（1）自噬调控——TMEM39A是自噬的负调控因子。高TMEM39A水平→促进SACM1L高尔基体靶向→高尔基体PI4P下降→ATG9（跨膜自噬蛋白，PI4P结合蛋白, Golgi/endosome→autophagosome运输）脱靶→LC3脂化（LC3-I→LC3-II, ATG3/ATG7/ATG12-ATG5-ATG16L1催化）位点减少→自噬体形成受抑（PMID:31806350）。低TMEM39A或TMEM39A突变（失PI4P结合功能）→SACM1L滞留ER→高尔基体PI4P维持→ATG9高尔基体保留→自噬正常/增强。（2）高尔基体-内体货物运输——TMEM39A经COPII囊泡（SEC23/SEC24/SEC13/SEC31外壳蛋白, 内质网ERES出芽）运输自身和SACM1L至ERGIC和高尔基体。TMEM39A的跨膜区含保守的DXE基序（Asp-X-Glu, COPII SEC24识别信号），突变DXE导致TMEM39A和SACM1L ER滞留→高尔基体PI4P持续高水平→高尔基体顺面膜蛋白回收to ER pathway（COPI coat, retrograde transport）异常→高尔基体形态异常和管状化。（3）细胞外基质（ECM）蛋白的大量分泌——TMEM39A与TMEM131协同促进大型COPII囊泡（直径>100 nm, 常规COPII ~60-80 nm）的形成以容纳超大ECM蛋白（collagen I/III/IV, fibronectin, laminin）（PMID:39521045）。TMEM39A的跨膜结构域作为COPII囊泡的"膜支架"增强膜曲度感应和囊泡扩张——胶原蛋白为大体积三螺旋结构（直径~1.5 nm, 长度>300 nm），需large COPII以横跨囊泡，TMEM39A功能缺失导致ECM蛋白分泌障碍。

**TE调控展望**：TMEM39A与TE调控的关联在于自噬介导的TE沉默和膜脂环境对TE复制的影响。自噬是细胞防御TE转座的核心机制——LINE-1逆转录转座中间体（ORF1p核糖核蛋白颗粒RNP+LINE-1 mRNA）和全长的LTR逆转录病毒样颗粒（VLP, 如HERV-K颗粒）均被p62/SQSTM1自噬受体识别后经自噬体包裹→与溶酶体融合→酸水解酶降解（virophagy/xenophagy, virophagy for retrotransposons）。TMEM39A对自噬的负调控意味着高TMEM39A表达→自噬降低→TE RNP/VLP清除减少→TE逆转录转座活性间接提高。核质定位（HPA Approved Nucleoplasm）提示TMEM39A可能经核膜内陷（nuclear invagination/NV, 核膜内陷形成的通道与ER膜连续）进入核质——核泳（nucleoplasmic reticulum）结构含ER膜成分和核孔复合体，TMEM39A可能影响核膜内陷的膜脂组成和核内PI4P梯度。核内PI4P参与核膜脂质信号和核actin聚合调控，间接影响染色质组织和TE区域（LINE-1, Alu, SVA）的核定位和转录可及性。虽然TMEM39A是典型的膜蛋白，其核质池的存在和自噬调控功能提供了TE宿主防御机制的膜生物学维度，值得在TMEM39A KO细胞中通过LINE-1 EGFP reporter和自噬通量（LC3-GFP/RFP tandem reporter, 自噬体-溶酶体融合指数）结合实验进行验证。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NV64-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000176142-TMEM39A

![](https://images.proteinatlas.org/39140/461_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/39140/461_F4_5_red_green.jpg)
![](https://images.proteinatlas.org/39140/462_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/39140/462_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/39140/464_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/39140/464_F4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 25**

| 40204783 | Genetic susceptibility to recurrent vulvovaginal candidiasis in an African population from Nairobi, Kenya. | Sci Rep 2025 |
| 39521045 | TMEM39A and TMEM131 facilitate bulk transport of ECM proteins through large COPII vesicle formation. | J Genet Genomics 2025 |
| 37810370 | miR-624 accelerates the growth of liver cancer cells by inhibiting EMC3. | Noncoding RNA Res 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM39A

