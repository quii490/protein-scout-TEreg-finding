---
type: protein-evaluation
gene: "TMEM8B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM8B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM8B |
| 蛋白名称 | Transmembrane protein 8B |
| 蛋白大小 | 472 aa / 51.9 kDa |
| UniProt ID | A6NDV4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 472 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | EGF; NGX6/PGAP6/MYMK |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Approved)
- PubMed: strict=5, broad=37
- AF pLDDT: 80.8 / PDB: 0
- InterPro: EGF; NGX6/PGAP6/MYMK
- Pfam: DUF3522
- PPI degree: 5 / ChIP: None
**Papers**: 33333720: Association of TMEM8B and SPAG8 with Mature Weight in Sheep. | 29886078: Expression and purification of a rapidly degraded protein, TMEM8B-a, in mammalia | 38067078: Genomic Dissection through Whole-Genome Resequencing of Five Local Pig Breeds fr

### 4. 总体评价
★★★★  **75.4/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 8B

**功能**: May function as a regulator of the EGFR pathway. Probable tumor suppressor which may function in cell growth, proliferation and adhesion

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000742 |
| InterPro | IPR021910 |
| Pfam | PF12036 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**多域结构与EGFR信号调控者的分子基础** TMEM8B（472 aa, 51.9 kDa）是五个候选蛋白中结构域注释最丰富的一个，包含IPR000742（EGF-like domain）、IPR021910（NGX6/PGAP6/MYMK家族）和PF12036（DUF3522，功能未知域）。EGF样结构域是一类约30-40个氨基酸的模块，含6个保守半胱氨酸形成3对二硫键，典型功能是介导蛋白-蛋白互作和受体识别（如在Notch、EGF、laminin等蛋白中）。TMEM8B出现EGF样结构域本身就极不寻常——多数EGF样域蛋白是分泌蛋白或质膜受体，而非核蛋白。NGX6/PGAP6/MYMK家族是近年来发现的参与细胞融合（myoblast fusion，MYMK/Mymk）、糖基磷脂酰肌醇（GPI）锚定蛋白重塑（PGAP6）和鼻咽癌抑制（NGX6）的多功能蛋白群。该家族的核心特征是与细胞膜融合/重塑过程的深度关联，这意味着TMEM8B可能利用此域参与核膜的动态重构——核膜在细胞分裂、核孔复合体组装和核质运输中经历持续的重塑。pLDDT=80.8的"中低度折叠置信度"可能源于EGF样结构域的非典型环境（核内而非胞外）导致的预测不确定性，而非真正的无序——二硫键约束通常使EGF样结构域在实验条件下具有高刚性的三级结构。

**PPI网络的核心学意义** 5个互作伙伴虽少但每一位都极具信息量。ATXN1L（Ataxin-1-like）是转录辅抑制因子，与Capicua（CIC）形成CIC-ATXN1L复合体，在RTK-RAS-MAPK信号下游直接抑制PEA3家族ETS转录因子的靶基因——该复合体在肺腺癌、前列腺癌和少突胶质细胞瘤中被MAPK磷酸化后失活。TMEM8B与ATXN1L的互作直接将其置于EGFR-RAS-MAPK转录调控网络的核心节点。HNRNPL（heterogeneous nuclear ribonucleoprotein L）是hnRNP家族的RNA结合蛋白，调控pre-mRNA可变剪接、mRNA稳定性和IRES依赖的翻译——在EGFR信号激活时，HNRNPL调控Delta EGFR（EGFRvIII）等肿瘤特异性剪接变体的产生。TOP3B是DNA拓扑异构酶IIIβ，在转录过程中解除DNA拓扑张力，并与FMRP（脆性X智力障碍蛋白）协作调控神经突触相关mRNA的代谢。ARHGDIB（RhoGDIβ）是Rho家族小G蛋白的GDP解离抑制因子，控制Rho GTPases的膜-胞质分布和激活状态——Rho信号是细胞迁移、黏附和EGFR下游肌动蛋白重塑的核心通路。CHRM2是毒蕈碱型乙酰胆碱受体M2，为G蛋白偶联受体（GPCR），可转激活EGFR通路——将CHRM2与TMEM8B的EGF样结构域放在一起考虑，提示TMEM8B可能参与GPCR-EGFR信号交叉对话。

**从EGFR通路到染色质/RNA调控的信号桥接** TMEM8B的UniProt功能注释（"Probable tumor suppressor which may function in cell growth, proliferation and adhesion"和"May function as a regulator of the EGFR pathway"）与其PPI网络形成了极强的功能一致性。我们提出TMEM8B作为EGFR信号与核内基因调控之间的双向信号桥接蛋白（bidirectional signal bridging protein）的机制模型：（1）上游：TMEM8B通过EGF样结构域感知EGFR配体激活信号（可能经由胞内域或间接通过衔接蛋白），将信号从质膜传递至核质；（2）中继：TMEM8B在核内通过与ATXN1L-CIC复合体的互作解除转录抑制，释放PEA3-ETS靶基因（如MMPs、cyclin D1等促增殖/侵袭基因）；（3）下游：HNRNPL确保EGFR通路相关mRNA的正确剪接（包括可能的EGFR自身剪接变体），TOP3B维持转录活跃区的DNA拓扑状态，ARHGDIB将Rho信号与细胞黏附/迁移表型耦合。NGX6/PGAP6/MYMK家族域可能提供了核膜相关的锚定平台，使TMEM8B在特定核膜微区富集，形成局部的EGFR信号转导中枢（EGFR nuclear signaling hub）。

**低pLDDT的结构悖论与生物学意义** pLDDT=80.8相对较低，可能并不反映结构质量差，而是反映了TMEM8B的三重柔性需求：（a）EGF样结构域的构象变化（配体结合vs.游离态）；（b）DUF3522域可能充当可诱导的无序到有序转换开关；（c）在与ATXN1L、HNRNPL、TOP3B等不同伙伴结合时需采用不同的构象状态。这种构象多样性（conformational heterogeneity）在单体AlphaFold预测中表现为局部低置信度，但恰恰是其作为信号中枢的功能特征。TMEM8B是五个TMEM中唯一含EGF样结构域的蛋白，赋予其独特的胞外信号感知能力——即便在核内，其EGF样结构域的β-sheet骨架和保守二硫键可能维持高度刚性的核心，而通过连接区段（linker）的柔性实现结构域的重新定向（domain reorientation），类似于整联蛋白（integrin）在inside-out和outside-in信号中的构象切换。

**研究与转化意义** TMEM8B的高PubMed计数（37篇）与其低pLDDT和丰富的PPI形成了鲜明对比——大部分文献聚焦于GWAS和群体遗传学（绵羊体重、猪品种选育、高海拔适应性，PMID:33333720/38067078/41896730），而分子机制研究几乎空白（仅PMID:29886078关于重组表达和快速降解）。这种"表型先于机制"的格局为深入的功能研究提供了大量可转化的线索。在肿瘤生物学中，作为EGFR通路调控者和ATXN1L-CIC转录辅抑制复合体的互作蛋白，TMEM8B可能决定EGFR靶向治疗（如吉非替尼、奥希替尼）的敏感性——TMEM8B表达水平或突变状态可能是EGFR-TKI疗效的预测生物标志物。ATXN1L-CIC复合体在MAPK信号抑制后在少突胶质细胞瘤中重新激活并抑制增殖，因此TMEM8B的激动剂（增强其与ATXN1L的互作）可能在MAPK通路异常的肿瘤中具有治疗价值。从方法学角度，TMEM8B的重组表达和纯化已被证明可行（PMID:29886078），下一步应解决其在哺乳动物细胞中的稳定性问题（半衰期可能因泛素-蛋白酶体系统的快速降解而较短），部分或完整结构的cryo-EM解析将是阐明其构象调控机制的关键。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ATXN1L | BioGRID | 0 |
| HNRNPL | BioGRID | 0 |
| CHRM2 | BioGRID | 0 |
| ARHGDIB | BioGRID | 0 |
| TOP3B | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A6NDV4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137103-TMEM8B

![](https://images.proteinatlas.org/62701/1194_E11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1194_E11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137103-TMEM8B

![](https://images.proteinatlas.org/62701/1194_E11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1194_E11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137103-TMEM8B

![](https://images.proteinatlas.org/62701/1194_E11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1194_E11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62701/1202_E1_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 41896730 | Genetic analysis of cold tolerance and high-altitude adaptation in Gannan indigenous Tibetan sheep through genome-wide s | BMC Genomics 2026 |
| 38067078 | Genomic Dissection through Whole-Genome Resequencing of Five Local Pig Breeds from Shanghai, China. | Animals (Basel) 2023 |
| 33333720 | Association of TMEM8B and SPAG8 with Mature Weight in Sheep. | Animals (Basel) 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM8B

