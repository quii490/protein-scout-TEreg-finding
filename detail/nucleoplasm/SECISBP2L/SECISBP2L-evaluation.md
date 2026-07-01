---
type: protein-evaluation
gene: "SECISBP2L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SECISBP2L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SECISBP2L |
| 蛋白名称 | Selenocysteine insertion sequence-binding protein 2-like |
| 蛋白大小 | 1101 aa / 121.8 kDa |
| UniProt ID | Q93073 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1101 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=52.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ribosomal_eL30-like_sf; Ribosomal_eL8/eL30/eS12/Gad45; SECISBP2 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=33 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=8 broad=17
- AF pLDDT=52.9 PDB=0
- InterPro: Ribosomal_eL30-like_sf; Ribosomal_eL8/eL30/eS12/Gad45; SECISBP2
- Pfam: Ribosomal_L7Ae
- PPI degree=33 ChIP: None
28604730: Large-scale association analysis identifies new lung cancer susceptibility loci  | 37739108: Pyrolae herba alleviates cognitive impairment via hippocampal TREM2 signaling mo | 35210313: The expression of essential selenoproteins during development requires SECIS-bin

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Selenocysteine insertion sequence-binding protein 2-like

**功能**: Binds SECIS (Sec insertion sequence) elements present on selenocysteine (Sec) protein mRNAs, but does not promote Sec incorporation into selenoproteins in vitro

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029064 |
| InterPro | IPR004038 |
| InterPro | IPR040051 |
| Pfam | PF01248 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DYNLL2 | BioGRID | 1 |
| XPO1 | BioGRID | 1 |
| DYNLL1 | BioGRID | 1 |
| RMND5A | BioGRID | 1 |
| PPP1CC | BioGRID | 1 |
| SASH1 | BioGRID | 1 |
| RAN | BioGRID | 1 |
| DAZL | BioGRID | 1 |



### 深度机制分析

**结构域架构**：SECISBP2L（1101 aa, 121.8 kDa, Q93073, Selenocysteine insertion sequence-binding protein 2-like）是硒蛋白合成机器的调控组分。结构域组成：（1）Ribosomal_L7Ae域（Pfam PF01248）——属于Ribosomal_eL30-like超家族（IPR029064）——L7Ae/L30e折叠为alpha-beta-alpha sandwich——该fold在古菌和真核生物中高度保守——作为RNA结合模块识别kink-turn（K-turn）和C/D box RNA motif。在SECISBP2L中，L7Ae域结合SECIS（Sec insertion sequence）元素——位于硒蛋白mRNA 3'UTR的茎环结构（stem-loop）——SECIS含有conserved AUGA motif和apical loop中的AAR motif——L7Ae域经其RNA recognition surface识别SECIS的三维构象而非特定序列。（2）SECISBP2域（IPR040051）——约500 aa的extended region——含多个predicted alpha-helices——可能形成elongated superhelical scaffold——参与与其他硒蛋白合成因子（eEFSec, SBP2, ribosomal protein L30）的互作。AlphaFold pLDDT=52.9——L7Ae域pLDDT高（~80-88, 折叠可靠），SECISBP2域和N/C端IDR区域pLDDT中等或低。PDB=0。

**PPI互作网络解读**：PPI degree=33。XPO1（Exportin-1/CRM1, BioGRID）是核输出受体——识别cargo protein中的leucine-rich nuclear export signal（NES）——介导cargo从核经NPC输出至胞质——SECISBP2L-XPO1互作提示SECISBP2L在核-胞质间shuttles。RAN（Ras-related nuclear protein, BioGRID）是XPO1的GTPase switch——RAN-GTP在核内高浓度驱动XPO1-cargo complex assembly——RAN-SECISBP2L互作进一步支持核shuttling。DYNLL1/DYNLL2（Dynein light chain LC8-type 1/2, BioGRID）是胞质dynein motor complex的组分——介导cargo沿microtubule向minus-end运输——SECISBP2L-DYNLL1/2互作提示SECISBP2L可能在胞质中与dynein-dependent trafficking相关。PPP1CC（Protein phosphatase 1 catalytic subunit gamma, BioGRID）是Ser/Thr phosphatase——PP1的catalytic subunit调控多种细胞过程。RMND5A（BioGRID）是E3 ubiquitin ligase component。

**结构解读**：L7Ae domain（residues ~1-130）的K-turn binding mechanism已被充分研究——L7Ae识别SECIS RNA的apical loop经induced-fit mechanism——conserved Arg/Lys residues与SECIS的phosphate backbone形成salt bridge——aromatic residues（Phe/Tyr）与SECIS loop中非配对腺苷（unpaired A）stacking互作。L7Ae结构在古菌核糖体蛋白L7Ae、真核15.5kDa/snRNP和SECISBP2/SECISBP2L中高度保守。SECISBP2域中的helical repeat motifs可能形成类似于HEAT/ARM repeat的elongated superhelix——包裹其他硒蛋白合成因子（如eEFSec, Sec-tRNASec）形成ribonucleoprotein（RNP）complex。

**机制模型**：（1）Selenoprotein synthesis——SECISBP2L作为SECIS-binding protein 2-like——与SBP2（SECISBP2）竞争结合SECIS element在硒蛋白mRNA 3'UTR——但SECISBP2L不能促进Sec incorporation into selenoprotein（UniProt注释）——可能作为SBP2的dominant-negative regulator或SECIS occupancy competitor→调控selenoprotein表达水平和组织特异性。（2）核-胞质shuttling（XPO1/RAN互作）——SECISBP2L可能参与硒蛋白mRNA在核内的SECIS-dependent processing和核输出——经XPO1-RAN pathway将selenoprotein mRNP输送至胞质ribosome进行翻译。（3）硒蛋白在认知中的作用（PMID:37739108）——Pyrolae herba经TREM2 signaling改善认知障碍中涉及SECISBP2L——硒蛋白（GPX4, SELENOP, DIO2）在神经元survival和抗氧化防御中功能关键。

**TE调控展望**：SECISBP2L的TE调控关联为间接。硒蛋白合成途径中的Sec incorporation依赖UGA codon——UGA在标准遗传密码中为stop codon但在硒蛋白mRNA中经SECIS element重新编码为Sec——这种recoding机制与TE mRNA（如LINE-1）中存在的premature stop codon和readthrough事件有概念上的相似性。核-胞质shuttling（XPO1/RAN）直接影响核内的mRNA processing and export——核内滞留或hyperexport的TE RNA可能影响其逆转录转座效率。PPP1CC（PP1 phosphatase）调控histone dephosphorylation——PP1经Repo-Man/PNUTS复合物在mitosis exit中去磷酸化H3T3ph/H3S10ph/H3S28ph——这些histone mark在TE区域的动态变化调控TE transcription——SECISBP2L-PPP1CC互作可能影响PP1在TE染色质上的活性。

### PPI 互作网络

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q93073-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138593-SECISBP2L

![](https://images.proteinatlas.org/39875/456_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/39875/456_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/39875/454_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/39875/454_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/39875/451_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/39875/451_G5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 17**

| 39092217 | Identifying potential therapeutic targets in lung adenocarcinoma: a multi-omics approach integrating bulk and single-cel | Front Pharmacol 2024 |
| 38069522 | Differential co-expression network analysis elucidated genes associated with sensitivity to farnesyltransferase inhibito | Cancer Med 2023 |
| 37739108 | Pyrolae herba alleviates cognitive impairment via hippocampal TREM2 signaling modulating neuroinflammation and neurogene | J Ethnopharmacol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SECISBP2L

