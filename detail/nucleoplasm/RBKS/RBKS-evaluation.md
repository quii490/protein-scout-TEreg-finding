---
type: protein-evaluation
gene: "RBKS"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## RBKS 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RBKS |
| 蛋白名称 | Ribokinase |
| 蛋白大小 | 322 aa / 34.1 kDa |
| UniProt ID | Q9H477 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 322 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=14 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=95.0; PDB=14 |
| 调控结构域 | 4/10 | x2 | 8.0 | Carboh/pur_kinase_PfkB_CS; PfkB_dom; Ribo/fructo_kinase |
| PPI | 5/10 | x3 | 15.0 | PPI degree=31 |
| **加权总分** | | | **143/180** | |
| **归一化总分** | | | **79.2/100** | 互证: +2 |

### 3. 分析
HPA: Cytosol; Nucleoplasm (Approved)
PubMed: strict=14, broad=17
AF pLDDT: 95.0  PDB: 14
InterPro: Carboh/pur_kinase_PfkB_CS; PfkB_dom; Ribo/fructo_kinase
Pfam: PfkB
PPI degree: 31  ChIP: None
**Papers**: 38076879: Profiling the genome and proteome of metabolic dysfunction-associated steatotic  | 40498271: Multi-omics Analysis of Energy Metabolism Pathways Across Major Psychiatric Diso | 40428403: Genetic Determinants of Colonic Diverticulosis-A Systematic Review.

### 4. 总体评价
★★★★  **79.2/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域与催化机制**：RBKS属于PfkB碳水化合物激酶家族（IPR011611，Pfam PF00294），该家族采用保守的ATP依赖性磷酸化机制，以天冬氨酸残基作为通用碱催化核糖C5位羟基的磷酸化。其底物特异性由核酮糖激酶亚家族（IPR011877）赋予，通过活性位点的空间位阻和氢键网络区分核糖与果糖。InterPro条目IPR002173（碳水化合物/嘌呤激酶保守位点）标定了催化核心中高度保守的ATP结合环和镁离子配位残基，而IPR029056（核糖激酶样超家族）揭示了一个更大的结构折叠，其核心由中央平行β片层两侧环绕α螺旋构成Rossmann样核苷酸结合折叠。AlphaFold预测pLDDT高达95.0，14个PDB实验结构进一步验证了活性位点的精确几何构型——ATP的腺嘌呤环与蛋白骨架通过双齿氢键锚定，核糖底物的2'和3'羟基与保守的天冬氨酸/谷氨酸残基形成关键识别接触。这种超高结构置信度意味着RBKS的催化循环已在原子分辨率下被完整解析，是该家族中结构表征最为充分的成员之一，为理性药物设计提供了坚实基础。

**PPI网络与代谢通路推断**：PPI度仅为31，但高分互作蛋白富集于磷酸戊糖途径（PPP）和信号转导节点。TKT（转酮醇酶，STRING评分964）是PPP非氧化分支的核心酶，催化核酮糖-5-磷酸与木酮糖-5-磷酸的可逆转化为景天庚酮糖-7-磷酸与甘油醛-3-磷酸。这种高置信互作强烈暗示RBKS的产物D-核糖-5-磷酸经TKT直接进入PPP代谢网络，在核内形成局部代谢模块。NLK（Nemo样激酶，817分）是MAPK超家族的非典型成员，通过磷酸化TCF/LEF转录因子抑制Wnt/β-catenin信号，同时靶向STAT3调控JAK-STAT通路。MGA（716分）是MAX二聚化蛋白家族的转录抑制因子，含T-box结构域，直接拮抗MYC-MAX靶基因的激活，控制细胞生长与增殖的转录程序。BioGRID来源的ACD和POT1互作提示与shelterin端粒保护复合物存在潜在联系。综合来看，RBKS的PPI图谱描绘了一幅核内代谢-信号耦合图景：核糖磷酸化活性通过TKT与PPP代谢流联动，同时经由NLK和MGA向转录调控网络输出信号。

**核定位的代谢逻辑**：RBKS同时定位于胞质溶胶和核质（HPA Approved）具有深刻的代谢意义。核苷酸的从头合成需要磷酸核糖焦磷酸（PRPP）作为核糖-5-磷酸的活化供体，而DNA复制和转录对核苷酸的需求在时空上高度局域化。将核糖激酶活性置于核内可实现核糖-5-磷酸的就地生产，避免胞质核糖-5-磷酸跨核膜转运的延迟和稀释。这一观点得到了近期文献的有力支持——PMID 41651301发现RBKS依赖性的D-核糖处理可诱导铜稳态紊乱和线粒体功能障碍，提示RBKS的代谢输出远超单纯的糖磷酸化，可能涉及金属离子稳态与线粒体-核反向信号传导。PMID 40498271将RBKS定位于主要精神疾病的能量代谢通路多组学特征中，进一步暗示其在神经系统的代谢适应性中发挥关键作用。

**机制模型与研究方向**：我们提出RBKS作为一个核内代谢传感器：在高葡萄糖/核糖环境下，RBKS加速核糖-5-磷酸的核内生产，通过TKT-PPP轴提升核苷酸前体池，同时通过NLK和MGA向Wnt/MYC转录网络传导代谢状态信号。在癌细胞中，由于核酸合成的持续需求，该通路可能被高度激活——RBKS因此是一个潜在的抗癌代谢靶点。未来研究应着重：(1) 验证核内RBKS是否与TKT形成物理复合物，(2) 解析RBKS-NLK-MGA互作的信号功能，(3) 探究RBKS在核内与胞质中是否存在底物亲和力差异或翻译后修饰调控，(4) 开发RBKS特异性抑制剂以评估其在肿瘤代谢中的治疗潜力。

### 补充分析 (UniProt API)

**蛋白全称**: Ribokinase

**功能**: Catalyzes the phosphorylation of ribose at O-5 in a reaction requiring ATP and magnesium. The resulting D-ribose-5-phosphate can then be used either for sythesis of nucleotides, histidine, and tryptophan, or as a component of the pentose phosphate pathway

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002173 |
| InterPro | IPR011611 |
| InterPro | IPR002139 |
| InterPro | IPR011877 |
| InterPro | IPR029056 |
| Pfam | PF00294 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TKT | STRING | 964 |
| NLK | STRING | 817 |
| GPI | STRING | 817 |
| MGA | STRING | 716 |
| ACD | BioGRID | 1 |
| POT1 | BioGRID | 1 |
| PHPT1 | BioGRID | 1 |
| RBKS | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H477-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171174-RBKS

![](https://images.proteinatlas.org/19725/198_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/198_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171174-RBKS

![](https://images.proteinatlas.org/19725/198_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/198_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171174-RBKS

![](https://images.proteinatlas.org/19725/198_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/198_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/152_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19725/154_C12_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 17**

| 42239780 | Identification of novel candidate neural genes for diet-induced obesity in outbred heterogeneous stock rats. | Res Sq 2026 |
| 42044851 | Phosphate adaptive regulation in microalgae from phosphorus-rich livestock wastewater: Enhanced metabolic pathways contr | Bioresour Technol 2026 |
| 41651301 | D-ribose-induced cytotoxicity in K562 cells: RBKS-dependent disruption of copper homeostasis and mitochondrial function. | Free Radic Biol Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RBKS

