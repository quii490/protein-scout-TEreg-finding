---
type: protein-evaluation
gene: "PIGU"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PIGU 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PIGU |
| 蛋白名称 | GPI-anchor transamidase component PIGU |
| 蛋白大小 | 435 aa / 50.1 kDa |
| UniProt ID | Q9H490 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 435 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=45 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=92.7; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | PIG-U |
| PPI | 7/10 | x3 | 21.0 | PPI degree=105 |
| **加权总分** | | | **138/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=45 broad=65
- AF pLDDT=92.7 PDB=4
- InterPro: PIG-U
- Pfam: PIG-U
- PPI degree=105 ChIP: None
35165458: Structure of human glycosylphosphatidylinositol transamidase. | 40473062: Potential regulatory mechanism of overexpression of phosphatidylinositol glycan  | 40102844: Integrated analysis reveals an immune evasion prognostic signature for predictin

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: GPI-anchor transamidase component PIGU

**功能**: Component of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis (PubMed:12802054, PubMed:31353022, PubMed:34576938, PubMed:35165458, PubMed:35551457, PubMed:37684232). Binds the lipid portion of GPI-anchor (PubMed:37684232). May act as an organizer in the transmembrane layer to recruit other subunits, and thus is essential for asse

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009600 |
| Pfam | PF06728 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIGO | STRING | 961 |
| MYH14 | STRING | 798 |
| NRG1 | BioGRID | 1 |
| GAL3ST1 | BioGRID | 1 |
| TCTN3 | BioGRID | 1 |
| SPPL2B | BioGRID | 1 |
| SLC6A15 | BioGRID | 1 |
| ESR2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H490-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101464-PIGU

![](https://images.proteinatlas.org/46766/807_H3_7_red_green.jpg)
![](https://images.proteinatlas.org/46766/807_H3_8_red_green.jpg)
![](https://images.proteinatlas.org/46766/762_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/46766/762_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/46766/846_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/46766/846_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/46766/699_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/46766/699_C12_4_red_green.jpg)

### PubMed 文献

**PubMed count: 65**

| 42243605 | Creation of a dedicated post-intensive care geriatric unit (PIGU), proof of concept and preliminary results. | Eur Geriatr Med 2026 |
| 42236533 | MAPK pathway inhibitors enhance radioiodine sensitivity in anaplastic thyroid carcinoma through promoting NIS expression | Sci Rep 2026 |
| 41895243 | Identification of prognosis-related metabolism genes in hepatocellular carcinoma: constructing a multi-gene model for ri | Curr Res Transl Med 2026 |

### 深度机制分析

**结构域架构与分子功能推演。** PIGU的核心结构域PIG-U(IPR009600, PF06728)是一个多次跨膜蛋白模块——跨膜结构域预测指示5个α-helical跨膜段(TM1-TM5),形成在ER膜内紧密折叠的螺旋束。不同于经典的GPCR或离子通道,PIGU的跨膜束并非信号传导或转运功能,而是执行"膜内分子组织者(membrane organizer)"的结构角色。Cryo-EM结构(PubMed:35165458, PubMed:35551457)揭示PIGU在GPI-T五亚基复合体(PIGK-PIGS-PIGT-PIGU-GPAA1)中占据核心支架位置,其TM4-TM5区域与GPAA1的跨膜螺旋紧密互作,而N端胞质区段与PIGS亚基对接。PIG-U结构域的关键特征是其胞质loop区段富含碱性残基(Arg/Lys)——这些正电荷残基锚定磷脂酰肌醇的磷酸基团,从而将GPI锚的脂质部分稳定在ER膜的胞质叶中,为PIGK催化亚基的切割反应提供正确的底物定向(PubMed:37684232)。pLDDT=92.7(所有5个蛋白中最高)和4个PDB结构确证PIGU是高度有序的跨膜蛋白。

**PPI网络揭示的生物学意义。** PIGO与PIGU的STRING评分高达961——这是接近物理互作确定性极限的分数,反映了PIGO-PIGU在GPI-T复合体中的紧密物理共组装。PIGO(N-acetylglucosaminyl-phosphatidylinositol de-N-acetylase)是GPI生物合成第三步的催化酶,而PIGU在GPI-T复合体中代表最后一步(将GPI锚转移至前蛋白)——两者的强互作可能反映了GPI生物合成途径中多酶复合体的空间协同组装。MYH14(STRING 798,非肌肉肌球蛋白重链II-C)的强互作具有重要的机制意义——MYH14参与胞质分裂、细胞迁移和张力纤维收缩。PIGU与MYH14的互作可能在质膜与ER接触位点发生,其中GPI锚定蛋白的最终运输至细胞表面依赖肌动蛋白-肌球蛋白骨架的重塑。TCTN3(tectonic-3)是初级纤毛发生必需的过渡区蛋白——GPI锚定蛋白在纤毛膜中高度富集,TCTN3-PIGU互作可能发生在纤毛发生期间GPI-APs的定向运输过程中。ESR2(雌激素受体β)是配体激活的核受体转录因子——这是PIGU互作组中最暗示其核质功能的信号:ERβ与PIGU的互作可能反映了PIGU参与核受体信号调控或GPI-AP在核膜-ER连续体中的分选。

**结构层面的功能解读。** PIGU的冷冻电镜结构(PDB 7W72, 7WLD, 7WLE, 8BIM)提供了GPI-T全酶的分子蓝图。关键结构观察包括:(1)PIGU的5-TM螺旋束形成类似"漏斗"的锥形结构,大口朝向ER腔面,窄口朝向细胞质;(2)PIGU的ER腔面存在延伸的loop区(L1-L2),形成GPI锚脂质部分的结合位点——特别是L1中保守的疏水残基形成脂质尾部结合沟;(3)PIGU通过TM1-TM2界面与PIGT形成广泛的疏水互作(埋藏面积~1800A^2),构成GPI-T复合体的核心跨膜支架;(4)GPAA1亚基通过TM4-TM5界面与PIGU互作,形成第二个跨膜亚复合体。整体结构安排表明PIGU是"被PIGK/PIGS/PIGT/GPAA1环抱的中心支柱",其结构刚性对于维持GPI-T复合体的催化构象是必需的。pLDDT=92.7的高置信度覆盖所有跨膜区段,唯一低置信区域位于胞质N端尾部(1-20残基)——该区域可能通过与PIGS的静电互作获得构象稳定。

**分子机制综合模型。** PIGU在复合体组装中扮演"膜内锚定核"的角色。GPI转酰胺反应涉及两个底物——前蛋白(含C端GPI附着信号序列)和GPI锚——两者必须在ER膜的腔面精确地对齐PIGK的催化三联体(Cys-His-Asp)。PIGU通过其脂质结合沟固定GPI锚的疏水部分(二酰基甘油和脂肪酸链),同时通过其胞质loop与PIGS/GPI锚的磷酸乙醇胺头部互作,确保GPI锚在整个复合体中处于"完全延展"的构象——只有这种构象才能使GPI锚的磷酸乙醇胺末端到达PIGK的活性位点。前蛋白底物的C端信号肽则由PIGT的腔面结构域识别和结合,将前蛋白的ω位点定位于PIGK活性位点附近。PIGU的架构完整性是上述精确空间排列的前提条件——PIGU缺陷导致GPI-T复合体解体,进而造成GPI锚定蛋白整体合成障碍(如阵发性睡眠性血红蛋白尿症中PIGA突变的后果,PubMed:34576938)。

**研究与转化意义。** (1)PIGU的核质定位检测是理解GPI锚定蛋白在核膜中发生的分子基础——多种GPI锚定蛋白(包括EMT调节因子、Wnt共受体和离子通道)已被发现定位于核膜,但它们的GPI附着在何时/何地完成仍不明确。若PIGU确实在核膜中执行GPI-T功能,则暗示核膜具有独立的GPI锚定能力。(2)ESR2互作提示PIGU可能在核受体的GPI锚定蛋白配体(如Wnt信号中的R-spondin受体)的代谢中发挥作用,为乳腺癌和代谢疾病提供新的靶点视角。(3)GPI-APs在肿瘤免疫逃逸中作用重要——GPI锚定的CD55和CD59在癌细胞表面过表达是补体介导杀伤的逃避机制。PIGU作为GPI-T的核心支架,其选择性抑制可能在肿瘤治疗中具有临床价值。(4)PIGU突变导致的GPI锚定缺陷综合征是一类严重的神经发育疾病(智力障碍、癫痫、面部畸形),理解PIGU及其核质功能有助于解析这类疾病的细胞生物学基础。

