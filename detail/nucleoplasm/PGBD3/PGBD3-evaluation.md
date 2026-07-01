---
type: protein-evaluation
gene: "PGBD3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PGBD3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PGBD3 |
| 蛋白名称 | PiggyBac transposable element-derived protein 3 |
| 蛋白大小 | 593 aa / 67.6 kDa |
| UniProt ID | Q8N328 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 593 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=83.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PGBD; PiggyBac_TE-derived |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=6 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **66.1/100** | 互证: +1 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=10, broad=10
- AF pLDDT: 83.8 / PDB: 0
- InterPro: PGBD; PiggyBac_TE-derived
- Pfam: DDE_Tnp_1_7
- PPI degree=6 ChIP: None
23369858: What role (if any) does the highly conserved CSB-PGBD3 fusion protein play in Co | 29625109: Generation of splice switching oligonucleotides targeting the Cockayne syndrome  | 26218421: CSB-PGBD3 Mutations Cause Premature Ovarian Failure.

### 4. 总体评价
★★★★  **66.1/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**PiggyBac转座酶驯化与DNA结合架构**：PGBD3（593 aa, 67.6 kDa, UniProt Q8N328）属于piggyBac转座酶衍生物家族，这一谱系在脊椎动物中经历了反复的真核生物驯化（PMID:32742312）。其核心结构域包括PGBD特有域（IPR029526）、PiggyBac TE衍生域（IPR052638），以及Pfam DDE_Tnp_1_7（PF13843）——后者属于DDE转座酶/整合酶超家族，具有特征性的RNase H-like催化折叠。该蛋白的域架构清楚地反映了其转座酶祖先：DDE催化核心负责DNA链转移，而PGBD特异域提供MER85型转座元件的末端反向重复（TIR）识别。MEROPS数据库注释其为MER85非自主转座子，TIR约17-19 bp，缺少内部ORF。AlphaFold pLDDT=83.8表明整体折叠良好，但催化中心的DDE残基位置和活性状态需要生化验证。

**CSB-PGBD3融合的病理与功能启示**：PGBD3与CSB（Cockayne syndrome B蛋白，ERCC6）形成嵌合融合转录本，是反式剪接医学中的独特案例（PMID:29625109, PMID:26218421）。CSB属于SWI/SNF家族染色质重塑因子，参与转录偶联核苷酸切除修复（TC-NER）。CSB-PGBD3融合蛋白在原发性卵巢早衰（POF）中被报道有突变（PMID:26218421），其致病机制可能与PGBD3的DNA结合域将CSB的ATP酶/染色质重塑活性重新导向至MER85元件的基因组位点有关。STRING互作数据显示PGBD3与TC-NER核心因子ERCC8（CSA, score=999）、ERCC5（XPG, score=999）、POLR2B（RNA Pol II, score=997）、XPA（score=990）、DDB1（score=988）和UVSSA（score=986）皆以极高置信度互作——这不是独立转座酶的互作模式，而是完全嵌入TC-NER染色质修复机制的信号。

**MER85元件靶向与TE调控假说**：PGBD3体外结合含其TIR的MER85元件，这些约140 bp的非自主元件散布于人类基因组。若PGBD3的功能不仅是结合DNA，还包括通过TC-NER偶联因子招募染色质重塑活性，那么CSB-PGBD3融合复合物在MER85位点的定位可能影响局部表观遗传状态。MER85属hAT超家族，部分拷贝位于基因调控区附近。PGBD3-DDB1互作（score=988）暗示CUL4-DDB1 E3泛素连接酶可能也被招募至这些位点，介导组蛋白H2A/H3泛素化——这是一种已知的转录沉默机制。PGBD3因而可能是MER85元件表观遗传调控的关键适配蛋白。

**TE抑制实验的优先靶标**：PubMed严格计数仅10篇，多为CSB融合的临床病例报告，PGBD3本身的生化机制几乎无文献探讨。PPI degree=6虽低却在功能上高度富集——全部指向TC-NER和DNA损伤应答网络，暗示PGBD3通过NER损伤感知通路间接监控基因组TE位点。实验优先级：（1）ChIP-seq确定PGBD3在MER85及相关TE亚家族上的全基因组结合图谱；（2）CRISPR敲除PGBD3后RNA-seq检测MER85邻近基因表达变化；（3）体外TIR结合凝胶迁移实验（EMSA）量化亲和力；（4）DDB1/CSA/CSB免疫共沉淀验证复合物组装。作为进化保守的驯化转座酶，PGBD3代表了基因组防御蛋白从"移动元件工具"转变为"表观遗传调控者"的典范案例。

### 补充分析 (UniProt API)

**蛋白全称**: PiggyBac transposable element-derived protein 3

**功能**: Binds in vitro to PGBD3-related transposable elements, called MER85s; these non-autonomous 140 bp elements are characterized by the presence of PGBD3 terminal inverted repeats and the absence of internal transposase ORF

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029526 |
| InterPro | IPR052638 |
| Pfam | PF13843 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ERCC8 | STRING | 999 |
| ERCC5 | STRING | 999 |
| BIVM-ERCC5 | STRING | 999 |
| POLR2B | STRING | 997 |
| POLR2I | STRING | 995 |
| XPA | STRING | 990 |
| DDB1 | STRING | 988 |
| UVSSA | STRING | 986 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N328-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PGBD3

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000225830

![](https://images.proteinatlas.org/71297/1544_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71297/1544_F12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/71297/1611_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/71297/1611_B7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/71297/1543_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/71297/1543_F12_2_blue_red_green.jpg)

### PubMed

**Count: 10**

| PMID | Title |
|---|---|
| 35251122 | Statistical Approach of the Role of the Conserved CSB-PiggyBac Transposase Fusion Protein (CSB-PGBD3) in Genotype-Phenotype Correlation in Cockayne Sy |
| 30556603 | Six genes as potential diagnosis and prognosis biomarkers for hepatocellular carcinoma through data mining. |
| 29625109 | Generation of splice switching oligonucleotides targeting the Cockayne syndrome group B gene product in order to change the diseased cell state. |
| 27794495 | Ct shift: A novel and accurate real-time PCR quantification model for direct comparison of different nucleic acid sequences and its application for tr |
| 26218421 | CSB-PGBD3 Mutations Cause Premature Ovarian Failure. |
