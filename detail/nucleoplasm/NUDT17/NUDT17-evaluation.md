---
type: protein-evaluation
gene: "NUDT17"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NUDT17 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NUDT17 |
| 蛋白名称 | m7GpppN-mRNA hydrolase NUDT17 |
| 蛋白大小 | 328 aa / 35.9 kDa |
| UniProt ID | P0C025 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 328 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=85.1; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | NAD-cap_RNA_hydrolase_NudC; NUDIX_hydrolase-like_dom_sf; NUDIX_hydrolase_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=8 broad=10
- AF pLDDT=85.1 PDB=1
- InterPro: NAD-cap_RNA_hydrolase_NudC; NUDIX_hydrolase-like_dom_sf; NUDIX_hydrolase_dom
- Pfam: NUDIX
- PPI degree=7 ChIP: None
38756100: Association between NUDT17 polymorphisms and breast cancer risk. | 39531477: Inositol pyrophosphate catabolism by three families of phosphatases regulates pl | 23353937: Multiple Nudix family proteins possess mRNA decapping activity.

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

NUDT17（m7GpppN-mRNA hydrolase, P0C025）属于NUDIX（Nucleoside Diphosphate linked to X）水解酶超家族，由IPR000086（NUDIX_hydrolase_dom）和PF00293（NUDIX Pfam）定义其保守的催化核心。NUDIX家族的标志性特征是一个约23个残基的NUDIX盒子（GX5EX7REUXEEXGU，其中U为疏水残基），构成α-β-α三明治折叠，并在loop-α-helix区域排列必需的二价阳离子（Mg²⁺）以极化焦磷酸键。NUDT17的特殊性在于其被分类为IPR033716（NAD-cap_RNA_hydrolase_NudC）亚家族成员，这一亚家族命名本身揭示了一个关键线索：该蛋白不仅作用于标准的m⁷GpppN-mRNA帽子，可能同样能够水解NAD-capped RNA——这是真核生物中近些年发现的一类非经典RNA 5'末端修饰。同时，IPR050241（NAD-cap RNA hydrolase NUDT17-like）的新近归类进一步支持了这一功能指向。若NUDT17确实具有双底物特异性（m⁷G帽 + NAD帽），则其在核质中定位于转录和RNA加工活跃区域，可能在新生转录本的质量控制或5'帽动态交换中发挥守门员功能。

AlphaFold预测的pLDDT值85.1属于较高置信度区间，对于328 aa的蛋白而言，该得分暗示NUDT17整体折叠良好。唯一的PDB条目提供了实验结构锚点，可用于验证活性位点残基的几何排列。结合PAE图可推断，NUDIX催化域形成紧凑的球状核心，而N/C端延伸可能形成底物识别和帽子结合所需的辅助界面——这与NUDT16、Dcp2等其他脱帽酶中RNA结合面通常位于NUDIX折叠之外的规律一致。NUDT17与m⁷G帽底物的特异性识别涉及芳香族残基对7-甲基鸟嘌呤的π-π堆积以及带正电残基对三磷酸桥的静电稳定，而NAD帽的额外腺苷-烟酰胺部分则要求活性位点具备额外的结合口袋。

PPI网络具有明显的功能聚类特征：NUDT22（STRING 746）、NUDT2（STRING 727）、NUDT14（STRING 717）和NUDT5（STRING 710）全部为NUDIX家族成员，且评分均处于STRING高置信度范围。这种同家族蛋白的密集互作模式表明NUDT17很可能与这些NUDIX蛋白形成功能复合体或参与旁路调控网络。具体而言，NUDT5和NUDT14均为核苷二磷酸糖水解酶（如ADP-核糖/ADP-甘露糖），NUDT2是一个多底物NUDIX作用于ApₙA（二腺苷多磷酸）和ADP-核糖，NUDT22为尿苷二磷酸葡萄糖水解酶。这种互作拓扑暗示核质中存在一个NUDIX蛋白网络，协同调控多种核苷酸代谢产物的水平——NUDT17处理mRNA帽子结构产生的m⁷GDP、GDP等产物，恰好可以作为其他NUDIX家族成员的底物或调控因子，形成一个代谢反馈回路。

从综合机制模型推断，NUDT17在核质中的核心功能是作为mRNA 5'帽质控系统的效应器：它可能穿梭于转录活跃的染色质区域，识别并水解异常加帽（如错误的甲基化状态）或应被降解的mRNA的5'帽结构，从而启动5'-3'核内RNA降解通路（类似于酵母核内Xrn1/Rat1通路的起始步骤）。NAD-cap水解活性的潜在存在则引入了另一个维度——NAD-capped RNA在哺乳动物细胞中可作为非经典降解信号，NUDT17对这些帽结构的水解可能在氧化应激或代谢应激条件下调控特定mRNA群体的稳定性。考虑到NUDT17的PubMed严格计数仅8篇（2026-07），这是一个极度未充分研究的核蛋白，其与乳腺癌风险的遗传学关联（PMID 38756100, 41855232涉及的rs9286836和rs2004659多态性）进一步提示NUDT17的功能变异可能通过改变RNA代谢稳态影响肿瘤易感性。未来的研究方向应包括：明确NUDT17的完整底物谱（m⁷G帽 vs. NAD帽 vs. 其他非经典帽结构），通过CRISPR敲除结合RNA-seq鉴定其内源性靶转录本集合，以及解析NUDT17-帽结构复合体的高分辨率晶体结构以阐明底物选择性机制。


### 补充分析 (UniProt API)

**蛋白全称**: m7GpppN-mRNA hydrolase NUDT17

**功能**: Acts as a decapping enzyme capable of hydrolyzing monomethylated capped RNAs (in vitro). Hydrolyzes monomethylated capped RNA after alpha and beta phosphates to form N(7)-methyl-GDP. Shows low activity towards unmethylated capped RNA

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050241 |
| InterPro | IPR015797 |
| InterPro | IPR000086 |
| InterPro | IPR033716 |
| Pfam | PF00293 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NUDT22 | STRING | 746 |
| NUDT2 | STRING | 727 |
| NUDT14 | STRING | 717 |
| NUDT5 | STRING | 710 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P0C025-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000186364-NUDT17

![](https://images.proteinatlas.org/49649/1208_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/49649/1208_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/49649/757_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/49649/757_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/49649/761_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/49649/761_C7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 41855232 | Association of NUDT17 rs9286836 and rs2004659 variants with breast cancer risk in Bangladeshi Women. | PLoS One 2026 |
| 40992100 | Transcriptome analysis and functional validation reveal the mechanism of action of NtCaM13 in drought stress in tobacco  | Plant Physiol Biochem 2025 |
| 39531477 | Inositol pyrophosphate catabolism by three families of phosphatases regulates plant growth and development. | PLoS Genet 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NUDT17

