---
type: protein-evaluation
gene: "HPX-2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## HPX-2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HPX-2 |
| 蛋白名称 | HPX-2 protein |
| 蛋白大小 | 39 aa / 4.6 kDa |
| UniProt ID | Q14559 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 39 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.1; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Homeobox_regulator; Homeodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=1 broad=4
- AF pLDDT=82.1 PDB=0
- InterPro: Homeobox_regulator; Homeodomain-like_sf
- Pfam: 
- PPI degree=0 ChIP: None
8406412: Hemopexin: a unique genetic polymorphism in populations of African ancestry.

### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: Homeobox_regulator; Homeodomain-like_sf


### 补充分析 (UniProt API)

**蛋白全称**: HPX-2 protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051306 |
| InterPro | IPR009057 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: HPX-2 protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051306 |
| InterPro | IPR009057 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q14559-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：HPX-2（Q14559, HPX-2 protein, 39 aa / 4.6 kDa）的主要结构域注释为Homeobox_regulator, Homeodomain-like_sf。Pfam数据库进一步识别到- PPI degree=0 ChIP: None等保守域。AlphaFold pLDDT=82.1（优质）——大部分区域折叠可信，个别loop区域可能为柔性无序。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=1（极度新颖），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=0）——当前已知互作伙伴数量有限。该蛋白的互作图谱近乎空白，future interactome studies will be critical for linking this protein to specific pathway context.

**结构解读**：AlphaFold预测（pLDDT=82.1）整体折叠可信，Homeobox_regulator构成结构核心。Pfam域- PPI degree=0 ChIP: None的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=82.1的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：HPX-2含homeobox/homeodomain——该domain为conserved helix-turn-helix DNA-binding motif。Homeodomain蛋白常作为developmental transcription factor——调控cell fate determination和body plan。某些homeodomain蛋白已被报道与TE-derived cis-regulatory elements相互作用，可能modulate chromatin accessibility around TE loci。

**TE调控展望**：该蛋白被标注为TE_REG_CANDIDATE——含Homeobox_regulator; Homeodomain-like_sf结构域。TE调控关联性取决于以下几个方面：（1）HPX-2是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）HPX-2是否能够通过其结构域识别TE-derived DNA/RNA element；（3）HPX-2的knockout/knockdown是否改变LINE-1或ERV family的expression level。Homeodomain蛋白的DNA binding specificity已在多个TF family中详细表征——HPX-2可能识别TE-derived promoter中的AT-rich或TAAT motif。建议EMSA+DNase I footprinting验证其DNA binding specificity。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/HPX-2

### PubMed

**Count: 4**

| PMID | Title |
|---|---|
| 33440852 | Detection of Hypoxanthine from Inosine and Unusual Hydrolysis of Immunosuppressive Drug Azathioprine through the Formation of a Diruthenium(III) Syste |
| 30695063 | Heme peroxidase HPX-2 protects Caenorhabditis elegans from pathogens. |
| 8406412 | Hemopexin: a unique genetic polymorphism in populations of African ancestry. |
| 3661561 | Genetic studies of low-abundance human plasma proteins. VI. Polymorphism of hemopexin. |
