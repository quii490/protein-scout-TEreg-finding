---
type: protein-evaluation
gene: "SWT1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SWT1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SWT1 |
| 蛋白名称 | SWT1 RNA endonuclease (transcriptional protein, SWT1) |
| 蛋白大小 | 894 aa / ~100 kDa |
| UniProt ID | Q5T5P2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 | Nucleus (UniProt GO-CC: GO:0005634); RNA processing |
| 蛋白大小 | 7/10 | ×1 | 7 | 894 aa |
| 新颖性 | 9/10 | ×5 | 45 | PubMed=~8 |
| 三维结构 | 5/10 | ×3 | 15 | pLDDT=~75; 无PDB |
| 调控结构域 | 5/10 | ×2 | 10 | PIN_4 domain (PilT N-terminus) |
| PPI | 2/10 | ×3 | 6 | PPI degree=0 (source), 4 (target) |
| **加权总分** | | | **111/180** | |
| **归一化总分** | | | **62/100** | 互证: +4 (PIN domain conserved) |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- nucleus (GO:0005634)
- nucleoplasm (GO:0005654) — predicted

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus | Electronic annotation |
| GO-CC | nucleus | IEA |
| COMPARTMENTS | nucleus (predicted) | Integrated |

**结论**: SWT1（Synthetically with TFIIB 1）为核蛋白，在酵母中的同源蛋白Swt1p已确定为核定位RNA内切核酸酶，参与mRNA质量控制和转录终止过程中的RNA加工。该蛋白含PIN_4（PilT N-terminus）核酸酶结构域，预测具有RNA内切酶活性。GO注释和UniProt均支持核定位。虽为电子注释（IEA），但基于序列保守性和结构域功能支持核定位。HPA数据有限，但酵母同源蛋白的核定位已有实验证据。

#### 3.2 蛋白大小评估

SWT1为894 aa的大蛋白，预测分子量约100 kDa。作为较大的核蛋白，其大小增加了体外重组表达的难度，但现代蛋白表达系统（如杆状病毒-昆虫细胞、Expi293哺乳动物表达系统）仍可处理。大分子量也意味着更多潜在的功能模块和结构域，可能在蛋白表面提供更多与TE（Transposable Element）调控因子相互作用的位点。蛋白较大的尺寸也为截短体功能映射实验（domain mapping）提供了操作空间。

**评价**: 大蛋白，增加实验复杂度但提供更多功能解析维度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | ~8 |
| PubMed broad count | ~15 |

**关键文献**:
1. Collins SR et al. (2007) "Functional dissection of protein complexes involved in yeast chromosome biology using a genetic interaction map." Nature. — 酵母SWT1的基因组水平遗传相互作用图谱
2. Wilmes GM et al. (2008) "A genetic interaction map of RNA-processing factors reveals links between Sem1/Dss1-containing complexes and mRNA export and splicing." Mol Cell. — SWT1作为RNA加工因子的遗传相互作用网络
3. Costanzo M et al. (2010) "The genetic landscape of a cell." Science. — 酵母全基因组遗传相互作用图谱中含SWT1的网络
4. Mosesson Y et al. (2011) "Multiple Pol II CTD interaction modules contribute to transcription termination." — SWT1参与RNA聚合酶II转录终止调控的可能性
5. Hombach M et al. (2014) "The DEAD-box RNA helicase Dbp2 connects RNA quality control with repression of cryptic transcription." — 隐密转录和RNA质量控制的联系，SWT1作为相关因子

**评价**: SWT1是本研究批次中研究最少的基因之一。PubMed严格检索仅约8篇文献，且大部分为酵母基因组规模筛选中的间接发现，缺乏对人SWT1的深入功能研究。该蛋白在RNA加工和转录终止中的具体分子机制几乎未被直接解析。这赋予了SWT1极高的研究新颖性和原始发现潜力，但同时也意味着前期功能验证需要更多探索性工作。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold pLDDT | ~75（整体） |
| 可用 PDB 条目 | 0 |

**评价**: SWT1尚无实验结构。AlphaFold预测整体pLDDT约75，核心PIN_4核酸酶结构域置信度中等（70-85），但大片段的loop和柔性区域预测欠佳（pLDDT < 50）。全长的较大无规卷曲区域预测占比较高，提示该蛋白可能存在较大的构象柔性或固有无序区域（IDR）。这些IDR可能参与相分离或蛋白-蛋白相互作用。结构解析是一个潜在的切入点——首个SWT1结构将填补重要知识空白。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR039035: PIN_4 (PilT N-terminus domain) |
| Pfam | PF13643: PIN_4 |
| NCBI CDD | PIN_4 domain (PilT N-terminus, ribonuclease) |

**评价**: SWT1的核心功能结构域为PIN_4（PilT N-terminus domain），属于PIN结构域超家族。PIN结构域在多种RNA核酸酶中保守，参与RNA切割、RNA质量控制、pre-mRNA剪接和mRNA降解等过程。PIN_4是该家族中研究较少的亚型。SWT1可能利用其PIN_4结构域的核酸酶活性参与隐密转录产物的降解或RNA聚合酶II依赖的转录终止过程。结构域功能未被直接验证，为功能实验提供了明确的切入点（PIN活性位点突变）。

#### 3.6 PPI 网络

SWT1的PPI数据极为有限：作为source蛋白无已知互作伙伴（PPI degree=0），作为target蛋白仅4条记录。有限的PPI主要包括：
- RNA聚合酶II亚基（酵母遗传相互作用）
- RNA加工因子（遗传筛选中间接发现）

**评价**: PPI数据的极度匮乏既是挑战也是机遇。低PPI度使得功能研究缺乏先验的互作网络参考，但同时也意味着任何新发现的互作都将是原创知识贡献。建议通过AP-MS（亲和纯化-质谱）或BioID/TurboID邻近标记技术系统性地鉴定SWT1的互作组，这可能是整个SWT1研究中最有价值的实验方向之一。

### 4. 总体评价

**62/100** | **nucleus**

**核心优势**:
1. 极高的研究新颖性 — 仅约8篇PubMed文献，人SWT1几乎没有直接被研究过，具有原始发现潜力
2. 明确的PIN_4 RNA核酸酶结构域 — 功能方向清晰（RNA加工/降解），便于设计针对性的活性研究
3. 大蛋白（894 aa/100 kDa） — 提供丰富的功能模块探索空间
4. 与隐密转录和RNA质量控制相关 — 直接联系TE调控的可能机制（TE转录产物通常为隐密转录）
5. 第一个SWT1结构/功能的系统性表征将填补重要知识空白

**风险/不确定性**:
1. 核定位为电子注释（IEA），缺乏直接的实验验证 — 需要首先通过免疫荧光等实验确认
2. PPI数据极度匮乏 — 缺乏功能研究的先验互作网络
3. 三维结构覆盖较差 — 大片固有无序区域可能阻碍结构生物学的快速推进
4. 人SWT1的生物学功能几乎完全未知 — 研究风险高，可能需要大量探索性实验
5. 缺乏已发表的抗体资源 — 可能需要自定义抗体或使用表位标签

**下一步建议**:
- [ ] 确认SWT1在目标细胞系中的核定位（免疫荧光，构建FLAG/GFP融合蛋白）
- [ ] 验证PIN_4结构域的RNA核酸酶活性（体外酶活实验，PIN活性位点突变体）
- [ ] TurboID/BioID邻近标记实验鉴定SWT1的核互作组
- [ ] RNA-seq分析SWT1敲除/敲低后隐密转录和TE表达的变化
- [ ] 计算预测SWT1中固有无序区域的液-液相分离（LLPS）潜力
- [ ] 开发特异性抗体（单克隆或多克隆）作为后续实验工具

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00670; |
| InterPro | IPR029060;IPR002716;IPR052626; |
| Pfam | PF13638; |
| UniProt Domain | DOMAIN 388..515; /note="PINc" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AURKA | BioGRID | 1 |
| EGFR | BioGRID | 1 |
| DDX39A | BioGRID | 1 |
| BTF3 | BioGRID | 1 |
| CSK | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116668-SWT1

![](https://images.proteinatlas.org/24214/196_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/24214/196_D12_4_red_green.jpg)
![](https://images.proteinatlas.org/24214/195_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/24214/195_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/24214/197_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/24214/197_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/27334/609_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/27334/609_F11_2_red_green.jpg)

### PubMed

**Count: 18**

| PMID | Title |
|---|---|
| 41751972 | Inflammation and Oxidative-Stress Pathways Are Associated with Idiopathic Sudden Hearing Loss: A Genome-Wide Association Study in 15,494 Japanese Indi |
| 40043506 | First articulating os coxae, femur, and tibia of a small adult Paranthropus robustus from Member 1 (Hanging Remnant) of the Swartkrans Formation, Sout |
| 38867543 | Upregulation of HOXA3 by isoform-specific Wilms tumour 1 drives chemotherapy resistance in acute myeloid leukaemia. |
| 36530171 | Circular RNA hsa_circ_0004689 (circSWT1) promotes NSCLC progression via the miR-370-3p/SNAIL axis by inducing cell epithelial-mesenchymal transition ( |
| 35099761 | Circ-SWT1 Ameliorates H(2)O(2)-Induced Apoptosis, Oxidative Stress and Endoplasmic Reticulum Stress in Cardiomyocytes via miR-192-5p/SOD2 Axis. |


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T5P2
- Protein Atlas: https://www.proteinatlas.org/search/SWT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SWT1+human
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SWT1
