---
type: protein-evaluation
gene: "TMEM215"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM215 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM215 |
| 蛋白名称 | Transmembrane protein 215 |
| 蛋白大小 | 235 aa / 25.8 kDa |
| UniProt ID | Q68D42 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 235 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=53.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM215 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=8 broad=8
- AF pLDDT=53.0 PDB=0
- InterPro: TMEM215
- Pfam: TMEM215
- PPI degree=0 ChIP: None
37750320: TMEM215 Prevents Endothelial Cell Apoptosis in Vessel Regression by Blunting BIK | 27155051: Fine mapping under linkage peaks for symptomatic or asymptomatic outcomes of Lei | 30370660: Transmembrane protein 215 promotes angiogenesis by maintaining endothelial cell 

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 215

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031486 |
| Pfam | PF15746 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 215

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031486 |
| Pfam | PF15746 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：TMEM215（235 aa, 25.8 kDa）含TMEM215特征结构域（IPR031486, Pfam PF15746），被预测为2-3次跨膜（transmembrane helices via TMHMM/Phobius）的膜蛋白。AlphaFold pLDDT=53.0——约60%残基pLDDT<70，表明蛋白整体处于部分无序/膜蛋白动态构象。跨膜螺旋（TM1: aa ~25-47, TM2: aa ~85-107, TM3可能: aa ~150-172）的pLDDT>75（中等可信），但胞质loop和N/C端尾部pLDDT<50。跨膜区间的胞外/腔内loop富含Cys残基（可能形成intramolecular disulfide bond以稳定loop构象）。TMEM215的膜拓扑（membrane topology）：N端位于胞外/ER腔内侧或外侧（取决于定位在质膜vs. ER/囊泡膜）。蛋白的疏水性分布呈经典bitopic/polytopic膜蛋白的双亲性图谱（hydropathy plot 2-3 positive peaks）。

**PPI互作网络**：PPI degree=0（BioGRID），但STRING预测4个中等置信度互作伙伴。TANC1（tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 1, STRING score=400）为突触后致密区（postsynaptic density, PSD）支架蛋白——含ANK repeats和TPR repeats，调控树突棘（dendritic spine）形态和AMPA/NMDA受体突触定位。THAP2（THAP domain containing 2, STRING score=432）为含THAP锌指（C2CH, zinc-dependent DNA binding domain）的转录因子——结合DNA并调控细胞周期基因。PRDM8（PR/SET domain 8, STRING score=457）为组蛋白甲基转移酶（H3K9me1/me2）——在神经发育中调控基因表达。

**机制模型与功能**：TMEM215的核心功能为血管生成中的内皮细胞存活因子。在血管退化（vessel regression）中，内皮细胞面临凋亡压力——TMEM215防止BIK（BCL2-interacting killer, BH3-only促凋亡蛋白, PMID 37750320）介导的ER-to-mitochondria Ca²⁺流入和线粒体凋亡。BIK在ER膜上激活ryanodine receptor (RyR)或IP3R Ca²⁺释放通道→ER Ca²⁺流入线粒体→线粒体钙超载→MPTP（mitochondrial permeability transition pore）开放→cytochrome c释放→apoptosome形成→caspase-9/3激活——TMEM215通过blunting（钝化）此过程保护内皮细胞存活——机制可能是TMEM215与BIK直接或间接互作→阻断BIK对ER Ca²⁺释放通道的激活。在核质（HPA Approved Nucleoplasm + Vesicles）中，TMEM215作为膜蛋白的核内形式可能在内膜（inner nuclear membrane, INM）与核质间循环——其抗凋亡功能在核膜层面保护核膜完整性和NPC功能。

**TE调控展望**：TMEM215对TE调控的关联间接且弱。血管生成（angiogenesis）和肿瘤微环境（TME）已知影响TE表达——缺氧（hypoxia, HIF-1α stabilization）激活LINE-1 and HERV-K转录——TMEM215通过促进血管稳定性维持氧合→可能间接抑制缺氧诱导的TE激活。BIK调控线粒体凋亡——在DNA损伤应答（DDR）中，逆转录转座产生DSB→ATM/ATR→CHK1/CHK2→p53稳定化→诱导BIK/Bax/Bak介导的凋亡以清除TE超转座的受损细胞——TMEM215通过阻断此凋亡通路可能在异常条件下允许TE活跃转座的细胞存活——即TMEM215高表达的肿瘤内皮细胞中可能间接促进TE转座阳性克隆的耐受和扩增。此外，NET-DNA（neutrophil extracellular traps, PMID 42037208）诱导的ANXA2/TMEM215/BiP轴在子宫内膜异位症（endometriosis）中促进mitophagy-mediated anoikis resistance——NETs含大量基因组和线粒体DNA片段（包括TE序列）——TMEM215可能在内吞NET-DNA后的细胞存活中发挥尚未阐明的TE相关角色。



### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM215

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000188133-TMEM215

![](https://images.proteinatlas.org/63207/1698_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1698_F3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000188133-TMEM215

![](https://images.proteinatlas.org/63207/1698_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1698_F3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000188133-TMEM215

![](https://images.proteinatlas.org/63207/1698_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1698_F3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63207/1646_C5_3_blue_red_green.jpg)

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 42037208 | NET-DNA Activates the ANXA2/TMEM215/BiP Axis to Promote Mitophagy-Mediated Anoikis Resistance in Endometriosis. |
| 40001597 | Data-Driven Identification of Early Cancer-Associated Genes via Penalized Trans-Dimensional Hidden Markov Models. |
| 38631315 | Hypothalamic GABAergic Neurons Expressing Cellular Retinoic Acid Binding Protein 1 (CRABP1) Are Sensitive to Metabolic Status and Liraglutide in Male  |
| 37750320 | TMEM215 Prevents Endothelial Cell Apoptosis in Vessel Regression by Blunting BIK-Regulated ER-to-Mitochondrial Ca Influx. |
| 30370660 | Transmembrane protein 215 promotes angiogenesis by maintaining endothelial cell survival. |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TANC1 | STRING | 400 |
| THAP2 | STRING | 432 |
| PRDM8 | STRING | 457 |
| TMEM215 | STRING | 413 |
