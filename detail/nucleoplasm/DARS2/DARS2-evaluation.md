---
type: protein-evaluation
gene: "DARS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## DARS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DARS2 |
| 蛋白名称 | Aspartate--tRNA ligase, mitochondrial |
| 蛋白大小 | 645 aa / 73.6 kDa |
| UniProt ID | Q6PI48 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 645 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=92 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=89.2; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Aa-tRNA-synt_II; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=176 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Supported)
- PubMed strict=92 broad=137
- AF pLDDT=89.2 PDB=1
- InterPro: Aa-tRNA-synt_II; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL
- Pfam: GAD; tRNA-synt_2; tRNA_anti-codon
- PPI degree=176 ChIP: None
39039092: Targeted degradation of extracellular mitochondrial aspartyl-tRNA synthetase mod | 40814755: Biallelic Variants in the DARS2 Gene as a Novel Cause of Axonal Charcot-Marie-To | 40948401: AAV9-DARS2 Gene Therapy Rescues Phenotype in Leukoencephalopathy with Brainstem 

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Aspartate--tRNA ligase, mitochondrial

**功能**: Catalyzes the attachment of aspartate to tRNA(Asp) in a two-step reaction: aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004364 |
| InterPro | IPR006195 |
| InterPro | IPR045864 |
| InterPro | IPR004524 |
| InterPro | IPR047089 |
| InterPro | IPR002312 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EARS2 | STRING | 929 |
| AARS | STRING | 907 |
| YARS | STRING | 898 |
| YARS2 | STRING | 881 |
| EIF2AK4 | STRING | 826 |
| KARS | STRING | 807 |
| IARS | STRING | 807 |
| EIF2AK1 | STRING | 802 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6PI48-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000117593-DARS2

![](https://images.proteinatlas.org/26528/213_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/26528/213_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/26528/212_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/26528/212_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/26528/214_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/26528/214_G2_2_red_green.jpg)

### 深度机制分析

**结构域架构**：DARS2（645 aa，73.6 kDa）是线粒体天冬氨酰-tRNA合成酶（AspRS），属于Class II aaRS家族（IPR004364/Aa-tRNA-synt_II）。其模块化架构含三个功能区：N端GAD（Glu-tRNAGln amidotransferase domain）样结构域（约1-80 aa）——对应IPR047089，可能参与tRNA反密码子结合域的变构调控；核心催化结构域（约80-500 aa，IPR006195/aa-tRNA-synth_II）——采用Class II合成酶特征性7条反平行β-链折叠（motif 1/2/3），活性位点含特征性motif 1（GΦxxGxxP）识别ATP，motif 2（FRxE/D）和motif 3（GΦGΦGΦER）识别tRNA acceptor茎端；C端反密码子结合结构域（约500-645 aa，IPR002312）——采用OB-fold（寡核苷酸/寡糖结合折叠）识别tRNA^Asp的反密码子（QUC/GUC变异）。AlphaFold pLDDT=89.2（本批次最高之一），实验PDB=1。HPA定位显示Mitochondria; Nucleoplasm（Supported）。

**PPI互作网络解读**：PPI degree=176，STRING互作网络紧密围绕线粒体翻译装置：EARS2（GluRS, STRING 929）——与DARS2在线粒体中共同负责tRNA氨基酰化，可能形成线粒体aaRS多酶超复合体；AARS（AlaRS, STRING 907）和YARS/YARS2（TyrRS, STRING 898/881）——线粒体和胞质aaRS的同工酶互作簇；KARS（LysRS, STRING 807）和IARS（IleRS, STRING 807）——进一步支持线粒体aaRS复合体的组织模型；EIF2AK4/GCN2（STRING 826）和EIF2AK1/HRI（STRING 802）——综合应激反应（ISR）激酶，由不带电荷的tRNA积累激活，磷酸化eIF2α抑制全局翻译同时选择性促进ATF4等应激基因的翻译。

**结构解读**：催化域的特征性7条反平行β-链折叠形成中央β-片层，活性位点位于片层一面。ATP采用'bent'构象结合——腺嘌呤环堆积于motif 1的Phe/Tyr残基上，三磷酸被motif 2的Arg和Mg²⁺离子配位。tRNA^Asp的受体茎（acceptor stem）在活性位点处识别：Class II合成酶从大沟侧接近受体茎，与Class I（小沟侧接近）形成对比。反密码子结合域的OB-fold由5条β-链形成闭合β-桶，识别GUC反密码子的三个碱基——其中C35（反密码子第二位）和G73（discriminator base）是AspRS识别tRNA^Asp特异性的主要决定因素。

**机制模型**：（1）线粒体经典功能：DARS2催化Asp + ATP → Asp-AMP + PPi（第一步腺苷酰化），Asp-AMP + tRNA^Asp → Asp-tRNA^Asp + AMP（第二步氨基酰化），为线粒体蛋白合成提供Asp-tRNA^Asp；（2）核质定位（Nucleoplasm Supported）：线粒体aaRS的核输入是新兴认知——DARS2可能通过N端含碱性残基富集区的隐蔽MTS（线粒体靶向信号）和NLS（核定位信号）的双重定位信号实现双重靶向。在核质中，DARS2可能参与核编码线粒体蛋白mRNA的翻译调控，或作为细胞器应激的核内信号传感器；（3）EIF2AK4/GCN2互作链将线粒体氨基酰化状态耦合至全局翻译程序——不带电荷的tRNA^Asp结合DARS2的活性位点诱导构象变化，释放的DARS2可能通过GCN2激酶激活ISR通路（PMID:39039092揭示了DARS2的细胞外靶向降解新功能，扩展了其功能范式）。

**TE调控展望**：DARS2不直接参与TE调控。但ISR通路（通过EIF2AK4/GCN2）的激活可导致翻译重编程——包括特定mRNA（如ATF4, CHOP, GADD34）的选择性翻译，而一些含有uORF（上游开放阅读框）的TE衍生转录本在ISR条件下的翻译效率可能改变。此外，线粒体功能障碍引起的逆行信号（retrograde signaling）可改变核基因组的染色质状态，包括特定TE家族（如SINE/Alu, 线粒体应激响应元件MOTEs）的去抑制。但这些机制过于间接，DARS2作为TE调控靶标不建议优先考虑。

### PubMed 文献

**PubMed count: 138**

| 42367688 | Vocal Cord Paresis and Neuropathic Pain in Infantile Leukoencephalopathy with Brainstem and Spinal Cord Involvement and  | Case Rep Neurol 2026 |
| 42164352 | DARS2 serves as an independent prognostic factor and participates in multiple biological processes in bladder urothelial | Transl Androl Urol 2026 |
| 41924482 | The iron-sulfur accelerator YgfZ modulates genome-wide IHF-binding dynamics to regulate replication initiation in Escher | Front Microbiol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DARS2

