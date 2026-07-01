---
type: protein-evaluation
gene: "DEFB106A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## DEFB106A 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DEFB106A |
| 蛋白名称 | Beta-defensin 106 |
| 蛋白大小 | 65 aa / 7.4 kDa |
| UniProt ID | Q8N104 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 65 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=82.3; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Beta_defensin_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=23 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +2 |
### 3. 分析
- HPA: nan (nan)
- PubMed: strict=2, broad=8
- AF pLDDT: 82.3 / PDB: 1
- InterPro: Beta_defensin_dom
- Pfam: Defensin_beta_2
- PPI degree=23 / ChIP: None
31404823: Region-specific gene expression in the epididymis of Yak. | 17928628: Alterations in gene expression in the caput epididymides of nonobstructive azoos
### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Beta-defensin 106

**功能**: Has antibacterial activity (PubMed:12600824). Acts as a ligand for C-C chemokine receptor CCR2 (PubMed:23938203)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR025933 |
| Pfam | PF13841 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Beta-defensin 106

**功能**: Has antibacterial activity (PubMed:12600824). Acts as a ligand for C-C chemokine receptor CCR2 (PubMed:23938203)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR025933 |
| Pfam | PF13841 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：DEFB106A（Q8N104, Beta-defensin 106, 65 aa / 7.4 kDa）的主要结构域注释为Beta_defensin_dom。Pfam数据库进一步识别到Defensin_beta_2等保守域。AlphaFold pLDDT=82.3（优质）——大部分区域折叠可信，个别loop区域可能为柔性无序。该蛋白已有1个实验PDB结构条目，为机械性研究提供直接的结构基础。PubMed=2（极度新颖），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=23）——BioGRID数据库记录的互作伙伴包括CTSV、PCYOX1L、TMEM2、IL37、CST6、EMC8。

**结构解读**：AlphaFold预测（pLDDT=82.3）整体折叠可信，Beta_defensin_dom构成结构核心。Pfam域Defensin_beta_2的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=82.3的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：DEFB106A的精确分子机制目前尚待阐明。基于结构域注释（Beta_defensin_dom）——可推测该蛋白可能参与macromolecular complex assembly或signaling cascade中的scaffold function。在nucleoplasm context中，该蛋白可能需要与已知nuclear factor形成functional complex才能执行完整的生物学功能。

**TE调控展望**：DEFB106A的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）DEFB106A是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）DEFB106A是否能够通过其结构域识别TE-derived DNA/RNA element；（3）DEFB106A的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定DEFB106A在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CTSV | BioGRID | 0 |
| PCYOX1L | BioGRID | 0 |
| TMEM2 | BioGRID | 0 |
| IL37 | BioGRID | 0 |
| CST6 | BioGRID | 0 |
| EMC8 | BioGRID | 0 |
| POF1B | BioGRID | 0 |
| RNASE7 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N104-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DEFB106A

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 31404823 | Region-specific gene expression in the epididymis of Yak. |
| 25574196 | Genomic alterations on 8p21-p23 are the most frequent genetic events in stage I squamous cell carcinoma of the lung. |
| 24970887 | Unique properties of human β-defensin 6 (hBD6) and glycosaminoglycan complex: sandwich-like dimerization and competition with the chemokine receptor 2 |
| 18595735 | Production of bioactive human beta-defensin 5 and 6 in Escherichia coli by soluble fusion expression. |
| 17928628 | Alterations in gene expression in the caput epididymides of nonobstructive azoospermic men. |
