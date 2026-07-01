---
type: protein-evaluation
gene: "KRT15"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KRT15 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRT15 |
| 蛋白名称 | Keratin, type I cytoskeletal 15 |
| 蛋白大小 | 456 aa / 49.2 kDa |
| UniProt ID | P19012 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Intermediate filaments; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 456 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=85 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=74.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | IF_conserved; IF_rod_dom; Keratin_I |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=170 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +2 |

### 3. 分析
- Intermediate filaments; Nucleoplasm (Supported)
- PubMed strict=85 broad=288
- AF pLDDT=74.2 PDB=0
- InterPro: IF_conserved; IF_rod_dom; Keratin_I
- Pfam: Filament
- PPI degree=170 ChIP: None
33691112: Human gastrointestinal epithelia of the esophagus, stomach, and duodenum resolve | 36512409: Krt14 and Krt15 differentially regulate regenerative properties and differentiat | 38007424: Keratin 15 protects against cigarette smoke-induced epithelial mesenchymal trans

### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Keratin, type I cytoskeletal 15

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018039 |
| InterPro | IPR039008 |
| InterPro | IPR002957 |
| Pfam | PF00038 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：KRT15（P19012, Keratin type I cytoskeletal 15, 456 aa / 49.2 kDa）的主要结构域注释为IF_conserved, IF_rod_dom, Keratin_I。Pfam数据库进一步识别到Filament等保守域。AlphaFold pLDDT=74.2（中等）——折叠域基本可信，但部分区域置信度较低，建议实验解析。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=85，该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=170）——BioGRID/STRING数据库记录的互作伙伴包括KRT14、MCM10、SMARCD1、PCM1、ZC2HC1C、LDOC1。其中MCM10、SMARCD1、KANSL1等具有染色质调控或转录相关功能——提示KRT15可能通过protein-protein interaction平台间接参与核内转录调控网络。

**结构解读**：AlphaFold预测（pLDDT=74.2）整体折叠可信，IF_conserved构成结构核心。Pfam域Filament的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=74.2提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：KRT15为intermediate filament（IF）家族keratin蛋白——其central rod domain（~310 aa）形成coiled-coil dimer→tetramer→apolar 10 nm filament。Keratin与SMARCD1（BAF chromatin remodeling complex subunit）和MCM10（DNA replication licensing factor）的互作暗示KRT15可能在核基质-染色质界面发挥structural role——通过接触chromatin remodeling complex间接影响TE区域的chromatin state。

**TE调控展望**：KRT15的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）KRT15是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）KRT15是否能够通过其结构域识别TE-derived DNA/RNA element；（3）KRT15的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定KRT15在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KRT14 | STRING | 731 |
| MCM10 | BioGRID | 1 |
| SMARCD1 | BioGRID | 1 |
| PCM1 | BioGRID | 1 |
| ZC2HC1C | BioGRID | 1 |
| LDOC1 | BioGRID | 1 |
| USHBP1 | BioGRID | 1 |
| KANSL1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P19012-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRT15

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171346-KRT15

![](https://images.proteinatlas.org/23910/1320_G5_6_red_green.jpg)
![](https://images.proteinatlas.org/23910/1320_G5_7_red_green.jpg)
![](https://images.proteinatlas.org/24554/1320_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/24554/1320_E5_4_red_green.jpg)

### PubMed

**Count: 288**

| PMID | Title |
|---|---|
| 42111259 | Regenerative potential of CD200(-) subpopulations of hair follicle bulge. |
| 41991644 | The KRT15 and KRT81 complex promotes lenvatinib resistance in thyroid cancer by upregulating DGKB mediated lipid metabolism. |
| 41907411 | KRT15 identified by scRNA-Seq and machine learning as stemness regulator and prognostic biomarker in ESCC. |
| 41819470 | KRT15 drives immunosuppression in esophageal squamous cell carcinoma through GSK3β/β-catenin/CD276 signaling. |
| 41817143 | Essential Role of CD63 in Maintaining Corneal Epithelial Identity in the Human Limbus. |
