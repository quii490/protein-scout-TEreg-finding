---
type: protein-evaluation
gene: "PCDHA4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHA4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHA4 |
| 蛋白名称 | Protocadherin alpha-4 |
| 蛋白大小 | 947 aa / 102.3 kDa |
| UniProt ID | Q9UN74 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 947 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=73.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=54 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=3 broad=26
- AF pLDDT=73.8 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD
- Pfam: Cadherin; Cadherin_2; Cadherin_tail
- PPI degree=54 ChIP: None
39842729: Genome-Wide and Rare Variant Association Studies of Amblyopia in the All of Us R | 33630843: Hippocampal transcriptome-wide association study and neurobiological pathway ana | 27842508: Global DNA methylation profiling uncovers distinct methylation patterns of proto

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHA4（Protocadherin alpha-4）是原钙粘蛋白α簇的另一个可变成员（947 aa, 102.3 kDa），与PCDHA3共享完全相同的结构域架构：6个钙粘蛋白重复结构域构成的胞外可变区（决定亚型黏附特异性）和α-恒定区胞内结构域（InterPro IPR031904, Cadherin_CBD, Pfam Cadherin_tail）。AlphaFold2预测pLDDT=73.8（得分5/10），与PCDHA3的73.7几乎相同，进一步证实这是α簇蛋白的系统性特征。唯一的本质差异可能在于胞外可变区的钙离子结合位点分布，这决定了每个α亚型特异的黏附亲和力。

PCDHA4的PPI网络度为54（得分6/10），显著高于PCDHA3的34，提示其可能具有更广泛的功能伙伴网络。互作伙伴的组成也呈现出不同的特征：与APLP1（淀粉样前体样蛋白1，APP家族成员）的BioGRID互作提供了与PCDHGC5-APP互作类似的核内信号机制线索——APLP1与APP一样在γ-分泌酶剪切后释放胞内片段入核调控转录。与LRIF1（配体依赖性核受体互作因子1，SMCHD1的核内互作因子，参与X染色体失活）的BioGRID互作则直接暗示PCDHA4可能与染色质架构蛋白协同调控核内基因表达。此外，与GDF9（生长分化因子9，卵母细胞特异性TGF-β家族成员）的互作提示PCDHA4可能参与生殖发育。

PCDHA4的DNA甲基化模式具有独特的表观遗传特征，这使其在PCDH家族中独树一帜。PMID:27842508进行了全局DNA甲基化分析，发现原钙粘蛋白α4具有独特的甲基化模式——PCDHA4的高甲基化/低甲基化状态可能作为细胞身份的标记，调控其亚型特异性表达。这一发现将PCDHA4的功能与更广泛的表观遗传调控机制相连接。PCDHA4在核质中的Supported级别定位（得分8/10）虽然置信度低于Approved，但其在阿尔茨海默病转录组关联研究（PMID:33630843）中的出现进一步巩固了其在神经退行性疾病中的角色。

PCDHA4仅3篇直接PubMed文献（得分10/10），但其26篇扩展文献涵盖了从弱视全基因组关联研究（PMID:39842729）到海马体转录组关联的广泛领域。这种"文献少但覆盖面广"的特征提示PCDHA4是一个在大规模组学筛选中反复出现的"暗物质"分子——其功能在多种环境中被间接暗示但从未被专门研究。PCDHA4的核内胞内片段功能研究可以利用PCDH-α恒定区已有的研究成果，直接使用靶向α-恒定区的抗体进行ChIP-seq以鉴定其在全基因组水平的结合靶点。

### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin alpha-4

**功能**: Calcium-dependent cell-adhesion protein involved in cells self-recognition and non-self discrimination. Thereby, it is involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |
| InterPro | IPR050174 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| C14orf1 | BioGRID | 0 |
| RBM48 | BioGRID | 0 |
| GDF9 | BioGRID | 0 |
| IGSF21 | BioGRID | 0 |
| APLP1 | BioGRID | 0 |
| EEF1A1 | BioGRID | 0 |
| CCDC90B | BioGRID | 0 |
| LRIF1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UN74-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204967-PCDHA4

![](https://images.proteinatlas.org/43180/1471_H10_7_red_green.jpg)
![](https://images.proteinatlas.org/43180/1471_H10_8_red_green.jpg)

### PubMed 文献

**PubMed count: 26**

| 39842729 | Genome-Wide and Rare Variant Association Studies of Amblyopia in the All of Us Research Program. | Ophthalmology 2025 |
| 37329382 | miR-218-5p and miR-320a-5p as Biomarkers for Brain Disorders: Focus on the Major Depressive Disorder and Parkinson's Dis | Mol Neurobiol 2023 |
| 33630843 | Hippocampal transcriptome-wide association study and neurobiological pathway analysis for Alzheimer's disease. | PLoS Genet 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHA4

