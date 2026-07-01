---
type: protein-evaluation
gene: "SH3BP5L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3BP5L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3BP5L |
| 蛋白名称 | SH3 domain-binding protein 5-like |
| 蛋白大小 | 393 aa / 43.5 kDa |
| UniProt ID | Q7L8J4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 393 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=0.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SH3BP5 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=32 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm; Vesicles (Approved)
- PubMed strict=4 broad=6
- AF pLDDT=0.0 PDB=0
- InterPro: SH3BP5
- Pfam: SH3BP5
- PPI degree=32 ChIP: None
39051763: RAB22A sorts epithelial growth factor receptor (EGFR) from early endosomes to re | 34128958: Tankyrase regulates epithelial lumen formation via suppression of Rab11 GEFs. | 41623179: SH3BP5L triggers the RAB11A-regulated integrin recycling network implicated in b

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SH3BP5L（SH3 domain-binding protein 5-like）是393个氨基酸的RAB11A特异性的鸟苷酸交换因子（GEF），在结构与功能上属于SH3BP5（Sab）蛋白家族。其核心功能结构域SH3BP5（IPR007940/PF05276）被预测为卷曲螺旋（coiled-coil）折叠——这一结构通常介导同源二聚化和RAB GTPase识别。SH3BP5L通过催化RAB11A上GDP/GTP的交换，激活RAB11A并促进其招募下游效应蛋白，驱动回收内体（recycling endosome）的膜运输。AlphaFold预测pLDDT为0.0，这是一个不寻常的极低值，可能反映该蛋白的极高程度无序性（IDP）或结构域边界注释错误。

HPA Approved的Golgi apparatus、Nucleoplasm及Vesicles三重定位提示SH3BP5L可能在细胞内膜系统与核质之间动态循环。经典的RAB11A效应因子（如RAB11FIP家族）通常定位於回收内体和反式高尔基网络——SH3BP5L的高尔基体定位与此一致，但其核质定位暗示了一种超越典型膜运输的核内功能。PPI网络（degree=32）中与TNKS/TNKS2（端锚聚合酶1/2，BioGRID评分=0）的互作尤为关键——TNKS通过PARsylation（聚ADP-核糖基化）调控Wnt/β-catenin信号和端粒维持，是重要的核内酶。

最新且最关键的发现为：SH3BP5L触发RAB11A调控的整合素（integrin）回收网络，在乳腺癌转移中发挥促迁移功能（PMID:41623179）。该发现确立了SH3BP5L-RAB11A轴在癌症中的功能性角色。分子机制模型为：SH3BP5L作为RAB11A的GEF，在细胞前沿（leading edge）局部激活RAB11A，驱动活性整合素从回收内体→质膜的极性运输，维持细胞迁移的方向性。TNKS的PARsylation可能调控SH3BP5L的稳定性或活性——类似TNKS调控AXIN的方式。

SH3BP5L作为极度新颖的核相关蛋白（PubMed=4, 新颖性10/10），其核质定位的功能意义是未来研究中最值得探索的方向。核内的SH3BP5L可能参与：（1）核膜处回收内体-核孔复合体接触位点的形成；（2）有丝分裂后的核膜重建过程中RAB11A活性的时空调控；（3）与TNKS依赖的Wnt转录复合体的核内调控。鉴于仅有4篇PubMed文献（其中最关键的是2026年JCI论文），SH3BP5L代表了真正前沿的、未被充分研究的信号节点——其GEF活性、RAB11A特异性和核定位的组合在人类蛋白组中具有独特特征。

**蛋白全称**: SH3 domain-binding protein 5-like

**功能**: Functions as a guanine nucleotide exchange factor (GEF) for RAB11A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007940 |
| Pfam | PF05276 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NINL | BioGRID | 0 |
| PLEKHA5 | BioGRID | 0 |
| YWHAG | BioGRID | 0 |
| RAB11B | BioGRID | 0 |
| BICD1 | BioGRID | 0 |
| THG1L | BioGRID | 0 |
| TNKS | BioGRID | 0 |
| TNKS2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7L8J4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000175137-SH3BP5L

![](https://images.proteinatlas.org/38068/435_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/38068/435_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/38068/445_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/38068/445_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/38068/448_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/38068/448_G4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 41623179 | SH3BP5L triggers the RAB11A-regulated integrin recycling network implicated in breast cancer metastasis. | J Clin Invest 2026 |
| 40759305 | Whole-transcriptome sequencing analysis of spinal neuronal ferroptosis in aggravating neuropathic pain. | Life Sci 2025 |
| 39753851 | Integrated Mendelian Randomization and Single-Cell Transcriptomics Analysis Identifies Critical Blood Biomarkers and Pot | CNS Neurosci Ther 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3BP5L

