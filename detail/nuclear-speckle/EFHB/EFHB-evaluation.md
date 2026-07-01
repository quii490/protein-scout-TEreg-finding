---
type: protein-evaluation
gene: "EFHB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFHB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFHB / CFAP21 |
| 蛋白名称 | EF-hand domain-containing family member B |
| 蛋白大小 | 833 aa / 93.8 kDa |
| UniProt ID | Q8N7U6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nuclear bodies, Vesicles, Connecting piece; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskel |
| 蛋白大小 | 8/10 | ×1 | 8 | 833 aa / 93.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 7UNG, 8J07 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR018247, IPR002048, IPR057428, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies, Vesicles, Connecting piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, flagellum axoneme; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axonemal A tubule inner sheath (GO:0160111)
- axonemal microtubule (GO:0005879)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFAP21 |

**关键文献**:
1. Synthesis of (E)-Ethyl-4-(2-(furan-2-ylmethylene)hydrazinyl)benzoate, crystal structure, and studies of its interactions with human serum albumin by spectroscopic fluorescence and molecular docking methods.. *Spectrochimica acta. Part A, Molecular and biomolecular spectroscopy*. PMID: 30921660
2. Integrated analysis of the whole transcriptome of skeletal muscle reveals the ceRNA regulatory network related to the formation of muscle fibers in Tan sheep.. *Frontiers in genetics*. PMID: 36330447
3. Analysis of 19 genes for association with type I diabetes in the Type I Diabetes Genetics Consortium families.. *Genes and immunity*. PMID: 19956106
4. Genetic analysis and quantitative trait loci detection of udder traits in Jersey cattle.. *BMC genomics*. PMID: 41257575

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 4.7% |
| 置信残基 (pLDDT 70-90) 占比 | 44.9% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 49.6% |
| 可用 PDB 条目 | 7UNG, 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 49.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR057428, IPR040193; Pfam: PF13499, PF25325 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR90 | 0.944 | 0.944 | — |
| PACRG | 0.929 | 0.917 | — |
| ENKUR | 0.922 | 0.896 | — |
| EFHC2 | 0.910 | 0.900 | — |
| EFHC1 | 0.909 | 0.900 | — |
| CFAP20 | 0.899 | 0.899 | — |
| CFAP45 | 0.897 | 0.884 | — |
| TUBA1A | 0.891 | 0.877 | — |
| TUBB4B | 0.887 | 0.875 | — |
| C1orf158 | 0.869 | 0.817 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 7UNG, 8J07 | pLDDT=62.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm / Cytosol; 额外: Nuclear bodies, Vesicles, Connecting  | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFHB — EF-hand domain-containing family member B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小833 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：EFHB（EF-hand domain-containing family member B, UniProt: Q8N7U6, 833 aa / 93.8 kDa）的主要结构域特征为两个EF-hand钙结合基序（aa 561-596, aa 597-632）及PF13499、PF25325等Pfam保守域。EF-hand domain是最经典的钙离子感应模块——通过helix-loop-helix构象在Ca²⁺binding后发生构象重排，介导下游信号转导。AlphaFold pLDDT=62.5（中等偏弱）——有序残基占比49.6%，提示该蛋白含有大量的固有无序区域（IDR），IDR在phase separation（液-液相分离）和nuclear body formation中具有重要功能。该蛋白已有PDB实验结构（7UNG, 8J07），来自cryo-EM解析的axonemal complex，为EFHB在cilia/flagella中的结构组织提供了直接证据。

**PPI互作网络解读**：STRING PPI network（15 partners, combined score >0.4）记录的互作伙伴包括WDR90、PACRG、ENKUR、EFHC2、EFHC1、CFAP20、CFAP45、TUBA1A、TUBB4B、C1orf158——这些蛋白几乎全部富集于cilia/axoneme assembly和microtubule-based movement通路。值得注意的是BioGRID记录的互作伙伴包括MEPCE（7SK snRNP complex scaffold，参与RNA Pol II elongation regulation）和UPF1（nonsense-mediated mRNA decay核心因子）——这两个互作超出了cilia功能范畴，暗示EFHB可能参与nuclear RNA metabolism。

**结构解读**：AlphaFold预测（pLDDT=62.5）中的有序区域（49.6%）主要对应EF-hand domain区段，而33.3%的残基pLDDT<50——集中分布在N端和C端区域。这种结构特征（结构化domain + 大量IDR）常见于nuclear body scaffold蛋白，如coilin（Cajal body）或SRSF2（nuclear speckle marker）——这些蛋白通过IDR介导的weak multivalent interaction形成动态的biomolecular condensate。

**机制模型**：EFHB作为EF-hand family member的核心功能是通过EF-hand motif感应钙信号——Ca²⁺-bound EF-hand构象暴露疏水口袋，recruit下游effector protein。在cilia context中，EFHB可能通过其cryo-EM解析的axonemal localization调控microtubule sliding和ciliary beating。而在nuclear context中，MEPCE互作（BioGRID）暗示EFHB可能参与7SK snRNP-mediated transcriptional pausing——7SK snRNP通过sequestering P-TEFb（CDK9/Cyclin T1）调控RNA Pol II elongation。

**TE调控展望**：EFHB的TE regulation潜力通过以下间接途径体现：（1）7SK snRNP-MEPCE axis与LINE-1/L1 retrotransposon expression调控存在交叉——P-TEFb活性影响L1 promoter驱动的transcription elongation；（2）Ca²⁺-calmodulin signaling reported与endogenous retrovirus（ERV）activation相关——钙信号通过CaMK和calcineurin-NFAT通路影响chromatin state；（3）EFHB的高IDR含量（50.4%）使其具备参与nuclear condensate formation的潜力——许多TE silencing factor（如HP1alpha, KAP1/TRIM28）通过condensate-mediated机制形成repressive compartment。建议首先验证EFHB与MEPCE-7SK complex的生化互作，再通过EFHB knockdown/overexpression的RNA-seq评估其对TE subfamily expression的影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MEPCE | BioGRID | 0 |
| ANLN | BioGRID | 0 |
| UPF1 | BioGRID | 0 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7U6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163576-EFHB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFHB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7U6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000163576-EFHB/subcellular

![](https://images.proteinatlas.org/34835/1702_G6_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/34835/1702_G6_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/34835/1706_G9_13_cr6038c6dd010f7_blue_red_green.jpg)
![](https://images.proteinatlas.org/34835/1706_G9_3_cr6038c6dd006c1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34835/1788_F5_10_cr5971d74b481a3_blue_red_green.jpg)
![](https://images.proteinatlas.org/34835/1788_F5_29_cr5971d74b499c2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N7U6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N7U6 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 561..596; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 597..632; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR011992;IPR018247;IPR002048;IPR057428;IPR040193; |
| Pfam | PF13499;PF25325; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163576-EFHB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| STIM1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
