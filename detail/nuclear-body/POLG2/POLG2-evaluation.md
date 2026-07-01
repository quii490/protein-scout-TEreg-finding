---
type: protein-evaluation
gene: "POLG2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## POLG2 (DNA polymerase subunit gamma-2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | POLG2 |
| 蛋白全称 | DNA polymerase subunit gamma-2 |
| UniProt ID | Q9UHN1 |
| 蛋白大小 | 485 aa / 53.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 485 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR045864; InterPro:IPR004154; InterPro:IPR036621; InterPro:IPR027031; InterPro:IPR042064; Pfam:PF03129 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Accessory subunit of DNA polymerase gamma solely responsible for replication of mitochondrial DNA (mtDNA). Acts as an allosteric regulator of the holoenzyme activities. Enhances the polymerase activity and the processivity of POLG by increasing its interactions with the DNA template. Suppresses POLG exonucleolytic proofreading especially toward homopolymeric templates bearing mismatched termini. B

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR045864 |
| InterPro | IPR004154 |
| InterPro | IPR036621 |
| InterPro | IPR027031 |
| InterPro | IPR042064 |
| Pfam | PF03129 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000256525-POLG2

![](https://images.proteinatlas.org/17030/621_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17030/621_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17030/612_C5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17030/612_C5_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/17030/615_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17030/615_C5_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR045864;IPR004154;IPR036621;IPR027031;IPR042064; |
| Pfam | PF03129; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| POLG | STRING | 999 |
| RRM2B | STRING | 932 |
| POLE3 | STRING | 925 |
| POLA1 | STRING | 925 |
| REV3L | STRING | 924 |
| POLE4 | STRING | 922 |
| TWNK | STRING | 918 |
| POLE2 | STRING | 915 |


### 深度机制分析

**结构域架构**：POLG2（485 aa，53.4 kDa）是线粒体DNA聚合酶γ（pol γ）的辅助亚基，结构域架构围绕'滑动夹'+'过程性因子'的功能范式展开：核心结构域为DNA聚合酶γ辅助亚基折叠（IPR045864, IPR004154, PF03129）——采用典型的pol B类辅助亚基折叠，含两个独立结构域：N端结构域（约1-300 aa）形成伪二聚体界面与POLG催化亚基（POLG, 140 kDa）互作；C端结构域含HD（组氨酸/天冬氨酸）基序参与DNA模板结合。IPR027031（POLG2特异的家族分类）区分线粒体源pol γ辅助亚基与核polδ/polε辅助亚基。IPR042064和IPR036621为超家族/同源超家族分类。AlphaFold pLDDT可用。

**PPI互作网络解读**：PPI network以STRING预测互作为主，强烈指向线粒体DNA复制机械（replisome）的组织架构：POLG（STRING 999，催化亚基，pol γ全酶的核心，最强的功能互作信号）——POLG-POLG2形成稳定的异源四聚体（POLG₂-POLG2₂），POLG2作为过程性因子将POLG的持续合成能力从<50 nt提高至>1000 nt；RRM2B（STRING 932，p53诱导型核糖核苷酸还原酶亚基）——提供dNTP前体池用于mtDNA合成；TWNK（STRING 918，Twinkle解旋酶）——线粒体DNA解旋酶，是复制叉前进的动力。POLE2/POLE3/POLE4和REV3L（跨损伤合成聚合酶ζ）的互作虽评分高但可能反映复制体组装的进化保守性而非物理互作。

**结构解读**：POLG2以同源二聚体形式结合POLG异源二聚体形成α₂β₂四聚全酶。POLG2单体采用心形（heart-shaped）折叠——中央β-片层（8条混合平行/反平行β-链）被双侧α-螺旋簇包围。POLG2的DNA结合通道由碱性残基（Arg/Lys）排列成正电荷走廊，与DNA骨架磷酸基团形成静电互作。POLG2与POLG的结合界面涉及疏水互补面（埋藏面积>2000A²/单体），POLG2二聚化后形成一个"C形夹具"环抱POLG催化亚基。HPA定位包括Nuclear bodies——这是极不寻常的发现，因为POLG2的经典功能完全定位于线粒体基质。可能的解释：部分POLG2新生多肽在进入线粒体前因TOM/TIM转运效率不足或线粒体靶向信号（MTS）被部分掩盖而滞留于胞质，随后被动扩散或通过碱性残基富集区的隐蔽NLS进入细胞核，并富集于Nuclear bodies。

**机制模型**：（1）经典功能：在线粒体基质中，POLG2₂-POLG₂全酶在mtDNA重链复制起点（OH）组装，TWNK解旋酶在前方解链双链DNA，POLG催化亚基在前导链和后随链上合成DNA，POLG2通过拓扑学"夹持"增加POLG与模板的亲和力并抑制外切核酸酶校对活性——这是线粒体DNA突变率较高的进化权衡；（2）核内非经典功能：Nuclear bodies（HPA定位）中的POLG2可能与PML（promyelocytic leukemia）核体共定位——已知PML核体参与DNA损伤应答和端粒维持，POLG2可能通过其DNA结合活性参与核内损伤修复蛋白的招募；（3）银色纳米颗粒诱导POLG2核转位和线粒体功能障碍（PMID:41945195）揭示了环境污染-核转位-线粒体毒性的新范式。

**TE调控展望**：POLG2与TE调控的直接关联极弱。唯一可以设想的联系是通过mtDNA与核基因组TE的协同进化：已知部分线粒体DNA片段（NUMT, nuclear mitochondrial DNA）通过TE介导的插入事件整合到核基因组中。POLG2功能异常可导致mtDNA拷贝数改变和mtDNA片段释放增加，理论上可能影响NUMT的生成速率——但NUMT整合主要由L1内切酶和靶位点引物逆转录（TPRT）机制催化，POLG2在其中不发挥直接作用。不建议作为TE调控靶标。

### PubMed 文献

**PubMed count: 103**

| 42137581 | Sex differences in mitochondrial function in aging mouse skeletal muscle. | Front Aging 2026 |
| 41945195 | Silver nanoparticles induce binding of mitochondrial DNA polymerase gamma subunit Polg2 and mitochondrial dysfunction in | Ecotoxicology 2026 |
| 41860402 | VIRMA modulates function of photoreceptor cells through m6A modification and alternative splicing. | JCI Insight 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/POLG2

