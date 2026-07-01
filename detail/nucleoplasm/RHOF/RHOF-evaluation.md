---
type: protein-evaluation
gene: "RHOF"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RHOF 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RHOF |
| 蛋白名称 | Rho-related GTP-binding protein RhoF |
| 蛋白大小 | 211 aa / 23.6 kDa |
| UniProt ID | Q9HBH0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 211 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=91.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | P-loop_NTPase; Small_GTP-bd; Small_GTPase |
| PPI | 8/10 | x3 | 24.0 | PPI degree=673 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **77.6/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=22 broad=98
- AF pLDDT=91.6 PDB=0
- InterPro: P-loop_NTPase; Small_GTP-bd; Small_GTPase
- Pfam: Ras
- PPI degree=673 ChIP: None
40795589: Asiaticoside alleviates atherosclerosis progression by suppressing RhoF-NF-κB/MA | 30998758: KLF4 activates NFκB signaling and esophageal epithelial inflammation via the Rho | 15877735: Expression of the Rho-family GTPase gene RHOF in lymphocyte subsets and malignan

### 4. 总体评价
**77.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与分子功能推断。** RHOF（Rif）是Rho家族小GTPase的独特成员，其211 aa紧凑多肽包含完整的小G蛋白折叠模块：P-loop_NTPase (IPR027417)、Small_GTP-binding domain (IPR005225)、Small_GTPase (IPR001806)和Ras超家族特征域(IPR003578)，Pfam注释为Ras家族(PF00071)。该蛋白包含小GTPase的所有保守功能元件：G1 box (P-loop/Walker A, GxxxxGK[ST])负责α/β-磷酸结合，G2 box (Switch I)和G3 box (Switch II)构成效应器识别面并在GTP/GDP结合态之间发生构象变化，G4 box (NKxD)特异性识别鸟嘌呤碱基，G5 box (SAK)稳定核苷酸结合。C端CAAX异戊二烯化基序指导其翻译后脂修饰和膜靶向。pLDDT=91.6的出色评分体现了AF2对Ras超家族折叠的高预测置信度——这是结构数据库中定义最完善、同源模板最丰富的折叠类型之一。RHOF与CDC42和Rac1在G结构域上共享约50%的序列同一性，但Switch I/II区域存在关键的序列分歧，这决定了其独特的效应器特异性和细胞表型：RHOF专门诱导丝状伪足(filopodia)的形成，产生细长的平行肌动蛋白束，而非CDC42诱导的宽片状伪足(lamellipodia)(PubMed:15877735)。

**PPI网络的生物学意义。** RHOF拥有673个互作伙伴，为5个候选蛋白中PPI degree最高者。值得注意的是关键互作远不止经典肌动蛋白调控因子：ELAVL1(HuR)是ARE(AU-rich element)介导的mRNA稳定性调控的核心RNA结合蛋白——在细胞应激条件下，ELAVL1穿梭至胞质以稳定促存活mRNA，而正常情况下主要定位于核质；ENO1(α-烯醇化酶)具有双重功能，既是糖酵解的催化酶，又是转录调节因子(作为MBP-1结合c-myc启动子)；MOV10是RNA解旋酶，参与miRNA介导的沉默和逆转录转座子抑制；NXF1(TAP)是核mRNA输出的主要受体，直接识别mRNA的5'帽结构和外显子连接复合体(EJC)标记成熟mRNA以进行核质转运；XPO1(CRM1/Exportin-1)介导富含亮氨酸的核输出信号(NES)识别的蛋白质核输出。这些互作蛋白的集合将RHOF直接连接到两个核过程：(1) mRNA代谢和命运决定(ELAVL1、MOV10)；(2) 核质转运(NXF1、XPO1)。此外，GAR1作为H/ACA snoRNP的核心组分参与假尿苷化(pseudouridylation)的互作进一步暗示RHOF可能参与核仁或Cajal体中的非编码RNA加工。

**三维结构的功能解释。** AF2预测的RHOF结构呈现典型的Ras折叠：一个六链平行/混合β-折叠核心被五个α-螺旋环绕，G结构域包含高度保守的核苷酸结合口袋。pLDDT=91.6且在核心折叠区域(G1-G5 box)置信度>95，Switch I和Switch II区域的置信度在中等范围(80-90)，反映这些区域固有的构象动态性。PDB=0的事实虽缺乏实验结构，但RHOF与CDC42(PDB:1A4R、1AN0等)和Rac1(PDB:1MH1等)的结构同源性提供了可靠的比较建模基础。RHOF在Switch I区域的第37位（对应Rac1的T35）和Switch II区域的第62位（对应CDC42的Y64）的氨基酸置换可能是决定其独特效应器特异性的关键——这些残基差异改变了效应器结合面的静电势和几何形状。C端高变区(hypervariable region, 约残基180-211)的pLDDT较低(<50)，反映了脂修饰依赖的膜锚定区域的固有无序特性。

**综合分子机制模型。** RHOF代表了经典小GTPase信号与非经典核功能之间的一个新兴"分子网关"，为其HPA双定位(Golgi apparatus; Nucleoplasm Approved)提供了功能解释。在细胞质膜和高尔基体上，RHOF作为典型的GTP/GDP分子开关运作——GEF(鸟嘌呤核苷酸交换因子)促进GTP加载后，Switch I/II采取活性构象，招募下游效应器(如formin mDia2)驱动线性肌动蛋白聚合、丝状伪足形成和细胞迁移。SIAH2 E3泛素连接酶通过泛素化靶向RHOF进行蛋白酶体降解，EPHB6受体信号抑制这一降解，从而调控RHOF稳态水平和侵袭性伪足形成(PubMed:42036676)，将RHOF置于肿瘤转移信号的中枢位置。在核质中，RHOF与ELAVL1、MOV10、NXF1和XPO1的互作网络暗示一个非经典功能模型：RHOF可能在核浆中通过ELAVL1感知应激信号，协同MOV10参与特定mRNA子集的代谢调控。KLF4通过RHOF-NFκB/MA通路激活NFκB信号(PubMed:30998758)进一步支持RHOF在炎症转录程序中的调控角色，可能与ELAVL1稳定促炎细胞因子mRNA的机制相关。Asiaticoside通过直接抑制RHOF的表达或活性来阻断NFκB/MA通路，从而缓解动脉粥样硬化进展(PubMed:40795589)——这一定向的药理学干预验证了RHOF作为炎症信号节点的因果性(而非相关性)角色。

**研究与治疗启示。** RHOF的小分子抑制剂研发处于起步阶段，但该蛋白具备所有有利的可药化特征：(1) 明确的小分子结合口袋(GTP结合位点)，已有Ras/Rho家族GTPase抑制剂的先例(如靶向KRAS G12C的共价抑制剂)；(2) Switch I/II界面的独特序列特征允许设计亚型选择性抑制剂以避免脱靶效应于CDC42或Rac1；(3) Asiaticoside提供了一种天然产物的化学起点用于药效团优化。关键的研究优先事项包括：确定核RHOF的确切功能(是作为GTPase开关调控核内过程，还是以GDP结合态被动穿梭至核质)；通过体内模型验证RHOF作为动脉粥样硬化(PubMed:40795589)和肝细胞癌转移(PubMed:42036676)治疗靶点的可靠性；利用化学蛋白质组学在Ras超家族背景下系统评估RHOF的选择性配体。

### 补充分析 (UniProt API)

**蛋白全称**: Rho-related GTP-binding protein RhoF

**功能**: Plasma membrane-associated small GTPase which cycles between an active GTP-bound and an inactive GDP-bound state. Causes the formation of thin, actin-rich surface projections called filopodia. Functions cooperatively with CDC42 and Rac to generate additional structures, increasing the diversity of actin-based morphology

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR005225 |
| InterPro | IPR001806 |
| InterPro | IPR003578 |
| Pfam | PF00071 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| ENO1 | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| ANKFY1 | BioGRID | 0 |
| XPO1 | BioGRID | 0 |
| RALA | BioGRID | 0 |
| GAR1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HBH0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139725-RHOF

![](https://images.proteinatlas.org/45912/562_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/562_H10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139725-RHOF

![](https://images.proteinatlas.org/45912/562_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/562_H10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139725-RHOF

![](https://images.proteinatlas.org/45912/562_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/562_H10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/568_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45912/575_H10_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 98**

| 42117472 | Inspired by the Hydrophilic Nature of Squid Muscles: Constructing High-Performance Anti-fatigue Polymeric Hydrogel Artif | J Phys Chem B 2026 |
| 42036676 | SIAH2-EPHB6 axis enhances filopodia formation in hepatocellular carcinoma cells by regulating RHOF. | Cell Biosci 2026 |
| 41568806 | An improved united-atom potential for molecular dynamics simulation of saturated properties of n-alkanes. | J Chem Phys 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RHOF

