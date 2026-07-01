---
type: protein-evaluation
gene: "MAP3K3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MAP3K3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MAP3K3 |
| 蛋白名称 | Mitogen-activated protein kinase kinase kinase 3 |
| 蛋白大小 | 626 aa / 70.9 kDa |
| UniProt ID | Q99759 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 626 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=90 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=66.9; PDB=6 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kinase-like_dom_sf; PB1-like; PB1_dom |
| PPI | 6/10 | x3 | 18.0 | PPI degree=86 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=90 broad=224
- AF pLDDT=66.9 PDB=6
- InterPro: Kinase-like_dom_sf; PB1-like; PB1_dom
- Pfam: PB1; Pkinase
- PPI degree=86 ChIP: None
40127145: Map3k3  (I441M) Knock-In Mouse Model of Cerebral Cavernous Malformations. | 41552909: Angiogenic switching in cerebral cavernous malformations driven by MAP3K3-PIK3CA | 35593587: miR-181b regulates vascular endothelial aging by modulating an MAP3K3 signaling 

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mitogen-activated protein kinase kinase kinase 3

**功能**: Component of a protein kinase signal transduction cascade. Mediates activation of the NF-kappa-B, AP1 and DDIT3 transcriptional regulators

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR053793 |
| InterPro | IPR000270 |
| InterPro | IPR034879 |
| InterPro | IPR000719 |
| Pfam | PF00564 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SQSTM1 | STRING | 973 |
| MAP2K3 | STRING | 970 |
| TRAF6 | STRING | 963 |
| CHUK | STRING | 961 |
| IKBKB | STRING | 959 |
| MAP3K2 | STRING | 952 |
| IKBKG | STRING | 949 |
| PAK1 | STRING | 922 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q99759-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198909-MAP3K3

![](https://images.proteinatlas.org/35410/806_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/35410/806_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/35410/820_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/35410/820_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/35410/810_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/35410/810_D9_4_red_green.jpg)
![](https://images.proteinatlas.org/35410/690_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/35410/690_B10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 224**

| 42151695 | NAA50-mediated SLU7 stabilization promotes cisplatin resistance in bladder cancer via regulating MAP3K3 mRNA nuclear exp | Cell Oncol (Dordr) 2026 |
| 41891922 | TIE2 links MEKK3-KLF2/4 and PI3K signaling in cerebral cavernous malformation. | J Exp Med 2026 |
| 41870631 | Identification of potential diagnostic and therapeutic apoptosis-related casual targets for osteoporosis: an integrated  | J Bone Miner Metab 2026 |

### 深度机制分析

MAP3K3（亦称MEKK3, 626 aa, 70.9 kDa）是丝裂原活化蛋白激酶（MAPK）信号级联中的核心激酶，属于MAP3K家族中响应炎症和应激信号的分支。其结构域架构由N端的PB1结构域（IPR000270）和C端的丝/苏氨酸蛋白激酶催化结构域（IPR011009）组成。PB1结构域是约80个氨基酸的模块，通过典型的前酸后碱（acidic-basic）表面电荷互补介导特定的异源二聚化——MAP3K3通过PB1结构域与MEK激酶（MAP2K3）、p62/SQSTM1等蛋白结合。蛋白激酶折叠在pLDDT=66.9时预测质量一般，但已有6个PDB条目提供实验结构——这是25个候选蛋白中PDB条目最多的之一，为结构导向药物设计提供了良好基础。

MAP3K3催化MAP2K（MEK）的激活磷酸化，后者进一步磷酸化并激活MAPK（ERK、JNK、p38），这一三级激酶级联最终调控NF-kappa-B、AP1和DDIT3转录因子的活性。在脑海绵状血管畸形（CCM）的病理生物学中，MAP3K3发挥核心作用——MAP3K3 I441M敲入小鼠模型精确重现了CCM表型（PMID:40127145），该突变导致MAP3K3激酶活性的获得性增强，触发KLF2/4转录因子的异常激活和血管生成切换（angiogenic switching, PMID:41552909）。TIE2受体将MAP3K3-MEK5-ERK5信号与PI3K信号联系起来阐明CCM发病机制（PMID:41891922）。

PPI网络极其丰富（BioGRID degree=86, STRING扩展），与SQSTM1（p62, STRING 973）、TRAF6（STRING 963, E3泛素连接酶）、CHUK/IKBKB/IKBKG（IKK复合物, STRING 961/959/949）和MAP2K3（STRING 970）形成炎症和NF-kappa-B信号的核心网络。HPA Nucleoplasm（Approved级别）定位与MAP3K3通过磷酸化激活核内转录因子（NF-kappa-B/AP1靶基因）的功能一致。

在TE调控方面，MAP3K3通过多条通路产生影响。首先，NF-kappa-B激活可结合TE来源的增强子和启动子（许多ERV/LTR含有NF-kappa-B基序），直接驱动TE转录。第二，MAP3K3-TIE2-KLF轴调控KLF转录因子的表达——KLF家族成员（特别是KLF4）已知结合富含CpG的序列和特定的TE亚家族。第三，MAP3K3-SQSTM1互作将自噬受体p62导入信号网络——p62通过选择性自噬降解LINE-1 ORF1p蛋白，这是TE蛋白质量控制的关键机制。因此MAP3K3通过磷酸化信号间接调控TE RNA和蛋白的多个层面。MAP3K3-CCM2L互作（STRING 740, 见上文CCM2L分析）为两个核蛋白在心血管TE调控中的协同作用提供了整合视角。MiR-181b调控MAP3K3信号参与血管内皮老化（PMID:35593587）提示MAP3K3在老化相关TE去抑制中可能具有时间依赖性功能。

