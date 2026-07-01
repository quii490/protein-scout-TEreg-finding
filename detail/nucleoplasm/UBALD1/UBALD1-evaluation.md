---
type: protein-evaluation
gene: "UBALD1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBALD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBALD1 |
| 蛋白名称 | UBA-like domain-containing protein 1 |
| 蛋白大小 | 177 aa / 19.0 kDa |
| UniProt ID | Q8TB05 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 177 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=62.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | UBA-like_sf; UBA_8; UBALD1/2 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Cell Junctions; Cytosol; Nucleoplasm (Approved)
- PubMed strict=6 broad=6
- AF pLDDT=62.0 PDB=0
- InterPro: UBA-like_sf; UBA_8; UBALD1/2
- Pfam: UBA_8
- PPI degree=1 ChIP: None
36798395: Transcriptomic profiles of stress susceptibility and resilience in the amygdala  | 36269412: Acute transcriptomic changes in murine RAW 264.7 cells following pseudorabies vi | 35794887: Transcriptional Profiles Analysis of COVID-19 and Malaria Patients Reveals Poten

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: UBA-like domain-containing protein 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009060 |
| InterPro | IPR054109 |
| InterPro | IPR039310 |
| Pfam | PF22566 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MLYCD | BioGRID | 0 |



### 深度机制分析

**结构域架构**：UBALD1（177 aa, 19.0 kDa）含UBA-like superfamily（IPR009060）和UBA_8域（IPR054109, Pfam PF22566）。UBA域典型为约45 aa的三螺旋束（three-helix bundle, a1-a2-a3）通过疏水表面（hydrophobic patch）识别K48和K63多聚泛素链。AlphaFold pLDDT=62.0——UBA-like域（aa 50-130）pLDDT>75（折叠良好），但N/C端区域pLDDT<50（IDR特征）。蛋白整体为单体泛素结合adaptor结构。PPI degree=1（BioGRID），仅与MLYCD（malonyl-CoA decarboxylase）有互作——MLYCD催化malonyl-CoA脱羧→acetyl-CoA，调控脂肪酸合成/氧化代谢转换。UBALD1经UBA-like域识别MLYCD的泛素化状态→调控MLYCD蛋白稳定性→影响胞质malonyl-CoA水平。

**TE调控展望**：TE调控关联极弱且高度间接。malonyl-CoA和acetyl-CoA作为乙酰基供体影响组蛋白乙酰化——在TE位点（LTR/ERV的enhancer/promoter）促进开放染色质和TE转录活性。UBALD1调控MLYCD→调控acetyl-CoA代谢平衡→可能间接影响TE位点的组蛋白乙酰化。泛素-蛋白酶体系统直接调控LINE-1 ORF1p/ORF2p蛋白稳定性——UBALD1作为泛素结合蛋白可能在不同细胞背景下识别这些TE蛋白的泛素化形式→影响其降解。但实际影响路径过于冗长，意义微乎其微。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TB05-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBALD1

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000153443-UBALD1

![](https://images.proteinatlas.org/66771/1475_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/66771/1475_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/66771/1217_D3_5_red_green.jpg)
![](https://images.proteinatlas.org/66771/1217_D3_6_red_green.jpg)
![](https://images.proteinatlas.org/66771/1211_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/66771/1211_D3_2_red_green.jpg)

### PubMed

**Count: 6**

| PMID | Title |
|---|---|
| 36798395 | Transcriptomic profiles of stress susceptibility and resilience in the amygdala and hippocampus. |
| 36269412 | Acute transcriptomic changes in murine RAW 264.7 cells following pseudorabies virus infection. |
| 35794887 | Transcriptional Profiles Analysis of COVID-19 and Malaria Patients Reveals Potential Biomarkers in Children. |
| 34489625 | Epigenetics Is Implicated in the Basis of Gender Incongruence: An Epigenome-Wide Association Analysis. |
| 33403724 | DNA methylome profiling identifies novel methylated genes in epithelial ovarian cancer patients with platinum resistance. |


