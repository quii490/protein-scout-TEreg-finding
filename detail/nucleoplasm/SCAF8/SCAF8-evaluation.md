---
type: protein-evaluation
gene: "SCAF8"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## SCAF8 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SCAF8 |
| 蛋白名称 | SR-related and CTD-associated factor 8 |
| 蛋白大小 | 1271 aa / 140.5 kDa |
| UniProt ID | Q9UPN6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1271 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=16 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=51.4; PDB=9 |
| 调控结构域 | 4/10 | x2 | 8.0 | CID_dom; ENTH_VHS; Nucleotide-bd_a/b_plait_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=68 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
HPA: Nucleoplasm (Enhanced)
PubMed: strict=16, broad=24
AF pLDDT: 51.4  PDB: 9
InterPro: CID_dom; ENTH_VHS; Nucleotide-bd_a/b_plait_sf
Pfam: CID; RRM_1
PPI degree: 68  ChIP: None
**Papers**: 31104839: SCAF4 and SCAF8, mRNA Anti-Terminator Proteins. | 36590686: Elongation factor-specific capture of RNA polymerase II complexes. | 33160353: Genomic analysis of circular RNAs in heart.

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

SCAF8（SR-related and CTD-associated Factor 8）是此批25个核蛋白中核定位证据最强的蛋白之一（Nucleoplasm Enhanced, 得分8/10），也是功能定义最精确的核内调控因子。1271 aa的巨大分子量（140.5 kDa）容纳了多个功能结构域：N端CID结构域（CTD-Interacting Domain, Pfam CID, InterPro IPR006569）是RNA聚合酶II大亚基（POLR2A）C端结构域（CTD）磷酸化形式的直接结合模块；中间含有ENTH/VHS超家族折叠（InterPro IPR008942）；C端含有两个RRM型RNA识别基序（Pfam RRM_1, InterPro IPR000504）和一个核苷酸结合α/β折叠结构域（InterPro IPR012677）。这种多结构域串联排布使SCAF8能够在RNA聚合酶II转录的多个层面同时执行功能。

SCAF8的PPI网络是其核内功能的最有力佐证。STRING网络中与PCF11的极高评分互作（STRING=964）尤为关键——PCF11是切割和聚腺苷酸化因子（CPA复合物）的核心组分，直接识别RNA聚合酶II CTD的Ser2磷酸化并介导转录终止和3'端加工。与SETX（senataxin, STRING=948）的互作则连接SCAF8与转录终止和R-loop解旋。与SSU72（STRING=784）、CPSF3（STRING=778）、CPSF2（STRING=745）、CPSF7（STRING=732）和WDR33（STRING=769）等一系列CPA复合物组分的紧密互作将SCAF8定位在RNA 3'端加工的核心枢纽。与RPRD2（RNA聚合酶II相关蛋白2, STRING=757）的互作进一步巩固了其在转录调控中的中心地位。

SCAF8的核心功能机制已在开创性研究中精准阐明。PMID:31104839首次揭示了SCAF4和SCAF8作为mRNA反终止因子的分子功能——它们通过结合磷酸化POLR2A CTD并随后结合新生RNA上早期poly(A)位点上游序列，抑制早期poly(A)位点的使用，从而防止截短的非功能性蛋白产物的积累。这一"anti-terminator"机制在基因组完整性维护中具有基础性意义，因为早期poly(A)位点的异常激活可产生显性负性蛋白截短体或毒性多肽。PMID:36590686通过延伸因子的特异性捕获进一步证实SCAF8在RNA聚合酶II复合物中的直接作用。最新研究（PMID:42288759）揭示了SCAF8的一个全新调控维度——PRKN（Parkin）介导SCAF8的泛素化降解，降低KLF5 mRNA的稳定性及其对EFNA5的转录激活，连接了线粒体自噬蛋白Parkin与核内转录终止调控。

SCAF8的pLDDT仅为51.4（得分7/10），但这极可能不反映真实的结构无序，而是因为1271 aa的巨大蛋白中多个结构域之间的柔性linker区域拉低了整体预测均值。PDB数据库中已有9个实验结构，主要覆盖CID结构域和RRM结构域的独立结构。16篇PubMed文献（得分9/10）虽然数量不多，但每一篇都质量极高。作为明确的核内反终止因子，SCAF8在核质Enhanced定位背景下的功能延伸——如其是否调控非编码RNA或增强子RNA（eRNA）的poly(A)位点选择——代表了mRNA加工领域的一个重要前沿问题。

### 补充分析 (UniProt API)

**蛋白全称**: SR-related and CTD-associated factor 8

**功能**: Anti-terminator protein required to prevent early mRNA termination during transcription (PubMed:31104839). Together with SCAF4, acts by suppressing the use of early, alternative poly(A) sites, thereby preventing the accumulation of non-functional truncated proteins (PubMed:31104839). Mechanistically, associates with the phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit (POLR2A), and subsequently binds nascent RNA upstream of early polyadenylation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006569 |
| InterPro | IPR008942 |
| InterPro | IPR012677 |
| InterPro | IPR035979 |
| InterPro | IPR000504 |
| InterPro | IPR034370 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCF11 | STRING | 964 |
| SETX | STRING | 948 |
| SSU72 | STRING | 784 |
| CPSF3 | STRING | 778 |
| WDR33 | STRING | 769 |
| RPRD2 | STRING | 757 |
| CPSF2 | STRING | 745 |
| CPSF7 | STRING | 732 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UPN6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000213079-SCAF8

![](https://images.proteinatlas.org/35601/593_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/35601/593_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/35601/594_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/35601/594_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/35601/596_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/35601/596_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/35602/436_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35602/436_B6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 42288759 | PRKN mediates the ubiquitination of SCAF8 to reduce the mRNA stability of KLF5 and its transcriptional activation of EFN | Cell Mol Biol Lett 2026 |
| 41804605 | 5-Aza-Cytidine Enhances Terminal Polyadenylation Site Usage for Full-Length Transcripts in Cells. | Genes Cells 2026 |
| 41361092 | (1)H, (13)C, and (15)N resonance assignments and solution structure of the CID domain of SR-related- and CTD-associated  | Biomol NMR Assign 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SCAF8

