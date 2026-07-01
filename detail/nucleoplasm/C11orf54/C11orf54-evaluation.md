---
type: protein-evaluation
gene: "C11orf54"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C11orf54 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | C11orf54 |
| 蛋白名称 | MHC class I alpha chain |
| 蛋白大小 | 265 aa / 29.5 kDa |
| UniProt ID | A0A024R3B0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 265 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=90.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | C11orf54_DUF1907 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=43 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=3, broad=7
- AF pLDDT: 90.0 / PDB: 0
- InterPro: C11orf54_DUF1907
- Pfam: DUF1907
- PPI degree: 43 / ChIP: None
37277441: C11orf54 promotes DNA repair via blocking CMA-mediated degradation of HIF1A. | 40737316: C11orf54 catalyzes L-xylulose formation in human metabolism. | 20464042: Proteomic analysis of clear cell renal cell carcinoma. Identification of potenti

### 4. 总体评价
★★★★  **66.7/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: MHC class I alpha chain

**功能**: Involved in the presentation of foreign antigens to the immune system

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003006 |
| InterPro | IPR003597 |
| InterPro | IPR050208 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：C11orf54（A0A024R3B0, MHC class I alpha chain, 265 aa / 29.5 kDa）的主要结构域注释为C11orf54_DUF1907。Pfam数据库进一步识别到DUF1907等保守域。AlphaFold pLDDT=90.0（极高质量）——该蛋白整体折叠高度可信，结构性表征良好。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=3（极度新颖），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=43）——BioGRID数据库记录的互作伙伴包括TRIP13、APP、VAC14、SSX2IP、CCT2、BCAT2。其中TRIP13等具有染色质调控或转录相关功能——提示C11orf54可能通过protein-protein interaction平台间接参与核内转录调控网络。

**结构解读**：AlphaFold预测（pLDDT=90.0）显示该蛋白具有明确的折叠结构域，其中C11orf54_DUF1907为保守的催化/结合模块。Pfam域DUF1907的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=90.0的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：C11orf54的DUF1907（Domain of Unknown Function 1907）保守域功能未知——但DUF domain通常形成stable globular fold。PMID:37277441报道C11orf54通过blocking CMA-mediated HIF1A degradation→promote DNA repair——提示该蛋白在genome integrity maintenance中具有functional role，可能indirectly influence TE region stability。

**TE调控展望**：C11orf54的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）C11orf54是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）C11orf54是否能够通过其结构域识别TE-derived DNA/RNA element；（3）C11orf54的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定C11orf54在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRIP13 | BioGRID | 0 |
| APP | BioGRID | 0 |
| VAC14 | BioGRID | 0 |
| SSX2IP | BioGRID | 0 |
| CCT2 | BioGRID | 0 |
| BCAT2 | BioGRID | 0 |
| AKR1A1 | BioGRID | 0 |
| AKR1C2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A024-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C11orf54

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000182919-C11orf54

![](https://images.proteinatlas.org/40088/539_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/40088/539_E3_5_red_green.jpg)
![](https://images.proteinatlas.org/40088/552_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/40088/552_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/40088/534_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/40088/534_E3_2_red_green.jpg)

### PubMed

**Count: 7**

| PMID | Title |
|---|---|
| 41827707 | Integrated ATAC-Seq and RNA-Seq Analyses Identify the Motif CGTTTCCGGT as an Arginine Deficiency-Responsive DNA Element in Cancer Cells. |
| 40737316 | C11orf54 catalyzes L-xylulose formation in human metabolism. |
| 40646607 | Insulin levels at 18-20 gestational weeks in pregnant women with obesity are associated with newborn abdominal fat deposition and DNA methylation in c |
| 37277441 | C11orf54 promotes DNA repair via blocking CMA-mediated degradation of HIF1A. |
| 35812443 | Computational Recognition of a Regulatory T-cell-specific Signature With Potential Implications in Prognosis, Immunotherapy, and Therapeutic Resistanc |


