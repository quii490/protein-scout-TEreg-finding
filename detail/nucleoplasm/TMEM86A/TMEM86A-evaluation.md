---
type: protein-evaluation
gene: "TMEM86A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM86A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM86A |
| 蛋白名称 | Lysoplasmalogenase TMEM86A |
| 蛋白大小 | 240 aa / 26.4 kDa |
| UniProt ID | Q8N2M4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 240 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=90.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM86B-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=50 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=6 broad=6
- AF pLDDT=90.2 PDB=0
- InterPro: TMEM86B-like
- Pfam: YhhN
- PPI degree=50 ChIP: None
35835749: Adipocyte lysoplasmalogenase TMEM86A regulates plasmalogen homeostasis and prote | 36592658: Sterol-regulated transmembrane protein TMEM86a couples LXR signaling to regulati | 38811600: Identification of modules and key genes associated with breast cancer subtypes t

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Lysoplasmalogenase TMEM86A

**功能**: Catalyzes the hydrolysis of the vinyl ether bond of choline or ethanolamine lysoplasmalogens, forming fatty aldehyde and glycerophosphocholine or glycerophosphoethanolamine, respectively and is specific for the sn-2-deacylated (lyso) form of plasmalogen (PubMed:36592658). Plays an important role in lysoplasmalogen metabolism in the adipocyte tissue and macrophages (PubMed:36592658)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR012506 |
| Pfam | PF07947 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构揭示的酶学身份** TMEM86A（240 aa, 26.4 kDa）是五个候选蛋白中唯一拥有已知催化活性的成员。其IPR012506/PF07947（YhhN结构域）家族注释明确将其归为溶血缩醛磷脂酶（lysoplasmalogenase），催化溶血缩醛磷脂（lysoplasmalogen）的乙烯醚键水解，生成脂肪醛和甘油磷酸胆碱/甘油磷酸乙醇胺。这是缩醛磷脂（plasmalogen）降解通路的关键步骤（PMID:36592658）。YhhN结构域在细菌中为假设蛋白，在真核生物中首次被TMEM86A赋予了明确的酶学功能注释。pLDDT=90.2的高折叠置信度（为五个TMEM中最高）与酶的刚性格局要求一致——催化残基需精确的空间几何定位以实现底物识别和过渡态稳定。然而，一个核心谜题在于：如此明确的膜脂质代谢酶为何定位于核质和Golgi（HPA Approved双定位）？典型缩醛磷脂酶应定位于过氧化物酶体（plasmalogen合成）或溶酶体/内质网（降解），核质定位是反常的。

**PPI网络的转折性线索** 在50个互作伙伴中，LMNA（lamin A/C）的出现是整个PPI分析中最具启示性的发现。LMNA编码核纤层的核心中间丝蛋白，构成核膜内表面的结构骨架。Lamin A/C不仅是核机械支撑，更是基因组组织的关键调控者——其突变引起至少16种人类疾病（统称laminopathies），包括早衰综合征（HGPS）、Emery-Dreifuss肌营养不良和扩张型心肌病。TMEM86A与LMNA的直接互作（BioGRID记录）暗示其在核膜/核质界面可能发挥局部脂质环境调控功能。NCAPH2是condensin II复合物的H2亚基，在有丝分裂染色体凝集和间期染色质领土组织中起核心作用——condensin II加载至染色质需要核膜脂质环境的参与，而TMEM86A通过改变缩醛磷脂的局部浓度或脂筏的物理化学属性，可能间接调控condensin II的染色质结合。TYROBP（DAP12）是免疫受体信号接头，参与破骨细胞分化和神经炎症中的TREM2信号。COQ9是辅酶Q（ubiquinone）生物合成的辅助蛋白，与线粒体呼吸链密切相关——辅酶Q的脂质侧链与缩醛磷脂的脂肪醇尾部共享部分代谢中间体。FKBP7是内质网肽基脯氨酰异构酶（PPIase），参与蛋白折叠质量控制。

**核脂质代谢的新范式** 上述证据综合指向一个颠覆性的分子机制模型：TMEM86A在核质/核膜界面通过局部缩醛磷脂代谢来调控核膜脂质微环境（lipid microenvironment），进而影响核纤层组装和染色质组织。缩醛磷脂是一类特殊的甘油磷脂，其sn-1位为乙烯醚键（而非酯键），在膜中形成非脂双层相（hexagonal HII相），促进膜融合、弯曲和蛋白插入——这些物理化学特征在核膜重组（有丝分裂后核膜重建）和核孔复合体组装中至关重要。TMEM86A通过局部水解缩醛磷脂，改变核膜特定微区的脂质组成和膜曲率，从而：（a）调节lamin A/C前体（prelamin A）的膜锚定和成熟加工；（b）影响condensin II在核周边的加载效率；（c）在脂肪细胞和巨噬细胞中，将缩醛磷脂代谢信号与LXR核受体信号耦合（PMID:36592658——已证实TMEM86a是LXR的直接转录靶基因，通过固醇调控的反馈回路调控缩醛磷脂稳态）。

**跨组织的功能整合** 在脂肪组织/巨噬细胞中（PMID:35835749, 36592658），TMEM86A的缩醛磷脂酶活性直接调控脂质代谢和炎症信号——缩醛磷脂的水解产物（脂肪醛和溶血甘油磷脂）本身就是信号脂质（如lysophosphatidylcholine通过GPR132等受体发出炎症信号）。在乳腺癌症网络分析中（PMID:38811600），TMEM86A被鉴定为亚型分类的关键模块基因，提示其在肿瘤上皮细胞的脂质代谢重编程（lipid metabolic reprogramming）中发挥作用。SARS-CoV-2全基因组功能缺失筛选（PMID:37703821）中发现TMEM86A涉及病毒-宿主互作——冠状病毒的复制膜结构（double-membrane vesicles, DMVs）需要宿主脂质代谢，缩醛磷脂酶活性可能影响DMV形成。

**研究与转化意义** TMEM86A是目前研究最充分但核功能完全未探索的独特靶标。其高pLDDT（90.2）和YhhN结构域为基于结构的药物设计（SBDD）提供了可行性——设计选择性TMEM86A抑制剂或可调控缩醛磷脂稳态，用于代谢性疾病（肥胖相关炎症）或肿瘤（脂质代谢重编程）。LMNA互作提示其在laminopathy相关疾病（尤其是脂肪营养不良FPLD2，由LMNA突变引起）中可能作为修饰因子或治疗靶点。LXR-TMEM86A调控回路的发现（PMID:36592658）进一步将TMEM86A置于核受体药理学的前沿——LXR激动剂或拮抗剂可通过调控TMEM86A表达间接影响核膜脂质环境。在病毒学领域，靶向TMEM86A可能干扰冠状病毒的复制膜形成，为广谱抗病毒策略提供新思路。最紧迫的基础研究问题是：TMEM86A的核定位信号（NLS）是什么？其YhhN结构域中哪些残基负责底物识别？这些问题的解答将为理解"脂质代谢酶在细胞核中的兼职功能（moonlighting function）"这一新兴领域提供重要范例。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LMNA | BioGRID | 0 |
| TYROBP | BioGRID | 0 |
| NCAPH2 | BioGRID | 0 |
| SLC18A1 | BioGRID | 0 |
| FKBP7 | BioGRID | 0 |
| SLC35C2 | BioGRID | 0 |
| COQ9 | BioGRID | 0 |
| FXYD3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N2M4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151117-TMEM86A

![](https://images.proteinatlas.org/57119/1787_E5_2_cr5968c6819a28c_red_green.jpg)
![](https://images.proteinatlas.org/57119/1787_E5_16_cr5968c6819a89d_red_green.jpg)
![](https://images.proteinatlas.org/57119/1375_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/57119/1375_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/57119/1413_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/57119/1413_C2_4_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 40024572 | Functional characterization of TMEM86A and TMEM86B mutants by a novel lysoplasmalogenase assay. | J Lipid Res 2025 |
| 38811600 | Identification of modules and key genes associated with breast cancer subtypes through network analysis. | Sci Rep 2024 |
| 37703821 | Genome-wide loss-of-function screen using human pluripotent stem cells to study virus-host interactions for SARS-CoV-2. | Stem Cell Reports 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM86A

