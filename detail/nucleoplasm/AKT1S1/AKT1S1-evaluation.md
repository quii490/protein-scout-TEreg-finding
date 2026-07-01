---
type: protein-evaluation
gene: "AKT1S1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, rebuilt]
status: shortlisted
---

## AKT1S1 (Uncharacterized protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | AKT1S1 |
| 蛋白名称 | Uncharacterized protein |
| UniProt ID | AKT1S1 |
| 蛋白大小 | 0 aa |
| 评估日期 | 2026-06-29 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | UniProt GO-CC data pending |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 0 aa |
| 研究新颖性 | 5/10 | ×5 | 25.0 | Data pending |
| 三维结构 | 5/10 | ×3 | 15.0 | AlphaFold predicted |
| 调控结构域 | 4/10 | ×2 | 8.0 | Data pending |
| PPI | 5/10 | ×3 | 15.0 | Data pending |
| **加权总分** | | | **90/180** | |
| **归一化总分 (/1.83)** | | | **49.2/100** | 互证: +0 |

### 3. 分析

This report was automatically rebuilt after file corruption. Full manual evaluation pending.

### 4. 总体评价

**Data pending** — requires full evaluation.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPTOR | STRING | 999 |
| MTOR | STRING | 999 |
| MLST8 | STRING | 999 |
| AKT1 | STRING | 995 |
| TTI1 | STRING | 993 |
| RPS6KB1 | STRING | 990 |
| EIF4EBP1 | STRING | 977 |
| RPS6KB2 | STRING | 972 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204673-AKT1S1

![](https://images.proteinatlas.org/21903/651_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/651_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204673-AKT1S1

![](https://images.proteinatlas.org/21903/651_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/651_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204673-AKT1S1

![](https://images.proteinatlas.org/21903/651_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/651_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/656_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21903/652_E8_2_blue_red_green.jpg)

### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### 深度机制分析

**结构域架构**：AKT1S1（PRAS40, Proline-rich AKT substrate 40 kDa）是mTORC1 complex的regulatory subunit——虽然此TrEMBL条目为uncharacterized且size=0 aa（应为data corruption artifact），canonical AKT1S1/PRAS40（UniProt Q96B36, 256 aa, 27.3 kDa）是mTORC1的negative regulator。N端富含Proline region（~40% Pro content, Pro-rich motifs mediating SH3 domain interaction）——TOS motif（TOR signaling motif, FxxDxxL/I）介导与RPTOR/raptor的直接结合——C端区域含AKT phosphorylation site（Thr246）——AKT-mediated Thr246 phosphorylation触发14-3-3 protein binding→PRAS40从mTORC1解离→解除inhibition——这是insulin/PI3K/AKT/mTORC1信号通路的key regulatory step。

**PPI互作网络解读**：PPI network富集mTORC1 pathway核心组分——RPTOR（STRING 999）结合PRAS40 TOS motif→recruit至mTORC1 complex。MTOR（STRING 999）是central serine/threonine kinase——PRAS40通过mask mTOR catalytic site抑制mTOR activity。AKT1（STRING 995）直接磷酸化PRAS40 Thr246→14-3-3 binding→dissociation from mTORC1。MLST8（STRING 999）稳定mTOR-RAPTOR interaction。RPS6KB1（S6K1, STRING 990）和EIF4EBP1（4E-BP1, STRING 977）为mTORC1 downstream translational effectors。

**结构解读**：PRAS40的TOS motif（FEMDI, aa129-133）形成short alpha-helical segment——被RPTOR RNC domain识别（PDB: 6BCU）。Thr246位于consensus AKT phosphorylation motif（RXRXXpS/T）——pThr246创建14-3-3 binding site（mode I）。

**机制模型**：PRAS40作为mTORC1 gatekeeper——growth factor withdrawal→AKT inactive→PRAS40 non-phosphorylated→constitutively inhibit mTORC1→suppress translation。Growth factor stimulation→PI3K/AKT→PRAS40 Thr246 phosphorylation→14-3-3 binding→mTORC1 released→S6K1/4E-BP1 activated→protein translation and cell growth。

**TE调控展望**：mTORC1通过translation control间接调控TE——S6K1 phosphorylates ribosomal protein S6→促进5'TOP mRNA translation→TE-encoded ORF（如LINE-1 ORF1/ORF2）可能受翻译调控影响。mTORC1也调控lipid biogenesis via SREBP1/2→membrane composition影响LINE-1 RNP nuclear import。但此entry corrupted（size=0 aa），实际TE评估应参考canonical PRAS40 entry（UniProt Q96B36）。

### PubMed References

**Papers: 133**

| PMID | Title |
|---|---|
| 41327199 | Deregulation of m6A-RNA methylation impairs adaptive hypertrophic response and drives maladaptation via mTORC1-S6K1-hyperactivation and autophagy impa |
| 41071193 | Comprehensive proteomic and pathological profiling identifies PRAS40 as a novel biomarker and mediator of primary immune checkpoint blockade resistanc |
| 40328211 | Canine prostate cancer cell transcriptome reveals important dysregulation in PI3K/AKT/mTOR pathway. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/AKT1S1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AKT1S1
