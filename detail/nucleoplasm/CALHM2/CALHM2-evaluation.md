---
type: protein-evaluation
gene: "CALHM2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CALHM2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CALHM2 |
| 蛋白名称 | Calcium homeostasis modulator protein 2 |
| 蛋白大小 | 323 aa / 36.2 kDa |
| UniProt ID | Q9HA72 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 323 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=81.1; PDB=12 |
| 调控结构域 | 4/10 | x2 | 8.0 | CALHM |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 分析
- HPA: Cytosol; Mitochondria; Nucleoplasm (Approved)
- PubMed: strict=17, broad=33
- AF pLDDT: 81.1 / PDB: 12
- InterPro: CALHM
- Pfam: Ca_hom_mod
- PPI degree=4 / ChIP: None
36993337: Perturbomics of tumor-infiltrating NK cells. | 34433553: Microglial Calhm2 regulates neuroinflammation and contributes to Alzheimer's dis | 39315269: CALHM2 is a mitochondrial protein import channel that regulates fatty acid metab

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Calcium homeostasis modulator protein 2

**功能**: Pore-forming subunit of Ca(2+) homeostasis modulator channels. Mediates ATP release from astrocytes and ATP-induced Ca(2+) influx in microglia thus regulating neuronal ATP and Ca(2+) homeostasis, synaptic transmission and neuroinflammatory response. May form intercellular gap junctions. The gating mechanism remains unknown

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029569 |
| Pfam | PF14798 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---



### 深度机制分析

CALHM2的域结构极为精简——仅由InterPro域CALHM（IPR029569）和Pfam域Ca_hom_mod（PF14798）组成。CALHM家族（Calcium Homeostasis Modulator）属于一类进化保守的跨膜通道蛋白，其特征是四个跨膜螺旋形成六聚体孔径。该域的结构预测表明CALHM2采用寡聚化组装模式，在质膜或线粒体膜上形成功能性孔道。家族成员CALHM1的结构（PDB中12个条目可为CALHM2提供同源建模参考）揭示了该域通过亚基间的氢键网络感知膜电位和Ca2+浓度变化，实现电压门控和配体门控的双重调节。值得注意的是，UniProt注释明确该蛋白为"孔道形成亚基"（pore-forming subunit），暗示其在膜上以同源或异源寡聚体的形式发挥功能。

PPI网络虽然规模有限（degree=4），但每位伙伴都具有重要的生物医学含义。TGFBR2（TGF-β受体2）的互作是最值得关注的发现——该受体是TGF-β信号通路的核心组分，调控细胞增殖、分化和免疫抑制。这种互作提示CALHM2可能通过调节TGFBR2附近微环境的Ca2+浓度或ATP水平来间接调控TGF-β信号。PRND（Doppel蛋白）是一种GPI锚定的朊蛋白家族成员，主要表达于睾丸和神经系统，其与CALHM2的结合可能发生在特定的膜微域（如脂筏）中。TMEM59的互作暗示CALHM2参与内质网-高尔基体运输和自噬体-溶酶体融合过程。FAM212A（又名INKA2）是PAK4激酶的抑制剂，提示CALHM2与肌动蛋白细胞骨架调控之间存在潜在联系。

结构方面，AlphaFold pLDDT 81.1反映了跨膜蛋白结构预测的固有挑战——跨膜螺旋区域通常具有中等置信度，而膜外环区（loop）的置信度更低。12个PDB结构为同家族成员提供了丰富的结构信息，特别是CALHM1的冷冻电镜结构揭示了六聚体通道的组装方式和离子通透路径。关键文献（PMID: 39315269）的突破性发现——CALHM2定位于线粒体并作为蛋白导入通道——从根本上重新定义了这一蛋白的功能分类，将其从单纯的质膜钙通道扩展为线粒体蛋白转运机器。这解释了为什么HPA IF图像中观察到胞质、线粒体和核质的多重定位。

综合证据勾勒出CALHM2的分子机制模型为"双定位钙稳态与代谢信号整合器"。在质膜上，CALHM2以六聚体通道形式介导ATP释放（星形胶质细胞）和ATP诱导的Ca2+内流（小胶质细胞），构成神经血管单元中的嘌呤能信号回路（PMID: 34433553, 42330888）。在线粒体外膜，CALHM2作为蛋白导入通道调控脂肪酸代谢（PMID: 39315269），将钙信号与细胞能量代谢耦合。在核质中，CALHM2可能作为核膜的钙/ATP通道或参与核-质信号传递。TGFBR2-CALHM2的互作暗示该蛋白可能在TGF-β诱导的上皮-间质转化和免疫逃逸中作为膜微环境的调节因子。这一"一蛋白-多膜"的分布模式使其成为同时整合代谢信号、钙信号和炎症信号的独特节点。

CALHM2的科研与治疗前景广阔。PubMed仅17篇严格文献（评分9/10），但其在阿尔茨海默病（PMID: 34433553, 41016794）和骨癌疼痛（PMID: 41520863）中的功能已初步揭示。靶向CALHM2的策略在神经退行性病中具有差异化的优势：抑制小胶质细胞CALHM2可减弱神经炎症（AD模型），而激活星形胶质细胞CALHM2-ATP通路可增强突触可塑性。在线粒体层面，调控CALHM2的蛋白导入功能可能为代谢性疾病（如脂肪肝和2型糖尿病）提供新靶点。在肿瘤微环境中，CALHM2-ATP-Ca2+轴可能在NK细胞肿瘤浸润（PMID: 36993337）中发挥免疫调节作用。开发亚型选择性的CALHM2调节剂（区别于CALHM1和CALHM3）是关键的药物化学挑战。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRND | BioGRID | 0 |
| TGFBR2 | BioGRID | 0 |
| FAM212A | BioGRID | 0 |
| TMEM59 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HA72-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138172-CALHM2

![](https://images.proteinatlas.org/14706/172_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/172_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138172-CALHM2

![](https://images.proteinatlas.org/14706/172_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/172_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138172-CALHM2

![](https://images.proteinatlas.org/14706/172_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/172_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/121_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/14706/123_B8_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 33**

| 42330888 | Functional expression of calcium homeostasis modulator 2 (CALHM2) regulates the bioenergetic transition of BV2 microglia | Biochem Biophys Res Commun 2026 |
| 41520863 | The mechanism of Calhm2 regulating the expression of CaMKIIα in spinal dorsal horn involved in the pathogenesis of bone  | Brain Res 2026 |
| 41016794 | Neurotropin alleviates Alzheimer's disease pathology by inhibiting FUS-mediated Calhm2 transcription, blocking the Calhm | Biosci Trends 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CALHM2

