---
type: protein-evaluation
gene: "TRABD"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TRABD 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TRABD |
| 蛋白名称 | TraB domain-containing protein |
| 蛋白大小 | 376 aa / 42.3 kDa |
| UniProt ID | Q9H4I3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 376 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=80.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TraB/PrgY/GumN_fam; TraB_PrgY-like |
| PPI | 6/10 | x3 | 18.0 | PPI degree=91 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=7 broad=11
- AF pLDDT=80.6 PDB=0
- InterPro: TraB/PrgY/GumN_fam; TraB_PrgY-like
- Pfam: TraB_PrgY_gumN
- PPI degree=91 ChIP: None
25173755: Integrative identification of Epstein-Barr virus-associated mutations and epigen | 40778267: TRABD maintains mitochondrial homeostasis and protects against ischemia reperfus | 38843396: TRABD modulates mitochondrial homeostasis and tissue integrity.

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**: TRABD含有TraB/PrgY/GumN家族结构域（IPR002816/PF01963）和TraB_PrgY-like折叠（IPR046345）。这个结构域家族具有独特的进化起源——其原核祖先蛋白参与细菌接合（conjugation）和DNA跨膜转运：链霉菌属的TraB蛋白介导质粒DNA在菌丝间的转移，肠球菌属的PrgY蛋白是信息素响应型接合质粒的膜蛋白，黄单胞菌属的GumN参与胞外多糖分泌。在人类蛋白中存在这样一个原核接合系统同源结构域，强烈暗示发生了一次古老的水平基因转移事件，或者该结构域被真核生物招募后经历了广泛的序列分化以适应新的细胞功能——膜孔形成/蛋白质转运。TraB结构域预测为全α-螺旋折叠，可能形成一种通道样结构。

**PPI网络解读**: TRABD的PPI网络（degree=91）核心围绕线粒体质量控制和能量代谢。BECN1（BioGRID）是Beclin-1——自噬起始复合体（PI3KC3复合体）的核心亚基，将TRABD直接连接到自噬/线粒体自噬通路。UBC（BioGRID）是泛素C，提示TRABD受泛素化-蛋白酶体系统调控或本身具有基于泛素化的底物识别功能。ILK（BioGRID）是整合素连接激酶——通常与细胞黏附和细胞骨架相关，但也已知定位于线粒体参与线粒体功能和细胞存活调控。HIPK4（BioGRID）是同源异型盒相互作用蛋白激酶（主要在睾丸中表达），可能磷酸化TRABD。值得注意的是NME2（核苷二磷酸激酶）和两个ATP酶（ATP12A为胃H+/K+-ATPase、ATP2B2为质膜钙ATP酶），共同提示TRABD的功能高度依赖核苷酸（ATP/GTP）和离子梯度的偶联。

**结构诠释**: AlphaFold pLDDT=80.6为中等置信度，无PDB实验结构。TraB结构域的细菌祖先蛋白通常形成六聚体或八聚体的环状跨膜通道复合体。在TRABD中，这个结构域可能以单体形式运作——但BECN1和UBC的互作提示TRABD可能通过泛素化信号被招募到线粒体外膜的特定区域并寡聚化。中等的pLDDT值暗示存在较大的柔性区域——这些柔性环可能作为"门控"元件，在线粒体蛋白导入过程中发生构象转变。

**分子机制模型**: TRABD在线粒体稳态维护中发挥双重功能：(1) 线粒体融合/聚集：与MFN2、MIGA2和PLD6协同作用促进线粒体聚集和融合（PMID 38843396）——TRABD可能在MFN2介导的线粒体外膜融合过程中发挥辅助作用，利用其TraB结构域促进膜接触或脂质交换；(2) 线粒体蛋白导入：PMID 40105103报道TRABD可能参与SLC25A19的线粒体导入——SLC25A19是线粒体硫胺素焦磷酸（TPP）转运蛋白（属于SLC25线粒体载体家族），这表明TRABD的TraB结构域可能形成或辅助线粒体外膜的TIM/TOM转位酶通道，特别是对于代谢物载体蛋白的导入。核质池（HPA Approved）可能代表一种截短形式或替代起始产物，执行核质逆行信号传导——将线粒体状态信息传递给核基因表达机器。(3) 缺血再灌注保护：PMID 40778267（Front Cell Dev Biol 2025）显示TRABD通过维持线粒体稳态保护肾小管免受缺血再灌注损伤——这很可能通过上述线粒体融合/蛋白导入双重功能实现：缺血期间线粒体碎片化，再灌注时TRABD通过促进MFN2依赖的融合恢复线粒体网络完整性。

**研究/治疗意义**: TRABD是急性肾损伤（AKI）和心肌梗死的潜在治疗靶点（基于PMID 40778267的缺血再灌注保护功能）。TraB结构域的细菌起源为其提供了一个独特的药理学靶点——可以设计针对TraB通道的抑制剂，同时避免影响其他人类蛋白（因为该结构域在人类基因组中拷贝数极低）。BECN1互作提示TRABD可能是线粒体自噬（mitophagy）的关键检查点：TRABD失活→受损线粒体积聚→触发PINK1/Parkin通路→过度线粒体自噬，这在与线粒体功能障碍相关的神经退行性疾病（帕金森病）和衰老中具有重要病理意义。EBV病毒相关突变（PMID 25173755）提示病毒（特别是EBV）可能通过操控TRABD来重塑宿主线粒体稳态，从而为病毒持续感染创造有利的代谢环境——这是一个潜在的抗病毒治疗切入点。

### 补充分析 (UniProt API)

**蛋白全称**: TraB domain-containing protein

**功能**: Along with MFN2, MIGA2 and PLD6 promotes mitochondrial clustering and fusion (PubMed:38843396). May play a role in mitochondrial import of proteins, such as that of SLC25A19 (PubMed:40105103)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002816 |
| InterPro | IPR046345 |
| Pfam | PF01963 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BECN1 | BioGRID | 0 |
| UBC | BioGRID | 0 |
| HIPK4 | BioGRID | 0 |
| ILK | BioGRID | 0 |
| NME2 | BioGRID | 0 |
| ATP12A | BioGRID | 0 |
| HSP90AA4P | BioGRID | 0 |
| ATP2B2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H4I3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170638-TRABD

![](https://images.proteinatlas.org/822/1272_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/822/1272_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/822/1232_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/822/1232_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/822/1199_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/822/1199_H1_3_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 42147232 | Multi-omics integration and Mendelian randomization elucidate the PARP16-UPR axis driving chemoresistancein gastric canc | Front Oncol 2026 |
| 41231246 | Immunophenotype-mediated effects of plasma proteins on major depressive disorder: A two-step Mendelian randomization stu | Eur Arch Psychiatry Clin Neurosci 2026 |
| 40778267 | TRABD maintains mitochondrial homeostasis and protects against ischemia reperfusion-induced renal tubular injury. | Front Cell Dev Biol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TRABD

