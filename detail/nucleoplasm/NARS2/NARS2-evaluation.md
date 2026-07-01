---
type: protein-evaluation
gene: "NARS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NARS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NARS2 |
| 蛋白名称 | Asparaginyl-tRNA synthetase |
| 蛋白大小 | 477 aa / 54.1 kDa |
| UniProt ID | Q96I59 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 477 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=45 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=91.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Aa-tRNA-synt_II; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=117 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Mitochondria; Nucleoplasm (Supported)
- PubMed strict=45 broad=68
- AF pLDDT=91.4 PDB=0
- InterPro: Aa-tRNA-synt_II; aa-tRNA-synth_II; aa-tRNA-synth_II/BPL/LPL
- Pfam: tRNA-synt_2; tRNA_anti-codon
- PPI degree=117 ChIP: None
26425749: Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. | 34374940: Novel phenotype and genotype spectrum of NARS2 and literature review of previous | 38310242: Novel NARS2 variants in a patient with early-onset status epilepticus: case stud

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Asparaginyl-tRNA synthetase

**功能**: Mitochondrial aminoacyl-tRNA synthetase that catalyzes the specific attachment of the asparagine amino acid (aa) to the homologous transfer RNA (tRNA), further participating in protein synthesis (PubMed:25385316). The reaction occurs in a two steps: asparagine is first activated by ATP to form Asn-AMP and then transferred to the acceptor end of tRNA(Asn) (Probable)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004364 |
| InterPro | IPR006195 |
| InterPro | IPR045864 |
| InterPro | IPR004522 |
| InterPro | IPR002312 |
| InterPro | IPR012340 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| YARS | STRING | 956 |
| YARS2 | STRING | 926 |
| EARS2 | STRING | 913 |
| MARS | STRING | 889 |
| TARSL2 | STRING | 887 |
| AARS | STRING | 881 |
| IARS | STRING | 871 |
| SARS | STRING | 871 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96I59-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137513-NARS2

![](https://images.proteinatlas.org/26793/2267_E1_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/26793/2267_E1_187_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137513-NARS2

![](https://images.proteinatlas.org/26793/2267_E1_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/26793/2267_E1_187_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137513-NARS2

![](https://images.proteinatlas.org/26793/2267_E1_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/26793/2267_E1_187_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 68**

| 42353806 | Multimodal Sequencing and Reanalysis Approaches to End the Diagnostic Odyssey of Individuals with Suspected Rare Monogen | Genes (Basel) 2026 |
| 42284239 | Neonatal Diabetes Mellitus in a Resource-Limited Setting: Clinical Spectrum, Genetic Heterogeneity, Impact of Malnutriti | Horm Res Paediatr 2026 |
| 41809011 | A universal regulatory mechanism for prevention of replication restart from RNA:DNA hybrids. | bioRxiv 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NARS2


### 深度机制分析

NARS2（Asparaginyl-tRNA synthetase, mitochondrial）是线粒体氨酰tRNA合成酶家族（aaRS-II类）的成员，其结构特征为三类保守结构域的组合：氨酰tRNA合成酶II类催化核心（InterPro:IPR006195, aa-tRNA-synth_II）、tRNA反密码子识别域（IPR045864, aa-tRNA-synth_II/BPL/LPL）以及N端附加结构域（IPR004364, Aa-tRNA-synt_II）。Pfam注释为tRNA-synt_2（PF00152, 催化结构域）和tRNA_anti-codon（PF01406, 反密码子绑合域）。AlphaFold预测结构整体良好（pLDDT=91.4），但该值反映的是全链均值，催化核心的置信度通常高于配体识别区段。

NARS2催化的两步反应是天冬酰胺-tRNA氨酰化的经典机制：第一步，天冬酰胺（Asn）被ATP激活形成Asn-AMP中间体，释放焦磷酸；第二步，活化的天冬酰胺从Asn-AMP转移至同源tRNA^(Asn)的3'端腺苷（PubMed:25385316）。这一反应是线粒体蛋白质合成的核心步骤——只有正确加载了天冬酰胺的tRNA^(Asn)才能进入线粒体核糖体参与翻译延伸。PPI互作网络（degree=117）进一步确认了NARS2在氨酰tRNA合成酶超复合体（MSC, multi-synthetase complex）中的嵌入：STRING高分互作伙伴包括YARS（score=956, 酪氨酰tRNA合成酶）、YARS2（score=926, 线粒体型）、EARS2（score=913, 线粒体谷氨酰tRNA合成酶）、MARS（score=889, 甲硫氨酰tRNA合成酶）和AARS/IARS/SARS（各种胞质aaRS酶），说明胞质和线粒体aaRS在空间和功能上高度关联。

NARS2的亚细胞定位为Cytosol-Mitochondria-Nucleoplasm三重分布（HPA Supported），核质定位的HPA信号可能反映了新合成的NARS2在进入线粒体前的胞质/核质转运中间态，或核内氨基酸感受（amino acid sensing）的非经典功能。aaRS-II类蛋白在特定条件下（如氧化应激、营养剥夺）可从线粒体转位至细胞核执行信号传导功能——这一"兼职功能"（moonlighting function）已在线粒体aaRS家族多名成员（如MARS, EARS2, YARS2）中被证实。

NARS2的临床关联集中在Leigh综合征及其谱系疾病。PubMed文献（PMID:26425749, PMID:34374940, PMID:38310242）统一指向NARS2双等位基因突变导致常染色体隐性线粒体脑肌病——表型从新生儿期致死性线粒体脑病到儿童期起病的癫痫性线粒体病不等。NARS2突变的功能后果是天冬氨酰化tRNA的充电效率下降，直接影响线粒体编码的呼吸链亚基（如MT-ND1至MT-ND6和MT-CO1至MT-CO3）的翻译，继而导致氧化磷酸化缺陷和ATP耗竭。综合来看，NARS2的深度机制模型为：aaRS-II催化核心+tRNA反密码子识别→线粒体Asn-tRNA^(Asn)充电→线粒体翻译维持→呼吸链复合体组装→能量代谢→细胞存活。该蛋白的核心功能在线粒体翻译，核质定位信号可能反映兼职功能，但直接参与TE调控的潜力极低（TE调控评估：极低）。



